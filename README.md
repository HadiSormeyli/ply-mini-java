# ply-mini-java

Mini java compiler using ply tool.<br /><br />


There are four phases:<br />
  
1.Lexer: complete.<br />
2.Parser: complete.<br />
3.Semantic: Syntax Tree is formed, and has uniqueness check and type check.<br />
4.Code generation: incomplete, just generate three address code for classes ,fields,methods and parameters.<br />

Mini_Java Grammar:<br />
  Program ::= (ClassDeclaration)* eot<br />
  ClassDeclaration ::= class id { (FieldDeclaration | MethodDeclaration)* }<br />
  FieldDeclaration ::= Declarators id;<br />
  MethodDeclaration ::= Declarators id (ParameterList? ) { Statement* (return Expression ;)? }<br />
  Declarators ::= (public | private)? static? Type<br />
  Type ::= PrimType | ClassType | ArrType<br />
  PrimType ::= int | boolean | void<br />
  ClassType ::= id<br />
  ArrType ::= ( int | ClassType ) []<br />
  ParameterList ::= Type id (, Type id)*<br />
  ArgumentList ::= Expression ( , Expression)*<br />
  Reference ::= ( this | id ) ( . id )*<br />
  Statement ::= { Statement* } | Type id = Expression ; | Reference ([ Expression ])? = Expression ; | Reference ( ArgumentList? ) ; | if ( Expression ) Statement (else Statement)? | while ( Expression ) Statement<br />
  Expression ::= Reference ( [ Expression ] )? | Reference ( ArgumentList? ) | unop Expression | Expression binop Expression | ( Expression ) | num | true | false | new (id ( ) | int [ Expression ] | id [ Expression ] )<br />
