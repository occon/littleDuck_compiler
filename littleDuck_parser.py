import ply.yacc as yacc
from littleDuck_lexer import tokens
from littleDuck_symbolTable import FuncDirectory, VarTable
from littleDuck_semanticCube import SemanticCube

funDir = FuncDirectory()
vars = VarTable()
semCube = SemanticCube()
currFunc = None

def p_programa(p):
    '''
    Programa : PROGRAM ID SEMICOLON VARS FUNCS MAIN Body END SEMICOLON
    '''
    p[0] = ('programa', p[2], p[4], p[5], p[7])
    funDir.addFunc('main', 'void')

def p_vars(p):
    '''
    VARS : VAR ListaVars COLON TYPE SEMICOLON
         | 
    '''
    p[0] = (p[2], p[4]) if len(p) == 6 else None

def p_lista_vars(p):
    '''
    ListaVars : ID COMMA ListaVars
              | ID
    '''
    if len(p) == 4:
        vars.addVar(p[1], p[3])
    elif len(p) == 5:
        vars.addVar(p[1], p[3])

def p_type(p):
    '''
    TYPE : INT
         | FLOAT
         | STRING
    '''
    p[0] = p[1]

def p_funcs(p):
    '''
    FUNCS : Funcion FUNCS
          | 
    '''
    p[0] = (p[1], p[2]) if len(p) == 3 else None


def p_funcion(p):
    '''
    Funcion : TipoFunc ID LPARENTH Parametros RPARENTH COLON Body
    '''
    global currFunc
    currFunc = p[2]
    funDir.addFunc(p[2], p[1])
    p[0] = ('funcion', p[1], p[2], p[4], p[7])

def p_tipofunc(p):
    '''
    TipoFunc : VOID
             | TYPE
    '''
    p[0] = p[1]

def p_parametros(p):
    '''
    Parametros : ID COMMA Parametros
               | ID COLON TYPE
               | 
    '''
    if len(p) == 4:
        vars.addVar(p[1], p[3])

def p_body(p):
    '''
    Body : LBRACE Statements RBRACE
    '''
    p[0] = p[2]

def p_statements(p):
    '''
    Statements : Statement Statements
               | 
    '''
    p[0] = (p[1], p[2]) if len(p) > 1 else None

def p_statement(p):
    '''
    Statement : ASSIGN
              | CONDITION
              | CYCLE
              | F_Call
              | Print
    '''
    p[0] = p[1]

def p_assign(p):
    '''
    ASSIGN : ID EQUAL Expresion SEMICOLON
    '''
    varType = vars.variables.get(p[1], None)
    expType = p[3]
    resType = semCube.getType(varType, '=', expType)
    p[0] = ('assign', p[1], p[3], resType)

def p_condition(p):
    '''
    CONDITION : IF LPARENTH Expresion RPARENTH Body 
              | IF LPARENTH Expresion RPARENTH Body ELSE Body
    '''
    p[0] = ('condition', p[3], p[5], p[7])

def p_cycle(p):
    '''
        CYCLE : WHILE LPARENTH Expresion RPARENTH Body SEMICOLON
              | DO Body WHILE LPARENTH Expresion RPARENTH SEMICOLON
    '''
    p[0] = ('cycle', p[3], p[5])

def p_f_call(p):
    '''
    F_Call : ID LPARENTH Expresiones RPARENTH SEMICOLON
    '''
    p[0] = ('f_call', p[1], p[3])

def p_expresiones(p):
    '''
    Expresiones : Expresion COMMA Expresiones
                | Expresion
                | 
    '''
    p[0] = (p[1], p[3]) if len(p) > 2 else p[1]

def p_print(p):
    '''
    Print : PRINT LPARENTH Expresiones RPARENTH SEMICOLON
    '''
    p[0] = ('print', p[3])

def p_expresion(p):
    '''
    Expresion : Expresion GREATERTHAN Exp
              | Expresion LESSTHAN Exp
              | Expresion NOTEQUAL Exp
              | Exp
    '''
    if len(p) == 4:
        resType = semCube.getType(p[1], p[2], p[3])
        p[0] = resType
    else:
        p[0] = p[1]

def p_exp(p):
    '''
    Exp : Exp PLUS Termino
        | Exp MINUS Termino
        | Termino
    '''
    if len(p) == 4:
        resType = semCube.getType(p[1], p[2], p[3])
        p[0] = resType
    else:
        p[0] = p[1]
    
def p_termino(p):
    '''
    Termino : Termino MULTIPLY Factor
            | Termino DIVIDE Factor
            | Factor
    '''
    if len(p) == 4:
        resType = semCube.getType(p[1], p[2], p[3])
        p[0] = resType
    else:
        p[0] = p[1]

def p_factor(p):
    '''
    Factor : LPARENTH Expresion RPARENTH
           | PLUS Subf
           | MINUS Subf
           | Subf
    '''
    if len(p) == 4:
        p[0] = p[2]    
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else : 
        p[0] = p[1]

def p_subf(p):
    '''
    Subf : CTE
         | ID
    '''
    p[0] = p[1]

def p_cte(p):
    '''
    CTE : CTE_INT
        | CTE_FLOAT
        | CTE_STRING
    '''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at END OF FILE")

parser = yacc.yacc()

if __name__ == '__main__':
    data = '''
    program programa2;
    var x: int;
    main {
        print("Hello World!");
    }
    end;
    '''
    res = parser.parse(data)
    print(res)
