from rply import ParserGenerator
from ast import Number, Sym, Sub, Print


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', '/.for ']
        )