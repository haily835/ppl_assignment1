# kiet
from main.bkit.utils.AST import ArrayLiteral, BinaryOp, CallExpr, CallStmt, FloatLiteral, IntLiteral
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_00_simple_program(self):
        input = """Var:x=9,b;"""
        expect = Program([ VarDecl(Id("x"),[],IntLiteral(9)), VarDecl(Id("b"),[],None) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_01_simple_program(self):
        input = """Var: a;
Var: b = 0x12;
Var: cAT, d_o_G, eAgl3_12, f0_X;
Var: m, n[10] = 2;
"""
        expect = Program([ VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],IntLiteral(18)), VarDecl(Id("cAT"),[],None),VarDecl(Id("d_o_G"),[],None), VarDecl(Id("eAgl3_12"),[],None),VarDecl(Id("f0_X"),[],None), VarDecl(Id("m"),[],None), VarDecl(Id("n"),[10],IntLiteral(2)) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_02_simple_program(self):
        input = """Var: x;

Function: foo
Body:
EndBody.

Function: main
Body:
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl(Id("foo"),[],([],[])), FuncDecl(Id("main"),[],([],[])) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_03_simple_program(self):
        input = """Var: x;

Function: foo
Body:
    If (d == 6) Then
        a = 7;
    EndIf.
EndBody.

Function: main
Body:
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("foo"), [], ( [], [ If( [(BinaryOp("==",Id("d"),IntLiteral(6)),[],[Assign(Id("a"),IntLiteral(7))])], ([],[]) ) ] ) ), FuncDecl(Id("main"),[],([],[])) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_04_simple_program(self):
        input = """Var: x;

Function: func
Parameter: n, m, a[2][3]
Body:
    Return n;
EndBody.

Function: foo
Body:
    Break;
    Continue;
EndBody.

Function: main
Body:
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("func"), [ VarDecl(Id("n"),[],None), VarDecl(Id("m"),[],None), VarDecl(Id("a"),[2,3],None) ], ([],[Return(Id("n"))])), FuncDecl(Id("foo"),[],([],[Break(),Continue()])), FuncDecl(Id("main"),[],([],[])) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_05(self):
        input = """Var: x, n, a = 10;

Function: main
Body:
    Var: c;
    c = True;
    While True Do a = a + 1; EndWhile.
    print(a);
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), VarDecl(Id("n"),[],None), VarDecl(Id("a"),[],IntLiteral(10)), FuncDecl( Id("main"), [], ( [VarDecl(Id("c"),[],None),], [ Assign(Id("c"),BooleanLiteral(True)), While(BooleanLiteral(True),([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])), CallStmt(Id("print"),[Id("a")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_06(self):
        input = """Var: x;

Function: main
Body:
    Var: a[100];
    x = { 11,    2   ,3};
    fact (x);
    fact (x*a[1] + 2);
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [VarDecl(Id("a"),[100],None)], [ Assign(Id("x"),ArrayLiteral([IntLiteral(11), IntLiteral(2), IntLiteral(3)])), CallStmt(Id("fact"),[Id("x")]), CallStmt(Id("fact"),[BinaryOp("+",BinaryOp("*",Id("x"),ArrayCell(Id("a"),[IntLiteral(1)])),IntLiteral(2))]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_07(self):
        input = """Var: x;

Function: main
Body:
    If n == 0 Then
        Return 1;
    Else
        Return 0;
    EndIf.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ If( [(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])], ([],[Return(IntLiteral(0))]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_08(self):
        input = """Var: x;

Function: main
Body:
    a[c - 1] = 9 - 6 * (b * c);
    a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign( ArrayCell(Id("a"),[BinaryOp("-",Id("c"),IntLiteral(1))]), BinaryOp("-",IntLiteral(9),BinaryOp("*",IntLiteral(6),BinaryOp("*",Id("b"),Id("c")))) ), Assign( ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]), BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_09(self):
        input = """Var: x;

Function: main
Body:
        Var: i;
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [VarDecl(Id("i"),[],None)], [ For( Id("i"), IntLiteral(0), BinaryOp("<",Id("i"),IntLiteral(10)), IntLiteral(2), ([],[ CallStmt(Id("writeln"),[Id("i")])]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_10(self):
        input = """Var: x;

Function: main
Body:
        Var: i;
        For (i = 0, i < 2, 5) Do
            i = 2.0*i + 4.5\\i;
            print(i);
        EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [VarDecl(Id("i"),[],None)], [ For( Id("i"), IntLiteral(0), BinaryOp("<",Id("i"),IntLiteral(2)), IntLiteral(5), ([],[ Assign(Id("i"),BinaryOp("+",BinaryOp("*",FloatLiteral(2.0),Id("i")),BinaryOp("\\",FloatLiteral(4.5),Id("i")))), CallStmt(Id("print"),[Id("i")]) ]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """Var: x = 9.01, y = 9e-9;

Function: main
Body:
    a_1 = 1;
    b = 2;
    writeln(max(a,b));
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],FloatLiteral(9.01)), VarDecl(Id("y"),[],FloatLiteral(9e-9)), FuncDecl( Id("main"), [], ( [], [ Assign(Id("a_1"),IntLiteral(1)), Assign(Id("b"),IntLiteral(2)), CallStmt(Id("writeln"),[CallExpr(Id("max"),[Id("a"),Id("b")])]), ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        input = """
Function: main
    Body:
        If (a == 0) || (b == 0) Then
            Return 0;
        EndIf.
        Return abs(a) * (abs(b) \\ gcd(a, b));
    EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ If( [(BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(0)),BinaryOp("==",Id("b"),IntLiteral(0))),[],[Return(IntLiteral(0))])], ([],[])), Return( BinaryOp("*", CallExpr(Id("abs"),[Id("a")]), BinaryOp("\\",CallExpr(Id("abs"),[Id("b")]),CallExpr(Id("gcd"),[Id("a"),Id("b")])))) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """
Function: foo
Parameter: a
Body:
    Return a*2;
EndBody.

Function: foo1
Parameter: x,y
Body:
    Return x+y;
EndBody.

Function: main
Body:
    Var: a;
    a = foo1(2,3);
EndBody.
"""
        expect = Program([ FuncDecl( Id("foo"), [VarDecl(Id("a"),[],None)], ( [], [Return(BinaryOp("*",Id("a"),IntLiteral(2)))] ) ), FuncDecl( Id("foo1"), [ VarDecl(Id("x"),[],None), VarDecl(Id("y"),[],None) ], ( [], [Return(BinaryOp("+",Id("x"),Id("y")))] ) ), FuncDecl( Id("main"), [], ( [VarDecl(Id("a"),[],None),], [Assign(Id("a"),CallExpr(Id("foo1"),[IntLiteral(2),IntLiteral(3)]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """
Function: main
Body:
    Var: i;
    For (i=0, i <= n, 1) Do
        f[i] = f[i-1] + f[i-2];
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [VarDecl(Id("i"),[],None)], [ For( Id("i"), IntLiteral(0), BinaryOp("<=",Id("i"),Id("n")), IntLiteral(1), ([], [Assign( ArrayCell(Id("f"),[Id("i")]), BinaryOp("+",ArrayCell(Id("f"),[BinaryOp("-",Id("i"),IntLiteral(1))]),ArrayCell(Id("f"),[BinaryOp("-",Id("i"),IntLiteral(2))]))) ]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """
Function: main
Body:
    pf_array = f_array[1];
    pi_array = i_array[1];
    For (i=low(i_array), i <= high(i_array), 1) Do
        i_array[i] = random(i)-random(100);
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(Id("pf_array"),ArrayCell(Id("f_array"),[IntLiteral(1)])), Assign(Id("pi_array"),ArrayCell(Id("i_array"),[IntLiteral(1)])), For( Id("i"), CallExpr(Id("low"),[Id("i_array")]), BinaryOp("<=",Id("i"), CallExpr(Id("high"),[Id("i_array")])), IntLiteral(1), ([], [Assign(ArrayCell(Id("i_array"),[Id("i")]),BinaryOp("-",CallExpr(Id("random"),[Id("i")]),CallExpr(Id("random"),[IntLiteral(100)])))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """
Function: main
Body:
    read(a);
    read(b);
    While a != b Do
        If a < b Then b = b - a; EndIf.
        If a > b Then a = a - b; EndIf.
    EndWhile.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("read"),[Id("a")]), CallStmt(Id("read"),[Id("b")]), While( BinaryOp("!=",Id("a"),Id("b")), ([], [ If([(BinaryOp("<",Id("a"),Id("b")),[],[Assign(Id("b"),BinaryOp("-",Id("b"),Id("a")))])],([],[])), If([(BinaryOp(">",Id("a"),Id("b")),[],[Assign(Id("a"),BinaryOp("-",Id("a"),Id("b")))])],([],[])) ]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """
Function: main
Body:
    read(a);
    read(b);
    Do
        If a < b Then b = b - a; EndIf.
        If a > b Then a = a - b; EndIf.
    While a != b
    EndDo.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("read"),[Id("a")]), CallStmt(Id("read"),[Id("b")]), Dowhile( ([], [ If([(BinaryOp("<",Id("a"),Id("b")),[],[Assign(Id("b"),BinaryOp("-",Id("b"),Id("a")))])],([],[])), If([(BinaryOp(">",Id("a"),Id("b")),[],[Assign(Id("a"),BinaryOp("-",Id("a"),Id("b")))])],([],[])) ]), BinaryOp("!=",Id("a"),Id("b")) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """
Function: foo
    Parameter: n
    Body:
    EndBody.

Function: goo
    Parameter: n
    Body:
    EndBody.

Function: hoo
    Parameter: n
    Body:
    EndBody.

Function: main
    Body:
        write(foo(goo(hoo())));
    EndBody.
"""
        expect = Program([ FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[])), FuncDecl(Id("goo"),[VarDecl(Id("n"),[],None)],([],[])), FuncDecl(Id("hoo"),[VarDecl(Id("n"),[],None)],([],[])), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("write"),[CallExpr(Id("foo"),[CallExpr(Id("goo"),[CallExpr(Id("hoo"),[])])])]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """
Function: main
Body:
    foo(a)[2] = 1;
    If (y == 0) Then x = x + 1;
    ElseIf (y > 0) Then x = x - 1;
    ElseIf (y == 0) Then x = x * 2;
    Else x = x\\2;
    EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(ArrayCell(CallExpr(Id("foo"),[Id("a")]),[IntLiteral(2)]),IntLiteral(1)),If( [ (BinaryOp("==",Id("y"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]), (BinaryOp(">",Id("y"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))]), (BinaryOp("==",Id("y"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("*",Id("x"),IntLiteral(2)))]), ], ([],[Assign(Id("x"),BinaryOp("\\",Id("x"),IntLiteral(2)))]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_20(self):
        input = """
Function: foo
Body:
    Var: j, y;
    For(y = 0, y < j, 5) Do
        j = x*x*y - z*z*y;
    EndFor.
    Continue;
EndBody.

Function: main
    Body:
        foo();
    EndBody.
"""
        expect = Program([ FuncDecl( Id("foo"), [], ( [VarDecl(Id("j"),[],None),VarDecl(Id("y"),[],None)], [For(Id("y"),IntLiteral(0),BinaryOp("<",Id("y"),Id("j")),IntLiteral(5),([],[Assign(Id("j"),BinaryOp("-",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("y")),BinaryOp("*",BinaryOp("*",Id("z"),Id("z")),Id("y"))))])),Continue()] ) ), FuncDecl( Id("main"), [], ( [], [CallStmt(Id("foo"),[])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        input = """Var: var_name1, variable_023 = "str";
Function: main
Body:
    readln (a, b, c);
    s = (a + b + c)\\.2.0;
    area = sqrt(s * (s - a)*(s-b)*(s-c));
    writeln(area);
EndBody.
"""
        expect = Program([ VarDecl(Id("var_name1"),[],None), VarDecl(Id("variable_023"),[],StringLiteral("str")), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("readln"),[Id("a"),Id("b"),Id("c")]), Assign(Id("s"),BinaryOp("\\.",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),FloatLiteral("2.0"))), Assign(Id("area"),CallExpr(Id("sqrt"),[BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("s"),BinaryOp("-",Id("s"),Id("a"))),BinaryOp("-",Id("s"),Id("b"))),BinaryOp("-",Id("s"),Id("c")))])), CallStmt(Id("writeln"),[Id("area")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_22(self):
        input = """Var: message="Hello, ";
Function: main
Body:
    writeln("Please enter your first name: ");
    readln(firstname);

    writeln("Please enter your surname: ");
    readln(surname);

    writeln();
    writeln(message, " ", firstname, " ", surname);
EndBody.
"""
        expect = Program([ VarDecl(Id("message"),[],StringLiteral("Hello, ")), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("writeln"),[StringLiteral("Please enter your first name: ")]), CallStmt(Id("readln"),[Id("firstname")]), CallStmt(Id("writeln"),[StringLiteral("Please enter your surname: ")]), CallStmt(Id("readln"),[Id("surname")]), CallStmt(Id("writeln"),[]), CallStmt(Id("writeln"),[Id("message"),StringLiteral(" "),Id("firstname"),StringLiteral(" "),Id("surname")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_23(self):
        input = """Var: drink = {"coffee", "tea", "milk", "water"};
Function: main
Body:
    writeln("Which drink do you want?");
    writeln("You can drink ", drink[0]);
EndBody.
"""
        expect = Program([ VarDecl(Id("drink"),[],ArrayLiteral([StringLiteral("coffee"),StringLiteral("tea"),StringLiteral("milk"),StringLiteral("water")])), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("writeln"),[StringLiteral("Which drink do you want?")]), CallStmt(Id("writeln"),[StringLiteral("You can drink "),ArrayCell(Id("drink"),[IntLiteral(0)])]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_24(self):
        input = """
Function: fibo
Parameter: n
Body:
    If n==1 Then fibonacci = 0;
    ElseIf n==2 Then fibonacci = 1;
    Else
        fibonacci = fibonacci(n-1) + fibonacci(n-2);
    EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("fibo"), [VarDecl(Id("n"),[],None)], ( [], [ If( [(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Assign(Id("fibonacci"),IntLiteral(0))]), (BinaryOp("==",Id("n"),IntLiteral(2)),[],[Assign(Id("fibonacci"),IntLiteral(1))])], ([],[Assign(Id("fibonacci"),BinaryOp("+",CallExpr(Id("fibonacci"),[BinaryOp("-",Id("n"),IntLiteral(1))]),CallExpr(Id("fibonacci"),[BinaryOp("-",Id("n"),IntLiteral(2))])))]) )] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_25(self):
        input = """Var: var_name1, variable_023 = "str";
Function: main
Body:
    ** initialize elements of array n to 0 **
    For (i=0,i<=10,1) Do
        n[i] = i + 100;     ** set element at location i to i + 100 **
                            ** output each array element's value **
    EndFor.

    For (j=0,j<=10,1) Do
        writeln("Element[", j, "] = ", n[j] );
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("var_name1"),[],None), VarDecl(Id("variable_023"),[],StringLiteral("str")), FuncDecl( Id("main"), [], ( [], [ For(Id("i"),IntLiteral(0),BinaryOp("<=",Id("i"),IntLiteral(10)),IntLiteral(1), ([], [Assign(ArrayCell(Id("n"),[Id("i")]),BinaryOp("+",Id("i"),IntLiteral(100)))])), For(Id("j"),IntLiteral(0),BinaryOp("<=",Id("j"),IntLiteral(10)),IntLiteral(1),([],[CallStmt(Id("writeln"),[StringLiteral("Element["),Id("j"),StringLiteral("] = "),ArrayCell(Id("n"),[Id("j")])])])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_26(self):
        input = """Var: var_name1;
Function: main
Body:
    Var: a = 10;
    While  a < 20  Do
        writeln("value of a: ", a);
        a = a + 1;
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("var_name1"),[],None), FuncDecl( Id("main"), [], ( [VarDecl(Id("a"),[],IntLiteral(10))], [While(BinaryOp("<",Id("a"),IntLiteral(20)),([],[CallStmt(Id("writeln"),[StringLiteral("value of a: "),Id("a")]),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_27(self):
        input = """Var: var_name1;
Function: main
Body:
    a = 10;
    ** check the boolean condition using if statement **
    If ( a < 20 ) Then
        ** if condition is true then print the following **
        writeln("a is less than 20 ");
    EndIf.
    writeln("value of a is : ", a);
EndBody.
"""
        expect = Program([ VarDecl(Id("var_name1"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("a"),IntLiteral(10)), If([(BinaryOp("<",Id("a"),IntLiteral(20)),[],[CallStmt(Id("writeln"),[StringLiteral("a is less than 20 ")])])],([],[])), CallStmt(Id("writeln"),[StringLiteral("value of a is : "),Id("a")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_28(self):
        input = """Var: temp = 0;
Function: main
Body:
    Var: len = 3, even = 0;
    Do
        len = temp + len;
        temp = temp + 1;
        If(len % 2 == 0) Then even = even + 1;
        EndIf.
    While (temp <. 20.0)
    EndDo.
EndBody.
"""
        expect = Program([ VarDecl(Id("temp"),[],IntLiteral(0)), FuncDecl( Id("main"), [], ( [ VarDecl(Id("len"),[],IntLiteral(3)), VarDecl(Id("even"),[],IntLiteral(0)) ], [ Dowhile(([],[ Assign(Id("len"),BinaryOp("+",Id("temp"),Id("len"))), Assign(Id("temp"),BinaryOp("+",Id("temp"),IntLiteral(1))), If([(BinaryOp("==",BinaryOp("%",Id("len"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("even"),BinaryOp("+",Id("even"),IntLiteral(1)))])],([],[]))]), BinaryOp("<.",Id("temp"),FloatLiteral(20.0))) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_29(self):
        input = """
Function: main
Body:
    If (a == 0) Then
        Return b;
    EndIf.
    While (!b == 0) Do
        If (a > b) Then
            a=a-b;
        Else
            b=b-a;
        EndIf.
    EndWhile.
    Return a;
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ If([(BinaryOp("==",Id("a"),IntLiteral(0)),[],[Return(Id("b"))])],([],[])), While(BinaryOp("==",UnaryOp("!",Id("b")),IntLiteral(0)), ([], [If( [(BinaryOp(">",Id("a"),Id("b")),[],[Assign(Id("a"),BinaryOp("-",Id("a"),Id("b")))])], ([],[Assign(Id("b"),BinaryOp("-",Id("b"),Id("a")))]))])), Return(Id("a")) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_30(self):
        input = """Var: a = 5;
Var: c, d = 6, e;
Var: m = {17,10.2}, n[10];

Function: main
Body:
    If (d == 6) Then
        a = 7;
        c = (d * e) \\ f;
    EndIf.
EndBody.
"""
        expect = Program([ VarDecl(Id("a"),[],IntLiteral(5)), VarDecl(Id("c"),[],None), VarDecl(Id("d"),[],IntLiteral(6)), VarDecl(Id("e"),[],None), VarDecl(Id("m"),[],ArrayLiteral([IntLiteral(17),FloatLiteral(10.2)])), VarDecl(Id("n"),[10],None), FuncDecl( Id("main"), [], ( [], [ If( [(BinaryOp("==",Id("d"),IntLiteral(6)),[],[Assign(Id("a"),IntLiteral(7)),Assign(Id("c"),BinaryOp("\\",BinaryOp("*",Id("d"),Id("e")),Id("f")))])],([],[])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))


    def test_31(self):
        input = """
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
    Var: a[100], x;
    x = { 11,    2   ,3};
    fact (x);
    fact (x*a[1] + 2);
EndBody.
"""
        expect = Program([ FuncDecl( Id("fact"), [VarDecl(Id("n"),[],None)], ( [], [ If( [(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])], ([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]) )])), FuncDecl( Id("main"), [], ( [VarDecl(Id("a"),[100],None),VarDecl(Id("x"),[],None)], [ Assign(Id("x"),ArrayLiteral([IntLiteral(11),IntLiteral(2),IntLiteral(3)])),CallStmt(Id("fact"),[Id("x")]),CallStmt(Id("fact"),[BinaryOp("+",BinaryOp("*",Id("x"),ArrayCell(Id("a"),[IntLiteral(1)])),IntLiteral(2))])] ) )])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_32(self):
        input = """Var: var_name1;
Function: foo
Parameter: n
Body:
    Var: a[100], x;
    x = {1,2,3};
    Return n;
EndBody.

Function: main
Body:
    Var: a[100], x;
    foo(x*a[x-1]);
EndBody.
"""
        expect = Program([ VarDecl(Id("var_name1"),[],None), FuncDecl( Id("foo"), [VarDecl(Id("n"),[],None)], ( [VarDecl(Id("a"),[100],None),VarDecl(Id("x"),[],None)], [Assign(Id("x"),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Return(Id("n"))] ) ), FuncDecl( Id("main"), [], ( [VarDecl(Id("a"),[100],None),VarDecl(Id("x"),[],None)], [CallStmt(Id("foo"),[BinaryOp("*",Id("x"),ArrayCell(Id("a"),[BinaryOp("-",Id("x"),IntLiteral(1))]))])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_33(self):
        input = """
Function: main
Body:
    a = 100;
    If (a == 10) Then
        writeln("Value of a is 10");
    ElseIf ( a == 20 ) Then
        writeln("Value of a is 20");
    ElseIf ( a == 30 ) Then
        writeln("Value of a is 30");
    Else
        writeln("None of the values is matching");
    EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [Assign(Id("a"),IntLiteral(100)), If( [(BinaryOp("==",Id("a"),IntLiteral(10)),[],[CallStmt(Id("writeln"),[StringLiteral("Value of a is 10")])]), (BinaryOp("==",Id("a"),IntLiteral(20)),[],[CallStmt(Id("writeln"),[StringLiteral("Value of a is 20")])]), (BinaryOp("==",Id("a"),IntLiteral(30)),[],[CallStmt(Id("writeln"),[StringLiteral("Value of a is 30")])])], ([],[CallStmt(Id("writeln"),[StringLiteral("None of the values is matching")])]) )] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_334(self):
        input = """Var: p ;
Function: goo
Body:
    Var: a, b, c;
    If (a+b>c) Then p = 0.5*(a+b+c);
    Else p = 0 ;
    EndIf.
EndBody.
"""
        expect = Program([ VarDecl(Id("p"),[],None), FuncDecl( Id("goo"), [], ( [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)], [If( [(BinaryOp(">",BinaryOp("+",Id("a"),Id("b")),Id("c")),[],[Assign(Id("p"),BinaryOp("*",FloatLiteral(0.5),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c"))))])], ([],[Assign(Id("p"),IntLiteral(0))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_35(self):
        input = """Var: x;
Function: main
    Body:
        For (i = 2, i <= 50, 1) Do
            For (j = 2, j <= i, 1) Do
                If (i % j) == 0  Then
                    Break;              ** if factor found, not prime **
                EndIf.
            EndFor.
            If (j == i) Then
                writeln(i , " is prime");
            EndIf.
        EndFor.
    EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [For(Id("i"),IntLiteral(2),BinaryOp("<=",Id("i"),IntLiteral(50)),IntLiteral(1),([],[ For(Id("j"),IntLiteral(2),BinaryOp("<=",Id("j"),Id("i")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),Id("j")),IntLiteral(0)),[],[Break()])],([],[]))])), If([(BinaryOp("==",Id("j"),Id("i")),[],[CallStmt(Id("writeln"),[Id("i"),StringLiteral(" is prime")])])],([],[])) ]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_36(self):
        input = """Var: m[10]={1,2,3,4,5,6}, r[7]={5,6,7,8,9};
Function: foo
Parameter: n
Body:
    For (i = 2, i <= 50, 1) Do
        For (j = 2, j <= i, 1) Do
            For (k = 0, k < 7, 1) Do
                c[i] = m[i] * r[i] ;
            EndFor.
        EndFor.
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("m"),[10],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)])), VarDecl(Id("r"),[7],ArrayLiteral([IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9)])), FuncDecl( Id("foo"), [VarDecl(Id("n"),[],None)], ( [], [ For(Id("i"),IntLiteral(2),BinaryOp("<=",Id("i"),IntLiteral(50)),IntLiteral(1),([],[For(Id("j"),IntLiteral(2),BinaryOp("<=",Id("j"),Id("i")),IntLiteral(1),([],[For(Id("k"),IntLiteral(0),BinaryOp("<",Id("k"),IntLiteral(7)),IntLiteral(1),([],[Assign(ArrayCell(Id("c"),[Id("i")]),BinaryOp("*",ArrayCell(Id("m"),[Id("i")]),ArrayCell(Id("r"),[Id("i")])))])) ])) ])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_37(self):
        input = """Var: x, ch, readkey;
Function: main
Body:
    writeln("Press \'"q\'" to exit...");
    ch = readkey;
    While ch != "q" Do
        writeln("Please press \'"q\'" to exit.");
        ch = readkey;
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), VarDecl(Id("ch"),[],None), VarDecl(Id("readkey"),[],None), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("writeln"),[StringLiteral("""Press '"q'" to exit...""")]), Assign(Id("ch"),Id("readkey")), While(BinaryOp("!=",Id("ch"),StringLiteral("q")),([],[CallStmt(Id("writeln"),[StringLiteral("""Please press '"q'" to exit.""")]),Assign(Id("ch"),Id("readkey"))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_38(self):
        input = """Var: n;
Function: main
Body:
    bl = True;
    If (n <= 1) Then bl = False;
    EndIf.

    For (i = 2, i < n, 1) Do
        If (n % i == 0) Then bl = False; EndIf.
    EndFor.
    Return bl;
EndBody.
"""
        expect = Program([ VarDecl(Id("n"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("bl"),BooleanLiteral(True)), If([(BinaryOp("<=",Id("n"),IntLiteral(1)),[],[Assign(Id("bl"),BooleanLiteral(False))])],([],[])), For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[Assign(Id("bl"),BooleanLiteral(False))])],([],[]))])), Return(Id("bl")) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_39(self):
        input = """
Function: list
Body:
    Var: a[6] = {12,45,56,37,48,50}, b[6] = {14,34,434,5,6,38}, i, count = 0;
    For (i = 0, i < 6, 5) Do
        If (a[i] >= b[i]) Then count = count + 1;
        EndIf.
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("list"), [], ( [ VarDecl(Id("a"),[6],ArrayLiteral([IntLiteral(12),IntLiteral(45),IntLiteral(56),IntLiteral(37),IntLiteral(48),IntLiteral(50)])), VarDecl(Id("b"),[6],ArrayLiteral([IntLiteral(14),IntLiteral(34),IntLiteral(434),IntLiteral(5),IntLiteral(6),IntLiteral(38)])), VarDecl(Id("i"),[],None), VarDecl(Id("count"),[],IntLiteral(0)) ], [ For( Id("i"), IntLiteral(0), BinaryOp("<",Id("i"),IntLiteral(6)), IntLiteral(5), ([], [ If([(BinaryOp(">=",ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("b"),[Id("i")])),[],[Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])],([],[])) ])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_40(self):
        input = """Var: x = 7;
Function: foo
    Body:
        Var: j = 8, y;
        For (y = 0, y < j, 5) Do
            If ((y == 3) || (y == 5)) Then j = x*x*y - z*z*y;
            Else j = 2*y + 5*y*y;
            EndIf.
        EndFor.
    EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],IntLiteral(7)), FuncDecl( Id("foo"), [], ( [VarDecl(Id("j"),[],IntLiteral(8)),VarDecl(Id("y"),[],None),], [For(Id("y"),IntLiteral(0),BinaryOp("<",Id("y"),Id("j")),IntLiteral(5),([],[ If([(BinaryOp("||",BinaryOp("==",Id("y"),IntLiteral(3)),BinaryOp("==",Id("y"),IntLiteral(5))),[],[Assign(Id("j"),BinaryOp("-",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("y")),BinaryOp("*",BinaryOp("*",Id("z"),Id("z")),Id("y"))))])], ([],[Assign(Id("j"),BinaryOp("+",BinaryOp("*",IntLiteral(2),Id("y")),BinaryOp("*",BinaryOp("*",IntLiteral(5),Id("y")),Id("y"))))]))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_41(self):
        input = """
Function: main
    Body:
        Var: i,z;
        For (i = 0, i < 10, 2) Do
            z = 2*i+6;
            If i == 4 Then Break; EndIf.
        EndFor.
    EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [VarDecl(Id("i"),[],None),VarDecl(Id("z"),[],None)], [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Assign(Id("z"),BinaryOp("+",BinaryOp("*",IntLiteral(2),Id("i")),IntLiteral(6))),If([(BinaryOp("==",Id("i"),IntLiteral(4)),[],[Break()])],([],[]))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_42(self):
        input = """
Function: foo
    Parameter: a[5], b
    Body:
        Var: i = 0;
        While (i < 5) Do
            a[i] = b +. 1.0;
            i = i + 1;
        EndWhile.
    EndBody.
"""
        expect = Program([ FuncDecl( Id("foo"), [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)], ( [VarDecl(Id("i"),[],IntLiteral(0))], [While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_43(self):
        input = """Var: var_name1;
Function: main
Body:
    Var: pow = 1;
    For (i=1, i<n, 1) Do
        pow = pow*num1;
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("var_name1"),[],None), FuncDecl( Id("main"), [], ( [VarDecl(Id("pow"),[],IntLiteral(1)),], [For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[Assign(Id("pow"),BinaryOp("*",Id("pow"),Id("num1")))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_44(self):
        input = """
Function: main
Body:
    s = "Hello, dear";
    writeln(s);
    s[1] = "J";    ** Replace the first character with J **
    s[5] = "y";    ** Replace the fifth character with y **
    writeln(s);    ** Jelly, dear **
    writeln("The length of s is ",ord(s[0]));
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(Id("s"),StringLiteral("Hello, dear")), CallStmt(Id("writeln"),[Id("s")]), Assign(ArrayCell(Id("s"),[IntLiteral(1)]),StringLiteral("J")), Assign(ArrayCell(Id("s"),[IntLiteral(5)]),StringLiteral("y")), CallStmt(Id("writeln"),[Id("s")]), CallStmt(Id("writeln"),[StringLiteral("The length of s is "),CallExpr(Id("ord"),[ArrayCell(Id("s"),[IntLiteral(0)])])]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_45(self):
        input = """
Function: main
Body:
    write("Enter a number : "); readln(s);
    val(s,r,e);
    If e != 0 Then
        writeln("Error at position : ",e);
    Else
        writeln("That was : ",r);
    EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("write"),[StringLiteral("Enter a number : ")]), CallStmt(Id("readln"),[Id("s")]), CallStmt(Id("val"),[Id("s"),Id("r"),Id("e")]), If([(BinaryOp("!=",Id("e"),IntLiteral(0)),[],[CallStmt(Id("writeln"),[StringLiteral("Error at position : "),Id("e")])])],([],[CallStmt(Id("writeln"),[StringLiteral("That was : "),Id("r")])])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_46(self):
        input = """
Function: main
Body:
    a[x[i] * 9] =  a[x[i] \\ 9] *  a[x[i] -. 9.3e-1];
    a[d - b[foo[c]]] = "This Is A String" ;
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [Assign(ArrayCell(Id("a"),[BinaryOp("*",ArrayCell(Id("x"),[Id("i")]),IntLiteral(9))]),BinaryOp("*",ArrayCell(Id("a"),[BinaryOp("\\",ArrayCell(Id("x"),[Id("i")]),IntLiteral(9))]),ArrayCell(Id("a"),[BinaryOp("-.",ArrayCell(Id("x"),[Id("i")]),FloatLiteral(9.3e-1))]))), Assign(ArrayCell(Id("a"),[BinaryOp("-",Id("d"),ArrayCell(Id("b"),[ArrayCell(Id("foo"),[Id("c")])]))]),StringLiteral("This Is A String"))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_47(self):
        input = """Var: x;
Function: giai_thua
Parameter: n
Body:
    If (n==1) Then Return 1;
    Else Return n*giai_thua(n-1);
    EndIf.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("giai_thua"), [VarDecl(Id("n"),[],None),], ( [], [If([(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Return(IntLiteral(1))])], ([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("giai_thua"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_48(self):
        input = """
Function: plus
Parameter: x,y
Body:
    Return x + y;
EndBody.

Function: minus
Parameter: x,y
Body:
    Return x - y;
EndBody.

Function: main
Body:
    print(plus(3,4));
    print(minus(4,3));
EndBody.
"""
        expect = Program([ FuncDecl( Id("plus"), [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)], ( [], [Return(BinaryOp("+",Id("x"),Id("y")))] ) ), FuncDecl( Id("minus"), [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)], ( [], [Return(BinaryOp("-",Id("x"),Id("y")))] ) ), FuncDecl( Id("main"), [], ( [], [CallStmt(Id("print"),[CallExpr(Id("plus"),[IntLiteral(3),IntLiteral(4)])]), CallStmt(Id("print"),[CallExpr(Id("minus"),[IntLiteral(4),IntLiteral(3)])])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_49(self):
        input = """Var: x;
Function: main
Body:
    x = 1;
    print(x);
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [Assign(Id("x"),IntLiteral(1)),CallStmt(Id("print"),[Id("x")])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_50(self):
        input = """Var: x;
Function: main
Body:
    writeln("Press '"q'" to exit...");
	ch = readkey;
	While ch != "q" Do
        writeln("Press '"q'" to exit...");
		ch = readkey;
	EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [CallStmt(Id("writeln"),[StringLiteral("""Press '"q'" to exit...""")]), Assign(Id("ch"),Id("readkey")), While(BinaryOp("!=",Id("ch"),StringLiteral("q")),([],[CallStmt(Id("writeln"),[StringLiteral("""Press '"q'" to exit...""")]),Assign(Id("ch"),Id("readkey"))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_51(self):
        input = """Var: month;
Function: main
Body:
    If (month == "July") || (month == "August") Then
        writeln("Month is either July or August.");
    EndIf.
EndBody.
"""
        expect = Program([ VarDecl(Id("month"),[],None), FuncDecl( Id("main"), [], ( [], [If([(BinaryOp("||",BinaryOp("==",Id("month"),StringLiteral("July")),BinaryOp("==",Id("month"),StringLiteral("August"))), [],[CallStmt(Id("writeln"),[StringLiteral("Month is either July or August.")])])],([],[]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_52(self):
        input = """Var: x;
Function: main
Body:
    Var: z = 10, i;
    While (z > 0) Do
        i = i + 1;
        z = z - 1;
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [VarDecl(Id("z"),[],IntLiteral(10)),VarDecl(Id("i"),[],None)], [While(BinaryOp(">",Id("z"),IntLiteral(0)),([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Assign(Id("z"),BinaryOp("-",Id("z"),IntLiteral(1)))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_53(self):
        input = """Var: n;
Function: main
Body:
    For (i=1,i<=10,1) Do
        writeln(n,"*",i,"=",n*i);
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("n"),[],None), FuncDecl( Id("main"), [], ( [], [For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),IntLiteral(10)),IntLiteral(1),([],[CallStmt(Id("writeln"),[Id("n"),StringLiteral("*"),Id("i"),StringLiteral("="),BinaryOp("*",Id("n"),Id("i"))])]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_54(self):
        input = """
Function: main
Body:
    a = 9 - (b * c);
    a = b % (10.0 \\. 1e-3 - d);
    a = "Tuan !@#$%^&* Kiet \\n";
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [Assign(Id("a"),BinaryOp("-",IntLiteral(9),BinaryOp("*",Id("b"),Id("c")))), Assign(Id("a"),BinaryOp("%",Id("b"),BinaryOp("-",BinaryOp("\.",FloatLiteral(10.0),FloatLiteral(1e-3)),Id("d")))), Assign(Id("a"),StringLiteral("""Tuan !@#$%^&* Kiet \\n"""))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_55(self):
        input = """Var: x;
Function: main
Body:
    For(y = 0, y < j, 5) Do
        While (z > 0) Do
            i = i + 1;
            z = z - 1;
        EndWhile.
        j = x*x*y - z*z*y;
    EndFor.
    Return;
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ For( Id("y"),IntLiteral(0),BinaryOp("<",Id("y"),Id("j")),IntLiteral(5), ([],[ While( BinaryOp(">",Id("z"),IntLiteral(0)), ([],[ Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))), Assign(Id("z"),BinaryOp("-",Id("z"),IntLiteral(1)))] ) ), Assign(Id("j"),BinaryOp("-",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("y")),BinaryOp("*",BinaryOp("*",Id("z"),Id("z")),Id("y")))) ]) ), Return(None) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_56(self):
        input = """
Function: main
Body:
    randomize();

    pf_array = f_array[1];
    pi_array = i_array[1];

    For (i=low(f_array), i <= high(f_array), 1) Do
        f_array[i] = (random()-random())*100;
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("randomize"),[]), Assign(Id("pf_array"),ArrayCell(Id("f_array"),[IntLiteral(1)])), Assign(Id("pi_array"),ArrayCell(Id("i_array"),[IntLiteral(1)])), For(Id("i"),CallExpr(Id("low"),[Id("f_array")]),BinaryOp("<=",Id("i"),CallExpr(Id("high"),[Id("f_array")])),IntLiteral(1),([],[Assign(ArrayCell(Id("f_array"),[Id("i")]),BinaryOp("*",BinaryOp("-",CallExpr(Id("random"),[]),CallExpr(Id("random"),[])),IntLiteral(100)))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_57(self):
        input = """Var: n;
Function: main
Body:
    While n != 0 Do
        t = m;
        m = n;
        n = t % n;
    EndWhile.
    Return m;
EndBody.
"""
        expect = Program([ VarDecl(Id("n"),[],None), FuncDecl( Id("main"), [], ( [], [ While(BinaryOp("!=",Id("n"),IntLiteral(0)),([],[Assign(Id("t"),Id("m")),Assign(Id("m"),Id("n")),Assign(Id("n"),BinaryOp("%",Id("t"),Id("n")))])), Return(Id("m")) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_58(self):
        input = """Var: x;
Function: main
Body:
    While n != "String" Do
        t = m *. 3.0;
        m = 9e-9 \\. n;
        n = "String";
    EndWhile.
    Return m;
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [While(BinaryOp("!=",Id("n"),StringLiteral("String")),([],[Assign(Id("t"),BinaryOp("*.",Id("m"),FloatLiteral(3.0))),Assign(Id("m"),BinaryOp("\.",FloatLiteral(9e-9),Id("n"))),Assign(Id("n"),StringLiteral("String"))])),Return(Id("m"))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_59(self):
        input = """
Function: foo
Parameter: n
Body:
EndBody.

Function: main
Body:
    foo();
    bar(1);
    nty(1, 2, 3);
    pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;
EndBody.
"""
        expect = Program([ FuncDecl( Id("foo"), [VarDecl(Id("n"),[],None)], ( [], [] ) ), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("foo"),[]), CallStmt(Id("bar"),[IntLiteral(1)]), CallStmt(Id("nty"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]), CallStmt(Id("pty"),[Id("hyy"),CallExpr(Id("dyf"),[]),CallExpr(Id("ily"),[IntLiteral(123),IntLiteral(456),Id("fay")]),CallExpr(Id("jtq"),[CallExpr(Id("gyh"),[])])]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_60(self):
        input = """Var: x;
Function: main
Body:
    readln (a, b, c);
    s = (a + b + c)\\.2.0;
    area = sqrt(s * (s - a)*(s-b)*(s-c));
    writeln(area);
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("readln"),[Id("a"),Id("b"),Id("c")]), Assign(Id("s"),BinaryOp("\.",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),FloatLiteral(2.0))), Assign(Id("area"),CallExpr(Id("sqrt"),[BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("s"),BinaryOp("-",Id("s"),Id("a"))),BinaryOp("-",Id("s"),Id("b"))),BinaryOp("-",Id("s"),Id("c")))])), CallStmt(Id("writeln"),[Id("area")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_61(self):
        input = """Var: i;
Function: main
Body:
    For (i=0, i <. 10.01, 1.1) Do
        writeln("abcdef");
        readln();
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("i"),[],None), FuncDecl( Id("main"), [], ( [], [For(Id("i"),IntLiteral(0),BinaryOp("<.",Id("i"),FloatLiteral(10.01)),FloatLiteral(1.1),([],[CallStmt(Id("writeln"),[StringLiteral("abcdef")]),CallStmt(Id("readln"),[])]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_62(self):
        input = """
Function: main
    Body:
        If n == 0 Then
            gcd = m;
        Else
            gcd = gcd(n, m % n);
        EndIf.
    EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Assign(Id("gcd"),Id("m"))])], ([],[Assign(Id("gcd"),CallExpr(Id("gcd"),[Id("n"),BinaryOp("%",Id("m"),Id("n"))]))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_63(self):
        input = """
Function: main
Body:
    writeln (power(exp(1.0),1.0)); ** Should print 2.72 **
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [CallStmt(Id("writeln"),[CallExpr(Id("power"),[CallExpr(Id("exp"),[FloatLiteral(1.0)]),FloatLiteral(1.0)])])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_64(self):
        input = """Var: r, d, c = 10.2;
Function: foo
    Parameter: n
    Body:
    EndBody.

Function: main
    Body:
        d = 2 * r;
        c =  pi * d;
        writeln("The circumference of the circle is ",c);
    EndBody.
"""
        expect = Program([ VarDecl(Id("r"),[],None), VarDecl(Id("d"),[],None), VarDecl(Id("c"),[],FloatLiteral(10.2)), FuncDecl( Id("foo"), [VarDecl(Id("n"),[],None)], ( [], [] ) ), FuncDecl( Id("main"), [], ( [], [Assign(Id("d"),BinaryOp("*",IntLiteral(2),Id("r"))), Assign(Id("c"),BinaryOp("*",Id("pi"),Id("d"))), CallStmt(Id("writeln"),[StringLiteral("The circumference of the circle is "),Id("c")])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_65(self):
        input = """Var: x;
Function: main
Body:
    Var: a;
    a = foo(x)[12] - g(f(x)) * abc(x);
EndBody.
"""
        expect = Program([
            VarDecl(Id("x"),[],None),
            FuncDecl(
                Id("main"),
                [],
                (
                    [VarDecl(Id("a"),[],None)],
                    [Assign(Id("a"),BinaryOp("-",ArrayCell(CallExpr(Id("foo"),[Id("x")]),[IntLiteral(12)]),BinaryOp("*",CallExpr(Id("g"),[CallExpr(Id("f"),[Id("x")])]),CallExpr(Id("abc"),[Id("x")]))))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_66(self):
        input = """
Function: main
Body:
    s = "Hello, dear";
    writeln(s);
    s[1] = "J";    ** Replace the first character with J **
    s[5] = "y";    ** Replace the fifth character with y **
    writeln(s);    ** Jelly, dear **
    writeln("The length of s is ",ord(s[0]));
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [Assign(Id("s"),StringLiteral("Hello, dear")), CallStmt(Id("writeln"),[Id("s")]), Assign(ArrayCell(Id("s"),[IntLiteral(1)]),StringLiteral("J")), Assign(ArrayCell(Id("s"),[IntLiteral(5)]),StringLiteral("y")), CallStmt(Id("writeln"),[Id("s")]), CallStmt(Id("writeln"),[StringLiteral("The length of s is "),CallExpr(Id("ord"),[ArrayCell(Id("s"),[IntLiteral(0)])])])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_67(self):
        input = """
Function: main
Body:
    write("Input an integer : "); readln(i);
    str(i,s);
    writeln("That was : ",s);
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [CallStmt(Id("write"),[StringLiteral("Input an integer : ")]), CallStmt(Id("readln"),[Id("i")]), CallStmt(Id("str"),[Id("i"),Id("s")]),CallStmt(Id("writeln"),[StringLiteral("That was : "),Id("s")])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_68(self):
        input = """Var: x;
Function: main
Parameter: tuan, kiet
Body:
    Var: b[2][3] = {{2,3,4},{4,5,6}};
    Var: c, d = 6, e, f;
    Var: m = {17,10.2}, n[10];
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [VarDecl(Id("tuan"),[],None),VarDecl(Id("kiet"),[],None)], ( [VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])), VarDecl(Id("c"),[],None), VarDecl(Id("d"),[],IntLiteral(6)), VarDecl(Id("e"),[],None), VarDecl(Id("f"),[],None), VarDecl(Id("m"),[],ArrayLiteral([IntLiteral(17),FloatLiteral(10.2)])), VarDecl(Id("n"),[10],None)], [] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_69(self):
        input = """Var: x;
Function: foo
Parameter: n
Body:
    a = 0;
    While True Do a = a + 1; EndWhile.
    Return a;
EndBody.

Function: main
Body:
    Var: a[100];
    foo(x);
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("foo"), [VarDecl(Id("n"),[],None)], ( [], [Assign(Id("a"),IntLiteral(0)), While(BooleanLiteral(True),([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])),Return(Id("a"))] ) ), FuncDecl( Id("main"), [], ( [VarDecl(Id("a"),[100],None)], [CallStmt(Id("foo"),[Id("x")])] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_70(self):
        input = """Var: a;
Function: main
Body:
    write("Nhap vao mot so:");
    readln(n);
    i = round( sqrt(n) );
    If( n % i != 0) Then
        writeln("N la so nguyen to");
    Else
        writeln("N khong la so nguyen to");
    EndIf.
EndBody.
"""
        expect = Program([ VarDecl(Id("a"),[],None), FuncDecl( Id("main"), [], ( [], [CallStmt(Id("write"),[StringLiteral("Nhap vao mot so:")]), CallStmt(Id("readln"),[Id("n")]), Assign(Id("i"),CallExpr(Id("round"),[CallExpr(Id("sqrt"),[Id("n")])])), If([(BinaryOp("!=",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[CallStmt(Id("writeln"),[StringLiteral("N la so nguyen to")])])],([],[CallStmt(Id("writeln"),[StringLiteral("N khong la so nguyen to")])]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_71(self):
        input = """Var: x;
Function: main
Body:
    If n<2 Then ngto=False; Else ngto=True; EndIf.
    For (i=2, i<=trunc(sqrt(n)), 1) Do
        If n % i == 0 Then
            ngto=False;
            Break;
        EndIf.
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [If([(BinaryOp("<",Id("n"),IntLiteral(2)),[],[Assign(Id("ngto"),BooleanLiteral(False))])],([],[Assign(Id("ngto"),BooleanLiteral(True))])), For(Id("i"),IntLiteral(2),BinaryOp("<=",Id("i"),CallExpr(Id("trunc"),[CallExpr(Id("sqrt"),[Id("n")])])),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[Assign(Id("ngto"),BooleanLiteral(False)),Break()])],([],[]))])) ]) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_72(self):
        input = """Var: k,s;
Function: main
Body:
    k=1; s=0;
    While k<=m Do
        If ngto(k)==True Then
            write(f,k);
            s=s+k;
        EndIf.
        k=k+1;
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("k"),[],None), VarDecl(Id("s"),[],None), FuncDecl( Id("main"), [], ( [], [Assign(Id("k"),IntLiteral(1)), Assign(Id("s"),IntLiteral(0)), While( BinaryOp("<=",Id("k"),Id("m")), ([], [If([(BinaryOp("==",CallExpr(Id("ngto"),[Id("k")]),BooleanLiteral(True)),[],[CallStmt(Id("write"),[Id("f"),Id("k")]),Assign(Id("s"),BinaryOp("+",Id("s"),Id("k")))])],([],[])), Assign(Id("k"),BinaryOp("+",Id("k"),IntLiteral(1)))]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_73(self):
        input = """Var: k;
Function: main
Body:
    k=m;
    While (k>2) && (ngto(k)==False) Do
        j=2;
        While (k%j!=0) && (ngto(k)==False) && (j<k) Do
            j=j+1;
        EndWhile.
        write(f,j);
        k=k \\ j;
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("k"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("k"),Id("m")), While( BinaryOp("&&",BinaryOp(">",Id("k"),IntLiteral(2)),BinaryOp("==",CallExpr(Id("ngto"),[Id("k")]),BooleanLiteral(False))), ([], [ Assign(Id("j"),IntLiteral(2)), While( BinaryOp("&&",BinaryOp("&&",BinaryOp("!=",BinaryOp("%",Id("k"),Id("j")),IntLiteral(0)),BinaryOp("==",CallExpr(Id("ngto"),[Id("k")]),BooleanLiteral(False))),BinaryOp("<",Id("j"),Id("k"))), ([],[ Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))) ])), CallStmt(Id("write"),[Id("f"),Id("j")]), Assign(Id("k"),BinaryOp("\\",Id("k"),Id("j"))) ]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_74(self):
        input = """
Function: main
Body:
   first = 0;
   second = 1;
   write(first);
   write(second);
   For (ix = 0, ix < n, 1) Do
      temp = first + second;
      first = second;
      second = temp;
      write(temp);
   EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [Assign(Id("first"),IntLiteral(0)), Assign(Id("second"),IntLiteral(1)), CallStmt(Id("write"),[Id("first")]), CallStmt(Id("write"),[Id("second")]), For(Id("ix"),IntLiteral(0),BinaryOp("<",Id("ix"),Id("n")),IntLiteral(1),([],[Assign(Id("temp"),BinaryOp("+",Id("first"),Id("second"))),Assign(Id("first"),Id("second")),Assign(Id("second"),Id("temp")),CallStmt(Id("write"),[Id("temp")])]))] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_75(self):
        input = """
Function: main
Body:
    number = 1;
    linecount = 0;
    ** Loop **
    While number <= maxnum Do
        linecount = linecount + 1;
        If linecount > 1 Then write (","); EndIf.
        write (number);
        If (linecount == numperline) && !(number * 2 > maxnum) Then
            writeln (",");
            linecount = 0;
        EndIf.
        number = number * base;
    EndWhile.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(Id("number"),IntLiteral(1)), Assign(Id("linecount"),IntLiteral(0)), While( BinaryOp("<=",Id("number"),Id("maxnum")),([],[ Assign(Id("linecount"),BinaryOp("+",Id("linecount"),IntLiteral(1))), If([(BinaryOp(">",Id("linecount"),IntLiteral(1)),[],[CallStmt(Id("write"),[StringLiteral(",")])])],([],[])), CallStmt(Id("write"),[Id("number")]), If([(BinaryOp("&&",BinaryOp("==",Id("linecount"),Id("numperline")),UnaryOp("!",BinaryOp(">",BinaryOp("*",Id("number"),IntLiteral(2)),Id("maxnum")))),[],[CallStmt(Id("writeln"),[StringLiteral(",")]),Assign(Id("linecount"),IntLiteral(0))])],([],[])), Assign(Id("number"),BinaryOp("*",Id("number"),Id("base"))) ])) ] )) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_76(self):
        input = """
Function: main
Body:
    clrscr();
    n=0;
    s=0;
    While s<1000 Do
        n=n+1;
        s=s+n;
    EndWhile.
    s=s-n;
    n=n-1;
    readln();
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("clrscr"),[]), Assign(Id("n"),IntLiteral(0)), Assign(Id("s"),IntLiteral(0)), While(BinaryOp("<",Id("s"),IntLiteral(1000)),([],[ Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))), Assign(Id("s"),BinaryOp("+",Id("s"),Id("n")))])), Assign(Id("s"),BinaryOp("-",Id("s"),Id("n"))), Assign(Id("n"),BinaryOp("-",Id("n"),IntLiteral(1))), CallStmt(Id("readln"),[]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_77(self):
        input = """Var: number;
Function: main
Body:
    number = 1;
    While number <= 5 Do
        writeln(number);
        number = number + 1;
    EndWhile.
    readln();
EndBody.
"""
        expect = Program([ VarDecl(Id("number"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("number"),IntLiteral(1)), While(BinaryOp("<=",Id("number"),IntLiteral(5)),([],[CallStmt(Id("writeln"),[Id("number")]),Assign(Id("number"),BinaryOp("+",Id("number"),IntLiteral(1)))])), CallStmt(Id("readln"),[]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_78(self):
        input = """Var: a;
Function: main
Body:
    a = 2;
    While (a <= 9) Do
        b = 1;
        While (b <= 9) Do
            writeln(a, " x ", b, " = ", (a * b));
            b = b + 1;
        EndWhile.
        a = a + 1;
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("a"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("a"),IntLiteral(2)), While( BinaryOp("<=",Id("a"),IntLiteral(9)), ([], [ Assign(Id("b"),IntLiteral(1)), While(BinaryOp("<=",Id("b"),IntLiteral(9)), ([],[CallStmt(Id("writeln"),[Id("a"),StringLiteral(" x "),Id("b"),StringLiteral(" = "),BinaryOp("*",Id("a"),Id("b"))]), Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))) ]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_79(self):
        input = """Var: a;
Function: main
Body:
    a = 1;
    Do
        writeln(a);
        a = a + 1;
    While (a > 5) EndDo.
    readln();
EndBody.
"""
        expect = Program([ VarDecl(Id("a"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("a"),IntLiteral(1)), Dowhile(([],[CallStmt(Id("writeln"),[Id("a")]),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]),BinaryOp(">",Id("a"),IntLiteral(5))), CallStmt(Id("readln"),[]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_80(self):
        input = """Var: x;
Function: main
Body:
    a = 1;
    While (a < 16) Do
        writeln(a);
        a = a + 1;
        If (a == 6) Then
            Break;
        EndIf.
    EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ Assign(Id("a"),IntLiteral(1)), While(BinaryOp("<",Id("a"),IntLiteral(16)),([],[ CallStmt(Id("writeln"),[Id("a")]), Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))), If([(BinaryOp("==",Id("a"),IntLiteral(6)),[],[Break()])],([],[]))]) ) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_81(self):
        input = """Var: x;
Function: main
Body:
    For (i = 1, i <= 10, 1) Do
        If i == 5 Then Continue; EndIf.
        writeln(i);
    EndFor.
    readln();
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),IntLiteral(10)),IntLiteral(1),([],[ If([(BinaryOp("==",Id("i"),IntLiteral(5)),[],[Continue()])],([],[])),CallStmt(Id("writeln"),[Id("i")])]) ), CallStmt(Id("readln"),[]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_82(self):
        input = """Var: s = "Abstract Syntax Tree";
Function: main
Body:
    While (s[1]==" ") Do delete(s,1,1); EndWhile.
    While (s[length(s)]==" ") Do delete(s,length(s),1); EndWhile.
    While (pos(" ",s)!=0) Do delete(s,pos(" ",s),1); EndWhile.
EndBody.
"""
        expect = Program([ VarDecl(Id("s"),[],StringLiteral("Abstract Syntax Tree")), FuncDecl( Id("main"), [], ( [], [ While(BinaryOp("==",ArrayCell(Id("s"),[IntLiteral(1)]),StringLiteral(" ")),([],[CallStmt(Id("delete"),[Id("s"),IntLiteral(1),IntLiteral(1)])])), While(BinaryOp("==",ArrayCell(Id("s"),[CallExpr(Id("length"),[Id("s")])]),StringLiteral(" ")),([],[CallStmt(Id("delete"),[Id("s"),CallExpr(Id("length"),[Id("s")]),IntLiteral(1)])])), While(BinaryOp("!=",CallExpr(Id("pos"),[StringLiteral(" "),Id("s")]),IntLiteral(0)),([],[CallStmt(Id("delete"),[Id("s"),CallExpr(Id("pos"),[StringLiteral(" "),Id("s")]),IntLiteral(1)])])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_83(self):
        input = """Var: m,n;
Function: main
Body:
    While m!=n Do
        If m>n Then m=m-n;
        ElseIf m<n Then n=n-m; Else EndIf.
    EndWhile.
    write("UCLN cua 2 so la ",m);
EndBody.
"""
        expect = Program([ VarDecl(Id("m"),[],None), VarDecl(Id("n"),[],None), FuncDecl( Id("main"), [], ( [], [ While(BinaryOp("!=",Id("m"),Id("n")),([],[ If([(BinaryOp(">",Id("m"),Id("n")),[],[Assign(Id("m"),BinaryOp("-",Id("m"),Id("n")))]) ,(BinaryOp("<",Id("m"),Id("n")),[],[Assign(Id("n"),BinaryOp("-",Id("n"),Id("m")))])],([],[]))])), CallStmt(Id("write"),[StringLiteral("UCLN cua 2 so la "),Id("m")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_84(self):
        input = """
Function: main
Body:
    readln(n);
    i=2;
    While (n % i != 0) Do
        i=i+1;
        If i>sqrt(n) Then write("So nguyen to");
        Else write("Khong la so nguyen to"); EndIf.
    EndWhile.
    readln();
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("readln"),[Id("n")]), Assign(Id("i"),IntLiteral(2)), While(BinaryOp("!=",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),([],[ Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))), If([(BinaryOp(">",Id("i"),CallExpr(Id("sqrt"),[Id("n")])),[],[CallStmt(Id("write"),[StringLiteral("So nguyen to")])])], ([],[CallStmt(Id("write"),[StringLiteral("Khong la so nguyen to")])])) ])), CallStmt(Id("readln"),[]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_85(self):
        input = """
Function: main
Body:
    n = sscript1_CompilerMessageCount;
    If !result Then
        If n > 0 Then
            For (i= 0,i <= n-1, 1) Do
                memo1_lines_add(n[i]);
            EndFor.
        EndIf.
    EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(Id("n"),Id("sscript1_CompilerMessageCount")), If([(UnaryOp("!",Id("result")),[],[ If([(BinaryOp(">",Id("n"),IntLiteral(0)),[],[ For(Id("i"),IntLiteral(0),BinaryOp("<=",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),IntLiteral(1),([],[ CallStmt(Id("memo1_lines_add"),[ArrayCell(Id("n"),[Id("i")])])]))])] ,([],[]))])], ([],[])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_86(self):
        input = """
Function: check_even
Parameter: x
Body:
    If x%2==0 Then Return(True);
    Else Return(False); EndIf.
EndBody.

Function: main
Body:
    print(check_even(2));
EndBody.
"""
        expect = Program([ FuncDecl(Id("check_even"),[VarDecl(Id("x"),[],None)],([],[ If([(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Return(BooleanLiteral(True))])],([],[Return(BooleanLiteral(False))]))])), FuncDecl(Id("main"),[],([],[ CallStmt(Id("print"),[CallExpr(Id("check_even"),[IntLiteral(2)])])])) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_87(self):
        input = """
Function: main
Body:
    fillchar(snt,sizeof(snt),True);
    snt[1]=False;
    i=2;
    While i<=trunc(sqrt(nmax)) Do
        While snt[i]==False Do inc(i); EndWhile.
        For (j=2 , j <= (nmax \\ i), 1) Do
            snt[i*j]=False;
        EndFor.
        inc(i);
    EndWhile.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("fillchar"),[Id("snt"),CallExpr(Id("sizeof"),[Id("snt")]),BooleanLiteral(True)]), Assign(ArrayCell(Id("snt"),[IntLiteral(1)]),BooleanLiteral(False)), Assign(Id("i"),IntLiteral(2)), While(BinaryOp("<=",Id("i"),CallExpr(Id("trunc"),[CallExpr(Id("sqrt"),[Id("nmax")])])),([],[ While(BinaryOp("==",ArrayCell(Id("snt"),[Id("i")]),BooleanLiteral(False)),([],[CallStmt(Id("inc"),[Id("i")])])), For(Id("j"),IntLiteral(2),BinaryOp("<=",Id("j"),BinaryOp("\\",Id("nmax"),Id("i"))),IntLiteral(1),([],[Assign(ArrayCell(Id("snt"),[BinaryOp("*",Id("i"),Id("j"))]),BooleanLiteral(False))])), CallStmt(Id("inc"),[Id("i")])])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_88(self):
        input = """
Function: main
Body:
    For (i=1, i<=n, 1) Do
        For (j=1, j<=n, 1) Do
            a[u][v]=0;
        EndFor.
    EndFor.

    For (i=1, i<=m, 1) Do
        a[u][v]=1;
        a[v][u]=1;
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("n")),IntLiteral(1),([],[ For(Id("j"),IntLiteral(1),BinaryOp("<=",Id("j"),Id("n")),IntLiteral(1),([],[Assign(ArrayCell(Id("a"),[Id("u"),Id("v")]),IntLiteral(0))]))])), For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("m")),IntLiteral(1),([],[ Assign(ArrayCell(Id("a"),[Id("u"),Id("v")]),IntLiteral(1)), Assign(ArrayCell(Id("a"),[Id("v"),Id("u")]),IntLiteral(1))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_89(self):
        input = """
Function: dfs
Parameter: v
Body:
    writeln(u);
    free[u] = False;

    For (v = 1, i <= n, 1) Do
        If (a[u][v]==True) && (free[v]==True) Then dfs(v); EndIf.
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("dfs"), [VarDecl(Id("v"),[],None),], ( [],[ CallStmt(Id("writeln"),[Id("u")]), Assign(ArrayCell(Id("free"),[Id("u")]),BooleanLiteral(False)), For(Id("v"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("n")),IntLiteral(1),([],[ If([(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("a"),[Id("u"),Id("v")]),BooleanLiteral(True)),BinaryOp("==",ArrayCell(Id("free"),[Id("v")]),BooleanLiteral(True))),[],[CallStmt(Id("dfs"),[Id("v")])])] ,([],[]))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_90(self):
        input = """
Function: main
Body:
    readln(n,m,s);
    For (i = 1, i <= m, 1) Do
        readln(u,v);
        a[u][v] = True;
        a[v][u] = True;
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ CallStmt(Id("readln"),[Id("n"),Id("m"),Id("s")]), For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("m")),IntLiteral(1),([],[ CallStmt(Id("readln"),[Id("u"),Id("v")]), Assign(ArrayCell(Id("a"),[Id("u"),Id("v")]),BooleanLiteral(True)), Assign(ArrayCell(Id("a"),[Id("v"),Id("u")]),BooleanLiteral(True))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_91(self):
        input = """
Function: bfs
Body:
    push(i);
    free[i] = False;

    While dau<=cuoi Do
        u = pop();
        writeln(u);
        For (v = 1, i <= n , 1) Do
            If (a[u][v]==True) && (free[v]==True) Then
                push(v);
                free[v] = False;
            EndIf.
        EndFor.
    EndWhile.
EndBody.
"""
        expect = Program([ FuncDecl( Id("bfs"), [], ( [], [ CallStmt(Id("push"),[Id("i")]), Assign(ArrayCell(Id("free"),[Id("i")]),BooleanLiteral(False)), While(BinaryOp("<=",Id("dau"),Id("cuoi")),([],[ Assign(Id("u"),CallExpr(Id("pop"),[])), CallStmt(Id("writeln"),[Id("u")]), For(Id("v"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("n")),IntLiteral(1),([],[ If([(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("a"),[Id("u"),Id("v")]),BooleanLiteral(True)),BinaryOp("==",ArrayCell(Id("free"),[Id("v")]),BooleanLiteral(True))),[],[ CallStmt(Id("push"),[Id("v")]), Assign(ArrayCell(Id("free"),[Id("v")]),BooleanLiteral(False))])], ([],[]))]))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_92(self):
        input = """
Function: main
Body:
    For (i=1, i<=m, 1) Do
        For (j=1, j<=n, 1) Do
            a[i][j]=0;
        EndFor.
    EndFor.

    push(data(tdx1,tdy1,0));
    a[tdx1][tdy1]=1;
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("m")),IntLiteral(1),([],[ For(Id("j"),IntLiteral(1),BinaryOp("<=",Id("j"),Id("n")),IntLiteral(1),([],[ Assign(ArrayCell(Id("a"),[Id("i"),Id("j")]),IntLiteral(0)) ])) ])), CallStmt(Id("push"),[CallExpr(Id("data"),[Id("tdx1"),Id("tdy1"),IntLiteral(0)])]), Assign(ArrayCell(Id("a"),[Id("tdx1"),Id("tdy1")]),IntLiteral(1)) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_93(self):
        input = """Var: x;
Function: main
Body:
    For (k=0, k<8, 1) Do
        tdx = cld[k]+x;
        tdy = clc[k]+y;
        If (1<=tdx) && (tdx <=m) && (1<=tdy) && (tdy <=n) && (a[tdx][tdy]==0) Then
            a[tdx][tdy]=1;
            push(data(tdx,tdy,dem+1));
            If (tdx==tdx2) && (tdy==tdy2) Then
                cout(dem+1);
                Return(0);
            EndIf.
        EndIf.
    EndFor.
EndBody.
"""
        expect = Program([ VarDecl(Id("x"),[],None), FuncDecl( Id("main"), [], ( [], [ For(Id("k"),IntLiteral(0),BinaryOp("<",Id("k"),IntLiteral(8)),IntLiteral(1),([],[ Assign(Id("tdx"),BinaryOp("+",ArrayCell(Id("cld"),[Id("k")]),Id("x"))), Assign(Id("tdy"),BinaryOp("+",ArrayCell(Id("clc"),[Id("k")]),Id("y"))), If([(BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",BinaryOp("<=",IntLiteral(1),Id("tdx")),BinaryOp("<=",Id("tdx"),Id("m"))),BinaryOp("<=",IntLiteral(1),Id("tdy"))),BinaryOp("<=",Id("tdy"),Id("n"))),BinaryOp("==",ArrayCell(Id("a"),[Id("tdx"),Id("tdy")]),IntLiteral(0))),[],[ Assign(ArrayCell(Id("a"),[Id("tdx"),Id("tdy")]),IntLiteral(1)), CallStmt(Id("push"),[CallExpr(Id("data"),[Id("tdx"),Id("tdy"),BinaryOp("+",Id("dem"),IntLiteral(1))])]), If([(BinaryOp("&&",BinaryOp("==",Id("tdx"),Id("tdx2")),BinaryOp("==",Id("tdy"),Id("tdy2"))),[],[ CallStmt(Id("cout"),[BinaryOp("+",Id("dem"),IntLiteral(1))]), Return(IntLiteral(0))])], ([],[]))])], ([],[]))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_94(self):
        input = """
Function: main
Body:
    khong=0;
    mot=0;
    For (i=1,i<=4,1) Do
        x=i+cld[k];
        y=j+clc[k];
        If b[x][y]==0 Then inc(khong);
        ElseIf b[x][y]==1 Then inc(mot);
        Else EndIf.
    EndFor.
    trong=4-khong-mot;
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(Id("khong"),IntLiteral(0)), Assign(Id("mot"),IntLiteral(0)), For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),IntLiteral(4)),IntLiteral(1),([],[ Assign(Id("x"),BinaryOp("+",Id("i"),ArrayCell(Id("cld"),[Id("k")]))), Assign(Id("y"),BinaryOp("+",Id("j"),ArrayCell(Id("clc"),[Id("k")]))), If([(BinaryOp("==",ArrayCell(Id("b"),[Id("x"),Id("y")]),IntLiteral(0)),[],[CallStmt(Id("inc"),[Id("khong")])]), (BinaryOp("==",ArrayCell(Id("b"),[Id("x"),Id("y")]),IntLiteral(1)),[],[CallStmt(Id("inc"),[Id("mot")])])], ([],[]))])), Assign(Id("trong"),BinaryOp("-",BinaryOp("-",IntLiteral(4),Id("khong")),Id("mot"))) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_95(self):
        input = """
Function: main
Body:
    sl=0;
    Do
        count=sl;
        update();
    While count!=sl EndDo.
    If sl==m*n Then xuat();
    Else writeln("Khong The"); EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(Id("sl"),IntLiteral(0)), Dowhile(([],[ Assign(Id("count"),Id("sl")), CallStmt(Id("update"),[])]),BinaryOp("!=",Id("count"),Id("sl"))), If([(BinaryOp("==",Id("sl"),BinaryOp("*",Id("m"),Id("n"))),[],[CallStmt(Id("xuat"),[])])], ([],[CallStmt(Id("writeln"),[StringLiteral("Khong The")])])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_96(self):
        input = """
Function: main
Body:
    For (i = 2, i < 10000, 1) Do
        If (prime[i]==True) Then
            num = i;
            For (j = 2, num*j <=max, 1) Do
                prime[num*j] = 0;
            EndFor.
        EndIf.
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),IntLiteral(10000)),IntLiteral(1),([],[ If([(BinaryOp("==",ArrayCell(Id("prime"),[Id("i")]),BooleanLiteral(True)),[],[ Assign(Id("num"),Id("i")), For(Id("j"),IntLiteral(2),BinaryOp("<=",BinaryOp("*",Id("num"),Id("j")),Id("max")),IntLiteral(1),([],[ Assign(ArrayCell(Id("prime"),[BinaryOp("*",Id("num"),Id("j"))]),IntLiteral(0))]))])], ([],[]))])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_97(self):
        input = """
Function: main
Body:
    digit[i] = j;
    temp = arr_to_num(digit);
    If (prime[temp] == -1) && (temp > 1000) && (dist[temp] == -1) Then
        dist[temp] = dist[s] + 1;
        push(temp);
    EndIf.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ Assign(ArrayCell(Id("digit"),[Id("i")]),Id("j")), Assign(Id("temp"),CallExpr(Id("arr_to_num"),[Id("digit")])), If([(BinaryOp("&&",BinaryOp("&&",BinaryOp("==",ArrayCell(Id("prime"),[Id("temp")]),UnaryOp("-",IntLiteral(1))),BinaryOp(">",Id("temp"),IntLiteral(1000))),BinaryOp("==",ArrayCell(Id("dist"),[Id("temp")]),UnaryOp("-",IntLiteral(1)))),[],[ Assign(ArrayCell(Id("dist"),[Id("temp")]),BinaryOp("+",ArrayCell(Id("dist"),[Id("s")]),IntLiteral(1))), CallStmt(Id("push"),[Id("temp")])])],([],[])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_98(self):
        input = """
Function: main
Body:
    For (i = 2, i < 10000, 1) Do
        If (prime[i]==True) Then
            num = i;
            For (j = 2, num*j <=max, 1) Do
                prime[num*j] =0;
            EndFor.
        EndIf.
    EndFor.
EndBody.
"""
        expect = Program([ FuncDecl( Id("main"), [], ( [], [ For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),IntLiteral(10000)),IntLiteral(1),([],[ If([(BinaryOp("==",ArrayCell(Id("prime"),[Id("i")]),BooleanLiteral(True)),[],[ Assign(Id("num"),Id("i")), For(Id("j"),IntLiteral(2),BinaryOp("<=",BinaryOp("*",Id("num"),Id("j")),Id("max")),IntLiteral(1),([],[Assign(ArrayCell(Id("prime"),[BinaryOp("*",Id("num"),Id("j"))]),IntLiteral(0))]))])], ([],[])) ])) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_99(self):
        input = """
Function: max
Parameter: x,y
Body:
    If x>y Then Return(x); Else Return(y); EndIf.
EndBody.

Function: min
Parameter: x,y
Body:
    If x<y Then Return(x); Else Return(y); EndIf.
EndBody.

Function: main
Body:
    test=0;
    Do
        readln(f,m,n);
        inc(test);
        gtmax=-10000;
        gtmin=10000;
        If (n==0) && (m==0) Then Break; EndIf.
        For (i=1, i<=m, 1) Do
            For (j=1, j<=n, 1) Do
                read(f,a[i][j]);
                gtmax=max(gtmax,a[i][j]);
                gtmin=min(gtmin,a[i][j]);
            EndFor.
            readln(f);
        EndFor.
        xuli();
    While True EndDo.
    close(f);
EndBody.
"""
        expect = Program([ FuncDecl( Id("max"), [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)], ( [], [If([(BinaryOp(">",Id("x"),Id("y")),[],[Return(Id("x"))])], ([],[Return(Id("y"))]))] ) ), FuncDecl( Id("min"), [VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)], ( [], [If([(BinaryOp("<",Id("x"),Id("y")),[],[Return(Id("x"))])], ([],[Return(Id("y"))]))] ) ), FuncDecl( Id("main"), [], ( [], [ Assign(Id("test"),IntLiteral(0)), Dowhile(([],[ CallStmt(Id("readln"),[Id("f"),Id("m"),Id("n")]), CallStmt(Id("inc"),[Id("test")]), Assign(Id("gtmax"),UnaryOp("-",IntLiteral(10000))), Assign(Id("gtmin"),IntLiteral(10000)), If([(BinaryOp("&&",BinaryOp("==",Id("n"),IntLiteral(0)),BinaryOp("==",Id("m"),IntLiteral(0))),[],[Break()])], ([],[])), For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("m")),IntLiteral(1),([],[ For(Id("j"),IntLiteral(1),BinaryOp("<=",Id("j"),Id("n")),IntLiteral(1),([],[ CallStmt(Id("read"),[Id("f"),ArrayCell(Id("a"),[Id("i"),Id("j")])]), Assign(Id("gtmax"),CallExpr(Id("max"),[Id("gtmax"),ArrayCell(Id("a"),[Id("i"),Id("j")])])), Assign(Id("gtmin"),CallExpr(Id("min"),[Id("gtmin"),ArrayCell(Id("a"),[Id("i"),Id("j")])]))])), CallStmt(Id("readln"),[Id("f")])])), CallStmt(Id("xuli"),[])]), BooleanLiteral(True)), CallStmt(Id("close"),[Id("f")]) ] ) ) ])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
