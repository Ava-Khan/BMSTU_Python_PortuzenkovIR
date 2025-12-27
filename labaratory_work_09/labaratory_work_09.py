from lexer import Lexer
from parser import Parser
from codegen import CodeGen

code = """
let x = 5;
let y = 3;
let sum = x + y;
print(sum);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(code)

pg = Parser()
pg.parse()
parser = pg.get_parser()
ast = parser.parse(tokens)

codegen = CodeGen()
codegen.create_ir(ast)

codegen.save_ir("output.ll")

codegen.run()
