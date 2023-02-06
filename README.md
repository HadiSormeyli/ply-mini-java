# ply-mini-java

Mini java compiler using ply tool.


There are four phases:
  
1.Lexer: complete.
2.Parser: complete.
3.Semantic: Syntax Tree is formed, and has uniqueness check and type check.
4.Code generation: incomplete, just generate three address code for classes ,fields,methods and parameters.

Mini_Java Grammar:
  Program ::= (ClassDeclaration)* eot
  ClassDeclaration ::= class id { (FieldDeclaration | MethodDeclaration)* }
  FieldDeclaration ::= Declarators id;
  MethodDeclaration ::= Declarators id (ParameterList? ) { Statement* (return Expression ;)? }
  Declarators ::= (public | private)? static? Type
  Type ::= PrimType | ClassType | ArrType
  PrimType ::= int | boolean | void
  ClassType ::= id
  ArrType ::= ( int | ClassType ) []
  ParameterList ::= Type id (, Type id)*
  ArgumentList ::= Expression ( , Expression)*
  Reference ::= ( this | id ) ( . id )*
  Statement ::= { Statement* } | Type id = Expression ; | Reference ([ Expression ])? = Expression ; | Reference ( ArgumentList? ) ; | if ( Expression ) Statement (else Statement)? | while ( Expression ) Statement
  Expression ::= Reference ( [ Expression ] )? | Reference ( ArgumentList? ) | unop Expression | Expression binop Expression | ( Expression ) | num | true | false | new (id ( ) | int [ Expression ] | id [ Expression ] )
