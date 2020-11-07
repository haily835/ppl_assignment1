import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    # test var declare
    def test_1_vardecl(self):
        """Simple program: int main() {} """
        input= """
Function: main
Body:
Var:x = 5;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(5))][]))])"""

        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_2_vardecl(self):
        input = """
Function: main
Body:
Var: b[2][3] = {{2,3,4},{4,5,6}};
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b),[IntLiteral(2),IntLiteral(3)],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6))))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_3_vardecl(self):
        input = """
Function: main
Body:
Var: c, d = 6, e, f;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(c)),VarDecl(Id(d),IntLiteral(6)),VarDecl(Id(e)),VarDecl(Id(f))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_4_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)])][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_5_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_6_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var:x = 5;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10))),VarDecl(Id(b),[IntLiteral(2),IntLiteral(3)],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),VarDecl(Id(x),IntLiteral(5))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # global var decl
    def test_7_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
EndBody."""
        expect = """Program([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10))),FuncDecl(Id(main)[],([][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_8_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
Var: a = 5, c = 6, d;
EndBody."""
        expect = """Program([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10))),FuncDecl(Id(main)[],([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(c),IntLiteral(6)),VarDecl(Id(d))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_9_vardecl(self):
        input = """
Var: m, n[10] = {True,False,True,False,True,False,True,False,True};
Function: main
Body:
Var: a = "string", c = 567e-11, d;
EndBody."""
        expect = """Program([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)],ArrayLiteral(BooleanLiteral(true),BooleanLiteral(false),BooleanLiteral(true),BooleanLiteral(false),BooleanLiteral(true),BooleanLiteral(false),BooleanLiteral(true),BooleanLiteral(false),BooleanLiteral(true))),FuncDecl(Id(main)[],([VarDecl(Id(a),StringLiteral(string)),VarDecl(Id(c),FloatLiteral(5.67e-09)),VarDecl(Id(d))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_10_vardecl(self):
        input = """
Var: m, n[10];
Function: another
Body:
Var: a,b,c = 10;
EndBody.
Function: main
Body:
Var: a,b,c = 10;
EndBody."""
        expect = """Program([VarDecl(Id(m)),VarDecl(Id(n),[IntLiteral(10)]),FuncDecl(Id(another)[],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][])),FuncDecl(Id(main)[],([VarDecl(Id(a)),VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_11_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 + 2 - 4 + 6;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(4)),IntLiteral(6)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_12_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 * 2;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,IntLiteral(10),BinaryOp(*,IntLiteral(2),IntLiteral(2))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_13_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_14_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3 || 4 && 6;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(6)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_15_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - (2 && 3);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(2)),BinaryOp(&&,IntLiteral(2),IntLiteral(3))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_16_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(+,IntLiteral(10),BinaryOp(-,IntLiteral(2),IntLiteral(2))),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_17_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = b + c[0] && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(+,Id(b),ArrayCell(Id(c),[IntLiteral(0)])),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_18_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 + foo(x, 6+7*8);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(+,IntLiteral(10),BinaryOp(-,IntLiteral(2),IntLiteral(2))),BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[Id(x),BinaryOp(+,IntLiteral(6),BinaryOp(*,IntLiteral(7),IntLiteral(8)))]))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_19_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 == e * 2 + 4[0];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(==,BinaryOp(&&,BinaryOp(+,IntLiteral(10),BinaryOp(-,IntLiteral(2),IntLiteral(2))),IntLiteral(3)),BinaryOp(+,BinaryOp(*,Id(e),IntLiteral(2)),ArrayCell(IntLiteral(4),[IntLiteral(0)]))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_20_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = !(-10 + (2 - 2)) && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,UnaryOp(!,BinaryOp(+,UnaryOp(-,IntLiteral(10)),BinaryOp(-,IntLiteral(2),IntLiteral(2)))),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_21_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = (!foo(-10 + (2 - 2)) && 3)[5+5];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),ArrayCell(BinaryOp(&&,UnaryOp(!,CallExpr(Id(foo),[BinaryOp(+,UnaryOp(-,IntLiteral(10)),BinaryOp(-,IntLiteral(2),IntLiteral(2)))])),IntLiteral(3)),[BinaryOp(+,IntLiteral(5),IntLiteral(5))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_22_expr(self):
        input = """
Function: main
Body:
a = b[1][2] + (c[1])[3] ;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+,ArrayCell(Id(b),[IntLiteral(1),IntLiteral(2)]),ArrayCell(ArrayCell(Id(c),[IntLiteral(1)]),[IntLiteral(3)])))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_23_expr(self):
        input = """
Function: main
Body:
a = -.b[1][2] +. (c[1])[3] * foo(f(x), y);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(+.,UnaryOp(-.,ArrayCell(Id(b),[IntLiteral(1),IntLiteral(2)])),BinaryOp(*,ArrayCell(ArrayCell(Id(c),[IntLiteral(1)]),[IntLiteral(3)]),CallExpr(Id(foo),[CallExpr(Id(f),[Id(x)]),Id(y)]))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_24_expr(self):
        input = """
Function: main
Body:
a = ---a;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a)))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_25_expr(self):
        input = """
Function: main
Body:
a = b[foo(x)][2][3][4];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),ArrayCell(Id(b),[CallExpr(Id(foo),[Id(x)]),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_26_expr(self):
        input = """
Function: main
Body:
a = !!!!!b[foo(x)][2][3][4];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,ArrayCell(Id(b),[CallExpr(Id(foo),[Id(x)]),IntLiteral(2),IntLiteral(3),IntLiteral(4)])))))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_27_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || b || d || k;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(||,BinaryOp(||,BinaryOp(||,BinaryOp(&&,BinaryOp(\.,BinaryOp(\,BinaryOp(*.,BinaryOp(*,BinaryOp(*,Id(a),Id(b)),Id(c)),Id(d)),Id(d)),Id(c)),Id(a)),Id(b)),Id(d)),Id(k)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_28_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || (b || d || k);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(\.,BinaryOp(\,BinaryOp(*.,BinaryOp(*,BinaryOp(*,Id(a),Id(b)),Id(c)),Id(d)),Id(d)),Id(c)),Id(a)),BinaryOp(||,BinaryOp(||,Id(b),Id(d)),Id(k))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_29_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))));
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),CallExpr(Id(foo),[Id(b),CallExpr(Id(foo),[Id(c),CallExpr(Id(foo),[Id(d),CallExpr(Id(f),[Id(k)])])])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_30_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))))[6\\7][a[2]];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(a),ArrayCell(CallExpr(Id(foo),[Id(b),CallExpr(Id(foo),[Id(c),CallExpr(Id(foo),[Id(d),CallExpr(Id(f),[Id(k)])])])]),[BinaryOp(\,IntLiteral(6),IntLiteral(7)),ArrayCell(Id(a),[IntLiteral(2)])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_31_expr(self):
        input = """
Function: main
Body:
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_32_expr(self):
        input = """
Function: main
Body:
v = foo() + !(foo() * a[4][5][6]);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(v),BinaryOp(+,CallExpr(Id(foo),[]),UnaryOp(!,BinaryOp(*,CallExpr(Id(foo),[]),ArrayCell(Id(a),[IntLiteral(4),IntLiteral(5),IntLiteral(6)])))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_33_expr(self):
        input = """
Function: main
Body:
v = foo(124, a[3][6], a && b);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(v),CallExpr(Id(foo),[IntLiteral(124),ArrayCell(Id(a),[IntLiteral(3),IntLiteral(6)]),BinaryOp(&&,Id(a),Id(b))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_34_expr(self):
        input = """
Function: main
Body:
v = !!!!!-------.-.-.-.a%b;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(v),BinaryOp(%,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-.,UnaryOp(-.,UnaryOp(-.,UnaryOp(-.,Id(a)))))))))))))))),Id(b)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_35_expr(self):
        input = """
Function: main
Body:
v = a != ((b != c) != d);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][Assign(Id(v),BinaryOp(!=,Id(a),BinaryOp(!=,BinaryOp(!=,Id(b),Id(c)),Id(d))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_36_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_37_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
Else 
        Break;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])Else([],[Break()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,336))


    def test_38_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        Var: a = 10;
        x = x + 1;
ElseIf x > 20 Then
        Var: x = 5;
        Break;
Else 
        Var: x = 6;
        Continue;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[VarDecl(Id(a),IntLiteral(10))],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[VarDecl(Id(x),IntLiteral(5))],[Break()])Else([VarDecl(Id(x),IntLiteral(6))],[Continue()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_39_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then x = x + 1;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then Break;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_40_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        Var: a = 0;
        x = x + 1;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then 
        Break;
        If x > 50 Then Continue; EndIf.
Else
        Var: b = 0;
        Continue;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[VarDecl(Id(a),IntLiteral(0))],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break(),If(BinaryOp(>,Id(x),IntLiteral(50)),[],[Continue()])])Else([VarDecl(Id(b),IntLiteral(0))],[Continue()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_41_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
ElseIf x > 20 Then
        If x > 50 Then Continue; EndIf.
        Break;
ElseIf x > 20 Then
        If x > 50 Then Continue; EndIf.
        Break;
ElseIf x > 20 Then
        Var: a[1] = {1};
        Break;
        If x > 50 Then Continue; EndIf.
Else
        Continue;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[If(BinaryOp(>,Id(x),IntLiteral(50)),[],[Continue()]),Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[If(BinaryOp(>,Id(x),IntLiteral(50)),[],[Continue()]),Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[VarDecl(Id(a),[IntLiteral(1)],ArrayLiteral(IntLiteral(1)))],[Break(),If(BinaryOp(>,Id(x),IntLiteral(50)),[],[Continue()])])Else([],[Continue()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_42_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
ElseIf x > 20 Then
        If x > 50 Then
                If x < 30 Then Break; ElseIf x > 50 Then Var: a = 10; x = x + 1; Else x = x - 1; EndIf.
        EndIf.
        Continue;
        Break;
ElseIf x > 20 Then
        If x > 50 Then Continue; EndIf.
        Break;
ElseIf x > 20 Then
        Break;
        If x > 50 Then Continue; ElseIf (x < 80) Then Break; EndIf.
Else
        Continue;
EndIf.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(x),IntLiteral(0))][If(BinaryOp(<,Id(x),IntLiteral(20)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[If(BinaryOp(>,Id(x),IntLiteral(50)),[],[If(BinaryOp(<,Id(x),IntLiteral(30)),[],[Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(50)),[VarDecl(Id(a),IntLiteral(10))],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])Else([],[Assign(Id(x),BinaryOp(-,Id(x),IntLiteral(1)))])]),Continue(),Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[If(BinaryOp(>,Id(x),IntLiteral(50)),[],[Continue()]),Break()])ElseIf(BinaryOp(>,Id(x),IntLiteral(20)),[],[Break(),If(BinaryOp(>,Id(x),IntLiteral(50)),[],[Continue()])ElseIf(BinaryOp(<,Id(x),IntLiteral(80)),[],[Break()])])Else([],[Continue()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_43_while(self):
        input = """
Function: main
Body:
While x < 20 Do x = x + 1; EndWhile.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][While(BinaryOp(<,Id(x),IntLiteral(20)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_44_while(self):
        input = """
Function: main
Body:
    While (x < 10) Do
        sum = sum + x;
        While( z > 10 ) Do
            z = z - 1;
        EndWhile.
    EndWhile.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][While(BinaryOp(<,Id(x),IntLiteral(10)),[],[Assign(Id(sum),BinaryOp(+,Id(sum),Id(x))),While(BinaryOp(>,Id(z),IntLiteral(10)),[],[Assign(Id(z),BinaryOp(-,Id(z),IntLiteral(1)))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_45_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][While(BinaryOp(&&,BinaryOp(&&,BinaryOp(<,Id(x),IntLiteral(10)),BinaryOp(!=,Id(x),IntLiteral(0))),CallExpr(Id(foo),[Id(x),Id(y)])),[],[Assign(Id(sum),BinaryOp(+,Id(sum),Id(x)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_46_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        Var: sum = 0, a[3];
        sum = sum + x;
        While ( x % 2 == 0 ) Do
                Var: k = 0;
                sum = sum - x;
        EndWhile. 
    EndWhile.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][While(BinaryOp(&&,BinaryOp(&&,BinaryOp(<,Id(x),IntLiteral(10)),BinaryOp(!=,Id(x),IntLiteral(0))),CallExpr(Id(foo),[Id(x),Id(y)])),[VarDecl(Id(sum),IntLiteral(0)),VarDecl(Id(a),[IntLiteral(3)])],[Assign(Id(sum),BinaryOp(+,Id(sum),Id(x))),While(BinaryOp(==,BinaryOp(%,Id(x),IntLiteral(2)),IntLiteral(0)),[VarDecl(Id(k),IntLiteral(0))],[Assign(Id(sum),BinaryOp(-,Id(sum),Id(x)))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_47_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        Var: sum = 0, a[3];
        sum = sum + x;
        While ( x % 2 == 0 ) Do
                Var: k = 0;
                sum = sum - x;
                Break;
        EndWhile. 
        While ( k % 2 == 0 ) Do
                Var: k = 0;
                sum = sum - x;
                Break;
        EndWhile. 
        Continue;
    EndWhile.
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([][While(BinaryOp(&&,BinaryOp(&&,BinaryOp(<,Id(x),IntLiteral(10)),BinaryOp(!=,Id(x),IntLiteral(0))),CallExpr(Id(foo),[Id(x),Id(y)])),[VarDecl(Id(sum),IntLiteral(0)),VarDecl(Id(a),[IntLiteral(3)])],[Assign(Id(sum),BinaryOp(+,Id(sum),Id(x))),While(BinaryOp(==,BinaryOp(%,Id(x),IntLiteral(2)),IntLiteral(0)),[VarDecl(Id(k),IntLiteral(0))],[Assign(Id(sum),BinaryOp(-,Id(sum),Id(x))),Break()]),While(BinaryOp(==,BinaryOp(%,Id(k),IntLiteral(2)),IntLiteral(0)),[VarDecl(Id(k),IntLiteral(0))],[Assign(Id(sum),BinaryOp(-,Id(sum),Id(x))),Break()]),Continue()])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_48_dowhile(self):
        input = """
Function: main
Body:
    Var: i;
    Do
        i = i + 1;
    While i < 20
    EndDo.
    
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i))][Dowhile([],[Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))],BinaryOp(<,Id(i),IntLiteral(20)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
        
    def test_49_dowhile(self):
        input = """
Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
        Do
            j = j - 1;
        While j > 0
        EndDo.
    While i < 20
    EndDo.
    
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(j),IntLiteral(10))][Dowhile([],[Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1))),Dowhile([],[Assign(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))],BinaryOp(>,Id(j),IntLiteral(0)))],BinaryOp(<,Id(i),IntLiteral(20)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_50_dowhile(self):
        input = """
Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
        Do
            j = j - 1;
        While j > 0
        EndDo.
        Do
            j = j - 1;
            Do
            j = j - 1;
            While j > 0
            EndDo.
        While j > 0
        EndDo.
    While i < 20
    EndDo.
    
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i),IntLiteral(0)),VarDecl(Id(j),IntLiteral(10))][Dowhile([],[Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1))),Dowhile([],[Assign(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))],BinaryOp(>,Id(j),IntLiteral(0))),Dowhile([],[Assign(Id(j),BinaryOp(-,Id(j),IntLiteral(1))),Dowhile([],[Assign(Id(j),BinaryOp(-,Id(j),IntLiteral(1)))],BinaryOp(>,Id(j),IntLiteral(0)))],BinaryOp(>,Id(j),IntLiteral(0)))],BinaryOp(<,Id(i),IntLiteral(20)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_51_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(i))][For(Id(i),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallStmt(Id(printLn),[Id(i)])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_52_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
        EndFor.
    EndFor.
    
EndBody."""
        expect = """ """
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_53_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, (i < 10) && (i % 2 == 0), 2*3) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = """ """
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
#     def test_11_function_declaration(self):
#         input = """Function: foo
# Parameter: a[5], c
# Body:
# EndBody.

# Function: main
# Body:
# EndBody."""
#         expect = "successful"
#         self.assertTrue(TestAST.checkASTGen(input, expect, 310))

#     def test_12_function_declaration(self):
#         input = """Function: foo
# Parameter: a[5], c, b[6][7]
# Body:
# EndBody.

# Function: foo1
# Parameter: a[5], c, b[6][7], d
# Body:
# EndBody.

# Function: main
# Body:
# EndBody."""
#         expect = "successful"
#         self.assertTrue(TestAST.checkASTGen(input, expect, 311))

#     def test_13_function_declaration(self):
#         input = """Function: foo
# Parameter: a[5], c
# Body:
#     Var: x,y,z;
# EndBody.

# Function: main
# Body:
#     Var k,m,n,o;
# EndBody."""
#         expect = "successful"
#         self.assertTrue(TestAST.checkASTGen(input, expect, 312))
