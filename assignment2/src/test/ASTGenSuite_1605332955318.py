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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[]))]))

        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_2_vardecl(self):
        input = """
Function: main
Body:
Var: b[2][3] = {{2,3,4},{4,5,6}};
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_3_vardecl(self):
        input = """
Function: main
Body:
Var: c, d = 6, e, f;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None)],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_4_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10];
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],None)],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_5_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)]))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_6_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var:x = 5;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])),VarDecl(Id("b"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("x"),[],IntLiteral(5))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # global var decl
    def test_7_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
EndBody."""
        expect = str(Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])),FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_8_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
Var: a = 5, c = 6, d;
EndBody."""
        expect = str(Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(10)])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("c"),[],IntLiteral(6)),VarDecl(Id("d"),[],None)],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_9_vardecl(self):
        input = """
Var: m, n[10] = {True,False,True,False,True,False,True,False,True};
Function: main
Body:
Var: a = "string", c = 567e-11, d;
EndBody."""
        expect = str(Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],StringLiteral("string")),VarDecl(Id("c"),[],FloatLiteral(5.67e-09)),VarDecl(Id("d"),[],None)],[]))]))
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
        expect = str(Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[IntLiteral(10)],None),FuncDecl(Id("another"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_11_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 + 2 - 4 + 6;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",BinaryOp("-",BinaryOp("+",BinaryOp("+",IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(4)),IntLiteral(6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_12_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 * 2;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",IntLiteral(10),BinaryOp("*",IntLiteral(2),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_13_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_14_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3 || 4 && 6;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(2)),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_15_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - (2 && 3);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",IntLiteral(10),IntLiteral(2)),BinaryOp("&&",IntLiteral(2),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_16_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("+",IntLiteral(10),BinaryOp("-",IntLiteral(2),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_17_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = b + c[0] && 3;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("+",Id("b"),ArrayCell(Id("c"),[IntLiteral(0)])),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_18_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 + foo(x, 6+7*8);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",BinaryOp("+",IntLiteral(10),BinaryOp("-",IntLiteral(2),IntLiteral(2))),BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[Id("x"),BinaryOp("+",IntLiteral(6),BinaryOp("*",IntLiteral(7),IntLiteral(8)))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_19_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 == e * 2 + 4[0];
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("==",BinaryOp("&&",BinaryOp("+",IntLiteral(10),BinaryOp("-",IntLiteral(2),IntLiteral(2))),IntLiteral(3)),BinaryOp("+",BinaryOp("*",Id("e"),IntLiteral(2)),ArrayCell(IntLiteral(4),[IntLiteral(0)]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_20_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = !(-10 + (2 - 2)) && 3;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),BinaryOp("&&",UnaryOp("!",BinaryOp("+",UnaryOp("-",IntLiteral(10)),BinaryOp("-",IntLiteral(2),IntLiteral(2)))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_21_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = (!foo(-10 + (2 - 2)) && 3)[5+5];
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(10))],[Assign(Id("a"),ArrayCell(BinaryOp("&&",UnaryOp("!",CallExpr(Id("foo"),[BinaryOp("+",UnaryOp("-",IntLiteral(10)),BinaryOp("-",IntLiteral(2),IntLiteral(2)))])),IntLiteral(3)),[BinaryOp("+",IntLiteral(5),IntLiteral(5))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_22_expr(self):
        input = """
Function: main
Body:
a = b[1][2] + (c[1])[3] ;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2)]),ArrayCell(ArrayCell(Id("c"),[IntLiteral(1)]),[IntLiteral(3)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_23_expr(self):
        input = """
Function: main
Body:
a = -.b[1][2] +. (c[1])[3] * foo(f(x), y);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+.",UnaryOp("-.",ArrayCell(Id("b"),[IntLiteral(1),IntLiteral(2)])),BinaryOp("*",ArrayCell(ArrayCell(Id("c"),[IntLiteral(1)]),[IntLiteral(3)]),CallExpr(Id("foo"),[CallExpr(Id("f"),[Id("x")]),Id("y")]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_24_expr(self):
        input = """
Function: main
Body:
a = ---a;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("a")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_25_expr(self):
        input = """
Function: main
Body:
a = b[foo(x)][2][3][4];
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),ArrayCell(Id("b"),[CallExpr(Id("foo"),[Id("x")]),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_26_expr(self):
        input = """
Function: main
Body:
a = !!!!!b[foo(x)][2][3][4];
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",ArrayCell(Id("b"),[CallExpr(Id("foo"),[Id("x")]),IntLiteral(2),IntLiteral(3),IntLiteral(4)])))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_27_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || b || d || k;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("||",BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("\.",BinaryOp("\\",BinaryOp("*.",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")),Id("d")),Id("c")),Id("a")),Id("b")),Id("d")),Id("k")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_28_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || (b || d || k);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("||",BinaryOp("&&",BinaryOp("\.",BinaryOp("\\",BinaryOp("*.",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")),Id("d")),Id("c")),Id("a")),BinaryOp("||",BinaryOp("||",Id("b"),Id("d")),Id("k"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_29_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))));
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),CallExpr(Id("foo"),[Id("b"),CallExpr(Id("foo"),[Id("c"),CallExpr(Id("foo"),[Id("d"),CallExpr(Id("f"),[Id("k")])])])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_30_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))))[6\\7][a[2]];
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[Id("b"),CallExpr(Id("foo"),[Id("c"),CallExpr(Id("foo"),[Id("d"),CallExpr(Id("f"),[Id("k")])])])]),[BinaryOp("\\",IntLiteral(6),IntLiteral(7)),ArrayCell(Id("a"),[IntLiteral(2)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_31_expr(self):
        input = """
Function: main
Body:
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_32_expr(self):
        input = """
Function: main
Body:
v = foo() + !(foo() * a[4][5][6]);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),BinaryOp("+",CallExpr(Id("foo"),[]),UnaryOp("!",BinaryOp("*",CallExpr(Id("foo"),[]),ArrayCell(Id("a"),[IntLiteral(4),IntLiteral(5),IntLiteral(6)])))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_33_expr(self):
        input = """
Function: main
Body:
v = foo(124, a[3][6], a && b);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),CallExpr(Id("foo"),[IntLiteral(124),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(6)]),BinaryOp("&&",Id("a"),Id("b"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_34_expr(self):
        input = """
Function: main
Body:
v = !!!!!-------.-.-.-.a%b;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),BinaryOp("%",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-.",UnaryOp("-.",UnaryOp("-.",UnaryOp("-.",Id("a")))))))))))))))),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_35_expr(self):
        input = """
Function: main
Body:
v = a != ((b != c) != d);
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("v"),BinaryOp("!=",Id("a"),BinaryOp("!=",BinaryOp("!=",Id("b"),Id("c")),Id("d"))))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],[])]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],([],[Break()]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[VarDecl(Id("a"),[],IntLiteral(10))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),(BinaryOp(">",Id("x"),IntLiteral(20)),[VarDecl(Id("x"),[],IntLiteral(5))],[Break()])],([VarDecl(Id("x"),[],IntLiteral(6))],[Continue()]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()])],[])]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[VarDecl(Id("a"),[],IntLiteral(0))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break(),If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[Continue()])],[])])],([VarDecl(Id("b"),[],IntLiteral(0))],[Continue()]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[Continue()])],[]),Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[Continue()])],[]),Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[VarDecl(Id("a"),[IntLiteral(1)],ArrayLiteral([IntLiteral(1)]))],[Break(),If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[Continue()])],[])])],([],[Continue()]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0))],[If([(BinaryOp("<",Id("x"),IntLiteral(20)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[If([(BinaryOp("<",Id("x"),IntLiteral(30)),[],[Break()]),(BinaryOp(">",Id("x"),IntLiteral(50)),[VarDecl(Id("a"),[],IntLiteral(10))],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))]))])],[]),Continue(),Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[Continue()])],[]),Break()]),(BinaryOp(">",Id("x"),IntLiteral(20)),[],[Break(),If([(BinaryOp(">",Id("x"),IntLiteral(50)),[],[Continue()]),(BinaryOp("<",Id("x"),IntLiteral(80)),[],[Break()])],[])])],([],[Continue()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_43_while(self):
        input = """
Function: main
Body:
While x < 20 Do x = x + 1; EndWhile.
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(20)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("<",Id("x"),IntLiteral(10)),([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("x"))),While(BinaryOp(">",Id("z"),IntLiteral(10)),([],[Assign(Id("z"),BinaryOp("-",Id("z"),IntLiteral(1)))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_45_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("x"),IntLiteral(10)),BinaryOp("!=",Id("x"),IntLiteral(0))),CallExpr(Id("foo"),[Id("x"),Id("y")])),([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("x")))]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("x"),IntLiteral(10)),BinaryOp("!=",Id("x"),IntLiteral(0))),CallExpr(Id("foo"),[Id("x"),Id("y")])),([VarDecl(Id("sum"),[],IntLiteral(0)),VarDecl(Id("a"),[IntLiteral(3)],None)],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("x"))),While(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),([VarDecl(Id("k"),[],IntLiteral(0))],[Assign(Id("sum"),BinaryOp("-",Id("sum"),Id("x")))]))]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("x"),IntLiteral(10)),BinaryOp("!=",Id("x"),IntLiteral(0))),CallExpr(Id("foo"),[Id("x"),Id("y")])),([VarDecl(Id("sum"),[],IntLiteral(0)),VarDecl(Id("a"),[IntLiteral(3)],None)],[Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("x"))),While(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),([VarDecl(Id("k"),[],IntLiteral(0))],[Assign(Id("sum"),BinaryOp("-",Id("sum"),Id("x"))),Break()])),While(BinaryOp("==",BinaryOp("%",Id("k"),IntLiteral(2)),IntLiteral(0)),([VarDecl(Id("k"),[],IntLiteral(0))],[Assign(Id("sum"),BinaryOp("-",Id("sum"),Id("x"))),Break()])),Continue()]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[Dowhile(([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),BinaryOp("<",Id("i"),IntLiteral(20)))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],IntLiteral(10))],[Dowhile(([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Dowhile(([],[Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))]),BinaryOp(">",Id("j"),IntLiteral(0)))]),BinaryOp("<",Id("i"),IntLiteral(20)))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],IntLiteral(10))],[Dowhile(([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Dowhile(([],[Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))]),BinaryOp(">",Id("j"),IntLiteral(0))),Dowhile(([],[Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Dowhile(([],[Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))]),BinaryOp(">",Id("j"),IntLiteral(0)))]),BinaryOp(">",Id("j"),IntLiteral(0)))]),BinaryOp("<",Id("i"),IntLiteral(20)))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("printLn"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_52_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        Var: isEqual = True;
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
        EndFor.
    EndFor.
    
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([VarDecl(Id("isEqual"),[],BooleanLiteral(True))],[For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(3),([],[CallStmt(Id("printLn"),[BinaryOp("*",Id("i"),Id("j"))])]))]))]))]))
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
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(1),BinaryOp("&&",BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0))),BinaryOp("*",IntLiteral(2),IntLiteral(3)),([],[CallStmt(Id("printLn"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_54_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        For (j = 1, j < 10, 3) Do
            Var: j;
            printLn(i*j);
        EndFor.
        For (j = 1, j < 10, 3) Do
            Var: isFalse = True;
            printLn(i*j);
        EndFor.
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
            For (j = 1, j < 10, 3) Do
            printLn(i*j);
            EndFor.
        EndFor.
    EndFor.
    
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(3),([VarDecl(Id("j"),[],None)],[CallStmt(Id("printLn"),[BinaryOp("*",Id("i"),Id("j"))])])),For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(3),([VarDecl(Id("isFalse"),[],BooleanLiteral(True))],[CallStmt(Id("printLn"),[BinaryOp("*",Id("i"),Id("j"))])])),For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(3),([],[CallStmt(Id("printLn"),[BinaryOp("*",Id("i"),Id("j"))]),For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(3),([],[CallStmt(Id("printLn"),[BinaryOp("*",Id("i"),Id("j"))])]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
        

    def test_55_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5);
    
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[CallStmt(Id("foo"),[IntLiteral(5)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_56_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5,"string", True);
    
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[CallStmt(Id("foo"),[IntLiteral(5),StringLiteral("string"),BooleanLiteral(True)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_57_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5 + 4 * 3 \\ 5,"string", True);
    
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(5),BinaryOp("\\",BinaryOp("*",IntLiteral(4),IntLiteral(3)),IntLiteral(5))),StringLiteral("string"),BooleanLiteral(True)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_58_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(True,incr(5), incr(6));
    
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[CallStmt(Id("foo"),[BooleanLiteral(True),CallExpr(Id("incr"),[IntLiteral(5)]),CallExpr(Id("incr"),[IntLiteral(6)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_59_return_stmt(self):
        input = """
Function: main
Body:
    Var: i;
    Return i * 2 * 3;  
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None)],[Return(BinaryOp("*",BinaryOp("*",Id("i"),IntLiteral(2)),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_60_return_stmt(self):
        input = """
Function: main
Body:
    Return foo(True,incr(5), incr(6));  
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Return(CallExpr(Id("foo"),[BooleanLiteral(True),CallExpr(Id("incr"),[IntLiteral(5)]),CallExpr(Id("incr"),[IntLiteral(6)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_61_return_stmt(self):
        input = """
Function: main
Body:
    Return;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_62_break_stmt(self):
        input = """
Function: main
Body:
    Break;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_63_continue_stmt(self):
        input = """
Function: main
Body:
    Continue;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Continue()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_64_mixstmt(self):
        input = """
Function: main
Body:
    Var: arr[2][3] = {{2,3,5},{6,7,8}};
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            printLn(arr[i][j]);
            sum = sum + arr[i][j];
        EndFor.
        i = i + 1;
    EndWhile.
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8)])])),VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("sum"),[],None)],[While(BinaryOp("<",Id("i"),IntLiteral(2)),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[CallStmt(Id("printLn"),[ArrayCell(Id("arr"),[Id("i"),Id("j")])]),Assign(Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("arr"),[Id("i"),Id("j")])))])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_65_mixstmt(self):
        input = """
Function: main
Body:
    Var: arrA[2][3] = {{2,3,5},{6,7,8}};
    Var: arrB[2][3] = {{2,3,5},{6,7,8}};
    Var: isEqual = True;
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            If((arrA[i][j]) != (arrB[i][j])) Then
                isEqual = False;
                Break;
            EndIf.
        EndFor.
        i = i + 1;
    EndWhile.
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arrA"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8)])])),VarDecl(Id("arrB"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8)])])),VarDecl(Id("isEqual"),[],BooleanLiteral(True)),VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("j"),[],None),VarDecl(Id("sum"),[],None)],[While(BinaryOp("<",Id("i"),IntLiteral(2)),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp("!=",ArrayCell(Id("arrA"),[Id("i"),Id("j")]),ArrayCell(Id("arrB"),[Id("i"),Id("j")])),[],[Assign(Id("isEqual"),BooleanLiteral(False)),Break()])],[])])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_66_mixstmt(self):
        input = """
Function: main
Body:
    Var: arrA[2][3] = {{2,3,5},{6,7,8}};
    While i < 2 Do
        Var: isEqual = True;
        For (j = 0, j < 3, 1) Do
            If((arrA[i][j]) != (arrB[i][j])) Then
                Var: isEqual = True;
                isEqual = False;
                Do
                    j = j - 1;
                    While j > 0
                EndDo.
                Break;
                foo();
            EndIf.
        EndFor.
        i = i + 1;
    EndWhile.
    Return i + 3;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("arrA"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8)])]))],[While(BinaryOp("<",Id("i"),IntLiteral(2)),([VarDecl(Id("isEqual"),[],BooleanLiteral(True))],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[If([(BinaryOp("!=",ArrayCell(Id("arrA"),[Id("i"),Id("j")]),ArrayCell(Id("arrB"),[Id("i"),Id("j")])),[VarDecl(Id("isEqual"),[],BooleanLiteral(True))],[Assign(Id("isEqual"),BooleanLiteral(False)),Dowhile(([],[Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))]),BinaryOp(">",Id("j"),IntLiteral(0))),Break(),CallStmt(Id("foo"),[])])],[])])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(BinaryOp("+",Id("i"),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_67_function_declaration(self):
        input = """Function: foo
Parameter: a[5], c
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[IntLiteral(5)],None),VarDecl(Id("c"),[],None)],([],[])),FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_68_function_declaration(self):
        input = """Function: foo
Parameter: a[5], c, b[6][7]
Body:
EndBody.

Function: foo1
Parameter: a[5], c, b[6][7], d
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[IntLiteral(5)],None),VarDecl(Id("c"),[],None),VarDecl(Id("b"),[IntLiteral(6),IntLiteral(7)],None)],([],[])),FuncDecl(Id("foo1"),[VarDecl(Id("a"),[IntLiteral(5)],None),VarDecl(Id("c"),[],None),VarDecl(Id("b"),[IntLiteral(6),IntLiteral(7)],None),VarDecl(Id("d"),[],None)],([],[])),FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_69_function_declaration(self):
        input = """Function: foo
Parameter: a[5], c
Body:
    Var: x,y,z;
EndBody.

Function: main
Body:
    Var: k,m,n,o;
EndBody."""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[IntLiteral(5)],None),VarDecl(Id("c"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[])),FuncDecl(Id("main"),[],([VarDecl(Id("k"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("o"),[],None)],[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_70_function_declaration(self):
        input = """
Function: foo
Parameter: a[5], c
Body:
    Var: x,y,z;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            printLn(arr[i][j]);
            sum = sum + arr[i][j];
        EndFor.
        i = i + 1;
    EndWhile.
EndBody.

Function: main
Parameter: d[5], e
Body:
    Var: k,m,n,o;
    For (j = 1, j < 10, 3) Do
            Var: j;
            printLn(i*j);
    EndFor.
EndBody."""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[IntLiteral(5)],None),VarDecl(Id("c"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[While(BinaryOp("<",Id("i"),IntLiteral(2)),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(3)),IntLiteral(1),([],[CallStmt(Id("printLn"),[ArrayCell(Id("arr"),[Id("i"),Id("j")])]),Assign(Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("arr"),[Id("i"),Id("j")])))])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))])),FuncDecl(Id("main"),[VarDecl(Id("d"),[IntLiteral(5)],None),VarDecl(Id("e"),[],None)],([VarDecl(Id("k"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("o"),[],None)],[For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(3),([VarDecl(Id("j"),[],None)],[CallStmt(Id("printLn"),[BinaryOp("*",Id("i"),Id("j"))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_71_function_declaration(self):
        input = """
Function: foo
Parameter: a[5], c
Body:
EndBody.

**Main function**
Function: main
Body:
**Comment
Comment**
Var: arrA[2][3] = {{2,3,5},{6,7,8}};
Var: arrB[2][3] = {{2,3,5},{6,7,8}};
EndBody."""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[IntLiteral(5)],None),VarDecl(Id("c"),[],None)],([],[])),FuncDecl(Id("main"),[],([VarDecl(Id("arrA"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8)])])),VarDecl(Id("arrB"),[IntLiteral(2),IntLiteral(3)],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8)])]))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))


# test simple expression
    def test_73_expr_simple(self):
        input = """Function: main
Body:
    a = 3 + 4;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+",IntLiteral(3),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_74_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 +. 4.6;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("+.",FloatLiteral(3.0),FloatLiteral(4.6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_75_expr_simple(self):
        input = """Function: main
Body:
    a = 3 - 4;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("-",IntLiteral(3),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_76_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 -. 4.6;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("-.",FloatLiteral(3.0),FloatLiteral(4.6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_77_expr_simple(self):
        input = """Function: main
Body:
    a = 3*4;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("*",IntLiteral(3),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_78_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 *. 4.6;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("*.",FloatLiteral(3.0),FloatLiteral(4.6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_79_expr_simple(self):
        input = """Function: main
Body:
    a = 3 \\ 4;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("\\",IntLiteral(3),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_80_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 \\. 4.6;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("\.",FloatLiteral(3.0),FloatLiteral(4.6)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_81_expr_simple(self):
        input = """Function: main
Body:
    a = 3 % 4;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("%",IntLiteral(3),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_82_expr_simple(self):
        input = """Function: main
Body:
    a = !foo(x);

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("!",CallExpr(Id("foo"),[Id("x")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_83_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) && True;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("&&",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_84_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) || True;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("||",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_85_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) == True;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("==",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_86_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) != True;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("!=",CallExpr(Id("foo"),[Id("x")]),BooleanLiteral(True)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_87_expr_simple(self):
        input = """Function: main
Body:
    a = 4 < 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_88_expr_simple(self):
        input = """Function: main
Body:
    a = 4 > 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_89_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <= 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<=",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_90_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >= 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">=",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_91_expr_simple(self):
        input = """Function: main
Body:
    a = 4 =/= 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("=/=",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_92_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <. 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<.",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_93_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >. 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">.",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_94_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >=. 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp(">=.",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_95_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <=. 3;

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),BinaryOp("<=.",IntLiteral(4),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_96_array(self):
        input = """Function: main
Body:
    a[3] = {True, False, True};
    d[3] = {5.6,5E-10,6.03};

EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(3)]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])),Assign(ArrayCell(Id("d"),[IntLiteral(3)]),ArrayLiteral([FloatLiteral(5.6),FloatLiteral(5e-10),FloatLiteral(6.03)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_97_array(self):
        input = """
Function: main
Body:
    c[3] = {{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}};
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("c"),[IntLiteral(3)]),ArrayLiteral([ArrayLiteral([StringLiteral("a"),StringLiteral("b"),StringLiteral("c")]),ArrayLiteral([StringLiteral("e"),StringLiteral("r"),StringLiteral("h")]),ArrayLiteral([StringLiteral("k"),StringLiteral("s"),StringLiteral("m")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_98_array(self):
        input = """
Function: main
Body:
    a[3*b[2][3][4]] = 5;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("*",IntLiteral(3),ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3),IntLiteral(4)]))]),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_99_array(self):
        input = """
Function: main
Body:
    (a + foo())[1] = a[3][4];
    4[1] = 5;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(BinaryOp("+",Id("a"),CallExpr(Id("foo"),[])),[IntLiteral(1)]),ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)])),Assign(ArrayCell(IntLiteral(4),[IntLiteral(1)]),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_100_complex_program(self):
        input = """
Function: binarySearch
Parameter: arr[10], l, r, x 
Body:
    If (r >= l) Then
        Var: mid;
        mid = l + (r - l) \ 2;
        ** If the element is present at the middle 
         itself **
        If ((arr[mid]) == x) Then
            Return mid;
        EndIf.
  
        ** If element is smaller than mid, then 
        it can only be present in left subarray **
        If ((arr[mid]) > x) Then
            Return binarySearch(arr, l, mid - 1, x); 
        EndIf.

        ** Else the element can only be present 
        in right subarray **
        Return binarySearch(arr, mid + 1, r, x); 
    EndIf.
  
    ** We reach here when element is not 
    present in array **
    Return -1; 
EndBody.
  
Function: main
Body:
    Var: arr[5] = { 2, 3, 4, 10, 40 }; 
    Var: x = 10; 
    Var: n , result;
    n = sizeof(arr) \ sizeof(arr[0]); 
    result = binarySearch(arr, 0, n - 1, x);
    If (result == -1) Then 
        printLn("Element is not present in array");
    Else
        printLn("Element is present at index: ");
        printLn(result); 
    EndIf.
EndBody."""
        expect = str(Program([FuncDecl(Id("binarySearch"),[VarDecl(Id("arr"),[IntLiteral(10)],None),VarDecl(Id("l"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("x"),[],None)],([],[If([(BinaryOp(">=",Id("r"),Id("l")),[VarDecl(Id("mid"),[],None)],[Assign(Id("mid"),BinaryOp("+",Id("l"),BinaryOp("\\",BinaryOp("-",Id("r"),Id("l")),IntLiteral(2)))),If([(BinaryOp("==",ArrayCell(Id("arr"),[Id("mid")]),Id("x")),[],[Return(Id("mid"))])],[]),If([(BinaryOp(">",ArrayCell(Id("arr"),[Id("mid")]),Id("x")),[],[Return(CallExpr(Id("binarySearch"),[Id("arr"),Id("l"),BinaryOp("-",Id("mid"),IntLiteral(1)),Id("x")]))])],[]),Return(CallExpr(Id("binarySearch"),[Id("arr"),BinaryOp("+",Id("mid"),IntLiteral(1)),Id("r"),Id("x")]))])],[]),Return(UnaryOp("-",IntLiteral(1)))])),FuncDecl(Id("main"),[],([VarDecl(Id("arr"),[IntLiteral(5)],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(10),IntLiteral(40)])),VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("n"),[],None),VarDecl(Id("result"),[],None)],[Assign(Id("n"),BinaryOp("\\",CallExpr(Id("sizeof"),[Id("arr")]),CallExpr(Id("sizeof"),[ArrayCell(Id("arr"),[IntLiteral(0)])]))),Assign(Id("result"),CallExpr(Id("binarySearch"),[Id("arr"),IntLiteral(0),BinaryOp("-",Id("n"),IntLiteral(1)),Id("x")])),If([(BinaryOp("==",Id("result"),UnaryOp("-",IntLiteral(1))),[],[CallStmt(Id("printLn"),[StringLiteral("Element is not present in array")])])],([],[CallStmt(Id("printLn"),[StringLiteral("Element is present at index: ")]),CallStmt(Id("printLn"),[Id("result")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))


    def test_101_complex_program(self):
        input = """
** Gobal variable declaration **
Var: a,b,c;
** Function declaration **
Function: printArray
Parameter: a, size
Body:
    ** Local variable declaration **
    Var: i;
    For (i = 0, i < size, 1) Do
        printLn(a[i]);
    EndFor.
EndBody.

Function: main
Body:
    Var: a[5] = {5,6,7,8,9};
    printArray(a,5);
EndBody.
"""
        expect = str(Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),FuncDecl(Id("printArray"),[VarDecl(Id("a"),[],None),VarDecl(Id("size"),[],None)],([VarDecl(Id("i"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("size")),IntLiteral(1),([],[CallStmt(Id("printLn"),[ArrayCell(Id("a"),[Id("i")])])]))])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[IntLiteral(5)],ArrayLiteral([IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9)]))],[CallStmt(Id("printArray"),[Id("a"),IntLiteral(5)])]))]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

    def test_102_complex_program(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    If n == 0 Then
        Return 1;
    Else
        Return n * fact (n - 1);
    EndIf.
EndBody.

Function: main
Body:
    x = 10;
    fact (x);
EndBody."""
        expect = str(Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))]))

        self.assertTrue(TestAST.checkASTGen(input, expect, 401))

    def test_103_array(self):
        input = """
Function: main
Body:
    x[10] = 1 + 3 + 2*6 - 4;
EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("c"),[IntLiteral(3)]),ArrayLiteral([ArrayLiteral([StringLiteral("a"),StringLiteral("b"),StringLiteral("c")]),ArrayLiteral([StringLiteral("e"),StringLiteral("r"),StringLiteral("h")]),ArrayLiteral([StringLiteral("k"),StringLiteral("s"),StringLiteral("m")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 402))

















