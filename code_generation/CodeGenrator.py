from semantic.SymbolTable import *
from tree.Nodes import *


stack = {}

class CodeGenerator() :


    def __init__(self):
         self.curClass = None
         self.curMethod = None
         self.scope = 0


    def visit(self, tree):
        code = '\n'
        classDeclarationList = tree.ClassDeclarationList
        while type(classDeclarationList) != NullNode:
            code += self.visitClass(classDeclarationList.ClassDeclaration)
            classDeclarationList = classDeclarationList.ClassDeclarationList

        self.writeCode(code)
        return code

    def writeCode(self, code):
        file = open("code_generation\code.txt", "w")
        file.write(code)
        file.close()

    def visitClass(self, classDeclaration):
        code = ''
        self.curClass = classDeclaration

        address = self.getNextAddress()
        stack[address] = self.curClass

        code += '(class declaration, ' + address + ','','')\n'

        fieldMethDecl = classDeclaration.FieldMethDecl
        while type(fieldMethDecl) != NullNode:
            if(type(fieldMethDecl.FieldMeth.FieldMeth) == MethodDeclaration):
                code += self.visitMethod(fieldMethDecl.FieldMeth.FieldMeth)
            elif(type(fieldMethDecl.FieldMeth.FieldMeth) == FieldDeclaration):
                self.scope = 300
                code += self.visitFiled(fieldMethDecl.FieldMeth.FieldMeth)
                self.scope = 0


            fieldMethDecl = fieldMethDecl.FieldMethDecl

        return code


    def visitFiled(self, filedDecleration):
        code = ''
        address = self.getNextAddress()


        self.curMethod = filedDecleration
        stack[address] = self.curMethod
        code += '(filed declaration, ' + address + ','','')\n'
            
        return code


    def visitMethod(self, methodDecleration):
        code = ''
        address = self.getNextAddress()


        self.curMethod = methodDecleration
        stack[address] = self.curMethod
        code += '(method declaration, ' + address + ','','')\n'
        
        code += self.visitMethodParameters()
        code += self.visitMethodBody()
        return code


    def visitMethodParameters(self):
        code = ''
        
        parameterList = self.curMethod.ParameterList
        if type(parameterList) != NullNode:
            address = self.getNextAddress()
            parameter = parameterList.Parameter
            code += '(parameter declaration, ' + address + ','','')\n'
            stack[address] = parameter
            commaParameter = parameterList.Parameter.CommaParameter
            while type(commaParameter) != NullNode:
                address = self.getNextAddress()
                code += '(parameter declaration, ' + address + ','','')\n'
                stack[address] = commaParameter
                commaParameter = commaParameter.CommaParameter
        return code

    def visitMethodBody(self):
        code = ''
        
        statementList = self.curMethod.StatementList
        while type(statementList) != NullNode:
            code += self.visitStatement(statementList.Statement.Statement)
            statementList = statementList.StatementList

        return code

    def visitStatement(self, statement):
        code = ''
        if type(statement) == IfStatement:
            code += self.visitIfStatement(statement)
        return code
            

    def visitIfStatement(self, ifStatement):
        code = ''

        return code


    def getNextAddress(self):
        return 't' + str (len (stack) + self.scope)
    

        


    