from rply import ParserGenerator
from ast import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator([
            'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
            'SUM', 'SUB', 'NUMBER', 'SEMI_COLON'
        ])

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        # Базовые правила для выражений
        @self.pg.production('expression : term')
        def expression_term(p):
            return p[0]

        @self.pg.production('expression : expression SUM term')
        @self.pg.production('expression : expression SUB term')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        # (чтобы учесть приоритет, если будут * и /)
        @self.pg.production('term : NUMBER')
        def term_number(p):
            return Number(p[0].value)

        @self.pg.production('term : OPEN_PAREN expression CLOSE_PAREN')
        def term_paren(p):
            return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Неожиданный токен {token}")

    def get_parser(self):
        return self.pg.build()