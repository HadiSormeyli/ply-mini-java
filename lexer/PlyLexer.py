from ply.lex import TOKEN

tokens = ['AND',
          'ASSIGNMENT',
          'COMMA',
          'LINECOMMENT',
          'MULTILINECOMMENT',
          'RIGHTSQRBRACKET',
          'LEFTSQRBRACKET',
          'DIVISION',
          'NOTEQUAL',
          'CONCAT',
          'EQUAL',
          'NOT',
          'IDEN',
          'RIGHTBRACE',
          'LEFTBRACE',
          'GREATEREQUAL',
          'GREATER',
          'LESSEQUAL',
          'LESS',
          'SUBSTRACTION',
          'UMINUS',
          'MULTIPLICATION',
          'NUMBER',
          'CIENTIFIC',
          'FLOAT',
          'OR',
          'RIGHTPARENT',
          'LEFTPARENT',
          'MODULO',
          'DOT',
          'SEMICOLON',
          'ADDITION'
          ]


reserved = {
    'boolean':'BOOLEAN',
    'class' : 'CLASS',
    'else' : 'ELSE',
    'false' : 'FALSE',
    'if' : 'IF',
    'int' : 'INT',
    'new' : 'NEW',
    'return' : 'RETURN',
    'this' : 'THIS',
    'true' : 'TRUE',
    'void' : 'VOID',
    'while' : 'WHILE',
    'private' : 'PRIVATE',
    'public' : 'PUBLIC',
    'static' : 'STATIC'
}


tokens += reserved.values()


t_AND = r'(\&\&|AND)'
t_ASSIGNMENT = r'='
t_COMMA = r','
t_LEFTSQRBRACKET = r'\['
t_RIGHTSQRBRACKET = r'\]'
t_DIVISION = r'\/'
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_NOT = r'!'
t_LEFTBRACE  = r'\{'
t_RIGHTBRACE = r'\}'
t_GREATEREQUAL = r'>='
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_LESS = r'<'
t_SUBSTRACTION = r'\-'
t_UMINUS = r'\-'
t_CONCAT = r'\+'
t_MULTIPLICATION = r'\*'
t_OR = r'(\|\|)|(OR)'
t_LEFTPARENT = r'\('
t_RIGHTPARENT = r'\)'
t_MODULO = r'%'
t_DOT = r'\.'
t_SEMICOLON = r';'
t_ADDITION = '\+'

def t_NUMBER(t):
    r'(-)?(\d+)'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR CONVERSION NUMERO %d", t.value)
        t.value = 0
    return t

def t_IDEN(t):
    r'[_a-zA-Z_]([a-zA-Z_0-9]*[a-zA-Z])?'
    t.type = reserved.get(t.value,'IDEN')
    if len(t.value)>20:
        t.value = t.value[:20]
    return t

def t_ignore_LINECOMMENT(t):
    r'//(.)*(\n)?'

def t_ignore_MULTILINECOMMENT(t):
    r'(/\*)(.|\n|\r)*(\*\/)'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    line = t.lexer.lineno
    print("Character %s not recognized at line %d" % (t.value[0], line))
    t.lexer.skip(1)
    

