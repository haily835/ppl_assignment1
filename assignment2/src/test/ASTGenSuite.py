import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_simple_program1(self):
        """test simple program with many var declared """
        input = """Var:x,y,z;"""
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(
            Id("y"), [], None), VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_program1(self):
        """test simple program with many var declared """
        input = """Var:asasx,y32223,z2213;"""
        expect = Program([VarDecl(Id("asasx"), [], None), VarDecl(
            Id("y32223"), [], None), VarDecl(Id("z2213"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_program2(self):
        """test simple program with many var declared """
        input = """Var:x[1][2][3],y[2],z;"""
        expect = Program([VarDecl(Id("x"), [1, 2, 3], None),
                          VarDecl(Id("y"), [2], None), VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_program3(self):
        """test simple program with many var declared """
        input = """Var:x;
                    Var:z;
                """
        expect = Program([VarDecl(Id("x"), [], None),
                          VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_simple_program4(self):
        """test simple program with many var declared """
        input = """Var:x,y,f;
                    Var:z;
                """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("f"), [], None),
                          VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_simple_program5(self):
        """test simple program with many var declared """
        input = """Var:x,y,f;
                    Var:z,k,h;
                """
        expect = Program([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("f"), [], None),
                          VarDecl(Id("z"), [], None), VarDecl(Id("k"), [], None), VarDecl(Id("h"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_simple_program6(self):
        """test simple program with many var declared """
        input = """Var:x[1][2],y,f;
                    Var:z,k,h[4][5];
                """
        expect = Program([VarDecl(Id("x"), [1, 2], None), VarDecl(Id("y"), [], None), VarDecl(
            Id("f"), [], None), VarDecl(Id("z"), [4, 5], None), VarDecl(Id("k"), [], None), VarDecl(Id("h"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_simple_program7(self):
        """test simple program with many var declared """
        input = """Var : z =  2;
                """
        expect = Program([VarDecl(Id("z"), [], IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_simple_program8(self):
        """test simple program with many var declared """
        input = """Var : z =  2,y,x,h, ccx3;
                """
        expect = Program([VarDecl(Id("z"), [], IntLiteral(2)), VarDecl(Id("y"), [], None), VarDecl(
            Id("x"), [], None), VarDecl(Id("h"), [], None), VarDecl(Id("ccx3"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_simple_program9(self):
        """test simple program with many var declared """
        input = """Var : z =  2,y=4,x= 3;
                """
        expect = Program([VarDecl(Id("z"), [], IntLiteral(2)), VarDecl(
            Id("y"), [], IntLiteral(4)), VarDecl(Id("x"), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_simple_program10(self):
        """test simple program with many var declared """
        input = """Var : z =  2,y=4,x= 3;
                    Var : z =  2,y=4,x= 3;
                """
        expect = Program([VarDecl(Id("z"), [], IntLiteral(2)), VarDecl(Id("y"), [], IntLiteral(4)), VarDecl(Id("x"), [], IntLiteral(
            3)), VarDecl(Id("z"), [], IntLiteral(2)), VarDecl(Id("y"), [], IntLiteral(4)), VarDecl(Id("x"), [], IntLiteral(3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_simple_program11(self):
        """test simple program with many var declared """
        input = """Var : z =  True;
                """
        expect = Program([VarDecl(Id("z"), [], BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_simple_program12(self):
        """test simple program with many var declared """
        input = """Var : z =  3.14;
                """
        expect = Program([VarDecl(Id("z"), [], FloatLiteral(3.14))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_simple_program13(self):
        """test simple program with many var declared """
        input = """Var : z = 12.3;
                """
        expect = Program([VarDecl(Id("z"), [], FloatLiteral(12.3))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_simple_program14(self):
        """test simple program with many var declared """
        input = """Var : z = "sasasa";
                """
        expect = Program([VarDecl(Id("z"), [], StringLiteral("sasasa"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_simple_program15(self):
        """test simple program with many var declared """
        input = """Var : z[3] = {1,2,3};
                """
        expect = Program([VarDecl(Id("z"), [3], ArrayLiteral(
            [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_simple_program16(self):
        """test simple program with many var declared """
        input = """Var : z[3] = {1,2,3},y[5] = {2,3,0,1,2};
                """
        expect = Program([VarDecl(Id("z"), [3], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])),
                          VarDecl(Id("y"), [5], ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(0), IntLiteral(1), IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_simple_program17(self):
        """test simple program with many var declared """
        input = """Var : k[4] = {"abc","adc","assa","mmhmmh"}, y[2]={21.23,12.21};
                """
        expect = Program([VarDecl(Id("k"), [4], ArrayLiteral([StringLiteral("abc"), StringLiteral("adc"), StringLiteral("assa"), StringLiteral("mmhmmh")])),
                          VarDecl(Id("y"), [2], ArrayLiteral([FloatLiteral(21.23), FloatLiteral(12.21)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_simple_program18(self):
        """test simple program with many var declared """
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = Program([VarDecl(Id("b"), [2, 3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(
            3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_empty_program(self):
        """test simple program with no var declared """
        input = """    """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_empty_function(self):
        """test simple program with no var declared """
        input = """
                Function: main
                    Body:
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_simple_function(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:
                        Var: x;
                    EndBody.
            """
        expect = Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_simple_function2(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:

                        Var: x= 3,z=32.2122,k="sasaas";
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(3)), VarDecl(Id("z"), [], FloatLiteral(32.2122)),
                                                     VarDecl(Id("k"), [], StringLiteral("sasaas"))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_simple_function2(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:

                        Var: x= 3,z=32.2122,k="sasaas";
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(3)), VarDecl(Id("z"), [], FloatLiteral(32.2122)),
                                                     VarDecl(Id("k"), [], StringLiteral("sasaas"))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_simple_function3(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:

                        Var: x= 3,z=32.2122,k="sasaas";
                        Var: x= True;
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(3)), VarDecl(Id("z"), [], FloatLiteral(32.2122)),
                                                     VarDecl(Id("k"), [], StringLiteral("sasaas")), VarDecl(Id("x"), [], BooleanLiteral(True))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_simple_function4(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:

                        Var: x[5]= {1,2,3,4,5};
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [5],
                                                             ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_simple_function4(self):
        """test simple program with function declared """
        input = """
                Function: fact
                Parameter: n
                Body:
                    Var: x,y,z;
                EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([VarDecl(
            Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_simple_function5(self):
        """test simple program with function declared """
        input = """
                Function: fact
                Parameter: n
                Body:
                    Var: x,y,z;
                EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([VarDecl(
            Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_simple_function6(self):
        """test simple program with function declared """
        input = """
                Function: fact
                Parameter: n,a[2][3]
                Body:
                    Var: x,y,z;
                EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [VarDecl(Id("n"), [2, 3], []), VarDecl(Id("a"), [], None)],
                                   ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_simple_function_and_var_declare(self):
        """test simple program with function declared """
        input = """
                Var: x_y_k,y,z;
                Var: l0323 = 4;
                Function: fact
                Parameter: n
                Body:
                    Var: x,y,z;
                EndBody.
            """
        expect = Program([VarDecl(Id("x_y_k"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None), VarDecl(Id("l0323"), [], IntLiteral(4)),
                          FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_simple_function_and_var_declare2(self):
        """test simple program with function declared """
        input = """
                Var: x_y_k,y,z;
                Var: l0323 = 4;
                Function: fact
                Parameter: n
                Body:
                    Var: x,y,z;
                EndBody.
            """
        expect = Program([VarDecl(Id("x_y_k"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None), VarDecl(Id("l0323"), [], IntLiteral(4)),
                          FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_simple_function_and_var_declare9(self):
        """test simple program with function declared """
        input = """
                Var: x_y_k,y,z;
                Var: l0323 = 4;
                Function: fact
                Parameter: n
                Body:
                    Var: x,y,z;
                EndBody.
                Function: act
                Parameter: n
                Body:
                    Var: x,y,z;
                EndBody.
            """
        expect = Program([VarDecl(Id("x_y_k"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None), VarDecl(Id("l0323"), [], IntLiteral(4)), FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)],
                                                                                                                                                                    ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], [])), FuncDecl(Id("act"), [VarDecl(Id("n"), [], None)], ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_simple_function_with_exp(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:
                        Var: x;
                        x = 3 == 4;
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], None)], [
                         Assign(Id("x"), BinaryOp("==", IntLiteral(3), IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_simple_function_with_exp1(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:
                        Var: x;
                        x = 3 != 4;
                        y = 3 >= 4;
                        z = 3 < 4;
                        k = 3 > 4;
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], None)], [Assign(Id("x"), BinaryOp("!=", IntLiteral(3),
                                                                                                            IntLiteral(4))), Assign(Id("y"), BinaryOp(">=", IntLiteral(3), IntLiteral(4))), Assign(Id("z"), BinaryOp("<", IntLiteral(3), IntLiteral(4))),
                                                                                   Assign(Id("k"), BinaryOp(">", IntLiteral(3), IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_simple_function_with_exp1(self):
        """test simple program with function declared """
        input = """
                Function: main
                    Body:
                        Var: x;
                        k = 3 =/= 4;
                        h = 5 <. 3;
                        z = 3 >. 4;
                        t = 2 <=. 10;
                        ku = 12 >=. 11;
                    EndBody.
            """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], None)], [Assign(Id("k"), BinaryOp("=/=", IntLiteral(3), IntLiteral(4))), Assign(Id("h"),
                                                                                                                                                          BinaryOp("<.", IntLiteral(5), IntLiteral(3))), Assign(Id("z"), BinaryOp(">.", IntLiteral(3), IntLiteral(4))),
                                                                                   Assign(Id("t"), BinaryOp("<=.", IntLiteral(2), IntLiteral(10))), Assign(Id("ku"), BinaryOp(">=.", IntLiteral(12), IntLiteral(11)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_simple_function_with_exp1s(self):
        """test simple program with function declared """
        input = """
                    Var : n = 30;
                    Function: fact
                    Parameter: n
                    Body:
                    a = 3 || c;
                    EndBody.
            """
        expect = Program([VarDecl(Id("n"), [], IntLiteral(30)), FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)],
                                                                         ([], [Assign(Id("a"), BinaryOp("||", IntLiteral(3), Id("c")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_simple_function_with_ifstmt(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([(BinaryOp(">", Id("a"), Id("b")), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_simple_function_with_ifstmt2(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    ElseIf (a < 3) Then
                    Else a = 4;
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([(BinaryOp(">", Id("a"), Id("b")), [], []), (BinaryOp("<", Id("a"), IntLiteral(3)), [], [])], ([], [Assign(Id("a"), IntLiteral(4))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_simple_function_with_ifstmt3s(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    Var: x = 3;
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([(BinaryOp(">", Id("a"), Id("b")), [VarDecl(Id("x"), [], IntLiteral(3))], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_simple_function_with_ifstmt3(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    Var: x = 3;
                    abcs = 3 * 3 - 3 + 4;
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([(BinaryOp(">", Id("a"), Id("b")), [VarDecl(Id("x"), [], IntLiteral(3))],
                                       [Assign(Id("abcs"), BinaryOp("+", BinaryOp("-", BinaryOp("*", IntLiteral(3), IntLiteral(3)), IntLiteral(3)), IntLiteral(4)))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_simple_function_with_ifstmt4(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    Var: x = 3;
                    abcs = 3 * 3 - 3 + 4;
                    ElseIf (a == b) Then
                    Var: c = 31.23;
                    kuc = 32 + 25 - 23;
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([
                (BinaryOp(">", Id("a"), Id("b")), [VarDecl(Id("x"), [], IntLiteral(3))], [Assign(Id("abcs"), BinaryOp(
                    "+", BinaryOp("-", BinaryOp("*", IntLiteral(3), IntLiteral(3)), IntLiteral(3)), IntLiteral(4)))]),
                (BinaryOp("==", Id("a"), Id("b")), [VarDecl(Id("c"), [], FloatLiteral(31.23))], [Assign(
                    Id("kuc"), BinaryOp("-", BinaryOp("+", IntLiteral(32), IntLiteral(25)), IntLiteral(23)))])
            ], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_simple_function_with_ifstmt4s(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    Var: x = 3;
                    abcs = 3 * 3 - 3 + 4;
                    ElseIf (a == b) Then
                    Var: c = 31.23;
                    kuc = 32 + 25 - 23;
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([
                (BinaryOp(">", Id("a"), Id("b")), [VarDecl(Id("x"), [], IntLiteral(3))], [Assign(Id("abcs"), BinaryOp(
                    "+", BinaryOp("-", BinaryOp("*", IntLiteral(3), IntLiteral(3)), IntLiteral(3)), IntLiteral(4)))]),
                (BinaryOp("==", Id("a"), Id("b")), [VarDecl(Id("c"), [], FloatLiteral(31.23))], [Assign(
                    Id("kuc"), BinaryOp("-", BinaryOp("+", IntLiteral(32), IntLiteral(25)), IntLiteral(23)))])
            ], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_simple_function_with_ifstmt5(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    If (a >b) Then
                    Var: x = 3;
                    abcs = 3 * 3 - 3 + 4;
                    ElseIf (a == b) Then
                    Var: c = 31.23;
                    kuc = 32 + 25 - 23;
                    Else a = 32;
                    a[3] = {1,2,3};
                    EndIf.
                    EndBody.
            """
        expect = Program([FuncDecl(
            Id("fact"), [], ([], [If([
                (BinaryOp(">", Id("a"), Id("b")), [VarDecl(Id("x"), [], IntLiteral(3))], [Assign(Id("abcs"), BinaryOp(
                    "+", BinaryOp("-", BinaryOp("*", IntLiteral(3), IntLiteral(3)), IntLiteral(3)), IntLiteral(4)))]),
                (BinaryOp("==", Id("a"), Id("b")), [VarDecl(Id("c"), [], FloatLiteral(31.23))], [Assign(
                    Id("kuc"), BinaryOp("-", BinaryOp("+", IntLiteral(32), IntLiteral(25)), IntLiteral(23)))])
            ], ([], [Assign(Id("a"), IntLiteral(32)), Assign(ArrayCell(Id("a"), [IntLiteral(3)]), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_simple_function_with_while(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    While a < 4 Do
                    EndWhile.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([],  [While(
            BinaryOp("<", Id("a"), IntLiteral(4)), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_simple_function_with_for_and_cmt(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    While a < 4 Do
                    ** This is a
                    * multi-line
                    * comment.
                    **
                    EndWhile.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([],  [While(
            BinaryOp("<", Id("a"), IntLiteral(4)), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_simple_function_with_for_and_cmt(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    For (i = 0, i < 10, 2) Do
                    EndFor.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([], [For(Id("i"), IntLiteral(0),
                                                             BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_simple_function_with_for_and_cmt2(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    For (i = 0, i < 10, i + 2) Do
                    Var: x[3] = {"abc","cdf","sasa"};
                    anh = em + em;
                    EndFor.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([], [For(Id("i"), IntLiteral(0),
                                                             BinaryOp("<", Id("i"), IntLiteral(10)), BinaryOp("+", Id("i"), IntLiteral(2)), ([VarDecl(Id("x"), [3], ArrayLiteral([StringLiteral("abc"), StringLiteral("cdf"), StringLiteral("sasa")]))], [Assign(Id("anh"), BinaryOp("+", Id("em"), Id("em")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_simple_function_with_for_and_cmt2(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    For (i = 0, i < 10, i + 2) Do
                    Var: x[3] = {"abc","cdf","sasa"};
                    anh = em + em;
                    EndFor.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([], [For(Id("i"), IntLiteral(0),
                                                             BinaryOp("<", Id("i"), IntLiteral(10)), BinaryOp("+", Id("i"), IntLiteral(2)), ([VarDecl(Id("x"), [3], ArrayLiteral([StringLiteral("abc"), StringLiteral("cdf"), StringLiteral("sasa")]))], [Assign(Id("anh"), BinaryOp("+", Id("em"), Id("em")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_simple_function_with_do_while_cmt2(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    Do 
                    While a < 3
                    EndDo.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Dowhile(
            ([], []), BinaryOp("<", Id("a"), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_simple_function_with_do_while_cmt3(self):
        """test simple program with function declared """
        input = """
                    Function: fact
                    Body:
                    Do 
                    Return ;
                    Continue;
                    While a < 3
                    EndDo.
                    EndBody.
            """
        expect = Program([FuncDecl(Id("fact"), [], ([], [Dowhile(
            ([], [Return(None), Continue()]), BinaryOp("<", Id("a"), IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))
