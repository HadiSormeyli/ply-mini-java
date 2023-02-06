import ply.lex as lex
import ply.yacc as yacc
from lexer.PlyLexer import * 
from parser.PlyParser import * 
from semantic.SymbolTable import SymbolTable  
from code_generation.CodeGenrator import CodeGenerator


file = open("test.java", "r")

input = file.readlines()
input = "".join(input)


lexer = lex.lex(debug=False)

lexer.input(input)


while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)




yacc.yacc(method='SLR')
tree = yacc.parse(input, debug=False)


symbolTable = SymbolTable(tree)

codeGenerator = CodeGenerator()
print(codeGenerator.visit(tree))

