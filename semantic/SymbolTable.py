
from tree.Nodes import *


errors = []


class SymbolTable:
    def __init__(self, program):
        self.program = program
        self.classes = {}

        classDeclarationList = program.ClassDeclarationList
        while type(classDeclarationList) != NullNode:
            self.addClass(classDeclarationList.ClassDeclaration)
            classDeclarationList = classDeclarationList.ClassDeclarationList
        
        if len(errors) != 0:
            print(errors)


    def addClass(self, classDeclaration):
        if self.containClass(classDeclaration.name):
            errors.append("Class " + classDeclaration.name + "  Has Been Defiend Already")
        else :
            self.classes[classDeclaration.name] = Class(classDeclaration)

    def containClass(self, name):
        return name in self.classes
    

class Class:
    def __init__(self, classDeclaration):
        self.name = classDeclaration.name
        self.fileds = {}
        self.methods = {}
        fieldMethDecl = classDeclaration.FieldMethDecl
        while type(fieldMethDecl) != NullNode:
            if(type(fieldMethDecl.FieldMeth.FieldMeth) == MethodDeclaration):
                self.addMethod(fieldMethDecl.FieldMeth.FieldMeth)
            elif(type(fieldMethDecl.FieldMeth.FieldMeth) == FieldDeclaration):
                self.addFiled(fieldMethDecl.FieldMeth.FieldMeth)
            fieldMethDecl = fieldMethDecl.FieldMethDecl

        for method in self.methods:
            self.methods[method].addParameters()

        for method in self.methods:
            self.methods[method].checkStatement()

    def addFiled(self, filedDeclaration):
        if self.containFiled(filedDeclaration.name):
            errors.append("Filed " + filedDeclaration.name + " has been defined already")
        else:
            self.fileds[filedDeclaration.name] = Filed(filedDeclaration)
    
    def containFiled(self, name):
        return name in self.fileds

    def addMethod(self, methodDeclaration):
        if self.containMethod(methodDeclaration.name):
            errors.append("Method " + methodDeclaration.name + " has been defined already")
        else :
            self.methods[methodDeclaration.name] = Method(self, methodDeclaration)
    
    def containMethod(self, name):
        return name in self.methods


    
    

class Filed :
    def __init__(self, filedDeclaration):
        self.type = filedDeclaration.type
        self.name = filedDeclaration.name


class Method:
    def __init__(self, methodClass, methodDeclaration):
        self.methodClass = methodClass
        self.methodDeclaration = methodDeclaration
        self.type = methodDeclaration.type
        self.name = methodDeclaration.name
        self.parameter = {}
        self.fileds = {}


    def checkStatement(self):
        statementList = self.methodDeclaration.StatementList
        while type(statementList) != NullNode:
            if type(statementList.Statement.Statement) == TypeAssign:
                self.checkTypeAssign(statementList.Statement.Statement)

            elif type(statementList.Statement.Statement) == ReferenceAssign:
                self.checkReferenceAssign(statementList.Statement.Statement)
            statementList = statementList.StatementList
        
    
    def checkReferenceAssign(self, referenceAssign):
        t = self.getFiledType(referenceAssign.name)
        if t != None:
            if type(referenceAssign.Expression.Expression) == ReferenceExpression:
                if not self.checkType(t, referenceAssign.Expression.Expression, 1):
                    errors.append("Type checks error")
            
            elif type(referenceAssign.Expression.Expression) == ReferenceArgumant:
                if self.methodClass.containMethod(referenceAssign.Expression.Expression.name):
                    method = self.methodClass.methods[referenceAssign.Expression.Expression.name]
                    if not self.checkType(t, method, 0):
                        errors.append("Type checks error")
        

            elif t == 'int' and type(referenceAssign.Expression.Expression) != int:
                errors.append("Type checks error")

            elif t == 'boolean'  and  type(referenceAssign.Expression.Expression) != str:
                errors.append("Type checks error")
            
            elif t != 'int' and type(referenceAssign.Expression.Expression) == int:
                errors.append("Type checks error")

            elif t != 'boolean' and type(referenceAssign.Expression.Expression) == str:
                errors.append("Type checks error")
            
        
    
    def checkTypeAssign(self, typeAssign):
        self.addFiled(typeAssign)
        if type(typeAssign.Expression.Expression) == ReferenceExpression:
            if not self.checkType(typeAssign.type, typeAssign.Expression.Expression, 1):
                errors.append("Type checks error")
        
        elif type(typeAssign.Expression.Expression) == ReferenceArgumant:
            if self.methodClass.containMethod(typeAssign.Expression.Expression.name):
                 method = self.methodClass.methods[typeAssign.Expression.Expression.name]
                 if not self.checkType(typeAssign.type, method, 0):
                    errors.append("Type checks error")
      
        elif typeAssign.type == 'int' and type(typeAssign.Expression.Expression) != int:
            errors.append("Type checks error")

        elif typeAssign.type == 'boolean'  and  type(typeAssign.Expression.Expression) != str:
            errors.append("Type checks error")
        
        elif typeAssign.type != 'int' and type(typeAssign.Expression.Expression) == int:
            errors.append("Type checks error")

        elif typeAssign.type != 'boolean' and type(typeAssign.Expression.Expression) == str:
            errors.append("Type checks error")
       
                


    def checkType(self, type1, expression, isMethod) :
        if isMethod == 0:
            tE = self.getMethodType(expression.name)
        elif isMethod == 1 :
            tE = self.getFiledType(expression.name)
        else : tE = expression.name

   

        if type(expression) == ReferenceExpression and type(expression.LEFTSQRBRACKETExpressionRIGHTSQRBRACKET) != NullNode:
            return type(tE) == ArrayType and tE.Type == type1
        

        if type(type1) == ArrayType and type(tE) == ArrayType:
            return type1.Type == tE.Type
        
        return type1 == tE
        

    
    def getMethodType(self, name):
        if name in self.methodClass.methods:
            return self.methodClass.methods[name].type   
        errors.append("Method " + name + "  does not defined")
    
    def getFiledType(self, name):
        if name == 'this' : return
        
        if name in self.parameter:
            return self.parameter[name].type
        
        if name in self.fileds:
            return self.fileds[name].type
        
        if name in self.methodClass.fileds:
            return self.methodClass.fileds[name].type
        
        errors.append("Filed " + name + "  does not defined")    
    
    
    def addFiled(self, typeAssign):
        if self.containFiled(typeAssign.name):
            errors.append("Filed " + typeAssign.name + "  has been defined already")
        else:
            self.fileds[typeAssign.name] = Filed(typeAssign)
    
    def containFiled(self, name):
        return name in self.fileds or name in self.parameter


    def addParameter(self, filedDeclaration):
        if self.containArgumant(filedDeclaration.name):
            errors.append("Filed " + filedDeclaration.name + "  has been defined already")
        else:
            self.parameter[filedDeclaration.name] = Filed(filedDeclaration)
    
    def containArgumant(self, name):
        return name in self.parameter

    def addParameters(self):
        parameterList = self.methodDeclaration.ParameterList
        if type(parameterList) != NullNode:
            parameter = parameterList.Parameter
            self.addParameter(parameter)
            commaParameter = parameterList.Parameter.CommaParameter
            while type(commaParameter) != NullNode:
                self.addParameter(commaParameter.CommaTypeId)
                commaParameter = commaParameter.CommaParameter

                