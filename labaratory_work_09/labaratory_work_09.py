from lexer import Lexer
from parser import Parser

# Самый простой тест
code = "print(2+2);"  # Проще некуда!

lexer = Lexer().get_lexer()
pg = Parser()
pg.parse()
parser = pg.get_parser()

tokens = lexer.lex(code)
ast = parser.parse(tokens)
ast.eval({})