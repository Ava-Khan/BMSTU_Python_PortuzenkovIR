from rply import ParserGenerator
from astt import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator([
            'NUMBER', 'IDENTIFIER',
            'LET', 'WHILE', 'TRUE', 'FALSE', 'PRINT',
            'ASSIGN', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
            'EQUALS', 'LESS_THAN', 'GREATER_THAN',
            'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACE', 'CLOSE_BRACE',
            'SEMI_COLON'
        ])

    def parse(self):
        @self.pg.production('program : statement_list')
        def program(p):
            return Block(p[0])

        @self.pg.production('statement_list : statement')
        @self.pg.production('statement_list : statement statement_list')
        def statement_list(p):
            if len(p) == 1:
                return [p[0]]
            return [p[0]] + p[1]

        # ============ ТИПЫ ИНСТРУКЦИЙ ============
        @self.pg.production('statement : expr_statement')
        @self.pg.production('statement : var_declaration')
        @self.pg.production('statement : while_statement')
        @self.pg.production('statement : block_statement')
        @self.pg.production('statement : print_statement')
        def statement(p):
            return p[0]

        # ============ PRINT ============
        @self.pg.production('print_statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def print_statement(p):
            return Print(p[2])

        # ============ ВЫРАЖЕНИЕ С ТОЧКОЙ ЗАПЯТОЙ ============
        @self.pg.production('expr_statement : expression SEMI_COLON')
        def expr_statement(p):
            return p[0]

        # ============ ОБЪЯВЛЕНИЕ ПЕРЕМЕННОЙ ============
        @self.pg.production('var_declaration : LET IDENTIFIER ASSIGN expression SEMI_COLON')
        def var_declaration(p):
            return Assign(Variable(p[1].value), p[3])

        # ============ ЦИКЛ WHILE ============
        @self.pg.production('while_statement : WHILE OPEN_PAREN expression CLOSE_PAREN statement')
        def while_statement(p):
            return WhileLoop(p[2], p[4])

        # ============ БЛОК ============
        @self.pg.production('block_statement : OPEN_BRACE statement_list CLOSE_BRACE')
        def block_statement(p):
            return Block(p[1])

        # ============ ВЫРАЖЕНИЯ ============

        # Базовые выражения
        @self.pg.production('expression : NUMBER')
        def expr_number(p):
            return Number(p[0].value)

        @self.pg.production('expression : IDENTIFIER')
        def expr_identifier(p):
            return Variable(p[0].value)

        @self.pg.production('expression : TRUE')
        @self.pg.production('expression : FALSE')
        def expr_boolean(p):
            return Boolean(p[0].value)

        # Присваивание
        @self.pg.production('expression : IDENTIFIER ASSIGN expression')
        def expr_assign(p):
            return Assign(Variable(p[0].value), p[2])

        # Скобки
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expr_paren(p):
            return p[1]

        # ============ БИНАРНЫЕ ОПЕРАЦИИ  ============

        # Сравнения
        @self.pg.production('expression : expression LESS_THAN expression')
        def expr_less(p):
            return LessThan(p[0], p[2])

        @self.pg.production('expression : expression GREATER_THAN expression')
        def expr_greater(p):
            return GreaterThan(p[0], p[2])

        @self.pg.production('expression : expression EQUALS expression')
        def expr_equals(p):
            return Equals(p[0], p[2])

        # Арифметика
        @self.pg.production('expression : expression PLUS expression')
        def expr_plus(p):
            return Sum(p[0], p[2])

        @self.pg.production('expression : expression MINUS expression')
        def expr_minus(p):
            return Sub(p[0], p[2])

        @self.pg.production('expression : expression MULTIPLY expression')
        def expr_multiply(p):
            return Mul(p[0], p[2])

        @self.pg.production('expression : expression DIVIDE expression')
        def expr_divide(p):
            return Div(p[0], p[2])

        # ============ ОШИБКИ ============
        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Синтаксическая ошибка: '{token.value}'")

    def get_parser(self):
        return self.pg.build()