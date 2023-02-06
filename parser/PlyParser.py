from tree.Nodes import *

precedence = (
    ('right', 'ASSIGNMENT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOTEQUAL', 'EQUAL'),
    ('left', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL'),
    ('left', 'ADDITION', 'SUBSTRACTION', 'CONCAT'),
    ('left', 'MULTIPLICATION', 'DIVISION', 'MODULO'),
    ('right','NEW', 'NOT','UMINUS'),
    ('left', 'DOT')
)



##########################
# Program ::= ClassDeclarationList* #
##########################
def p_Program(p):
    'Program : ClassDeclarationList'
    p[0] = Program(p[1])

def p_ClassDeclarationList(p):
    'ClassDeclarationList : ClassDeclaration ClassDeclarationList'
    p[0] = ClassDeclarationList(p[1], p[2])

def p_ClassDeclarationList1(p):
    'ClassDeclarationList : lambda'
    p[0] = NullNode()

#####################################################################
# ClassDeclaration ::= class id '{' (FieldDeclaration | MethodDeclaration)*)* '}' #
#####################################################################

def p_ClassDeclaration(p):
    'ClassDeclaration : CLASS IDEN LEFTBRACE FieldMethDecl RIGHTBRACE'
    p[0] = ClassDeclaration(Iden(p[2],p.lineno(1)), p[4])

def p_FieldMethDecl(p):
    'FieldMethDecl : FieldMeth FieldMethDecl'
    p[0] = FieldMethDecl(p[1],p[2])

def p_FieldMethDecl1(p):
    'FieldMethDecl : lambda'
    p[0] = NullNode()

def p_FieldMeth(p):
    '''FieldMeth : FieldDeclaration
                 | MethodDeclaration'''
    p[0] = FieldMeth(p[1])

######################################
# FieldDeclaration ::= Declarators id;#
######################################

def p_FieldDeclaration(p):
    'FieldDeclaration : Declarators IDEN SEMICOLON'
    p[0] = FieldDeclaration(p[1], Iden(p[2], p.lineno(1)))

def p_Declarators(p):
    'Declarators : Access Static Type'
    p[0] = Declarators(p[1], p[2], p[3])

def p_Access(p):
    '''Access : PUBLIC 
              | PRIVATE
              | lambda'''
    p[0] = Access(p[1])

def p_Static(p):
    '''Static : STATIC
              | lambda'''
    p[0] = Static(p[1])

    
#########################################################
# MethodDeclaration ::= Declarators id (ParameterList? ) { Statement* (return Expression ;)? } #
#########################################################

def p_MethodDeclaration(p):
    'MethodDeclaration : Declarators IDEN LEFTPARENT ParameterList RIGHTPARENT LEFTBRACE StatementList MethodReturn RIGHTBRACE'
    p[0] = MethodDeclaration(p[1], Iden(p[2], p.lineno(1)), p[4],p[7],p[8])

def p_ParameterList(p):
    '''ParameterList : Parameter'''
    p[0] = ParameterList(p[1])

def p_ParameterList1(p):
    'ParameterList : lambda'
    p[0] = NullNode()
        

def p_Parameter(p):
    'Parameter : Type IDEN CommaParameter'
    p[0] = Parameter(p[1], Iden(p[2], p.lineno(1)), p[3])

def p_CommaParameter(p):
    'CommaParameter : CommaTypeId CommaParameter'
    p[0] = CommaParameter(p[1], p[2])
    

def p_CommaParameter1(p):
    'CommaParameter : lambda'
    p[0] = NullNode()
    

def p_CommaTypeId(p):
    'CommaTypeId : COMMA Type IDEN'
    p[0] = CommaTypeId(p[2],Iden(p[3],p.lineno(1)))

def p_StatementList(p):
    'StatementList : Statement StatementList'
    p[0] = StatementList(p[1], p[2])

def p_StatementList1(p):
    'StatementList : lambda'
    p[0] = NullNode()

def p_MethodReturn(p):
    'MethodReturn : RETURN Expression SEMICOLON'
    p[0] = MethodReturn(p[2])

def p_MethodReturn1(p):
    'MethodReturn : lambda'
    p[0] = NullNode()

#########################################################
# Type ::= PrimType | ClassType | ArrType #
#########################################################

def p_Type(p):
    '''Type : PrimType 
            | ClassType
            | ArrType'''
    p[0] = Type(p[1])

def p_PrimType(p):
    '''PrimType : INT
                | BOOLEAN 
                | VOID'''
    p[0] = PrimType(p[1])

def p_ClassType(p):
    'ClassType : IDEN'
    p[0] = ClassType(Iden(p[1],p.lineno(1)))

def p_ArrType(p):
    '''ArrType : ArrayType LEFTSQRBRACKET RIGHTSQRBRACKET'''
    p[0] =  ArrType(p[1])

def p_ArrayType(p):
    '''ArrayType : INT 
                 | ClassType'''
    p[0] = ArrayType(p[1])
    
#########################################################
# ArgumentList ::= Expression ( , Expression)* #
#########################################################

def p_ArgumentList(p):
    '''ArgumentList : Argument'''
    p[0] = ArgumentList(p[1])

def p_ArgumentList1(p):
    '''ArgumentList : lambda'''
    p[0] = NullNode()
    

def p_Argument(p):
    'Argument : Expression CommaExpressionList'
    p[0] = Argument(p[1], p[2])

def p_CommaExpressionList(p):
    'CommaExpressionList : CommaExpression CommaExpressionList'
    p[0] = CommaExpressionList(p[1], p[2])
    

def p_CommaExpressionList1(p):
    'CommaExpressionList : lambda'
    p[0] = NullNode()
    

def p_CommaExpression(p):
    'CommaExpression : COMMA Expression'
    p[0] = CommaExpression(p[2])


#########################################################
# Reference ::= ( this | id ) ( . id )* #
#########################################################

def p_Reference(p):
    'Reference : ReferenceType DotIdList'
    p[0] = Reference(p[1], p[2])

def p_ReferenceType(p):
    '''ReferenceType : THIS
                     | IDEN'''
    p[0] = ReferenceType(Iden(p[1],p.lineno(1)))
        
        
def p_DotIdList(p):
    'DotIdList : DotId DotIdList'
    p[0] = DotIdList(p[1], p[2])

def p_DotIdList1(p):
    'DotIdList : lambda'
    p[0] = NullNode()


def p_DotId(p):
    'DotId : DOT IDEN'
    p[0] = DotId(Iden(p[2],p.lineno(1)))
    



#########################################################
# Statement ::= { Statement* } 
#               | Type id = Expression ; 
#               | Reference ([ Expression ])? = Expression ; 
#               | Reference ( ArgumentList? ) ; 
#               | if ( Expression ) Statement (else Statement)? 
#               | while ( Expression ) Statement #
#########################################################


def p_Statement(p):
    '''Statement : LeftBraceStatementRightBracet 
                 | TypeAssign
                 | ReferenceAssign
                 | ReferenceArgumantSemicolon
                 | IfStatement
                 | WhileStatement'''
    p[0] = Statement(p[1])


def p_LeftBraceStatementRightBracet(p):
    'LeftBraceStatementRightBracet : LEFTBRACE StatementList RIGHTBRACE'
    p[0] = LeftBraceStatementRightBracet(p[2])

def p_TypeAssign(p):
    'TypeAssign : Type IDEN ASSIGNMENT Expression SEMICOLON'
    p[0] = TypeAssign(p[1], Iden(p[2], p.lineno(1)), p[4])

def p_ReferenceAssign(p):
    'ReferenceAssign : Reference LEFTSQRBRACKETExpressionRIGHTSQRBRACKET ASSIGNMENT Expression SEMICOLON'
    p[0] = ReferenceAssign(p[1], p[2], p[4])

def p_LEFTSQRBRACKETExpressionRIGHTSQRBRACKET(p):
    'LEFTSQRBRACKETExpressionRIGHTSQRBRACKET : LEFTSQRBRACKET Expression RIGHTSQRBRACKET'
    p[0] = LEFTSQRBRACKETExpressionRIGHTSQRBRACKET(p[2])

def p_LEFTSQRBRACKETExpressionRIGHTSQRBRACKET1(p):
    'LEFTSQRBRACKETExpressionRIGHTSQRBRACKET : lambda'
    p[0] = NullNode()

def p_ReferenceArgumantSemicolon(p):
    'ReferenceArgumantSemicolon : ReferenceArgumant SEMICOLON'
    p[0] = ReferenceArgumantSemicolon(p[1])

    
def p_ReferenceArgumant(p):
    'ReferenceArgumant : Reference LEFTPARENT ArgumentList RIGHTPARENT'
    p[0] = ReferenceArgumant(p[1], p[3])


def p_IfStatement(p):
    'IfStatement : IF LEFTPARENT Expression RIGHTPARENT Statement ElseStament'
    p[0] = IfStatement(p[3],p[5],p[6])

def p_ElseStament(p):
    'ElseStament : ELSE Statement'
    p[0] = ElseStament(p[2])

def p_ElseStament1(p):
    'ElseStament : lambda'
    p[0] = NullNode()

def p_WhileStatement(p):
    'WhileStatement : WHILE LEFTPARENT Expression RIGHTPARENT Statement'
    p[0] = WhileStatement(p[3],p[5])


#########################################################
# Expression ::= Reference ( [ Expression ] )? 
#               | Reference ( ArgumentList? ) 
#               | unop Expression 
#               | Expression binop Expression 
#               | ( Expression ) 
#               | num 
#               | true 
#               | false 
#               | new (id ( ) or int [ Expression ] or id [ Expression ] ) #
#########################################################

def p_Expression(p):
    '''Expression : ReferenceExpression 
                  | ReferenceArgumant
                  | UnopExpression
                  | LEFTPARENTExpressionRIGHTPARENT
                  | BinopExpression
                  | NUMBER
                  | TRUE
                  | FALSE
                  | NewInstance'''
    p[0] = Expression(p[1])

def p_ReferenceExpression(p):
    'ReferenceExpression : Reference LEFTSQRBRACKETExpressionRIGHTSQRBRACKET'
    p[0] = ReferenceExpression(p[1], p[2])


def p_UnopExpression(p):
    '''UnopExpression : UnaryMinus
                      | UnaryNot'''
    p[0] = UnopExpression(p[1])


def p_UnaryNot(p):
    'UnaryNot : NOT Expression'
    p[0] = UnaryNot(p[2])
    

def p_UnaryMinus(p):
    'UnaryMinus : SUBSTRACTION Expression %prec UMINUS'
    p[0] = UnaryMinus(p[2])


def p_LEFTPARENTExpressionRIGHTPARENT(p):
    'LEFTPARENTExpressionRIGHTPARENT : LEFTPARENT Expression RIGHTPARENT'
    p[0] = LEFTPARENTExpressionRIGHTPARENT(p[2])

def p_BinopExpression(p):
    '''BinopExpression : Expression ADDITION Expression
                      | Expression SUBSTRACTION Expression
                      | Expression MULTIPLICATION Expression
                      | Expression DIVISION Expression
                      | Expression MODULO Expression
                      | Expression AND Expression
                      | Expression OR Expression
                      | Expression CONCAT Expression
                      | Expression LESS Expression
                      | Expression LESSEQUAL Expression
                      | Expression GREATER Expression
                      | Expression GREATEREQUAL Expression
                      | Expression EQUAL Expression
                      | Expression NOTEQUAL Expression'''
    p[0] = BinopExpression(p[1], p[2], p[3])

def p_NewInstance(p):
    'NewInstance : NEW NewObject'
    p[0] = NewInstance(p[2])

def p_NewObject(p):
    '''NewObject : NewClass
                 | NewIntArray
                 | NewIdArray'''
    p[0] = NewObject(p[1])

def p_NewClass(p):
    'NewClass : IDEN LEFTPARENT RIGHTPARENT'
    p[0] = NewClass(Iden(p[1],p.lineno(1)))


def p_NewIntArray(p):
    'NewIntArray : INT LEFTSQRBRACKET Expression RIGHTSQRBRACKET'
    p[0] = NewIntArray()


def p_NewIdArray(p):
    'NewIdArray : IDEN LEFTSQRBRACKET Expression RIGHTSQRBRACKET'
    p[0] = NewIdArray(p[1])


def p_error(error):
    print("Syntax Error: Unexpected '%s', near line '%s' " % (error.value, error.lineno) )

def p_lambda(p):
    'lambda : '

    

