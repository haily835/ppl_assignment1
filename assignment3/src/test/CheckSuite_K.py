import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_redeclared1(self):
        """Simple program: main"""
        input = """
                Var: a,a;
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared2(self):
        """Simple program: main"""
        input = """
                Var: a;
                Var: a;
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared3(self):
        """Simple program: main"""
        input = """
                Var: a[2][3];
                Var: a;
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared4(self):
        """Simple program: main"""
        input = """
                Var: a[2][3];
                Function: a
                Body: 
                EndBody.
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Function(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared5(self):
        """Simple program: main"""
        input = """
                Function: a
                Parameter: a,a
                Body: 
                EndBody.
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared6(self):
        """Simple program: main"""
        input = """
                Function: a
                Parameter: a
                Body: 
                Var: a;
                EndBody.
                Function: main
                Body: 
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared6(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var: a,a;
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclared7(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var: a;
                Var: a;
                EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclared8(self):
        """Simple program: main"""
        input = """
                Function: b
                Body: 
                Var: a;
                EndBody.
                 Function: main
                 Body: 
                Var: a;
                EndBody.
                Function: c
                Body: 
                Var: a;
                Var: a;
                EndBody.
                """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_undeclared1(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                a = 3;
                EndBody."""
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_undeclared2(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var: a;
                a = 3;
                a = b;
                EndBody."""
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_undeclared3(self):
        """Simple program: main"""
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
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_undeclared4(self):
        """Simple program: main"""
        input = """
                Var: b;
                Function: main
                Body: 
                Var: a;
                a = 3;
                a = b;
                b = c;
                EndBody.
                """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared5(self):
        """Simple program: main"""
        input = """
                Var: b;
                Function: main
                Body: 
                Var: a;
                a = too();
                a = b;
                b = c;
                EndBody.
                """
        expect = str(Undeclared(Function(), "too"))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_typemismatch1(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: x,y,z
                Body: 
                x =2;
                y =3.0;
                x = x + y;
                EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp("+", Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_typemismatch2(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var : a;
                Var : b;
                a = 3;
                b = 3.3;
                a = b;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"), Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_typemismatch3(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var : a[2][2] ;
                Var: b = 2;
                Var: c = 2;
                b = a[2][2] +. 2.2;
                c = a[2][1] + 1;
                EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"), BinaryOp(
            "+.", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(2)]), FloatLiteral(2.2)))))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_typemismatch2(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var : a[2][2] ;
                Var: b;
                Var: c;
                b = a[2][2] +. 2.2;
                c = a[2][2] + 2;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp(
            "+", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(2)]), IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_typemismatch4(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter:  a[2][2] 
                Body: 
                Var: b,c;
                b = a[2][2] +. 2.2;
                c = a[2][0] + 2;
                EndBody."""
        expect = str(TypeMismatchInExpression(BinaryOp(
            "+", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(0)]), IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_passbyref_val(self):
        """Simple program: main"""
        input = """
                Var: a;
                Function: main
                Body: 
                a = 3;
                EndBody.
                Function: lain
                Body: 
                Var: b;
                a= 3.3;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(
            Assign(Id("a"), FloatLiteral(3.3))))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_passbyref_val2(self):
        """Simple program: main"""
        input = """
                Var: a[1][2] = {{2,3}};
                Function: main
                Body: 
                a[0][0] = 1.1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(
            Assign(ArrayCell(Id("a"), [IntLiteral(0), IntLiteral(0)]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_passbyref_val3(self):
        """Simple program: main"""
        input = """
                Var: a[1][2];
                Function: main
                Body: 
                a[0][0] = 1.1;
                EndBody.
                Function: lain
                Body: 
                a[0][0] = 1;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(
            Assign(ArrayCell(Id("a"), [IntLiteral(0), IntLiteral(0)]), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_passbyref_val4(self):
        """Simple program: main"""
        input = """
                Var: a[1][2];
                Function: main
                Body: 
                Var: a[1][2];
                a[0][0] = 1.1;
                EndBody.
                Function: lain
                Body: 
                a[0][0] = 1;
                a[0][0] = 1.2;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(
            Assign(ArrayCell(Id("a"), [IntLiteral(0), IntLiteral(0)]), FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_passbyref_val5(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var: a[1][2];
                a[0][0] = 1.1;
                EndBody.
                Function: lain
                Body: 
                a[0][0] = 1;
                a[0][0] = 1.2;
                EndBody.
                """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_passbyref_val5(self):
        """Simple program: main"""
        input = """
                Function: main
                Body: 
                Var: a[1][2];
                a[0][0] = 1.1;
                EndBody.
                Function: lain
                Body: 
                a[0][0] = 1;
                a[0][0] = 1.2;
                EndBody.
                """
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_passbyref_val6(self):
        """Simple program: main"""
        input = """
                Function: lain
                Parameter: a
                Body:
                a = 3;
                EndBody.
                Function: main
                Body: 
                lain();
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("lain"), [])))
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_passbyref_val7(self):
        """Simple program: main"""
        input = """
                Function: lain
                Parameter: a
                Body:
                a = 3;
                EndBody.
                Function: main
                Parameter: b
                Body: 
                b = 3 + lain();
                EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("lain"), [])))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_passbyref_val8(self):
        """Simple program: main"""
        input = """
                Function: lain
                Parameter: a
                Body:
                lain(3);
                EndBody.
                Function: main
                Parameter: b
                Body: 
                lain(b);
                EndBody.
                """
        expect = str(TypeCannotBeInferred(CallStmt(Id("lain"), [Id("b")])))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_passbyref_val9(self):
        """Simple program: main"""
        input = """
                Function: lain
                Body:
                Return 3;
                EndBody.
                Function: main
                Parameter: b
                Body: 
                lain();
                EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("lain"), [])))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_passbyref_val10(self):
        """Simple program: main"""
        input = """
                Function: lain
                Parameter:x,y
                Body:
                x = 3;
                lain(4.3,0);
                EndBody.
                Function: main
                Body: 
                EndBody.
                """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id("lain"), [FloatLiteral(4.3), IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_infering(self):
        """Simple program: main"""
        input = """
                Var: a;
                Function: lain
                Body:
                a = main();
                EndBody.
                Function: main
                Body: 
                Return 1;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(
            Assign(Id("a"), CallExpr(Id("main"), []))))
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_infering2(self):
        """Simple program: main"""
        input = """
                Var: a;
                Function: foo
                Parameter: k
                Body:
                EndBody.
                Function: main
                Body: 
                Var: y,a,x;
                y = a + foo(x) ;
                EndBody.
                """
        expect = str(TypeCannotBeInferred(
            Assign(Id("y"), BinaryOp("+", Id("a"), CallExpr(Id("foo"), [Id("x")])))))
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_infering2(self):
        """Simple program: main"""
        input = """
                Var: a[1],b[2];
                Function: foo
                Body:
                a[1] = b[2];
                EndBody.
                Function: main
                Body: 
                EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(
            ArrayCell(Id("a"), [IntLiteral(1)]), ArrayCell(Id("b"), [IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_infering3(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: y
                Body: 
                main(3.3);
                y = 4;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("y"), IntLiteral(4))))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_infering4(self):
        """Simple program: main"""
        input = """
                Function: main
                Parameter: x,y,z
                Body:
                x = 4;
                z = 2;
                main(x,5.3,z);
                y = 4;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("y"), IntLiteral(4))))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_infering5(self):
        """Simple program: main"""
        input = """
                Function: foo
                Body:
                Return 1.1;
                EndBody.
                Function: main
                Parameter: y
                Body: 
                main(foo());
                y = 4;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("y"), IntLiteral(4))))
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_infering6(self):
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
                main(x,foo(),loo());
                y = 4;
                EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id("y"), IntLiteral(4))))
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_34(self):
        """Simple program: main"""
        input = """
                Function: foo
                Body:
                Return 1.1;
                EndBody.
                Function: main
                Body: 
                Var: x,y,a;
                y = a + foo(x) ;

                EndBody.
                """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"), [Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        """Simple program: main"""
        input = """
                Function: foo
                Parameter: x
                Body:
                Return 1.1;
                EndBody.
                Function: main
                Body: 
                Var: x,y,a;
                y = a + foo(x) ;

                EndBody.
                """
        expect = str(TypeCannotBeInferred(
            Assign(Id("y"), BinaryOp("+", Id("a"), CallExpr(Id("foo"), [Id("x")])))))
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        """Simple program: main"""
        input = """
                Function: main
                    Body:
                        foo()[0] = 1; **1**
                    EndBody.

                Function: foo
                    Body:
                        Return 0; **2**
                    EndBody.
                """
        expect = str(TypeCannotBeInferred(
            Assign(ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(0)]), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        """Simple program: main"""
        input = """
                Function: foo
                    Body:
                        Var: a[2][2];
                        Return a; **2**
                    EndBody.
                Function: main
                    Body:
                        foo() = 1; **1**
                    EndBody.
                """
        expect = str(TypeMismatchInStatement(
            Assign(CallExpr(Id("foo"), []), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        """Simple program: main"""
        input = """
                Function: foo
                    Body:
                        Var: a[2][2];
                        Return a[1]; **2**
                    EndBody.
                Function: main
                    Body:
                        foo() = 1; **1**
                    EndBody.
                """
        expect = str(TypeMismatchInExpression(
            ArrayCell(Id("a"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        """Simple program: main"""
        input = """
                Var: a;
                Function: foo
                    Body:
                        a = 3;
                    EndBody.
                Function: main
                    Body:
                        a = 3.3;
                    EndBody.
                """
        expect = str(TypeMismatchInStatement(
            Assign(Id("a"), FloatLiteral(3.3))))
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        """Simple program: main"""
        input = """
                Var: a = 3;
                Function: foo
                    Parameter: b
                    Body:
                    Var: c,d;
                    c = b +.d;
                    EndBody.
                Function: main
                    Body:
                    foo(a);
                    EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        """Simple program: main"""
        input = """
                Var: a ;
                Function: foo
                    Parameter: b
                    Body:
                    Var: c,d;
                    c = b +.d;
                    EndBody.
                Function: main
                    Body:
                    foo(a);
                    a = 1;
                    EndBody.
                """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"), [Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        """Simple program: main"""
        input = """
                Var: a = 3;
                Function: foo
                    Parameter: b
                    Body:
                    b = 3 + 3;
                    EndBody.
                Function: main
                    Body:
                    foo(a);
                    a = 4;
                    EndBody.
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [Id("a")])))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        """Simple program: main"""
        input = """ Var: x;
                Function: main
                Body:
                foo(1.1);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 1;
                EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id("x"), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        """Simple program: main"""
        input = """ Var: x;
                Function: main
                Body:
                foo(1.1,2.4,3);
                EndBody.
                Function: foo
                Parameter: x,y,z
                Body:
                    y = 2.3 *. z;
                EndBody.
                    """
        expect = str(TypeMismatchInExpression(
            BinaryOp("*.", FloatLiteral(2.3), Id("z"))))
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        """Simple program: main"""
        input = """ Var: x[2] = {2,2};
                Function: main
                Body:
                foo(x[2]);
                EndBody.
                Function: foo
                Parameter: x
                Body:
                    x = 3.5;
                EndBody.
                    """
        expect = str(TypeMismatchInStatement(
            Assign(Id("x"), FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        """Simple program: main"""
        input = """ 
                Function: main
                Body:
                Var: x[2][1] = {{2},{2}};
                Var: b[2] = {1,1};
                x[1] = b[1];
                EndBody.
                    """
        expect = str(TypeMismatchInExpression(
            ArrayCell(Id("x"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        """Simple program: main"""
        input = """ 
                Function: main
                Parameter: n
                Body:
                    n = 3.1;
                    If n == 0 Then
                    Else
                    EndIf.
                EndBody.
                    """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("n"),IntLiteral(0))))
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_48(self):
        """Simple program: main"""
        input = """ 
                Function: main
                Parameter: n
                Body:
                    Var: a;
                    n =  (3 \\ 4 - 1 + 4 * 2  \\ 2) % 2 \\ 3;
                    a = n \\. 3;
                EndBody.
                    """
        expect = str(TypeMismatchInExpression(BinaryOp("\\.",Id("n"),IntLiteral(3))))
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_49(self):
        """Simple program: main"""
        input = """ 
                Function: main
                Parameter: n
                Body:
                    Var: a;
                    n =  (((3 \\ 4 - 1 + 4 * 2  \\ 2) % 2) \\ 3);
                    a = 2.3 +. 4.2 % 2.1  \\. 3.0;
                EndBody.
                    """
        expect = str(TypeMismatchInExpression(BinaryOp("%",FloatLiteral(4.2),FloatLiteral(2.1))))
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_50(self):
        """Simple program: main"""
        input = """ 
                Function: main
                Parameter: n
                Body:
                    Var: c;
                    n = 3;
                    If n == 0 Then
                    c = 3.3;
                    ElseIf (n == 3) Then 
                    c = 4.5;
                    Else
                    c = 2;
                    EndIf.
                EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id("c"),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_51(self):
        """Simple program: main"""
        input = """ Var: x;
                    Function: main
                    Body:
                        x = 1;
                        If (x==1) Then 
                        Var: x = 1.1;
                        ElseIf (x == 3) Then 
                        Var: c = 4.5;
                        Else
                        EndIf.
                        x = c;
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_52(self):
        """Simple program: main"""
        input = """ Function: main
                    Body:
                        Var: x = 1;
                        Var: y = 0.5;
                        Var: a;
                        a = -foo(1, 1, 1, 1);
                    EndBody.
                    Function: foo
                    Parameter: a,b,c,d
                    Body:
                        Var: k;
                        k = a + b + c + d;
                        Return 3.5;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        """Simple program: main"""
        input = """ Function: main
                    Body:
                        Var: x = 1;
                        Var: y = 0.5;
                        Var: a;
                        a = -foo(1, 1, 1, 1);
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(3.5))))
        self.assertTrue(TestChecker.test(input, expect, 452))
