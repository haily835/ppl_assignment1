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
Var a,b,c = 10;
EndBody.
Function: main
Body:
Var a,b,c = 10;
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
Var b,c = 10;
a = 10 + 2 - 2 && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_14_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = 10 + 2 - 2 && 3 || 4 && 6;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(6)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_15_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = 10 + 2 - (2 && 3);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(-,BinaryOp(+,IntLiteral(10),IntLiteral(2)),BinaryOp(&&,IntLiteral(2),IntLiteral(3))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_16_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = 10 + (2 - 2) && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(+,IntLiteral(10),BinaryOp(-,IntLiteral(2),IntLiteral(2))),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_17_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = b + c[0] && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(+,Id(b),ArrayCell(Id(c),[IntLiteral(0)])),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_18_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = 10 + (2 - 2) && 3 + foo(x, 6+7*8);
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,BinaryOp(+,IntLiteral(10),BinaryOp(-,IntLiteral(2),IntLiteral(2))),BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[Id(x),BinaryOp(+,IntLiteral(6),BinaryOp(*,IntLiteral(7),IntLiteral(8)))]))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_19_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = 10 + (2 - 2) && 3 == e * 2 + 4[0];
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(==,BinaryOp(&&,BinaryOp(+,IntLiteral(10),BinaryOp(-,IntLiteral(2),IntLiteral(2))),IntLiteral(3)),BinaryOp(+,BinaryOp(*,Id(e),IntLiteral(2)),ArrayCell(IntLiteral(4),[IntLiteral(0)]))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_20_expr(self):
        input = """
Function: main
Body:
Var b,c = 10;
a = !(-10 + (2 - 2)) && 3;
EndBody."""
        expect = """Program([FuncDecl(Id(main)[],([VarDecl(Id(b)),VarDecl(Id(c),IntLiteral(10))][Assign(Id(a),BinaryOp(&&,UnaryOp(!,BinaryOp(+,UnaryOp(-,IntLiteral(10)),BinaryOp(-,IntLiteral(2),IntLiteral(2)))),IntLiteral(3)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,319))


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
