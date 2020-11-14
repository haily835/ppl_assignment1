import unittest
from TestUtils import TestAST
from AntiAST import *

class ASTGenSuite(unittest.TestCase):

    # test var declare
    def test_1_vardecl(self):
        """Simple program: int main() {} """
        input= """
Function: main
Body:
Var:x = 5;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[]))])

        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_2_vardecl(self):
        input = """
Function: main
Body:
Var: b[2][3] = {{2,3,4},{4,5,6}};
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_3_vardecl(self):
        input = """
Function: main
Body:
Var: c, d = 6, e, f;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_4_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10];
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_5_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_6_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var:x = 5;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("x"),[],IntLiteral(5))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # global var decl
    def test_7_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
EndBody."""
        expect = Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_8_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
Var: a = 5, c = 6, d;
EndBody."""
        expect = Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("c"),[],IntLiteral(6)),VarDecl(Id("d"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_9_vardecl(self):
        input = """
Var: m, n[10] = {True,False,True,False,True,False,True,False,True};
Function: main
Body:
Var: a = "string", c = 567e-11, d;
EndBody."""
        expect = Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],StringLiteral("string")),VarDecl(Id("c"),[],FloatLiteral(5.67e-09)),VarDecl(Id("d"),[],None)],[]))])
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
        expect = Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("another"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

# test simple expression
    def test_11_expr_simple(self):
        input = """Function: main
Body:
    a = 3 + 4;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_12_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 +. 4.6;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+.",FloatLiteral(3.0),FloatLiteral(4.6)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_13_expr_simple(self):
        input = """Function: main
Body:
    a = 3 - 4;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("-",IntLiteral(3),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_14_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 -. 4.6;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("-.",FloatLiteral(3.0),FloatLiteral(4.6)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_15_expr_simple(self):
        input = """Function: main
Body:
    a = 3*4;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("*",IntLiteral(3),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_16_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 *. 4.6;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("*.",FloatLiteral(3.0),FloatLiteral(4.6)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_17_expr_simple(self):
        input = """Function: main
Body:
    a = 3 \\ 4;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("\\",IntLiteral(3),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_18_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 \\. 4.6;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("\.",FloatLiteral(3.0),FloatLiteral(4.6)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_19_expr_simple(self):
        input = """Function: main
Body:
    a = 3 % 4;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("%",IntLiteral(3),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_20_expr_simple(self):
        input = """Function: main
Body:
    a = !foo(x);

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("!",CallExpr(Id("foo"),[Id("x")])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_21_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) && True;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("&&",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_22_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) || True;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("||",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_23_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) == True;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("==",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_24_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) != True;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("!=",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_25_expr_simple(self):
        input = """Function: main
Body:
    a = 4 < 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_26_expr_simple(self):
        input = """Function: main
Body:
    a = 4 > 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_27_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <= 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<=",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_28_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >= 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">=",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_29_expr_simple(self):
        input = """Function: main
Body:
    a = 4 =/= 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("=/=",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_30_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <. 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<.",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_31_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >. 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">.",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_32_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >=. 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">=.",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_33_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <=. 3;

EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<=.",IntLiteral(4),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_34_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 + 2 - 4 + 6;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",BinaryOp("-",BinaryOp("+",BinaryOp("+",IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(4)),IntLiteral(6)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_35_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 * 2;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",IntLiteral(10),BinaryOp("*",IntLiteral(2),IntLiteral(2))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_36_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_37_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3 || 4 && 6;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(6)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_38_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - (2 && 3);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(2)),BinaryOp("&&",IntLiteral(2),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_39_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("+",IntLiteral(10),BinaryOp("-",IntLiteral(2),IntLiteral(2))),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_40_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = b + c[0] && 3;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("+",Id("b"),ArrayCell(Id("c"),[IntLiteral(0)])),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_41_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 + foo(x, 6+7*8);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("+",IntLiteral(10),BinaryOp("-",IntLiteral(2),IntLiteral(2))),BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[Id("x"),BinaryOp("+",IntLiteral(6),BinaryOp("*",IntLiteral(7),IntLiteral(8)))]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_42_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 == e * 2 + 4[0];
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("==",BinaryOp("&&",BinaryOp("+",IntLiteral(10),BinaryOp("-",IntLiteral(2),IntLiteral(2))),IntLiteral(3)),BinaryOp("+",BinaryOp("*",Id("e"),IntLiteral(2)),ArrayCell(IntLiteral(4),[IntLiteral(0)]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_20_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = !(-10 + (2 - 2)) && 3;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",UnaryOp("!",BinaryOp("+",UnaryOp("-",IntLiteral(10)),BinaryOp("-",IntLiteral(2),IntLiteral(2)))),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_21_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = (!foo(-10 + (2 - 2)) && 3)[5+5];
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),ArrayCell(BinaryOp("&&",UnaryOp("!",CallExpr(Id("foo"),[BinaryOp("+",UnaryOp("-",IntLiteral(10)),BinaryOp("-",IntLiteral(2),IntLiteral(2)))])),IntLiteral(3)),[BinaryOp("+",IntLiteral(5),IntLiteral(5))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_22_expr(self):
        input = """
Function: main
Body:
a = b[1][2] + (c[1])[3] ;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2)]),ArrayCell(ArrayCell(Id("c"),[IntLiteral(1)]),[IntLiteral(3)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_23_expr(self):
        input = """
Function: main
Body:
a = -.b[1][2] +. (c[1])[3] * foo(f(x), y);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+.",UnaryOp("-.",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2)])),BinaryOp("*",ArrayCell(ArrayCell(Id("c"),[IntLiteral(1)]),[IntLiteral(3)]),CallExpr(Id("foo"),[CallExpr(Id("f"),[Id("x")]),Id("y")]))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_24_expr(self):
        input = """
Function: main
Body:
a = ---a;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("a")))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_25_expr(self):
        input = """
Function: main
Body:
a = b[foo(x)][2][3][4];
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),ArrayCell(Id("b"),[CallExpr(Id("foo"),[Id("x")]),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_26_expr(self):
        input = """
Function: main
Body:
a = !!!!!b[foo(x)][2][3][4];
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",ArrayCell(Id("b"),[CallExpr(Id("foo"),[Id("x")]),IntLiteral(2),IntLiteral(3),IntLiteral(4)])))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_27_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || b || d || k;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("||",BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("\.",BinaryOp("\\",BinaryOp("*.",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")),Id("d")),Id("c")),Id("a")),Id("b")),Id("d")),Id("k")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_28_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || (b || d || k);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("||",BinaryOp("&&",BinaryOp("\.",BinaryOp("\\",BinaryOp("*.",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")),Id("d")),Id("c")),Id("a")),BinaryOp("||",BinaryOp("||",Id("b"),Id("d")),Id("k"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_29_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))));
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),CallExpr(Id("foo"),[Id("b"),CallExpr(Id("foo"),[Id("c"),CallExpr(Id("foo"),[Id("d"),CallExpr(Id("f"),[Id("k")])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_30_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))))[6\\7][a[2]];
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[Id("b"),CallExpr(Id("foo"),[Id("c"),CallExpr(Id("foo"),[Id("d"),CallExpr(Id("f"),[Id("k")])])])]),[BinaryOp("\\",IntLiteral(6),IntLiteral(7)),ArrayCell(Id("a"),[IntLiteral(2)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_31_expr(self):
        input = """
Function: main
Body:
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_32_expr(self):
        input = """
Function: main
Body:
v = foo() + !(foo() * a[4][5][6]);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),BinaryOp("+",CallExpr(Id("foo"),[]),UnaryOp("!",BinaryOp("*",CallExpr(Id("foo"),[]),ArrayCell(Id("a"),[IntLiteral(4),IntLiteral(5),IntLiteral(6)])))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_33_expr(self):
        input = """
Function: main
Body:
v = foo(124, a[3][6], a && b);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),CallExpr(Id("foo"),[IntLiteral(124),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(6)]),BinaryOp("&&",Id("a"),Id("b"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_34_expr(self):
        input = """
Function: main
Body:
v = !!!!!-------.-.-.-.a%b;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),BinaryOp("%",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-.",UnaryOp("-.",UnaryOp("-.",UnaryOp("-.",Id("a")))))))))))))))),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_35_expr(self):
        input = """
Function: main
Body:
v = a != ((b != c) != d);
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),BinaryOp("!=",Id("a"),BinaryOp("!=",BinaryOp("!=",Id("b"),Id("c")),Id("d"))))]))])
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
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],[])]))])
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
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_43_while(self):
        input = """
Function: main
Body:
While x < 20 Do x = x + 1; EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(20)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    def test_44_if(self):
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
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_45_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("x"),IntLiteral(10)),BinaryOp("!=",Id("x"),IntLiteral(0))),CallExpr(Id("foo"),[Id("x"),Id("y")])),([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("x")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_46_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("printLn"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_47_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5);
    
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[CallStmt(Id("foo"),[IntLiteral(5)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_48_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5,"string", True);
    
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[CallStmt(Id("foo"),[IntLiteral(5),StringLiteral("string"),BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_49_return_stmt(self):
        input = """
Function: main
Body:
    Return;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_50_continue_stmt(self):
        input = """
Function: main
Body:
    Continue;
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_51_return_stmt(self):
        input = """
Function: main
Body:
    Var: i;
    Return i * 2 * 3;  
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[Return(BinaryOp("*",BinaryOp("*",Id("i"),IntLiteral(2)),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_52_return_stmt(self):
        input = """
Function: main
Body:
    Return foo(True,incr(5), incr(6));  
EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[Return(CallExpr(Id("foo"),[BooleanLiteral(True),CallExpr(Id("incr"),[IntLiteral(5)]),CallExpr(Id("incr"),[IntLiteral(6)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
     def test_53_function_declaration(self):
        input = """Function: foo
Parameter: a[5], c
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[5],None),VarDecl(Id("c"),[],None)],([],[])),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))