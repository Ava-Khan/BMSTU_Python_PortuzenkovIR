from llvmlite import ir, binding
from astt import *

class CodeGen:
    def __init__(self):
        self.binding = binding
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_function()

        # Словарь для хранения переменных (имя -> значение LLVM)
        self.variables = {}
        self.counter = 0  # Счетчик для уникальных имен форматных строк

    def _config_llvm(self):
        """Настройка LLVM"""
        self.module = ir.Module(name="js_compiler")
        self.module.triple = self.binding.get_default_triple()

        # Создаем функцию main
        func_type = ir.FunctionType(ir.IntType(32), [], False)
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def _create_execution_engine(self):
        """Создание ExecutionEngine"""
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_mod = self.binding.parse_assembly("")
        self.engine = self.binding.create_mcjit_compiler(backing_mod, target_machine)

    def _declare_print_function(self):
        """Объявление функции printf"""
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    def _create_format_string(self, value):
        """Создание форматной строки для printf"""
        self.counter += 1
        fmt_name = f"fstr_{self.counter}"

        # Создаем строку формата "%d\n\0"
        fmt = "%d\n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))

        # Создаем глобальную переменную для форматной строки
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=fmt_name)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt

        # Возвращаем указатель на форматную строку
        voidptr_ty = ir.IntType(8).as_pointer()
        return self.builder.bitcast(global_fmt, voidptr_ty)

    def visit(self, node):
        """Посетитель для узлов AST"""
        if node is None:
            return None

        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    def visit_Number(self, node):
        """Обработка чисел"""
        return ir.Constant(ir.IntType(32), int(node.value))

    def visit_Variable(self, node):
        """Обработка переменных"""
        if node.name in self.variables:
            # Загружаем значение из памяти
            return self.builder.load(self.variables[node.name])
        else:
            # Переменная не определена, возвращаем 0
            return ir.Constant(ir.IntType(32), 0)

    def visit_Sum(self, node):
        """Обработка сложения"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.add(left, right)

    def visit_Sub(self, node):
        """Обработка вычитания"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.sub(left, right)

    def visit_Mul(self, node):
        """Обработка умножения"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.mul(left, right)

    def visit_Div(self, node):
        """Обработка деления"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.sdiv(left, right)

    def visit_Assign(self, node):
        """Обработка присваивания"""
        # Вычисляем значение
        value = self.visit(node.right)

        # Получаем имя переменной
        var_name = node.left.name

        # Выделяем память для переменной (если еще не выделена)
        if var_name not in self.variables:
            ptr = self.builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = ptr

        # Сохраняем значение
        self.builder.store(value, self.variables[var_name])
        return value

    def visit_Equals(self, node):
        """Обработка сравнения на равенство"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.icmp_signed('==', left, right)

    def visit_LessThan(self, node):
        """Обработка сравнения 'меньше'"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.icmp_signed('<', left, right)

    def visit_GreaterThan(self, node):
        """Обработка сравнения 'больше'"""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self.builder.icmp_signed('>', left, right)

    def visit_WhileLoop(self, node):
        """Обработка цикла while"""
        # Создаем блоки для цикла
        cond_block = self.main_func.append_basic_block(name="while_cond")
        body_block = self.main_func.append_basic_block(name="while_body")
        end_block = self.main_func.append_basic_block(name="while_end")

        # Переходим к проверке условия
        self.builder.branch(cond_block)

        # Блок проверки условия
        self.builder.position_at_end(cond_block)
        cond_value = self.visit(node.condition)
        self.builder.cbranch(cond_value, body_block, end_block)

        # Тело цикла
        self.builder.position_at_end(body_block)
        self.visit(node.body)
        # Возвращаемся к проверке условия
        self.builder.branch(cond_block)

        # Выход из цикла
        self.builder.position_at_end(end_block)
        return None

    def visit_Block(self, node):
        """Обработка блока кода"""
        result = None
        for stmt in node.statements:
            result = self.visit(stmt)
        return result

    def visit_Print(self, node):
        """Обработка команды print"""
        # Вычисляем значение для печати
        value = self.visit(node.value)

        # Создаем форматную строку
        fmt_ptr = self._create_format_string(value)

        # Вызываем printf
        self.builder.call(self.printf, [fmt_ptr, value])
        return value

    def visit_Boolean(self, node):
        """Обработка булевых значений"""
        return ir.Constant(ir.IntType(1), 1 if node.value.lower() == 'true' else 0)

    def create_ir(self, ast):
        """Создание IR для AST"""
        self.visit(ast)
        # Возвращаем 0 из main
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        # Валидация
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()

        # Добавляем в движок
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()

        return mod

    def save_ir(self, filename):
        """Сохранение IR в файл"""
        with open(filename, 'w') as f:
            f.write(str(self.module))
        print(f"LLVM IR сохранен в {filename}")

    def run(self):
        """Запуск скомпилированного кода"""
        func_ptr = self.engine.get_function_address("main")

        import ctypes
        cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(func_ptr)
        result = cfunc()
        print(f"Код завершился с результатом: {result}")
        return result