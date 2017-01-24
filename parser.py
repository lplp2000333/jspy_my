import ply.yacc
from lexer import Lexer

class Parser(object):
    def __init__(self, lexer=None, start='program', debug=False):
        self.tokens = lexer.tokens
        self.lexer = lexer
        self.parser = ply.yacc.yacc(module=self, start=start, debug=debug)








