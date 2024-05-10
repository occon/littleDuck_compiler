import ply.lex as lex

tokens = [
    'cteInt',
    'cteFloat', 
    'cteChar',
    'cteString',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPARENTH',
    'RPARENTH',
]

reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'void': 'VOID',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'do': 'DO',
    'end': 'END'
}

operators = [ '+', '-', '*', '/' ]

tokens += list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_LPARENTH = r'\('
t_RPARENTH = r'\)'

t_ignore    = ' \t'

def t_cteInt(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_cteFloat(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_cteString(t):
    r'"(\\.|[^"\\])*"'
    t.value = str(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
  + -20 *2
'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
