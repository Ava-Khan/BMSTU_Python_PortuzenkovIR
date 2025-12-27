from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):


        # 1. Ключевые слова (должны быть ПЕРЕД идентификаторами!)
        self.lexer.add("LET", r"let")
        self.lexer.add("WHILE", r"while")
        self.lexer.add("IF", r"if")
        self.lexer.add("ELSE", r"else")
        self.lexer.add("TRUE", r"true")
        self.lexer.add("FALSE", r"false")
        self.lexer.add("RETURN", r"return")
        self.lexer.add("PRINT", r"print")

        # 2. Литералы
        self.lexer.add("NUMBER", r"\d+")
        self.lexer.add("STRING", r'"[^"]*"')

        # 3. Операторы и разделители
        self.lexer.add("ASSIGN", r"=")
        self.lexer.add("PLUS", r"\+")
        self.lexer.add("MINUS", r"-")
        self.lexer.add("MULTIPLY", r"\*")
        self.lexer.add("DIVIDE", r"/")
        self.lexer.add("EQUALS", r"==")
        self.lexer.add("NOT_EQUALS", r"!=")
        self.lexer.add("LESS_THAN", r"<")
        self.lexer.add("GREATER_THAN", r">")
        self.lexer.add("LESS_EQUAL", r"<=")
        self.lexer.add("GREATER_EQUAL", r">=")

        self.lexer.add("OPEN_PAREN", r"\(")
        self.lexer.add("CLOSE_PAREN", r"\)")
        self.lexer.add("OPEN_BRACE", r"\{")
        self.lexer.add("CLOSE_BRACE", r"\}")
        self.lexer.add("SEMI_COLON", r";")
        self.lexer.add("COMMA", r",")

        self.lexer.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")

        # 4. Игнорируемые символы
        self.lexer.ignore(r"\s+")
        self.lexer.ignore(r"//[^\n]*\n?")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()