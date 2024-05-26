from ply import lex


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
    'end': 'END',
}

tokens = [
    'ID',
    'CTE_INT',
    'CTE_FLOAT', 
    'CTE_STRING',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPARENTH',
    'RPARENTH',
    'LBRACE',
    'RBRACE',
    'LESSTHAN',
    'GREATERTHAN',
    'EQUAL',
    'NOTEQUAL',
    'COMMA',
    'COLON',
    'SEMICOLON',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_LPARENTH = r'\('
t_RPARENTH = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_EQUAL = r'='
t_NOTEQUAL = r'!='
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';' 
t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTE_FLOAT(t):
    r'[-]?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'[-]?\d+'
    t.value = int(t.value)
    return t

def t_CTE_STRING(t):
    r'"(\\.|[^"\\])*"'
    t.value = t.value.strip('"')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    program programa1;
    var a: int, b: float;
    b = 4.56;
    main {
        print("Hello World!");
        if (x = 1) {
            print("x is equal to 1");
        }
    }
    end
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)