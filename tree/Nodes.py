class Node:
    pass

class NullNode(Node):
    def __init__(self):
        self.type = 'void'

    def is_null(self):
        return True

    def show(self):
        print ('null node')

class Iden(Node):
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

    def show(self):
        print ('id')


class Program(Node):
    def __init__(self, ClassDeclarationList):
        self.ClassDeclarationList = ClassDeclarationList
        self.name = 'Program'

    def show(self):
        print ('Program : ClassDeclarationList')
        self.ClassDeclarationList.show()

    def getClass(self) : return self.ClassDeclarationList 


class ClassDeclarationList(Node):
    def __init__(self, ClassDeclaration, ClassDeclarationList):
        self.ClassDeclaration = ClassDeclaration
        self.ClassDeclarationList = ClassDeclarationList
        self.name = 'ClassDeclarationList'

    def show(self):
        print('ClassDeclarationList : ClassDeclaration ClassDeclarationList')
        self.ClassDeclaration.show()
        self.ClassDeclarationList.show()


class ClassDeclaration(Node):
    def __init__(self, Iden, FieldMethDecl):
        self.Iden = Iden
        self.FieldMethDecl = FieldMethDecl
        self.name = self.Iden.name

    def show(self):
        print('ClassDecl : CLASS IDEN LEFTBRACE FieldMethDecl RIGHTBRACE')
        self.FieldMethDecl.show()

class FieldMethDecl(Node):
    def __init__(self, FieldMeth, FieldMethDecl):
        self.FieldMeth = FieldMeth
        self.FieldMethDecl = FieldMethDecl
        self.name = 'FieldMethdDecl'

    def show(self):
        print ('FieldMethDecl : FieldMeth FieldMethDecl')
        self.FieldMeth.show()
    

class FieldMeth(Node):
    def __init__(self, FieldMeth):
        self.FieldMeth = FieldMeth
        self.name = 'FieldMethd'

    def show(self):
        print ('''FieldMeth : FieldDeclaration | MethodDeclaration''')
        self.FieldMeth.show()


class FieldDeclaration(Node):
    def __init__(self, Declarators,Iden):
        self.Declarators = Declarators
        self.Iden = Iden 
        self.type = Declarators.type
        self.name = self.Iden.name

    def show(self):
        print ('FieldDeclaration : Declarators IDEN SEMICOLON')
        self.Declarators.show()
        self.Iden.show()

class Declarators(Node):

    def __init__(self, Access,Static,Type):
        self.Access = Access
        self.Static = Static 
        self.Type = Type 
        self.name = 'Declarators'
        self.type = self.Type.Type

    def show(self):
        print ('Declarators : Access Static Type')

class Access(Node):
    def __init__(self, Access):
        self.Access = Access
        self.name = 'Access'

    def show(self):
        print ('''Access : PUBLIC  | PRIVATE | lambda''')

class Static(Node):
    def __init__(self, Static):
        self.Static = Static
        self.name = 'Static'

    def show(self):
        print ('''Static : STATIC  | lambda''')

class MethodDeclaration(Node):
    def __init__(self, Declarators,Iden,ParameterList,StatementList,MethodReturn):
        self.Declarators = Declarators
        self.Iden = Iden 
        self.ParameterList = ParameterList
        self.StatementList = StatementList
        self.MethodReturn = MethodReturn 
        self.name = self.Iden.name
        self.type = self.Declarators.type

    def show(self):
        print ('MethodDeclaration : Declarators IDEN LEFTPARENT ParameterList RIGHTPARENT LEFTBRACE StatementList MethodReturn RIGHTBRACE')
        self.Declarators.show()
        self.Iden.show()
        self.ParameterList.show()
        self.StatementList.show()
        self.MethodReturn.show()


class ParameterList(Node):
    def __init__(self, Parameter):
        self.Parameter = Parameter
        self.name = 'ParameterList'

    def show(self):
        print ( '''ParameterList : Parameter  | lambda''')
        self.Parameter.show()

class Parameter(Node):
    def __init__(self, Type, Iden,CommaParameter):
        self.Type = Type
        self.Iden = Iden
        self.CommaParameter = CommaParameter
        self.type = self.Type.Type 
        self.name = self.Iden.name

    def show(self):
        print ( 'Parameter : Type IDEN CommaParameter')
        self.Type.show()
        self.Iden.show()
        self.CommaParameter.show()

class CommaParameter(Node):
    def __init__(self, CommaTypeId, CommaParameter ):
        self.CommaTypeId = CommaTypeId
        self.CommaParameter = CommaParameter
        self.name = 'CommaParameter'

    def show(self):
        print ( 'CommaParameter : CommaTypeId CommaParameter')
        self.CommaTypeId.show()

class CommaTypeId(Node):
    def __init__(self, Type, Iden ):
        self.Type = Type
        self.Iden = Iden
        self.name = self.Iden.name
        self.type = self.Type.Type

    def show(self):
        print ( 'CommaTypeId : COMMA Type IDEN')
        self.Type.show()
        self.Iden.show()


class StatementList(Node):
    def __init__(self, Statement, StatementList ):
        self.Statement = Statement
        self.StatementList = StatementList
        self.name = 'StatementList'

    def show(self):
        print ( 'StatementList : Statement StatementList')
        self.Statement.show()
        self.StatementList.show()

class MethodReturn(Node):
    def __init__(self, Expression ):
        self.Expression = Expression
        self.name = 'MethodReturn'

    def show(self):
        print ( 'MethodReturn : RETURN Expression SEMICOLON')
        self.Expression.show()
    
class Type(Node):
    def __init__(self, Type):
        self.Type = Type.Type
        self.name = 'Type'

    def show(self):
        print ('Type : PrimType | ClassType | ArrType')
        self.Type.show()

class PrimType(Node):
    def __init__(self, Type):
        self.Type = Type
        self.name = 'PrimType'

    def show(self):
        print ('PrimType : INT | BOOLEAN | VOID')

class ClassType(Node):
    def __init__(self, Type ):
        self.Type = Type.name
        self.name = 'ClassType'

    def show(self):
        print ('ClassType : IDEN')


class ArrType(Node):
    def __init__(self, Type):
        self.Type = Type
        self.name = 'ArrType'

    def show(self):
        print ('ArrType : ArrayType LEFTSQRBRACKET RIGHTSQRBRACKET')

class ArrayType(Node):
    def __init__(self, Type):
        if type(Type) == ClassType:
            self.Type = Type.Type
        else :
            self.Type = Type
        self.name = 'ArrayType'

    def show(self):
        print ('ArrayType : INT | ClassType')

class ArgumentList(Node):
    def __init__(self, Argument):
        self.Argument = Argument
        self.name = 'ArgumentList'

    def show(self):
        print ('ArgumentList : Argument | lambda')
        self.Argument.show()

class Argument(Node):
    def __init__(self, Expression, CommaExpressionList):
        self.Expression = Expression
        self.CommaExpressionList = CommaExpressionList
        self.name = 'Argument'

    def show(self):
        print ('Argument : Expression CommaExpressionList')
        self.Expression.show()
        self.CommaExpressionList.show()


class CommaExpressionList(Node):
    def __init__(self, CommaExpression, CommaExpressionList):
        self.CommaExpression = CommaExpression
        self.CommaExpressionList = CommaExpressionList
        self.name = 'CommaExpressionList'

    def show(self):
        print ('CommaExpressionList : CommaExpression CommaExpressionList')
        self.CommaExpression.show()
        self.CommaExpressionList.show()

class CommaExpression(Node):
    def __init__(self, Expression):
        self.Expression = Expression
        self.name = 'CommaExpression'

    def show(self):
        print ('CommaExpression : COMMA Expression')
        self.Expression.show()


class Reference(Node):
    def __init__(self, ReferenceType,DotIdList):
        self.ReferenceType = ReferenceType
        self.DotIdList = DotIdList
        self.name = self.ReferenceType.ReferenceType

    def show(self):
        print ('Reference : ReferenceType DotIdList')
        if self.ReferenceType != 'this':
            self.ReferenceType.show()
        self.DotIdList.show()

class ReferenceType(Node):
    def __init__(self, ReferenceType):
        self.ReferenceType = ReferenceType
        if self.ReferenceType != 'this':
            self.ReferenceType = ReferenceType.name
        self.name = 'ReferenceType'

    def show(self):
        print ('ReferenceType : THIS | IDEN')

class DotIdList(Node):
    def __init__(self, DotId,DotIdList):
        self.DotId = DotId
        self.DotIdList = DotIdList
        self.name = 'DotIdList'

    def show(self):
        print ('DotIdList : DotId DotIdList')


class DotId(Node):
    def __init__(self, Iden):
        self.Iden = Iden
        self.name = 'DotId'

    def show(self):
        print ('DotId : DOT IDEN')
        self.Iden.show()



class Statement(Node):
    def __init__(self, Statement):
        self.Statement = Statement
        self.name = 'Statement'

    def show(self):
        print ('Statement : LeftBraceStatementRightBracet  | TypeAssign | ReferenceAssign | ReferenceArgumantSemicolon | IfStatement | WhileStatement')
        self.Statement.show()


class LeftBraceStatementRightBracet(Node):
    def __init__(self, StatementList):
        self.StatementList = StatementList
        self.name = 'LeftBraceStatementRightBracet'

    def show(self):
        print ('LeftBraceStatementRightBracet : LEFTBRACE StatementList RIGHTBRACE')
        self.StatementList.show()

class TypeAssign(Node):
    def __init__(self, Type, Iden, Expression):
        self.Type = Type
        self.Iden = Iden
        self.Expression = Expression
        self.name = self.Iden.name
        self.type = self.Type.Type

    def show(self):
        print ('TypeAssign : Type IDEN ASSIGNMENT Expression SEMICOLON')
        self.Type.show()
        self.Iden.show()
        self.Expression.show()
    
class ReferenceAssign(Node):
    def __init__(self, Reference, LEFTSQRBRACKETExpressionRIGHTSQRBRACKET, Expression):
        self.Reference = Reference
        self.LEFTSQRBRACKETExpressionRIGHTSQRBRACKET = LEFTSQRBRACKETExpressionRIGHTSQRBRACKET
        self.Expression = Expression
        self.name = self.Reference.name

    def show(self):
        print ('ReferenceAssign : Reference LEFTSQRBRACKETExpressionRIGHTSQRBRACKET ASSIGNMENT Expression SEMICOLON')
        self.Reference.show()
        self.LEFTSQRBRACKETExpressionRIGHTSQRBRACKET.show()
        self.Expression.show()

class LEFTSQRBRACKETExpressionRIGHTSQRBRACKET(Node):
    def __init__(self, Expression):
        self.Expression = Expression
        self.name = 'LEFTSQRBRACKETExpressionRIGHTSQRBRACKET'

    def show(self):
        print ('LEFTSQRBRACKETExpressionRIGHTSQRBRACKET : LEFTSQRBRACKET Expression RIGHTSQRBRACKET')
        self.Expression.show()

class ReferenceArgumantSemicolon(Node):
    def __init__(self, ReferenceArgumant):
        self.ReferenceArgumant = ReferenceArgumant
        self.name = 'ReferenceArgumantSemicolon'

    def show(self):
        print ('ReferenceArgumantSemicolon : ReferenceArgumant SEMICOLON')
        self.ReferenceArgumant.show()

class ReferenceArgumant(Node):
    def __init__(self, Reference, ArgumentList):
        self.Reference = Reference
        self.ArgumentList = ArgumentList
        self.name = self.Reference.name

    def show(self):
        print ('ReferenceArgumant : Reference LEFTPARENT ArgumentList RIGHTPARENT')
        self.Reference.show()
        self.ArgumentList.show()

class IfStatement(Node):
    def __init__(self, Expression, Statement, ElseStament):
        self.Expression = Expression
        self.Statement = Statement
        self.ElseStament = ElseStament
        self.name = 'IfStatement'

    def show(self):
        print ('IfStatement : IF LEFTPARENT Expression RIGHTPARENT Statement ElseStament')
        self.Expression.show()
        self.Statement.show()
        self.ElseStament.show()

class ElseStament(Node):
    def __init__(self, Statement):
        self.Statement = Statement
        self.name = 'ElseStament'

    def show(self):
        print ('ElseStament : ELSE Statement')
        self.Statement.show()


class WhileStatement(Node):
    def __init__(self, Expression,Statement):
        self.Expression = Expression
        self.Statement = Statement
        self.name = 'WhileStatement'

    def show(self):
        print ('WhileStatement : WHILE LEFTPARENT Expression RIGHTPARENT Statement')
        self.Expression.show()
        self.Statement.show()


class Expression(Node):
    def __init__(self, Expression):
        self.Expression = Expression
        Type = type(self.Expression)


        if(Type == int):
            self.type = 'int'
        elif(Type == str):
            self.type = 'boolean'

        self.name = 'Expression'

    def show(self):
        print ('Expression : ReferenceExpression | ReferenceArgumant | UnopExpression | LEFTPARENTExpressionRIGHTPARENT | BinopExpression | NUMBER | TRUE | FALSE | NewInstance')


class ReferenceExpression(Node):
    def __init__(self, Reference,LEFTSQRBRACKETExpressionRIGHTSQRBRACKET):
        self.Reference = Reference
        self.LEFTSQRBRACKETExpressionRIGHTSQRBRACKET = LEFTSQRBRACKETExpressionRIGHTSQRBRACKET
        self.name = self.Reference.name

    def show(self):
        print ('ReferenceExpression : Reference LEFTSQRBRACKETExpressionRIGHTSQRBRACKET')
        self.Reference.show()
        self.LEFTSQRBRACKETExpressionRIGHTSQRBRACKET.show()


class UnopExpression(Node):
    def __init__(self, UnopExpression):
        self.UnopExpression = UnopExpression
        self.name = 'UnopExpression'

    def show(self):
        print ('UnopExpression : UnaryMinus | NOT')
        print(UnaryMinus)

    
class UnaryNot(Node):
    def __init__(self, Expression):
        self.Expression = Expression
        self.name = 'UnaryMinus'

    def show(self):
        print ('UnaryMinus : SUBSTRACTION Expression %prec UMINUS')
        self.Expression.show()


class UnaryMinus(Node):
    def __init__(self, Expression):
        self.Expression = Expression
        self.name = 'UnaryMinus'

    def show(self):
        print ('UnaryMinus : SUBSTRACTION Expression %prec UMINUS')
        self.Expression.show()

class LEFTPARENTExpressionRIGHTPARENT(Node):
    def __init__(self, Expression):
        self.Expression = Expression
        self.name = 'LEFTPARENTExpressionRIGHTPARENT'

    def show(self):
        print ('LEFTPARENTExpressionRIGHTPARENT : LEFTPARENT Expression RIGHTPARENT')
        self.Expression.show()

class BinopExpression(Node):
    def __init__(self, Expression, Operation, Expression2):
        self.Expression = Expression
        self.Operation = Operation
        self.Expression2 = Expression2
        self.name = 'BinopExpression'

    def show(self):
        print ('BinopExpression : Expression ADDITION Expression | Expression SUBSTRACTION Expression | Expression MULTIPLICATION Expression | Expression DIVISION Expression | Expression MODULO Expression | Expression AND Expression | Expression OR Expression | Expression CONCAT Expression | Expression LESS Expression | Expression LESSEQUAL Expression | Expression GREATER Expression | Expression GREATEREQUAL Expression | Expression EQUAL Expression | Expression NOTEQUAL Expression')
        self.Expression.show()
        print (self.Operation)
        self.Expression2.show()


class NewInstance(Node):
    def __init__(self, NewObject):
        self.NewObject = NewObject
        self.name = self.NewObject.name

    def show(self):
        print ('NewInstance : NEW NewObject')
        self.NewObject.show()


class NewObject(Node):
    def __init__(self, NewObject):
        self.NewObject = NewObject
        self.name = self.NewObject.name

    def show(self):
        print ('NewObject : NewClass | NewIntArray | NewIdArray')
        self.NewObject.show()

class NewClass(Node):
    def __init__(self, Iden):
        self.Iden = Iden
        self.name = self.Iden.name

    def show(self):
        print ('NewClass : IDEN LEFTPARENT RIGHTPARENT')
        self.Iden.show()
    
class NewIntArray(Node):
    def __init__(self):
        self.name = NewIntArray

    def show(self):
        print ('NewIntArray : INT LEFTSQRBRACKET RIGHTSQRBRACKET')

class NewIdArray(Node):
    def __init__(self, Iden):
        self.Iden = Iden
        self.name = self.Iden

    def show(self):
        print ('NewIdArray : IDEN LEFTSQRBRACKET RIGHTSQRBRACKET')
        self.Iden.show()