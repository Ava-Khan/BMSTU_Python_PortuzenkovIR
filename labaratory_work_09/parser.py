from rply import ParserGenerator
from ast import *

class Parser:

    def __init__(self):
        self.pg = ParserGenerator([
            'NUMBER', 'STRING', 'IDENTIFIER', 'FUNCTION_CALL',
            'LET', 'IF', 'ELSE', 'WHILE', 'TRUE', 'FALSE', 'RETURN',
            'ASSIGN', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
            'EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'GREATER_THAN',
            'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACE', 'CLOSE_BRACE',
            'SEMI_COLON', 'COMMA'
        ])

    def parse(self):
        @self.pg.production('program : statements')
        def program(p):
            return Block(p[0])

        @self.pg.production('statements : statement')
        @self.pg.production('statements : statement statements')
        def statements(p):
            if len(p) == 1:
                return [p[0]]
            return [p[0]] + p[1]

        @self.pg.production('statement : expression SEMI_COLON')
        @self.pg.production('statement : variable_declaration SEMI_COLON')
        @self.pg.production('statement : if_statement')
        @self.pg.production('statement : while_statement')
        @self.pg.production('statement : block_statement')
        @self.pg.production('statement : function_call SEMI_COLON')
        def statement(p):
            return p[0]

        @self.pg.production('variable_declaration : LET IDENTIFIER ASSIGN expression')
        def variable_declaration(p):
            return Assign(Variable(p[1].value), p[3])

        @self.pg.production('block_statement : OPEN_BRACE statements CLOSE_BRACE')
        def block_statement(p):
            return Block(p[1])

        @self.pg.production('if_statement : IF OPEN_PAREN expression CLOSE_PAREN statement')
        @self.pg.production('if_statement : IF OPEN_PAREN expression CLOSE_PAREN statement ELSE statement')
        def if_statement(p):
            if len(p) == 5:
                return IfStatement(p[2], p[4])
            else:
                return IfStatement(p[2], p[4], p[6])

        @self.pg.production('while_statement : WHILE OPEN_PAREN expression CLOSE_PAREN statement')
        def while_statement(p):
            return WhileLoop(p[2], p[4])

        @self.pg.production('function_call : FUNCTION_CALL arguments CLOSE_PAREN')
        def function_call(p):
            func_name = p[0].value[:-1]  # Убираем открывающую скобку
            return FunctionCall(func_name, p[1])

        @self.pg.production('arguments : ')
        @self.pg.production('arguments : expression')
        @self.pg.production('arguments : expression COMMA arguments')
        def arguments(p):
            if len(p) == 0:
                return []
            if len(p) == 1:
                return [p[0]]
            return [p[0]] + p[2]

        @self.pg.production('expression : NUMBER')
        def expression_number(p):
            return Number(p[0].value)

        @self.pg.production('expression : STRING')
        def expression_string(p):
            return String(p[0].value)

        @self.pg.production('expression : TRUE')
        @self.pg.production('expression : FALSE')
        def expression_boolean(p):
            return Boolean(p[0].value)

        @self.pg.production('expression : IDENTIFIER')
        def expression_variable(p):
            return Variable(p[0].value)

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MULTIPLY expression')
        @self.pg.production('expression : expression DIVIDE expression')
        @self.pg.production('expression : expression EQUALS expression')
        @self.pg.production('expression : expression NOT_EQUALS expression')
        @self.pg.production('expression : expression LESS_THAN expression')
        @self.pg.production('expression : expression GREATER_THAN expression')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            op = p[1]

            op_map = {
                'PLUS': Sum,
                'MINUS': Sub,
                'MULTIPLY': Mul,
                'DIVIDE': Div,
                'EQUALS': Equals,
                'NOT_EQUALS': NotEquals,
                'LESS_THAN': LessThan,
                'GREATER_THAN': GreaterThan
            }

            return op_map[op.gettokentype()](left, right)

        @self.pg.production('expression : IDENTIFIER ASSIGN expression')
        def expression_assign(p):
            return Assign(Variable(p[0].value), p[2])

        @self.pg.production('expression : expression NOT_EQUALS expression')
        def expression_not_equeals(p):
            left = p[0]
            right = p[2]
            return NotEquals(left, right)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_paren(p):
            return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Неожиданный токен {token}")

        @self.pg.production('statement : RETURN expression SEMI_COLON')
        @self.pg.production('statement : RETURN SEMI_COLON')
        def return_statement(p):
            if len(p) == 3:
                return Return(p[1])
            else:
                return Return(None)

    def get_parser(self):
        return self.pg.build()