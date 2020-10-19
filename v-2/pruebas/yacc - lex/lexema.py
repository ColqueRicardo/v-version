import ply.lex as lex

# Declaración de palabras reservadas

reserved = {

    'public': 'public',

    'private': 'private',

    'static': 'static',

    'final': 'final',

    'void': 'void',

    'main': 'main',

    'class': 'class',

    'while': 'while',

    'if': 'if',

    'else': 'else',

}
# Declaración de tokens

tokens = ['TIPODATO', 'ABREPARENT', 'CIERRAPARENT', 'PUNTOCOMA', 'ABRELLAVE', 'CIERRALLAVE', 'ID', 'IGUAL', 'PUNTO', 'COMA',
          'ABRECORCHETE', 'CIERRACORCHETE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'LT', 'GT',
          'LE', 'GE', 'EQ', 'NE','COMILLA'] + list(reserved.values())


# Definición de tokens


# Comments


def t_commentario(t):
    r'/[\*][a-zA-Z0-9\n]*[\*]/'
    t.lexer.lineno += t.value.count('\n')

    pass


def t_ID(t):
    r'[a-zA-Z]+[a-zA-Z0-9_]*'

    t.type = reserved.get(t.value, 'ID')

    return t



def t_TIPODATO(t):

    r'char|byte|double'

    return t


t_COMILLA = r'\''
t_ABREPARENT = r'\('

t_CIERRAPARENT = r'\)'

t_PUNTOCOMA = r'\;'

t_ABRELLAVE = r'\{'

t_CIERRALLAVE = r'\}'

t_IGUAL = r'='

t_COMA = r','

t_PUNTO = r'\.'

t_ABRECORCHETE = r'\['

t_CIERRACORCHETE = r'\]'

# Operators

t_PLUS = r'\+'

t_MINUS = r'-'

t_TIMES = r'\*'

t_MOD = r'%'

t_LT = r'<'

t_GT = r'>'

t_LE = r'<='

t_GE = r'>='

t_EQ = r'=='

t_NE = r'!='


# Tokens a ignorar

t_ignore = " \t"

# Función error

def t_error(t):
    print("Error Lexico: %s" % repr(t.value[0]))

    lex.lexer.skip(1)

# Contador de línea

def t_newline(t):
    r';\n'

    t.lexer.lineno += 1



# Construcción del lexer

lexer = lex.lex()
while True:
    text= input()
    lexer.input(text)
    while True:
       tok = lexer.token()
       if not tok: break
       print(tok)
