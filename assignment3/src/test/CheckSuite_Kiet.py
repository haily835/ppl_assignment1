import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_00(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_01(self):
        """Complex program"""
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_02(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_03(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_04(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_05(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_06(self):
        """Simple program: main"""
        input = """
                Var: a,a;
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_07(self):
        """Simple program: main"""
        input = """ Var: x;
                    Function: main
                    Body:
                        x = 1;
                        x = 2.2;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(2.2))))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_08(self):
        """Simple program: main"""
        input = """ Var: x = 300;
                    Function: main
                    Body:
                        x = 1;
                        x = True;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_09(self):
        """Simple program: main"""
        input = """ Var: x, y[3] = {1,2,3}, z = True;
                    Function: main
                    Body:
                        x = 1.0;
                        x = y[2];
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),ArrayCell(Id("y"),[IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        input = """ Var: x = 1, x;
                    Function: main
                    Body:
                        x = 1.0;
                        x = True;
                    EndBody."""
        expect = str(Redeclared(Variable(), "x"))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        input = """ Function: main
                    Parameter: x, x
                    Body:
                        Return;
                    EndBody."""
        expect = str(Redeclared(Parameter(), "x"))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        input = """
                Function: main
                Body: 
                    Var: a;
                    a = 3;
                    a = b;
                EndBody.
                Function: abc
                Body: 
                    Var:b;
                    b = a;
                EndBody.
                """
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        input = """
                Function: main
                Parameter: x,y,z
                Body: 
                    x = 2;
                    y = 3.0;
                    x = x + y;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+", Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    If main(main(5)) Then 
                    EndIf. 
                EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        """Simple program: main"""
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
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    foo()[0] = 1; **1**
                EndBody.

                Function: foo
                Body:
                    Return 0; **2**
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    Var: x;
                    Do
                        x = 1; **1**
                    While x **2** EndDo.
                EndBody."""
        expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id("x"),IntLiteral(1))]),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    foo(1.1);
                EndBody.

                Function: foo
                Parameter: x
                Body:
                    x = 1;    
                    Return;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_19(self):
        input = """
                Function: main
                Body:
                    Var: a[2],b[4];
                    a = b;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_20(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    Var: a[2],b[4];
                    a[2] = 1;
                    b[3] = 2.0;
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_21(self):
        input = """
                Function: main
                Body:
                    Var: a[2],b[4];
                    a[2] = 1;
                    b[3] = 2;
                    a[1] = b[1];
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_22(self):
        input = """
                Function: foo
                Parameter: x
                Body:
                    foo(1);
                    Return; 
                EndBody.
                Function: main
                Body:
                    foo(1.1);
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[FloatLiteral(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x, y
                Body:
                    Var: z;
                    While (True) Do
                        z = foo(1, foo(x, True));
                    EndWhile.
                    Return y && z;
                EndBody.

                Function: main
                Body:
                    foo(2,False);
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("z"),CallExpr(Id("foo"),[IntLiteral(1),CallExpr(Id("foo"),[Id("x"),BooleanLiteral(True)])]))))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        input = """
                Function: foo
                Parameter: x, y
                Body:
                    Var: z = True;
                    While (True) Do
                        z = foo(1, False);
                    EndWhile.
                    Return y && z;
                EndBody.

                Function: main
                Body:
                    Var: m = 1;
                    m = foo(2,False);
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("m"),CallExpr(Id("foo"),[IntLiteral(2),BooleanLiteral(False)]))))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        """Simple program: main"""
        input = """
                Var: z[3] = {1,2,3};
                Function: main
                Parameter: x, y
                Body:
                    z[x] = 1; 
                    x = "String";
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),StringLiteral("String"))))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input = """
                Function: main 
                Body: 
                    Var: a = 1, x; 
                    a = foo(x); 
                EndBody. 
                Function: foo
                Parameter: x
                Body:
                    Return;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[Id("x")]))))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        """Simple program: main"""
        input = """
                Var: test;
                Function: main
                Parameter: x
                Body:
                    x = 1;
                    x = test[0];
                EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("test"),[IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        """Simple program: main"""
        input = """
                Var: a;
                Function: main
                Body:
                    foo();
                    a = 1;
                EndBody.

                Function: foo
                Body:
                    a = 1.1; 
                    Return;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        """Simple program: main"""
        input = """
                Function : print
                Parameter : x
                Body:
                    Return;
                EndBody.

                Function: m
                Body:
                    Var : value = 12345;
                    Return value;
                EndBody.

                Function: main
                Parameter : x, y
                Body: 
                    print(m); 
                    Return 0;
                EndBody."""
        expect = str(Undeclared(Identifier(),"m"))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input = """
                Var: b;
                Function: main
                Body: 
                    Var: a;
                    a = 3;
                    a = b;
                    b = c;
                EndBody. """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input = """
                Function: main
                Parameter: x,y,z
                Body: 
                    x =2;
                    y =3.0;
                    x = x + y;
                EndBody. """
        expect = str(TypeMismatchInExpression(BinaryOp("+", Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        input = """
                Function: main
                Body: 
                    Var : a[2][2] ;
                    Var: b;
                    Var: c;
                    b = a[2][2] +. 2.2;
                    c = a[2][2] + 2;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(2)]),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: x, y ,z
                Body:
                    y = x || (z > x);
                    x = 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: a[3] = {1,2,3};
                        Var: b[3];
                        b = a;
                        a = b;
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    Var: a;
                    a = foo();
                EndBody.
                Function: foo
                Body:
                    Return 1;
                EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        """Simple program: main"""
        input = """
                Var: a;

                Function: main
                Body:
                    a = 1;
                    a = foo();
                EndBody.

                Function: foo
                Body:
                    Return 1.1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        """Simple program: main"""
        input = """
                Function: foo
                Body:
                    If True Then Return 1;
                    ElseIf False Then Return 0;
                    Else Return -1;
                    EndIf.
                EndBody.

                Function: main
                Body:
                    Var: a;
                    a = foo();
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: x, y
                Body:
                    x = 1;
                    main(1.1, 0);
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[FloatLiteral(1.1),IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        """Simple program: main"""
        input = """
                Function: foo 
                Parameter: x,y
                Body:
                    Return;
                EndBody.
                
                Function: main
                Parameter: x,y
                Body:
                    foo(1, 2);  
                    foo(1. , 2.); 
                EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[FloatLiteral(1.0),FloatLiteral(2.0)])))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        foo(1,2,3);
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        """Simple program: main"""
        input = """
                Function: f
                Parameter: a
                Body:
                    f(3);
                EndBody.

                Function: main
                Parameter: b
                Body: 
                    f(b);
                EndBody."""
        expect = str(TypeCannotBeInferred(CallStmt(Id("f"), [Id("b")])))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        """Simple program: main"""
        input = """
                Var: a[1][2] = {{2,3}};
                Function: main
                Body: 
                    a[0][0] = 1.1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("a"), [IntLiteral(0), IntLiteral(0)]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        """Simple program: main"""
        input = """
                Function: main
                Body:
                    Var: x = True;
                    While x Do
                        Var: x;
                    EndWhile.
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        """Simple program: main"""
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
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: i;
                        While i Do
                            Var: i;
                            i = i + 1;
                        EndWhile.
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: i;
                        For(i = 1, i + 10, True) Do
                        EndFor.
                   EndBody."""
        expect = str(TypeMismatchInStatement(For(Id('i'),IntLiteral(1),BinaryOp('+',Id('i'),IntLiteral(10)),BooleanLiteral(True),([],[]))))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: i;
                        For(i = 1, i < 10, 1) Do
                            Var: i = 2;
                            i = i - 1;
                        EndFor.
                        i = 1.1;
                   EndBody."""
        expect = str(TypeMismatchInStatement( Assign(Id("i"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self):
        input = """ Function: main
                    Body:
                        Var: i;
                        For(i = 1, i < 10, 1) Do
                            Var: i = 2;
                            i = i -. 1.1;
                            i = "str";
                        EndFor.
                        i = 1.1;
                    EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("-.",Id("i"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input = """Function: main
                   Body:
                        Var: i;
                        For(i = 1, i < 10, 1) Do
                            Var: i = True;
                            While i Do
                                Var: i;
                                i = i + 1;
                            EndWhile.
                        EndFor.
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_51(self):
        """Simple program: main"""
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
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        """Simple program: main"""
        input = """
                Var: a;

                Function: foo
                Parameter: k
                Body:
                    Return;
                EndBody.

                Function: main
                Body: 
                    Var: y,a,x;
                    y = a + foo(x) ;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        """Simple program: main"""
        input = """
                Function: foo
                Body:
                    Return 1.1;
                EndBody.

                Function: loo
                Body:
                    Return True;
                EndBody.

                Function: main
                Parameter: x,y,z
                Body: 
                    x = 2;
                    main(x, foo(), loo());
                    y = 4;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("y"), IntLiteral(4))))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_54(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: i = 1000;
                        For(i = 1, i < 10, 1) Do
                            Var: i = True;
                            While i Do
                                Var: i;
                                i = i + 1;
                                If i > 1 Then
                                    Var: i;
                                    i = 111;
                                EndIf.
                            EndWhile.
                        EndFor.
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_55(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: i = 1000;
                        For(i = 1, i < 10, 1) Do
                            Var: i = True;
                            While i Do
                                i = i + 1;
                                If i > 1 Then EndIf.
                            EndWhile.
                        EndFor.
                   EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("+",Id("i"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_56(self):
        """Simple program: main"""
        input = """
                Var: a;

                Function: foo
                Parameter: b
                Body:
                    Var: c, d;
                    c = b +. d;
                    Return;
                EndBody.

                Function: main
                Body:
                    Var: a = 1.1;
                    foo(a);
                    a = 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_57(self):
        """Simple program: main"""
        input = """ Function: main
                    Body:
                        Var: x[2][1] = {{2},{2}};
                        Var: b[2] = {1,1};
                        x[1] = b[1];
                    EndBody."""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_58(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: n;
                        n = 3.1;
                        If n == 0 Then Else EndIf.
                   EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("n"),IntLiteral(0))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_59(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: n
                Body:
                    Var: a;
                    n = (3 \\ 4 - 1 + 4 * 2  \\ 2) % 2 \\ 3;
                    a = n \\. 3;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("\\.",Id("n"),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_60(self):
        """Simple program: main"""
        input = """ Function: main
                    Body:
                        Var: c, n;
                        n = 3;
                        If n == 0 Then c = 3.3;
                        ElseIf (n == 3) Then c = 4.5;
                        Else c = 2; EndIf.
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("c"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_61(self):
        """Simple program: main"""
        input = """
                    Var: a[6], b, c, d;
                    Function: main
                    Body:
                        Var: x;
                        a[c - 1] = 9 - 6 * (b * c);
                        a[3 + 2] = a[b] + 4;
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_62(self):
        """Simple program: main"""
        input = """
                Var: a;
                Function: foo
                Parameter: b
                Body:
                    Var: c, d;
                    c = b +. d;
                EndBody.
                Function: main
                Body:
                    foo(a);
                    a = 1;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("a")])))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_63(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x;
                        x = 1;
                        For (x = 1, x < 100, 20) Do
                            Var: x;
                            x = True;
                            While x Do
                                x = False;
                                If !x Then x = 1; EndIf.
                            EndWhile.
                        EndFor.
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_64(self):
        """Simple program: main"""
        input = """
                Var: x;
                Var: y;

                Function: main
                Body:
                    test(1, 2.0);
                    test(x, y);
                    x = x + y;
                EndBody.

                Function: test
                Parameter: a, b
                Body:
                EndBody.
                """
        expect = str(TypeCannotBeInferred(CallStmt(Id("test"),[Id("x"),Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_65(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x, y, z, t;
                        x = 1;
                        x = y; 
                        y = z;
                        z = t;
                        t = x;
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_66(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: a, b, c;
                        Do
                            a = True;
                            b = "str";
                            c = 1.1;
                        While a EndDo.
                        If b == "s" Then c = 2.2; EndIf.
                   EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("b"),StringLiteral("s"))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_67(self):
        """Simple program: main"""
        input = """
                    Function: foo
                    Parameter: x
                    Body:
                        If (x) Then Return 1;
                        Else Return 0; EndIf.
                    EndBody.
                    Function: main
                    Body:
                        Var: x = 1;
                        x = foo(False);
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_68(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    If (x) Then Return 1;
                    Else Return 0; EndIf.
                EndBody.
                Function: main
                Body:
                    Var: x = True;
                    x = foo(False);
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("foo"),[BooleanLiteral(False)]))))
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_69(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    x = 1.1;
                    Return { True };
                EndBody.

                Function: main
                Parameter: x, y
                Body:
                    Var: a[1];
                    a[1] = foo(2.2)[0];
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_70(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                    x = True;
                    Return { {1},{2},{3} };
                EndBody.

                Function: main
                Parameter: x, y
                Body:
                    Var: a[3][1];
                    a = foo(False);
                EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x = 1, y = 2.2;
                        For (x = 30, x < 100, 1) Do
                            Var: x;
                            x = 12121;
                            y = 3.3;
                        EndFor.
                        x = 12121;
                        y = 4.4;
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x, xx, xxx;
                        x = xx;
                        xx = xxx;
                        xx = 2.2;
                   EndBody."""
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("xx"))))
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        """Simple program: main"""
        input = """
                    Function: f
                    Body:
                        main();
                        Return 1;
                    EndBody.
                    Function: h
                    Body:
                        main();
                        Return 2.2;
                    EndBody.
                    Function: k
                    Body:
                        main();
                        Return True;
                    EndBody.
                    Function: main
                    Body:
                        Var: x = 200, y = 1e-3, z = True;
                        x = f();
                        y = h();
                        z = k();
                    EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x = 1, y, z;
                        z = (x > 100) && y;
                        y = z || x;
                   EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp("||",Id("z"),Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x = 1, y, z;
                        z = (x > 100) && y || True;
                        If z Then y = True; Else y = False; EndIf.
                        x = False;
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: a[10], x
                Body:
                    If a[x] Then
                        x = 2.1 +. 3.0;
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BinaryOp("+.",FloatLiteral(2.1),FloatLiteral(3.0)))))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        input = """
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                    If main(x) Then
                        x = foo(x);
                    EndIf.
                EndBody.
                Function: main
                Parameter: x
                Body:
                    If foo(x) Then
                        Return True;
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInStatement(If([(CallExpr(Id("foo"),[Id("x")]),[],[Return(BooleanLiteral(True))])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_78(self):
        input = """
                Function: x
                Body:
                EndBody.
                Function: main
                Body:
                    x = 1;
                EndBody.
		        """
        expect = str(Undeclared(Identifier(),"x"))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        input = """
                Function: main
                Parameter: x
                Body:
                    Var: i = 0, j;
                    If main(i) Then
                        If x == 0 Then
                            Return j;
                        Else
                            Return main(j);
                        EndIf.
                    EndIf.
                EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[Id("j")])))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        input = """
                Function: a
                Parameter: x
                Body:
                    Return 1;
                EndBody.

                Function: b
                Parameter: x
                Body:
                    Return 1.2;
                EndBody.

                Function: main
                Body:
                    Var: x = 2, y = 1e9;
                    x = a(1);
                    y = b(3.0);
                EndBody.
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input = """
                Function: main
                Parameter: main
                Body:
                    If main Then
                        Var: main;
                        For (main = main, main == main, main) Do
                            Var: main;
                            While main =/= main Do
                                Var: main;
                                Do
                                    Return main;
                                While main && main EndDo.
                            EndWhile.
                        EndFor.
                    EndIf.
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Return(Id("main"))))
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input = """
                Var: a, b;
                Function: a
                Body:
                    Return a() + b;
                EndBody.
                Function: b
                Body:
                    Return a + b();
                EndBody.
                Function: main
                Body:
                    Return a + b;
                EndBody.
                """
        expect = str(Redeclared(Function(),"a"))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        input = """
                Var: a[10];
                Function: main
                Body:
                    Var: x;
                    x = a[x]; 
                EndBody.
                Function: foo
                Body:
                    a[0] = 0.5;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),ArrayCell(Id("a"),[Id("x")]))))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        input = """
                Function: foo
                Body:
                    Var: a;
                EndBody.
                Function: main
                Body:
                    a = 1;
                EndBody.
                """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
        input = """
                Function: foo
                Body:
                    Var: x, y;
                    x = y;
                EndBody.
                Function: main
                Body:
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input = """
                Function: main
                Body:
                    Var: x = 0;
                    foo(x);
                EndBody.
                Function: foo
                Parameter: a, b
                Body:
                    Return;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        input = """
                Var: x;
                Function: main
                Body:
                    x = 1 + int_of_float(2.0);
                EndBody.
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        """Simple program: main"""
        input = """
                Var: x;
                Function: main
                Body:
                    x = 1;
                    x = main();
                    main();
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[])))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x;
                        x = True || (x && (1 < 2));
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self):
        input = """
                Var: x = 0, y[5], z[5][5], t[5][5][5];
                Function: main
                Body:
                    t[z[y[x]][x]][y[x]][x] = 0;
                EndBody.
		        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_91(self):
        input = """
                Function: foo
                Parameter: a
                Body:
                    a = 0;
                    a = main(a);
                    foo(main(a));
                EndBody.
                Function: main
                Parameter: a
                Body:
                    a = foo(a);
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),CallExpr(Id("foo"),[Id("a")]))))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: a, b;
                        a = 1.2;
                        b = a;
                        b = -. a;
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
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
                EndBody. """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
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
                    e = e +. foo();
                EndBody.

                Function: foo
                Body:
                    Return 3.0;
                EndBody.
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_96(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
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
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x"),BooleanLiteral(False),StringLiteral("2")])))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_98(self):
        """Simple program: main"""
        input = """Function: main
                   Body:
                        Var: x, y, z;
                        x = y || True;
                        y = z && x;
                        z = True;
                   EndBody."""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input = """
                Function: main
                Parameter: x, y
                Body:
                    Var: a;
                    x = 0;
                    a = 1;
                    main(x, a);
                    y = 1.0;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,499))
 