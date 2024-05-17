INT = 'int'
FLOAT = 'float'
STRING = 'string'
BOOL = 'bool'

ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'
GT = '>'
LT = '<'
EQ = '=='
NEQ = '!='


semanticCube = {
    INT: {
        ADD: { INT: INT, FLOAT: FLOAT, STRING: None },
        SUB: { INT: INT, FLOAT: FLOAT, STRING: None },
        MUL: { INT: INT, FLOAT: FLOAT, STRING: None },
        DIV: { INT: FLOAT, FLOAT: FLOAT, STRING: None },
        GT:  { INT: BOOL, FLOAT: BOOL, STRING: None },
        LT:  { INT: BOOL, FLOAT: BOOL, STRING: None },
        EQ:  { INT: BOOL, FLOAT: BOOL, STRING: None },
        NEQ: { INT: BOOL, FLOAT: BOOL, STRING: None },
    },
    FLOAT: {
        ADD: { INT: FLOAT, FLOAT: FLOAT, STRING: None },
        SUB: { INT: FLOAT, FLOAT: FLOAT, STRING: None },
        MUL: { INT: FLOAT, FLOAT: FLOAT, STRING: None },
        DIV: { INT: FLOAT, FLOAT: FLOAT, STRING: None },
        GT:  { INT: BOOL, FLOAT: BOOL, STRING: None },
        LT:  { INT: BOOL, FLOAT: BOOL, STRING: None },
        EQ:  { INT: BOOL, FLOAT: BOOL, STRING: None },
        NEQ: { INT: BOOL, FLOAT: BOOL, STRING: None },
    },
    STRING: {
        ADD: { INT: None, FLOAT: None, STRING: STRING },
        SUB: { INT: None, FLOAT: None, STRING: None },
        MUL: { INT: None, FLOAT: None, STRING: None },
        DIV: { INT: None, FLOAT: None, STRING: None },
        GT:  { INT: None, FLOAT: None, STRING: BOOL },
        LT:  { INT: None, FLOAT: None, STRING: BOOL },
        EQ:  { INT: None, FLOAT: None, STRING: BOOL },
        NEQ: { INT: None, FLOAT: None, STRING: BOOL },
    }
}

def getType(left, op, right):
    return semanticCube.get(left, {}).get(op, {}).get(right, {})