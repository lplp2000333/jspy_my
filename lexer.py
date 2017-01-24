import ply.lex as lex

class Lexer(object):
    def __init__(self):
        self.lexer = lex.lex(debug=True, module=self)

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    keywords = ('IF',)
    keyword_map = {}
    for r in keywords:
        keyword_map[r.lower()] = r

    tokens = keywords + ('ID', 'NUMBER', 'TRUE', 'FALSE',
       'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
        'SEMICOLON',

        # Assignment operators
        'EQUALS'
    )

    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'/'
    t_MOD       = r'%'    

    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_LBRACE    = r'\{'
    t_RBRACE    = r'\}'
    t_SEMICOLON = r';' 

    t_EQUALS    = r'='

    def t_TRUE(self, t):
        r'true'
        t.value = True
        return t

    def t_FALSE(self, t):
        r'false'
        t.value = False
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.keyword_map.get(t.value, 'ID')
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    def t_NUMBER(self, t):
        r'\d+'
        t.value = float(t.value)
        return t

    t_ignore = ' \t'

    def t_error(self, t):
        print 'Error at %s line %d' % (t.value[0], t.lexer.lineno)
        t.lexer.skip(1)

if __name__ == "__main__":
    l = Lexer()
    l.input("if(1){a=10;}")
    while True:
        tok = l.token()
        if not tok:
            break
        print tok


