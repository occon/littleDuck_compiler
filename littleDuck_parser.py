import ply.yacc as yacc
from littleDuck_lexer import tokens

def p_programa(p):
    '''
    Programa : PROGRAM ID SEMICOLON VARS FUNCS MAIN Body END SEMICOLON
    '''

def p_vars(p):
    '''
    VARS : VAR ListaVars COLON TYPE SEMICOLON
         | 
    '''

def p_lista_vars(p):
    '''
    ListaVars : ID COMMA ListaVars
              | ID
    '''

def p_type(p):
    '''
    TYPE : INT
         | FLOAT
         | STRING
    '''

def p_funcs(p):
    '''
    FUNCS : Funcion FUNCS
          | 
    '''

def p_funcion(p):
    '''
    Funcion : TipoFunc ID LPARENTH Parametros RPARENTH COLON Body
    '''

def p_tipofunc(p):
    '''
    TipoFunc : VOID
             | TYPE
    '''

def p_parametros(p):
    '''
    Parametros : ID COMMA Parametros
               | ID COLON TYPE
               | 
    '''

def p_body(p):
    '''
    Body : LBRACE Statements RBRACE
    '''

def p_statements(p):
    '''
    Statements : Statement Statements
               | 
    '''

def p_statement(p):
    '''
    Statement : ASSIGN
              | CONDITION
              | CYCLE
              | F_Call
              | Print
    '''

def p_assign(p):
    '''
    ASSIGN : ID EQUAL Expresion SEMICOLON
    '''

def p_condition(p):
    '''
    CONDITION : IF LPARENTH Expresion RPARENTH Body 
              | IF LPARENTH Expresion RPARENTH Body ELSE Body
    '''

def p_cycle(p):
    '''
        CYCLE : WHILE LPARENTH Expresion RPARENTH Body SEMICOLON
              | DO Body WHILE LPARENTH Expresion RPARENTH SEMICOLON
    '''

def p_f_call(p):
    '''
    F_Call : ID LPARENTH Expresiones RPARENTH SEMICOLON
    '''

def p_expresiones(p):
    '''
    Expresiones : Expresion COMMA Expresiones
                | Expresion
                | 
    '''

def p_print(p):
    '''
    Print : PRINT LPARENTH Expresiones RPARENTH SEMICOLON
    '''

def p_expresion(p):
    '''
    Expresion : Expresion GREATERTHAN Exp
              | Expresion LESSTHAN Exp
              | Expresion NOTEQUAL Exp
              | Exp
    '''

def p_exp(p):
    '''
    Exp : Exp PLUS Termino
        | Exp MINUS Termino
        | Termino
    '''

def p_termino(p):
    '''
    Termino : Termino MULTIPLY Factor
            | Termino DIVIDE Factor
            | Factor
    '''

def p_factor(p):
    '''
    Factor : LPARENTH Expresion RPARENTH
           | PLUS Subf
           | MINUS Subf
           | Subf
    '''

def p_subf(p):
    '''
    Subf : CTE
         | ID
    '''

def p_cte(p):
    '''
    CTE : CTE_INT
        | CTE_FLOAT
        | CTE_STRING
    '''

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
