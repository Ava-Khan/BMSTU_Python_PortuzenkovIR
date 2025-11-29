class Number:
    def init(self, value):
        self.value = value

    def eval(self, context):
        return int(self.value)

class String:
    def init(self, value):
        self.value = value

    def eval(self, context):
        return str(self.value[1:-1])  # Убираем кавычки

class Boolean:
    def init(self, value):
        self.value = value

    def eval(self, context):
        return self.value.lower() == 'true'

class Variable:
    def init(self, name):
        self.name = name

    def eval(self, context):
        return context.get(self.name)

class BinaryOp:
    def init(self, left, right):
        self.left = left
        self.right = right

class Sum(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) + self.right.eval(context)

class Sub(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) - self.right.eval(context)

class Mul(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) * self.right.eval(context)

class Div(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) / self.right.eval(context)

class Assign(BinaryOp):
    def eval(self, context):
        value = self.right.eval(context)
        context[self.left.name] = value
        return value

class Equals(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) == self.right.eval(context)

class NotEquals(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) != self.right.eval(context)

class LessThan(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) < self.right.eval(context)

class GreaterThan(BinaryOp):
    def eval(self, context):
        return self.left.eval(context) > self.right.eval(context)

class Print:
    def init(self, value):
        self.value = value

    def eval(self, context):
        print(self.value.eval(context))

class IfStatement:
    def init(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def eval(self, context):
        if self.condition.eval(context):
            return self.then_branch.eval(context)
        elif self.else_branch:
            return self.else_branch.eval(context)
        return None

class WhileLoop:
    def init(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self, context):
        result = None
        while self.condition.eval(context):
            result = self.body.eval(context)
        return result

class Block:
    def init(self, statements):
        self.statements = statements

    def eval(self, context):
        result = None
        for statement in self.statements:
            result = statement.eval(context)
        return result

class FunctionCall:
    def init(self, name, args):
        self.name = name
        self.args = args

    def eval(self, context):
        # Базовая реализация встроенных функций
        if self.name == 'console.log':
            values = [arg.eval(context) for arg in self.args]
            print(*values)
            return None
        return None

class Return:
    def __init__(self, value):