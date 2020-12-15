import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    
    def test_redeclared_variable_0(self):
        input = """
Function: main
Body:
    Var: x,y,z,x;
EndBody.
"""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_redeclared_variable_1(self):
        input = """
Function: main
Body:
    Var: x,y,z;
    Var: k;
    Var: x;
EndBody.
        """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_2(self):
        input = """
Var: printLn;
Function: main
Body:
    Var: printLn;
EndBody.
"""
        expect = str(Redeclared(Variable(), "printLn"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable_3(self):
        input = """
Var: x, y, z;
Var: k;
Var: x = 5;
Function: main
Body:
EndBody.
        """
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_4(self):
        """Raise no error"""
        input = """
Var: x, y, z;
Function: main
Body:
    Var: x;
    Var: y;
    Var: z;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable_5(self):
        """Raise no error"""
        input = """
Var: x, y, z;
Function: main
Body:
    Var: x;
    Var: y;
    Var: z;
EndBody.

Var: x, y, z;
Function: foo
    Var: x;
    Var: y;
    Var: z;
Body:
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclare_function_6(self):
        input = """
Function: foo1
Body:
EndBody.

Function: foo1
Body:
EndBody.

Function: main
Body:
EndBody.
        """
        expect = str(Redeclared(Function(), "foo1"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_function_7(self):
        input = """
Function: main
Body:
EndBody.

Function: main
Body:
EndBody.
        """
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclare_parameter_8(self):
        input = """
Function: main
Parameter: a, b, c, a
Body:
EndBody.
        """
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_parameter_9(self):
        input = """
Function: main
Parameter: a, b, c, a[5]
Body:
EndBody.
        """
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_variable_with_para_10(self):
        input = """
Function: main
Parameter: a, b, c
Body:
    Var: a = 5;
EndBody.
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_variable_with_function_11(self):
        """Raise no error"""
        input = """
Function: main
Parameter: a, b, c
Body:
    Var: main;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_redeclared_globle_variable_with_function_12(self):
        input = """
Var: foo;
Function: foo
Parameter: a, b, c
Body:
    Var: main;
EndBody.
Function: main
Parameter: a, b, c
Body:
    Var: main;
EndBody.
        """
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_redeclared_fuction_with_builtin_function_13(self):
        input = """
Function: printLn
Parameter: a, b, c
Body:
EndBody.

Function: main
Body:
EndBody.
        """
        expect = str(Redeclared(Function(), "printLn"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclared_parammter_with_function_14(self):
        input = """
Function: foo
Parameter: a, b, c, foo
Body:
EndBody.

Function: main
Body:
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_local_variable_with_outside_scope_15(self):
        """Raise no error because different scope"""
        input = """
Function: foo
Parameter: a, b, c, foo
Body:
    Var: printLn;
EndBody.

Function: main
Body:
    Var: foo;
    Var: main;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,415))
    
    # test undeclare variable 
    def test_undeclared_variable_16(self):
        input = """
Function: main
Body:
    a = 5;
EndBody.
        """
        expect = str(Undeclared(Identifier(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_global_variable_17(self):
        input = """
Var: a;
Function: main
Body:
    a = 5;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_global_variable_18(self):
        """Raise no error"""
        input = """
Var: a;
Function: main
Body:
    main();
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_global_variable_19(self):
        """Raise no error"""
        input = """
Var: a;
Function: main
Parameter: x, y
Body:
    main(2,3);
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_global_func_call_20(self):
        """Raise no error"""
        input = """
Function: main
Parameter: x, y
Body:
    foo(2);
EndBody.

Function: foo
Parameter: a
Body:
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_func_call_21(self):
        """Raise no error"""
        input = """
Function: main
Parameter: x, y
Body:
    foo(2);
EndBody.
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_func_call_22(self):
        """Raise no error"""
        input = """
Function: main
Parameter: x, y
Body:
    foo(2);
EndBody.
        """
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_var_call_23(self):
        """Raise no error"""
        input = """
Function: main
Body:
    a[5] = 3;
EndBody.
        """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_var_call_24(self):
        input = """
Function: main
Body:
Var: m, n[10];
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_type_cannot_be_inferred_25(self):
        input = """
Function: main
Body:
    Var: a;
    foo(a);
EndBody.
Function: foo
Parameter: a
Body:
EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("a")])))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_type_cannot_be_inferred_26(self):
        input = """
Function: main
Body:
    Var: a;
    foo(a);
EndBody.
Function: foo
Parameter: a
Body:
    a = True;
EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"), [Id("a")])))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_type_cannot_be_inferred_27(self):
        input = """
Function: main
Body:
    Var: a = 1;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_type_cannot_be_inferred_28(self):
        input = """
Function: main
Body:
    Var: a = 1;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_type_cannot_be_inferred_29(self):
        input = """
Function: main
Body:
    Var: a;
    a = 1;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_type_cannot_be_inferred_30(self):
        input = """
Function: main
Body:
    Var: a;
    a = 1 + foo();
EndBody.

Function: foo
Body:
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,430))

# adding expect here
    def test_type_cannot_be_inferred_31(self):
        input = """
Function: main
Body:
    Var: a;
    Var: y;
    Var: x;
    y = a + foo(x);
EndBody.

Function: foo
Parameter: x
Body:
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'),BinaryOp('+',Id('a'),CallExpr(Id('foo'),[Id('x')])))))
        self.assertTrue(TestChecker.test(input,expect,431))

# adding expect here    
    def test_type_cannot_be_inferred_32(self):
        input = """
Function: main
Body:
    Var: a;
    Var: y;
    Var: x;
    y = a + foo(x);
EndBody.

Function: foo
Parameter: x
Body:
    x = 1;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'),BinaryOp('+',Id('a'),CallExpr(Id('foo'),[Id('x')])))))
        self.assertTrue(TestChecker.test(input,expect,432))

# adding expect here
    def test_type_cannot_be_inferred_33(self):
        input = """
Function: main
Body:
    Var: a;
    Var: y;
    y = a;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'),Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,433))

# adding expect here
    def test_type_cannot_be_inferred_34(self):
        input = """
Function: main
Body:
    Var: a;
    Var: y;
    y = foo();
EndBody.

Function: foo
Body:
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('y'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_stmt_void_func_35(self):
        input = """
Function: main
Body:
    foo();
EndBody.

Function: foo
Body:
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_stmt_void_func_36(self):
        input = """
Function: main
Body:
    foo();
EndBody.

Function: foo
Body:
    Return 1;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_stmt_args_func_37(self):
        input = """
Function: main
Body:
    foo(1,1);
EndBody.

Function: foo
Parameter: x, y
Body:
    Return;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_stmt_args_func_38(self):
        input = """
Function: main
Body:
    foo(1,1);
    foo(1,1.3);
EndBody.

Function: foo
Parameter: x, y
Body:
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1), FloatLiteral(1.3)])))
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_stmt_args_func_39(self):
        input = """
Function: main
Body:
    foo(1,1,1);
EndBody.

Function: foo
Parameter: x, y
Body:
    Return;
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [IntLiteral(1), IntLiteral(1), IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_stmt_args_func_40(self):
        input = """
Function: main
Body:
    Var: x = 1;
    Var: y = 0.5;
    x = y;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_stmt_args_func_41(self):
        input = """
Function: main
Body:
    Var: x = 1;
    Var: y = 0.5;
    Var: a;
    a = x + foo(1, 1, 1, 1);
EndBody.

Function: foo
Parameter: a,b,c,d
Body:
    Return a + b + c + d;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_stmt_args_func_42(self):
        input = """
Function: main
Body:
    Var: x = 1;
    Var: y = 0.5;
    Var: a;
    a = -foo(1, 1, 1, 1);
EndBody.

Function: foo
Parameter: a,b,c,d
Body:
    Var k;
    k = a + b + c + d;
    Return 3.5;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_stmt_args_func_43(self):
        input = """
Function: foo
Parameter: a,b,c,d
Body:
    Var: k;
    k = a + b + c + d;
    Return 1;
EndBody.
Function: main
Body:
    Var: a;
    a = foo(1, foo(2,2,2,2), 1, 1);
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_if_stmt_44(self):
        input = """
Function: main
Body:
    Var: a = True;
    If a Then
        Var: a;
        a = 1 + a;
    EndIf.
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_if_stmt_45(self):
        input = """
Function: main
Body:
    Var: a = 1;
    If a Then
        Var: a;
        a = True;
    EndIf.
EndBody.
        """
        expect = str(TypeMismatchInStatement(
            If(
                [
                    (Id('a'), 
                    [VarDecl(Id('a'), [], None)],
                    [Assign(Id('a'), BooleanLiteral(True))]
                    )
                ],
                ([],[])
            )
        ))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_if_stmt_46(self):
        input = """
Function: main
Body:
    Var: a = True;
    If a Then
        Var: a;
        a = 1;
        If a Then 
        EndIf.
    EndIf.
EndBody.
        """
        expect = str(TypeMismatchInStatement(
            If([(Id('a'), [], [])],([],[]))
        ))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_if_stmt_47(self):
        input = """
Function: main
Body:
    Var: a = True;
    
    If a Then
        Var: a;
        a = 1;
    Else If (a && True) Then
        Var: a;
    Else
        Var: a;
    EndIf.
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_if_stmt_48(self):
        input = """
Function: main
Body:
    Var: a = True;
    
    If a Then
        a = 1;
    Else If (a && True) Then
        Var: a;
    Else
        Var: a;
    EndIf.
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_if_stmt_49(self):
        input = """
Function: main
Body:
    Var: a = True;
    
    If a Then
        Var: a;
        If True Then
            a = 1;
        EndIf.
    EndIf.
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_if_stmt_50(self):
        input = """
Function: main
Body:
    Var: a = True;
    
    If a Then
        If True Then
            If True Then
                a = 1;
            EndIf.
        EndIf.
    EndIf.
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_for_stmt_51(self):
        input = """
Function: main
Body:
    Var: i,j;
    For(i = 1, i < 10, 1) Do
        For(j = 1, j < 10, 1) Do
        EndFor.
    EndFor
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,451))


    def test_for_stmt_52(self):
        input = """
Function: main
Body:
    Var: i;
    For(i = 1, i < 10, 1) Do
        Var: j;
        For(j = 1, j < 10, 1) Do
        EndFor.
    EndFor
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_for_stmt_53(self):
        input = """
Function: main
Body:
    Var: i;
    For(i = 1, i + 10, 1) Do
    EndFor.
EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),IntLiteral(1),BinaryOp('+',Id('i'),IntLiteral(10)),IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_for_stmt_54(self):
        input = """
Function: main
Body:
    Var: i;
    For(i = 1, i + 10, 1) Do
    EndFor.
EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),IntLiteral(1),BinaryOp('+',Id('i'),IntLiteral(10)),IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_for_stmt_55(self):
        input = """
Function: main
Body:
    Var: i;
    For(i = 1, i + 10, True) Do
    EndFor.
EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),IntLiteral(1),BinaryOp('+',Id('i'),IntLiteral(10)),BooleanLiteral(True),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_while_stmt_56(self):
        input = """
Function: main
Body:
    While True Do
    EndWhile.
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_while_stmt_57(self):
        input = """
Function: main
Body:
    While 1 Do
    EndWhile.
EndBody.
        """
        expect = str(TypeMismatchInStatement(While(IntLiteral(1),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_while_stmt_58(self):
        input = """
Function: main
Body:
    Var: x = True
    While x Do
        Var: x;
    EndWhile.
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_while_stmt_59(self):
        input = """
Function: main
Body:
    Var: x = True;
    While foo() Do
        Var: x;
        If True Then
            Var: x;
        EndIf.
    EndWhile.
EndBody.

Function: foo
Body:
    Return True;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_while_stmt_60(self):
        input = """
Function: main
Body:
    Var: x = True;
    Var: a = 1, b = "string", c[3];
    While foo(a,b,c[2]) Do
        Var: x;
    EndWhile.
EndBody.

Function: foo
Parameter: a,b,c
Body:
    Return True;
EndBody.
        """
        expect = str(TypeCannotBeInferred(While(CallExpr(Id('foo'),[Id('a'),Id('b'),ArrayCell(Id('c'),[IntLiteral(2)])]),([VarDecl(Id('x'),[],None)],[]))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_call_stmt_61(self):
        input = """
Function: foo
Parameter: a,b
Body:
    a = 1;
    b = 5;
EndBody.
Function: main
Body:
    foo(1.0,1.5);

EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[FloatLiteral(1.0),FloatLiteral(1.5)])))
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_call_stmt_62(self):
        input = """
Function: foo
Parameter: a,b
Body:
    a = 1;
    b = 5;
EndBody.
Function: main
Body:
    Var: a,b;
    foo(a,b);
EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id('foo'),[Id('a'),Id('b')])))
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_call_stmt_63(self):
        input = """
Function: main
Parameter: a,b
Body:
    a = 1;
    b = 1;
    main(1.0,1.0);
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[FloatLiteral(1.0),FloatLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_dowhile_stmt_64(self):
        input = """
Function: main
Parameter: a,b
Body:
    Do
    Var: a;
    a = 1;
    While True
    EndDo.
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_dowhile_stmt_65(self):
        input = """
Function: main
Body:
    Var: a = 5;
    Do
    Var: a;
    a = 1;
    While a
    EndDo.
EndBody.
        """
        expect = str(TypeMismatchInStatement(Dowhile(([VarDecl(Id('a'), [], None)],[Assign(Id('a'), IntLiteral(1))]), Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_assign_stmt_66(self):
        input = """
Function: foo
Body:
EndBody.

Function: main
Body:
    Var: a = 1;
    foo();

    foo() = a
    
EndBody.

        """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id('foo'), []), Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_assign_stmt_67(self):
        input = """
Function: foo
Body:
EndBody.

Function: main
Body:
    Var: a = 1;
    Var: b,c;
    b = a;
    a = c;
    
EndBody.

        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_assign_stmt_68(self):
        input = """
Function: foo
Body:
EndBody.

Function: main
Body:
    Var: a[3] = {1,2,4};
    Var: b[3];
    b = a;
    a = b;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_assign_stmt_69(self):
        input = """
Function: foo
Body:
EndBody.

Function: main
Body:
    Var: a[3] = {1,2,4};
    Var: b[5][6];
    b = a;
EndBody.

        """
        expect = str(TypeMismatchInStatement(Assign(Id('b'), Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_nested_call_70(self):
        input = """
Function: main
Parameter: x
Body:
    main(main(5));
EndBody.

        """
        expect = str(TypeCannotBeInferred(CallStmt(Id('main'),[CallExpr(Id('main'),[IntLiteral(5)])])))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_call_71(self):
        input = """
Function: foo
Body:
    Return 3;
EndBody.

Function: main
Body:
    foo();
EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'), [])))
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_call_72(self):
        input = """

Function: main
Body:
    foo();
EndBody.
Function: foo
Body:
    Return 3;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_call_73(self):
        input = """
Function: main
Body:
    Var: a;
    a = a +. foo();
EndBody.
Function: foo
Body:
    Return 3;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_call_74(self):
        input = """

Function: main
Body:
    Var: a;
    a = a +. foo();
EndBody.
Function: foo
Body:
    Return foo();
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_call_75(self):
        input = """
Var: a[1] = {0};

Function: foo
    Parameter: x
    Body:
        Return a;
    EndBody.

Function: main
    Body:
        foo(0)[0] = foo(0.0)[0];
    EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_arr_76(self):
        input = """
Function: main
Body:
    Var: a[5];
    Var: b[3];
    b = a;
EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('b'), Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_arr_77(self):
        input = """
Function: main
Body:
    Var: a;
    a[0] = 1;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('a'),[IntLiteral(0)]), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_arr_78(self):
        input = """
Function: main
Body:
    Var: a[3];
    a[0] = 1;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_call_79(self):
        input = """
Function: main
Body:
    foo()[0] = 1;
EndBody.

Function: foo
Body:
    Return 3;
EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(0)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_call_80(self):
        input = """
Function: foo
Body:
    Var a[3];
    Return a;
EndBody.

Function: main
Body:
    foo()[0] = 1;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_call_81(self):
        input = """
Function: main
Body:
    Var: a,b,c,d,e;
    b = !(a==a) && (d <. 2.0) && (c != c);
    e = e +. foo()
EndBody.

Function: foo
Body:
    Return 3.0;
EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_call_82(self):
        input = """
Function: main
Body:
    Var: a,b,c,d,e;
    Var: f,g,h,i,k;
    b = a +. a;
    c = a -. a;
    d = d *. d;
    e = e \. e;
    f = b =/= b;
    g = c <. c;
    h = i <=. i;
    e = e +. foo()
EndBody.

Function: foo
Body:
    Return 3.0;
EndBody.
"""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_call_83(self):
        input = """
Function: main
Body:
    Var: a;
    a = a + foo(a);
EndBody.
Function: foo
Parameter: a
Body:
EndBody.
"""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_arr_84(self):
        input = """
Function: main
Body:
    Var: a[1][2][3] , b;
    b = b + a[1];
EndBody.
"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_arr_85(self):
        input = """
Function: main
Body:
    Var: a[1][2][3] , b = 5;
    b = b + a[b][b][foo()];
EndBody.
Function: foo
Body:
    Return 3;
EndBody.
"""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,485))


    def test_call_expr_86(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    x = 3;
    y = True;
    z = "String";
EndBody.
Function: main
Body:
    foo(3, False, 2);
EndBody.
"""
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(3),BooleanLiteral(False),IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_call_expr_87(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    x = 3;
    y = True;
    z = "String";
EndBody.
Function: main
Body:
    Var: x;
    x = x + foo(3, False, "2");
EndBody.
"""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_call_expr_87(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    x = 3;
    y = True;
    z = "String";
EndBody.
Function: main
Body:
    Var: x;
    x = x + foo(3, False, "2");
EndBody.
"""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_call_expr_88(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    x = 3;
    y = True;
    z = "String";
    Return 3;
EndBody.
Function: main
Body:
    Var: x;
    x = x + foo(foo(x, True, string_of_int(x)), False, "2");
EndBody.
"""
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_call_expr_89(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    x = 3;
    y = True;
    z = "String";
    Return 3;
EndBody.
Function: main
Body:
    Var: x;
    x = x + foo(x, False, "2", x);
EndBody.
"""
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[Id('x'),BooleanLiteral(False),StringLiteral('2'),Id('x')])))
        self.assertTrue(TestChecker.test(input,expect,489))


    def test_call_expr_90(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    x = 3;
    y = True;
    z = "String";
    Return 3;
EndBody.
Function: main
Body:
    Var: x;
    x = foo(x, False, "2") + foo(x, False, "2");
EndBody.
"""
        expect = str(TypeCannotBeInferred(Assign(Id('x'),BinaryOp('+',CallExpr(Id('foo'),[Id('x'),BooleanLiteral(False),StringLiteral('2')]),CallExpr(Id('foo'),[Id('x'),BooleanLiteral(False),StringLiteral('2')])))))
        self.assertTrue(TestChecker.test(input,expect,490))


    def test_call_stmt_91(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    foo(3,2,1);
    x = True;
EndBody.
Function: main
Body:
EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id('x'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_call_stmt_92(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    z = 1 + foo(3,2,1);
    x = True;
EndBody.
Function: main
Body:
EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id('x'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_call_stmt_93(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    z = 1 + foo(3,2,1);
    foo(3,2,1);
EndBody.
Function: main
Body:
EndBody.
"""
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(3),IntLiteral(2),IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_call_stmt_94(self):
        input = """
Function: main
Body:
    foo(2,2,2);
EndBody.
Function: foo
Parameter: x, y, z
Body:
    Var: a;
    a = 1.0 +. foo(3,2,1);
EndBody.
"""
        expect = str(TypeMismatchInExpression(BinaryOp('+.',FloatLiteral(1.0),CallExpr(Id('foo'),[IntLiteral(3),IntLiteral(2),IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_main_error_95(self):
        input = """
Function: foo
Parameter: x, y, z
Body:
    Var: a;
    a = 1.0 +. foo(3,2,1);
EndBody.
"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,501))
