from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Ключевые слова
        self.lexer.add("LET", r"let")
        self.lexer.add("CONST", r"const")
        self.lexer.add("IF", r"if")
        self.lexer.add("ELSE", r"else")
        self.lexer.add("WHILE", r"while")
        self.lexer.add("TRUE", r"true")
        self.lexer.add("FALSE", r"false")
        self.lexer.add("FUNCTION", r"function")
        self.lexer.add("RETURN", r"return")
        self.lexer.add("PRINT", r"print")

        # Идентификаторы и функции
        self.lexer.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")
        self.lexer.add("FUNCTION_CALL", r"console\.log|[a-zA-Z_][a-zA-Z0-9_]*\(")

        # Литералы
        self.lexer.add("NUMBER", r"\d+")
        self.lexer.add("STRING", r"\"[^\"]*\"|'[^']*'")

        # Операторы
        self.lexer.add("ASSIGN", r"=")
        self.lexer.add("SUM", r"\+")
        self.lexer.add("SUB", r"\-")
        self.lexer.add("MULTIPLY", r"\*")
        self.lexer.add("DIVIDE", r"\/")
        self.lexer.add("EQUALS", r"==")
        self.lexer.add("NOT_EQUALS", r"!=")
        self.lexer.add("LESS_THAN", r"<")
        self.lexer.add("GREATER_THAN", r">")

        # Скобки и разделители
        self.lexer.add("OPEN_PAREN", r"\(")
        self.lexer.add("CLOSE_PAREN", r"\)")
        self.lexer.add("OPEN_BRACE", r"\{")
        self.lexer.add("CLOSE_BRACE", r"\}")
        self.lexer.add("SEMI_COLON", r";")
        self.lexer.add("COMMA", r",")

        # Игнорируем пробелы и комментарии
        self.lexer.ignore(r"\s+")
        self.lexer.ignore(r"//[^\n]*\n?")
        self.lexer.ignore(r"/\*.*?\*/")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()