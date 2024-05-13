import os
import sys
import pytest

# Añade la carpeta raíz (un nivel arriba) al `sys.path`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa el lexer correctamente ahora
from littleDuck_lexer import lexer

# Función para procesar un texto con el lexer
def tokenize(input_text):
    lexer.input(input_text)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

# Función para comparar un token con los valores esperados
def assert_token(token, expected_type, expected_value):
    assert token.type == expected_type
    assert token.value == expected_value

# Prueba 1: Comprobación de palabras reservadas y delimitadores
def test_reserved_keywords_and_delimiters():
    data = 'program main; var x : int;'
    tokens = tokenize(data)
    assert_token(tokens[0], 'PROGRAM', 'program')
    assert_token(tokens[1], 'MAIN', 'main')
    assert_token(tokens[2], 'SEMICOLON', ';')
    assert_token(tokens[3], 'VAR', 'var')
    assert_token(tokens[4], 'ID', 'x')
    assert_token(tokens[5], 'COLON', ':')
    assert_token(tokens[6], 'INT', 'int')
    assert_token(tokens[7], 'SEMICOLON', ';')

# Prueba 2: Expresiones aritméticas
def test_arithmetic_expressions():
    data = 'x = 3 + 5 * (10 - 2);'
    tokens = tokenize(data)
    assert_token(tokens[0], 'ID', 'x')
    assert_token(tokens[1], 'EQUAL', '=')
    assert_token(tokens[2], 'CTE_INT', 3)
    assert_token(tokens[3], 'PLUS', '+')
    assert_token(tokens[4], 'CTE_INT', 5)
    assert_token(tokens[5], 'MULTIPLY', '*')
    assert_token(tokens[6], 'LPARENTH', '(')
    assert_token(tokens[7], 'CTE_INT', 10)
    assert_token(tokens[8], 'MINUS', '-')
    assert_token(tokens[9], 'CTE_INT', 2)
    assert_token(tokens[10], 'RPARENTH', ')')
    assert_token(tokens[11], 'SEMICOLON', ';')

# Prueba 3: Literales de tipo flotante y cadenas
def test_floats_and_strings():
    data = 'var x : float; x = 4.56; print("Pancho!");'
    tokens = tokenize(data)
    assert_token(tokens[0], 'VAR', 'var')
    assert_token(tokens[1], 'ID', 'x')
    assert_token(tokens[2], 'COLON', ':')
    assert_token(tokens[3], 'FLOAT', 'float')
    assert_token(tokens[4], 'SEMICOLON', ';')
    assert_token(tokens[5], 'ID', 'x')
    assert_token(tokens[6], 'EQUAL', '=')
    assert_token(tokens[7], 'CTE_FLOAT', 4.56)
    assert_token(tokens[8], 'SEMICOLON', ';')
    assert_token(tokens[9], 'PRINT', 'print')
    assert_token(tokens[10], 'LPARENTH', '(')
    assert_token(tokens[11], 'CTE_STRING', 'Pancho!')
    assert_token(tokens[12], 'RPARENTH', ')')
    assert_token(tokens[13], 'SEMICOLON', ';')

# Prueba 4: Estructuras condicionales
def test_conditionals():
    data = 'if (x != 5) { print("No da 5"); } else { print("Da 5"); }'
    tokens = tokenize(data)
    assert_token(tokens[0], 'IF', 'if')
    assert_token(tokens[1], 'LPARENTH', '(')
    assert_token(tokens[2], 'ID', 'x')
    assert_token(tokens[3], 'NOTEQUAL', '!=')
    assert_token(tokens[4], 'CTE_INT', 5)
    assert_token(tokens[5], 'RPARENTH', ')')
    assert_token(tokens[6], 'LBRACE', '{')
    assert_token(tokens[7], 'PRINT', 'print')
    assert_token(tokens[8], 'LPARENTH', '(')
    assert_token(tokens[9], 'CTE_STRING', 'No da 5')
    assert_token(tokens[10], 'RPARENTH', ')')
    assert_token(tokens[11], 'SEMICOLON', ';')
    assert_token(tokens[12], 'RBRACE', '}')
    assert_token(tokens[13], 'ELSE', 'else')
    assert_token(tokens[14], 'LBRACE', '{')
    assert_token(tokens[15], 'PRINT', 'print')
    assert_token(tokens[16], 'LPARENTH', '(')
    assert_token(tokens[17], 'CTE_STRING', 'Da 5')
    assert_token(tokens[18], 'RPARENTH', ')')
    assert_token(tokens[19], 'SEMICOLON', ';')
    assert_token(tokens[20], 'RBRACE', '}')

if __name__ == '__main__':
    pytest.main([__file__])