import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_variable_declare_part_1(self):
        """test variable declare part"""
        input = """Var: x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_variable_declare_part_2(self):
        """test variable declare part"""
        input = """Var: x, y, z;"""
        expect = Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_variable_declare_part_3(self):
        """test variable declare part"""
        input = """Var: x[1];"""
        expect = Program([VarDecl(Id("x"),[1], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_variable_declare_part_4(self):
        """test variable declare part"""
        input = """Var: x[1], y, z;"""
        expect = Program([VarDecl(Id("x"), [1], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_variable_declare_part_5(self):
        """test variable declare part"""
        input = """Var: x[1], y[2], z[3];"""
        expect = Program([VarDecl(Id("x"), [1], None),VarDecl(Id("y"), [2], None),VarDecl(Id("z"), [3], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_variable_declare_part_6(self):
        """test variable declare part"""
        input = """Var: x[1][2][3], y;"""
        expect = Program([VarDecl(Id("x"),[1,2,3], None),VarDecl(Id("y"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_variable_declare_part_7(self):
        """test variable declare part"""
        input = """Var: x[1][2], y[3][4];"""
        expect = Program([VarDecl(Id("x"), [1,2], None),VarDecl(Id("y"), [3,4], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
 
    def test_variable_declare_part_8(self):
        """test variable declare part"""
        input = """Var: a = 5, b = 10, c = 16;"""
        expect = Program([VarDecl(Id("a"), [], IntLiteral(5)),VarDecl(Id("b"), [], IntLiteral(10)),VarDecl(Id("c"), [], IntLiteral(16))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_variable_declare_part_9(self):
        """test variable declare part"""
        input = """Var: a = 5.9e-1, b = 10.123, c = 10.e+10;"""
        expect = Program([VarDecl(Id("a"), [], FloatLiteral(0.59)),VarDecl(Id("b"), [], FloatLiteral(10.123)),VarDecl(Id("c"), [], FloatLiteral(100000000000.0))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_variable_declare_part_10(self):
        """test variable declare part"""
        input = """Var: a = True, b = True, c = False;"""
        expect = Program([VarDecl(Id("a"), [], BooleanLiteral("true")),VarDecl(Id("b"), [], BooleanLiteral("true")),VarDecl(Id("c"), [], BooleanLiteral("false"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_variable_declare_part_11(self):
        """test variable declare part"""
        input = """Var: a = True, b = True, c = False;"""
        expect = Program([VarDecl(Id("a"), [], BooleanLiteral("true")),VarDecl(Id("b"), [], BooleanLiteral("true")),VarDecl(Id("c"), [], BooleanLiteral("false"))]) 
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_variable_declare_part_12(self):
        """test variable declare part"""
        input = """Var: a = "True", b = "hello", c = "world";"""
        expect = Program([VarDecl(Id("a"), [], StringLiteral("True")),VarDecl(Id("b"), [], StringLiteral("hello")),VarDecl(Id("c"), [], StringLiteral("world"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_variable_declare_part_13(self):
        """test variable declare part"""
        input = """Var: b[2] = {1,2,3};"""
        expect = Program([VarDecl(Id("b"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_variable_declare_part_14(self):
        """test variable declare part"""
        input = """Var: a, b[2][3] = {{2,3,4},{4,5,6}}, c = True;"""
        expect = Program([VarDecl(Id("a"), [], None),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"), [], BooleanLiteral("true"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_variable_declare_part_15(self):
        """test variable declare part"""
        input = """Var: a = 1, b[2][3] = {{2,3,4},{4,5,6}}, c[1] = {True};"""
        expect = Program([VarDecl(Id("a"), [],IntLiteral(1)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[1],ArrayLiteral([BooleanLiteral("true")]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_variable_declare_part_16(self):
        """test variable declare part"""
        input = """Var: a[2][3] = {{"hi","22"},{22.5,3.23},{4E-123,6e+2}}, b[2][3] = {{2,3,4},{4,5,6}}, c[1] = {True};"""
        expect = Program([VarDecl(Id("a"),[2,3],ArrayLiteral([ArrayLiteral([StringLiteral("hi"),StringLiteral("22")]),ArrayLiteral([FloatLiteral(22.5),FloatLiteral(3.23)]),ArrayLiteral([FloatLiteral(4e-123),FloatLiteral(600.0)])])),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[1],ArrayLiteral([BooleanLiteral("true")]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_variable_declare_part_17(self):
        """test variable declare part"""
        input = """Var: x;
        Var: y;
        Var: z;"""
        expect = Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_variable_declare_part_18(self):
        """test variable declare part"""
        input = """Var: x, y, z;
        Var: a, b, c;
        Var: ohio, pensylvania;"""
        expect = Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None),VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None),VarDecl(Id("c"), [], None),VarDecl(Id("ohio"), [], None),VarDecl(Id("pensylvania"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_variable_declare_part_19(self):
        """test variable declare part"""
        input = """Var: x = 6, y = 2.0e-1, z = 12.2;
        Var: a = "Hello", b = "Nihao";
        Var: lst[2][3] = {{True, 1 ,0}, {False, 2, True}}, str = "1852086";"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(6)),VarDecl(Id("y"),[],FloatLiteral(0.2)),VarDecl(Id("z"),[],FloatLiteral(12.2)),VarDecl(Id("a"),[],StringLiteral("Hello")),VarDecl(Id("b"),[],StringLiteral("Nihao")),VarDecl(Id("lst"),[2,3],ArrayLiteral([ArrayLiteral([BooleanLiteral("true"),IntLiteral(1),IntLiteral(0)]),ArrayLiteral([BooleanLiteral("false"),IntLiteral(2),BooleanLiteral("true")])])),VarDecl(Id("str"),[],StringLiteral("1852086"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_variable_declare_part_20(self):
        """test variable declare part"""
        input = """Var: x = 6;
        Var: y[2] = {1321.2e-1, 2.11};
        Var: flage = True;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(6)),VarDecl(Id("y"),[2],ArrayLiteral([FloatLiteral(132.12),FloatLiteral(2.11)])),VarDecl(Id("flage"),[],BooleanLiteral("true"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # function decls with no body content
    def test_function_declare_part_1(self):
        """test function declaration part"""
        input = """Function: main
                        Body:
                        EndBody."""
        expect = Program([FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_function_declare_part_2(self):
        """test function declaration part"""
        input = """Function: main
                        Parameter: a, b, c
                        Body:
                        EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_function_declare_part_3(self):
        """test function declaration part"""
        input = """Function: main
                        Parameter: a, b[1], c[2][3]
                        Body:
                        EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[1],None),VarDecl(Id("c"),[2,3],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_function_declare_part_4(self):
        """test function declaration part"""
        input = """Function: main
                        Parameter: x[3], y[1], z[2]
                        Body:
                        EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[3],None),VarDecl(Id("y"),[1],None),VarDecl(Id("z"),[2],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_function_declare_part_5(self):
        """test function declaration part"""
        input = """Function: main
                        Parameter: x[3], y[1], z[2], w
                        Body:
                        EndBody."""
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[3],None),VarDecl(Id("y"),[1],None),VarDecl(Id("z"),[2],None),VarDecl(Id("w"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_function_declare_part_6(self):
        """test function declaration part"""
        input =  """Function: fact
                        Body:
                        EndBody.

                    Function: main
                        Body:
                        EndBody.
                """
        expect = Program([FuncDecl(Id("fact"),[],([],[])),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_function_declare_part_7(self):
        """test function declaration part"""
        input =  """Function: fact
                        Parameter: x, y
                        Body:
                        EndBody.

                    Function: main
                        Parameter: a[1], b[2]
                        Body:
                        EndBody.
                """
        expect = Program([FuncDecl(Id("fact"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[])),FuncDecl(Id("main"),[VarDecl(Id("a"),[1],None),VarDecl(Id("b"),[2],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_function_declare_part_8(self):
        """test function declaration part"""
        input =  """Function: fact
                        Parameter: x[2][3], y, z, w[2]
                        Body:
                        EndBody.

                    Function: main
                        Parameter: a[1], b[2]
                        Body:
                        EndBody.
                """
        expect = Program([FuncDecl(Id("fact"),[VarDecl(Id("x"),[2,3],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("w"),[2],None)],([],[])),FuncDecl(Id("main"),[VarDecl(Id("a"),[1],None),VarDecl(Id("b"),[2],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    
    def test_function_declare_part_9(self):
        """test function declaration part"""
        input =  """Function: fact1
                        Parameter: q, w, r, t
                        Body:
                        EndBody.

                    Function: fact2
                        Parameter: x[2][3], y, z, w[2]
                        Body:
                        EndBody.

                    Function: main
                        Parameter: a[1], b[2]
                        Body:
                        EndBody.
                """
        expect = Program([FuncDecl(Id("fact1"),[VarDecl(Id("q"),[],None),VarDecl(Id("w"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("t"),[],None)],([],[])),FuncDecl(Id("fact2"),[VarDecl(Id("x"),[2,3],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("w"),[2],None)],([],[])),FuncDecl(Id("main"),[VarDecl(Id("a"),[1],None),VarDecl(Id("b"),[2],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    # function decls with body content
    def test_function_declare_part_10(self):
        """test function declaration part"""
        input =  """Function: main
                        Parameter: a, b
                        Body:
                            Var: x, y;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_function_declare_part_11(self):
        """test function declaration part"""
        input =  """Function: main
                        Parameter: a, b
                        Body:
                            Var: x;
                            Var: y;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_function_declare_part_12(self):
        """test function declaration part"""
        input =  """Function: main
                        Parameter: a, b
                        Body:
                            Var: x;
                            Var: y[2] = {1,2};
                        EndBody.
                """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

        #Assign statements
    def test_function_declare_part_13(self):
        """test function declaration part"""
        input =  """Function: assign
                        Parameter: a, b
                        Body:
                            Var: r = 10., v;
                            v = 4 *. r;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("assign"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",IntLiteral(4),Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_function_declare_part_14(self):
        """test function declaration part"""
        input =  """Function: assign
                        Parameter: a
                        Body:
                            a = 11;
                        EndBody.
                """
        expect = Program([FuncDecl(Id('assign'),[VarDecl(Id('a'),[],None)],([],[Assign(Id('a'),IntLiteral(11))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_function_declare_part_15(self):
        """test function declaration part"""
        input =  """Function: assign
                        Parameter: a,b
                        Body:
                            a = 11;
                            b = 12;
                        EndBody.
                """
        expect = Program([FuncDecl(Id('assign'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Assign(Id('a'),IntLiteral(11)),Assign(Id('b'),IntLiteral(12))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_function_declare_part_16(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            int = 10;
                            float = 20.e+2;
                            toString = "Hiii";
                        EndBody.
                """
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('int'),IntLiteral(10)),Assign(Id('float'),FloatLiteral(2000.0)),Assign(Id('toString'),StringLiteral('Hiii'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_function_declare_part_17(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            arr = {1,2,3,4};
                            foo[2] = 1.3;
                            foo[2+1] = 3;
                        EndBody.
                """
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('arr'),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)])),Assign(ArrayCell(Id('foo'),[IntLiteral(2)]),FloatLiteral(1.3)),Assign(ArrayCell(Id('foo'),[BinaryOp('+',IntLiteral(2),IntLiteral(1))]),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_function_declare_part_18(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            arr[2] = {1};
                            foo[2] = {{1.3},{1}};
                            string[20] = "My name is";
                        EndBody.
                """
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(ArrayCell(Id('arr'),[IntLiteral(2)]),ArrayLiteral([IntLiteral(1)])),Assign(ArrayCell(Id('foo'),[IntLiteral(2)]),ArrayLiteral([ArrayLiteral([FloatLiteral(1.3)]),ArrayLiteral([IntLiteral(1)])])),Assign(ArrayCell(Id('string'),[IntLiteral(20)]),StringLiteral('My name is'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_function_declare_part_18(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            arr[2] = {1};
                            foo[2] = {{1.3},{1}};
                            string[20] = "My name is";
                        EndBody.
                """
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(ArrayCell(Id('arr'),[IntLiteral(2)]),ArrayLiteral([IntLiteral(1)])),Assign(ArrayCell(Id('foo'),[IntLiteral(2)]),ArrayLiteral([ArrayLiteral([FloatLiteral(1.3)]),ArrayLiteral([IntLiteral(1)])])),Assign(ArrayCell(Id('string'),[IntLiteral(20)]),StringLiteral('My name is'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_function_declare_part_19(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            arr[2] = {1};
                            foo[2 + arr[1]] = {{1.3},{1}};
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(ArrayCell(Id('arr'),[IntLiteral(2)]),ArrayLiteral([IntLiteral(1)])),Assign(ArrayCell(Id('foo'),[BinaryOp('+',IntLiteral(2),ArrayCell(Id('arr'),[IntLiteral(1)]))]),ArrayLiteral([ArrayLiteral([FloatLiteral(1.3)]),ArrayLiteral([IntLiteral(1)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

        #Assign statements with expression precedence
    def test_function_declare_part_20(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            Var: r = 10., v;
                            v = v + (4. \. 3.) *. 3.14 *. r *. r *. r;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([VarDecl(Id('r'),[],FloatLiteral(10.0)),VarDecl(Id('v'),[],None)],[Assign(Id('v'),BinaryOp('+',Id('v'),BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('*.',BinaryOp('\.',FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id('r')),Id('r')),Id('r'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_function_declare_part_21(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            Var: v;
                            v = ((v + foo[2]) \ 2) + 10;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([VarDecl(Id('v'),[],None)],[Assign(Id('v'),BinaryOp('+',BinaryOp('\\',BinaryOp('+',Id('v'),ArrayCell(Id('foo'),[IntLiteral(2)])),IntLiteral(2)),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_function_declare_part_22(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            v = (15 + 270) * 12 \ 10 + foo();
                            lst[a + recur(2, 5)] = 20 - (a + foo())[7];
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('v'),BinaryOp('+',BinaryOp('\\',BinaryOp('*',BinaryOp('+',IntLiteral(15),IntLiteral(270)),IntLiteral(12)),IntLiteral(10)),CallExpr(Id('foo'),[]))),Assign(ArrayCell(Id('lst'),[BinaryOp('+',Id('a'),CallExpr(Id('recur'),[IntLiteral(2),IntLiteral(5)]))]),BinaryOp('-',IntLiteral(20),ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[])),[IntLiteral(7)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_function_declare_part_23(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            boolFlag = 20 - (a() + b())[7] >= 2;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('boolFlag'),BinaryOp('>=',BinaryOp('-',IntLiteral(20),ArrayCell(BinaryOp('+',CallExpr(Id('a'),[]),CallExpr(Id('b'),[])),[IntLiteral(7)])),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_function_declare_part_24(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            boolFlag1 = v < foo(r + f(r + g(x)));
                            boolFlag2 = 20 - (a + foo())[7] >= 2;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('boolFlag1'),BinaryOp('<',Id('v'),CallExpr(Id('foo'),[BinaryOp('+',Id('r'),CallExpr(Id('f'),[BinaryOp('+',Id('r'),CallExpr(Id('g'),[Id('x')]))]))]))),Assign(Id('boolFlag2'),BinaryOp('>=',BinaryOp('-',IntLiteral(20),ArrayCell(BinaryOp('+',Id('a'),CallExpr(Id('foo'),[])),[IntLiteral(7)])),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_function_declare_part_25(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            boolFlag1 = !(v < foo(r + f(r + g(x)))) && True;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('boolFlag1'),BinaryOp('&&',UnaryOp('!',BinaryOp('<',Id('v'),CallExpr(Id('foo'),[BinaryOp('+',Id('r'),CallExpr(Id('f'),[BinaryOp('+',Id('r'),CallExpr(Id('g'),[Id('x')]))]))]))),BooleanLiteral('true')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_function_declare_part_26(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            boo[1] = arr[10 + grrr()];
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(ArrayCell(Id('boo'),[IntLiteral(1)]),ArrayCell(Id('arr'),[BinaryOp('+',IntLiteral(10),CallExpr(Id('grrr'),[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_function_declare_part_27(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            boo = boo1(boo2(boo3()));
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('boo'),CallExpr(Id('boo1'),[CallExpr(Id('boo2'),[CallExpr(Id('boo3'),[])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_function_declare_part_28(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            (a + pointer[5])[10] = (15 + 270) * 12 \ 10 + foo();
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(ArrayCell(BinaryOp('+',Id('a'),ArrayCell(Id('pointer'),[IntLiteral(5)])),[IntLiteral(10)]),BinaryOp('+',BinaryOp('\\',BinaryOp('*',BinaryOp('+',IntLiteral(15),IntLiteral(270)),IntLiteral(12)),IntLiteral(10)),CallExpr(Id('foo'),[])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_function_declare_part_29(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            x = foo[a + foo_(2, 5. *. 10)] && !isTrue > 0;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('x'),BinaryOp('>',BinaryOp('&&',ArrayCell(Id('foo'),[BinaryOp('+',Id('a'),CallExpr(Id('foo_'),[IntLiteral(2),BinaryOp('*.',FloatLiteral(5.0),IntLiteral(10))]))]),UnaryOp('!',Id('isTrue'))),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_function_declare_part_30(self):
        """test function declaration part"""
        input =  """Function: assign
                        Body:
                            x = (2 + 10) * -10 && True == 4 +. 5 || False;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('assign'),[],([],[Assign(Id('x'),BinaryOp('==',BinaryOp('&&',BinaryOp('*',BinaryOp('+',IntLiteral(2),IntLiteral(10)),UnaryOp('-',IntLiteral(10))),BooleanLiteral('true')),BinaryOp('||',BinaryOp('+.',IntLiteral(4),IntLiteral(5)),BooleanLiteral('false'))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

        #call statement
    def test_function_declare_part_31(self):
        """test function declaration part"""
        input =  """Function: callStmt
                        Body:
                            f(2 + x, 4. \. y);
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('callStmt'),[],([],[CallStmt(Id('f'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\.',FloatLiteral(4.0),Id('y'))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_function_declare_part_32(self):
        """test function declaration part"""
        input =  """Function: callStmt
                        Body:
                            f(2 + x, 4. \. y);
                            goo(f() + arr[2]);
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('callStmt'),[],([],[CallStmt(Id('f'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\.',FloatLiteral(4.0),Id('y'))]),CallStmt(Id('goo'),[BinaryOp('+',CallExpr(Id('f'),[]),ArrayCell(Id('arr'),[IntLiteral(2)]))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_function_declare_part_33(self):
        """test function declaration part"""
        input =  """Function: callStmt
                        Body:
                            foo();
                            bar(1);
                            nty(1, 2, 3);
                            lem(hyy, dyf(), lem(123, 456, fay), aas(gyh()));
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('callStmt'),[],([],[CallStmt(Id('foo'),[]),CallStmt(Id('bar'),[IntLiteral(1)]),CallStmt(Id('nty'),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),CallStmt(Id('lem'),[Id('hyy'),CallExpr(Id('dyf'),[]),CallExpr(Id('lem'),[IntLiteral(123),IntLiteral(456),Id('fay')]),CallExpr(Id('aas'),[CallExpr(Id('gyh'),[])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_function_declare_part_34(self):
        """test function declaration part"""
        input =  """Function: callStmt
                        Body:
                            drawLine(10,5);
                            drawLine(10,6);
                            drawLine(10,7);
                            drawLine(10,10);
                            readkey();
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('callStmt'),[],([],[CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id('readkey'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_function_declare_part_34(self):
        """test function declaration part"""
        input =  """Function: callStmt
                        Body:
                            drawLine(10,5);
                            drawLine(10,6);
                            drawLine(10,7);
                            drawLine(10,10);
                            readkey();
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('callStmt'),[],([],[CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(10)]),CallStmt(Id('readkey'),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_function_declare_part_35(self):
        """test function declaration part"""
        input =  """Function: callStmt
                        Body:
                            drawLine(10,5);
                            drawLine1(10, drawLine());
                            drawLine2(drawLine1(),7);
                            drawLine(10,10);
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('callStmt'),[],([],[CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id('drawLine1'),[IntLiteral(10),CallExpr(Id('drawLine'),[])]),CallStmt(Id('drawLine2'),[CallExpr(Id('drawLine1'),[]),IntLiteral(7)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(10)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

        #While do statements
    def test_function_declare_part_36(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            While ((a == 4) && (c == 4)) 
                            Do
                                println(x);
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([],[While(BinaryOp('&&',BinaryOp('==',Id('a'),IntLiteral(4)),BinaryOp('==',Id('c'),IntLiteral(4))),([],[CallStmt(Id('println'),[Id('x')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_function_declare_part_37(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            While True 
                            Do
                                Var: x = 1;
                                println(x);
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([],[While(BooleanLiteral('true'),([VarDecl(Id('x'),[],IntLiteral(1))],[CallStmt(Id('println'),[Id('x')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_function_declare_part_38(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            Var: i = 0;
                            While (i < 5)
                            Do 
                                a[i] = b +. 1.0;
                                i = i + 1;
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([VarDecl(Id('i'),[],IntLiteral(0))],[While(BinaryOp('<',Id('i'),IntLiteral(5)),([],[Assign(ArrayCell(Id('a'),[Id('i')]),BinaryOp('+.',Id('b'),FloatLiteral(1.0))),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_function_declare_part_39(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            While i != 0 
                            Do
                                i = i - 1;
                                writeln(i);
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([],[While(BinaryOp('!=',Id('i'),IntLiteral(0)),([],[Assign(Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_function_declare_part_40(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Parameter: a
                        Body:
                            While a > 10
                            Do
                                Var: b;
                                println(a+b);
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[VarDecl(Id('a'),[],None)],([],[While(BinaryOp('>',Id('a'),IntLiteral(10)),([VarDecl(Id('b'),[],None)],[CallStmt(Id('println'),[BinaryOp('+',Id('a'),Id('b'))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_function_declare_part_41(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Parameter: a
                        Body:
                            Var: x[1] = 2;
                            While a > 10
                            Do
                                println(a+b);
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[VarDecl(Id('a'),[],None)],([VarDecl(Id('x'),[1],IntLiteral(2))],[While(BinaryOp('>',Id('a'),IntLiteral(10)),([],[CallStmt(Id('println'),[BinaryOp('+',Id('a'),Id('b'))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_function_declare_part_42(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Parameter: a
                        Body:
                            While a > 10
                            Do
                                foo(goo(1));
                                lmao();
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[VarDecl(Id('a'),[],None)],([],[While(BinaryOp('>',Id('a'),IntLiteral(10)),([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_function_declare_part_43(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            While foo() < arr[2]
                            Do
                                lmao();
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([],[While(BinaryOp('<',CallExpr(Id('foo'),[]),ArrayCell(Id('arr'),[IntLiteral(2)])),([],[CallStmt(Id('lmao'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_function_declare_part_44(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            While a > 10
                            Do
                                foo(goo(1));
                                lmao();
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([],[While(BinaryOp('>',Id('a'),IntLiteral(10)),([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_function_declare_part_45(self):
        """test function declaration part"""
        input =  """Function: whileDoStmt
                        Body:
                            Var: x[2] = {2};
                            While a > 10
                            Do
                        
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('whileDoStmt'),[],([VarDecl(Id('x'),[2],ArrayLiteral([IntLiteral(2)]))],[While(BinaryOp('>',Id('a'),IntLiteral(10)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

        # Do While statements
    def test_function_declare_part_46(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: x[2] = {2};
                            Do
                                foo(goo(1));
                                lmao();
                            While a > 10
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('x'),[2],ArrayLiteral([IntLiteral(2)]))],[Dowhile(([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])]),BinaryOp('>',Id('a'),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_function_declare_part_47(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Do 
                            While i != 0 
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([],[Dowhile(([],[]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_function_declare_part_48(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: x[2] = {2};
                            Do 
                                i = i - 1;
                                writeln(i);
                            While i != 0
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('x'),[2],ArrayLiteral([IntLiteral(2)]))],[Dowhile(([],[Assign(Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),CallStmt(Id('writeln'),[Id('i')])]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_function_declare_part_49(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: x[2] = {2};
                            Do 
                                Var: y = 1;
                                writeln(y);
                            While i != 0
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('x'),[2],ArrayLiteral([IntLiteral(2)]))],[Dowhile(([VarDecl(Id('y'),[],IntLiteral(1))],[CallStmt(Id('writeln'),[Id('y')])]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

        # Do While statements with break continue stmt
    def test_function_declare_part_50(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: i = 10;
                            Do 
                                goo();
                                Break;
                            While i != 0
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('i'),[],IntLiteral(10))],[Dowhile(([],[CallStmt(Id('goo'),[]),Break()]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_function_declare_part_51(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: i = 10;
                            Do 
                                Continue;
                                Break;
                            While i != 0
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('i'),[],IntLiteral(10))],[Dowhile(([],[Continue(),Break()]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_function_declare_part_52(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: i = 10;
                            Do 
                                Continue;
                            While i != 0
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('i'),[],IntLiteral(10))],[Dowhile(([],[Continue()]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

        # Nested while statement
    def test_function_declare_part_53(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Var: i = 10;
                            Do 
                                i = i - 1;
                                Do 
                                    i = i - 1;
                                While i != 0
                                EndDo.
                            While i != 0
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([VarDecl(Id('i'),[],IntLiteral(10))],[Dowhile(([],[Assign(Id('i'),BinaryOp('-',Id('i'),IntLiteral(1))),Dowhile(([],[Assign(Id('i'),BinaryOp('-',Id('i'),IntLiteral(1)))]),BinaryOp('!=',Id('i'),IntLiteral(0)))]),BinaryOp('!=',Id('i'),IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_function_declare_part_54(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            While fx()
                            Do
                                While gx()
                                Do
                                    writeln(i);
                                EndWhile.
                            EndWhile.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([],[While(CallExpr(Id('fx'),[]),([],[While(CallExpr(Id('gx'),[]),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_function_declare_part_55(self):
        """test function declaration part"""
        input =  """Function: doWhileStmt
                        Body:
                            Do
                                While gx()
                                Do
                                    Break;
                                EndWhile.
                            While fx()
                            EndDo.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('doWhileStmt'),[],([],[Dowhile(([],[While(CallExpr(Id('gx'),[]),([],[Break()]))]),CallExpr(Id('fx'),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    # For loop statements
    def test_function_declare_part_56(self):
        """test function declaration part"""
        input =  """Function: forStmt
                        Body:
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('forStmt'),[],([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_function_declare_part_57(self):
        """test function declaration part"""
        input =  """Function: forStmt
                        Body:
                            For (i = foo(), i < 10, 2) Do
                                writeln(i);
                                Continue;
                            EndFor.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('forStmt'),[],([],[For(Id('i'),CallExpr(Id('foo'),[]),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')]),Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_function_declare_part_58(self):
        """test function declaration part"""
        input =  """Function: forStmt
                        Body:
                            For (i = foo(), i < 10, 2) Do
                             
                            EndFor.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('forStmt'),[],([],[For(Id('i'),CallExpr(Id('foo'),[]),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_function_declare_part_59(self):
        """test function declaration part"""
        input =  """Function: forStmt
                        Body:
                            For (i = foo(), i < 10, 2) Do
                                For (i = 0, i < 10, 2) Do
                                    writeln(i);
                                EndFor.
                            EndFor.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('forStmt'),[],([],[For(Id('i'),CallExpr(Id('foo'),[]),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_function_declare_part_60(self):
        """test function declaration part"""
        input =  """Function: forStmt
                        Body:
                            For (i = foo(), i < arr[1], 2) Do
                                bFlag = True;
                                arr[1] = arr[1] - 1;
                            EndFor.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('forStmt'),[],([],[For(Id('i'),CallExpr(Id('foo'),[]),BinaryOp('<',Id('i'),ArrayCell(Id('arr'),[IntLiteral(1)])),IntLiteral(2),([],[Assign(Id('bFlag'),BooleanLiteral('true')),Assign(ArrayCell(Id('arr'),[IntLiteral(1)]),BinaryOp('-',ArrayCell(Id('arr'),[IntLiteral(1)]),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

        # Return statement
    def test_function_declare_part_61(self):
        """test function declaration part"""
        input =  """Function: returnStmt
                        Body:
                            Return;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('returnStmt'),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_function_declare_part_62(self):
        """test function declaration part"""
        input =  """Function: returnStmt
                        Body:
                            print(i);
                            Return returnStmt(i + 1);
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('returnStmt'),[],([],[CallStmt(Id('print'),[Id('i')]),Return(CallExpr(Id('returnStmt'),[BinaryOp('+',Id('i'),IntLiteral(1))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_function_declare_part_63(self):
        """test function declaration part"""
        input =  """Function: returnStmt
                        Body:
                            Return f(2 + x, 4. \. y);
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('returnStmt'),[],([],[Return(CallExpr(Id('f'),[BinaryOp('+',IntLiteral(2),Id('x')),BinaryOp('\.',FloatLiteral(4.0),Id('y'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

        # If statements
    def test_function_declare_part_64(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 0 Then
                                Return 1;
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_function_declare_part_65(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 0 Then
                                Return 1;
                            ElseIf n == 1 Then
                                Break;
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))]),(BinaryOp('==',Id('n'),IntLiteral(1)),[],[Break()])],[(),()])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_function_declare_part_66(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 0 Then
                                Return ;
                            ElseIf n == 1 Then
                                Return ;
                            Else
                                Break;
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(None)]), (BinaryOp('==',Id('n'),IntLiteral(1)),[],[Return(None)])], ([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_function_declare_part_67(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 0 Then
                                Return ;
                            Else
                                Break;
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(None)])], ([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_function_declare_part_68(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])], ([],[Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_function_declare_part_69(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 0o12 Then
                                Return 1;
                            Else
                                Return goo();
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(10)),[],[Return(IntLiteral(1))])], ([],[Return(CallExpr(Id('goo'),[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_function_declare_part_70(self):
        """test function declaration part"""
        input =  """Function: ifStmt
                        Body:
                            If n == 1 Then
                                Var: x = 10;
                                Return True;
                            Else
                                Var: y = 1;
                                Return goo();
                            EndIf.
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id('ifStmt'),[],([],[If([(BinaryOp('==',Id('n'),IntLiteral(1)),[VarDecl(Id('x'),[],IntLiteral(10))],[Return(BooleanLiteral('true'))])], ([VarDecl(Id('y'),[],IntLiteral(1))],[Return(CallExpr(Id('goo'),[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

        #Complete program test
    def test_program_1(self):
        """test program"""
        input =  """Var: x = 4;  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            foo(x , x + 1);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],IntLiteral(4)),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([],[CallStmt(Id('foo'),[Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_program_2(self):
        """test program"""
        input =  """Var: x = 4;  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],IntLiteral(4)),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[IntLiteral(2)],IntLiteral(1))],[Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_program_2(self):
        """test program"""
        input =  """Var: x = 4;  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],IntLiteral(4)),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_program_3(self):
        """test program"""
        input =  """Var: x = 4;  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],IntLiteral(4)),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_program_4(self):
        """test program"""
        input =  """Var: x = 4;  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            boo[1] = arr[10 + grrr()];
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],IntLiteral(4)),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[Assign(ArrayCell(Id('boo'),[IntLiteral(1)]),ArrayCell(Id('arr'),[BinaryOp('+',IntLiteral(10),CallExpr(Id('grrr'),[]))])),CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_program_5(self):
        """test program"""
        input =  """Var: x = 4;  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            While a > 10
                            Do
                                foo(goo(1));
                                lmao();
                            EndWhile.
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            boo[1] = arr[10 + grrr()];
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],IntLiteral(4)),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[While(BinaryOp('>',Id('a'),IntLiteral(10)),([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[Assign(ArrayCell(Id('boo'),[IntLiteral(1)]),ArrayCell(Id('arr'),[BinaryOp('+',IntLiteral(10),CallExpr(Id('grrr'),[]))])),CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_program_6(self):
        """test program"""
        input =  """Var: x[1][2] = {{1,2}};  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            While a[0][1] > 10
                            Do
                                foo(goo(1));
                                lmao();
                            EndWhile.
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            boo[1] = arr[10 + grrr()];
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)])])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[While(BinaryOp('>',ArrayCell(Id('a'),[IntLiteral(0),IntLiteral(1)]),IntLiteral(10)),([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[Assign(ArrayCell(Id('boo'),[IntLiteral(1)]),ArrayCell(Id('arr'),[BinaryOp('+',IntLiteral(10),CallExpr(Id('grrr'),[]))])),CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_program_7(self):
        """test program"""
        input =  """Var: x[1][2] = {{1,2}};  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            While a[0][1] > 10
                            Do
                                foo(goo(1));
                                lmao();
                            EndWhile.
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            drawLine(10,5);
                            drawLine(10,6);
                            drawLine(10,7);
                            drawLine(10,10);
                            boo[1] = arr[10 + grrr()];
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)])])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[While(BinaryOp('>',ArrayCell(Id('a'),[IntLiteral(0),IntLiteral(1)]),IntLiteral(10)),([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(10)]),Assign(ArrayCell(Id('boo'),[IntLiteral(1)]),ArrayCell(Id('arr'),[BinaryOp('+',IntLiteral(10),CallExpr(Id('grrr'),[]))])),CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_program_8(self):
        """test program"""
        input =  """Var: x[1][2] = {{1,2}};  
                    Function: foo
                        Parameter: a, b
                        Body:
                            Var: z[2] = 1;
                            While a[0][1] > 10
                            Do
                                foo(goo(1));
                                lmao();
                            EndWhile.
                            For (i = 0, i < 10, 2) Do
                                writeln(i);
                            EndFor.
                            Return a + b;
                        EndBody.
                    
                    Function: main
                        Body:
                            Var: m = 2;
                            If bool_of_string ("True") Then
                                a = int_of_string (read ());
                                b = float_of_int (a) +. 2.0;
                            EndIf.
                            drawLine(10,5);
                            drawLine(10,6);
                            drawLine(10,7);
                            drawLine(10,10);
                            boo[1] = arr[10 + grrr()];
                            foo(x , m);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)])])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('z'),[2],IntLiteral(1))],[While(BinaryOp('>',ArrayCell(Id('a'),[IntLiteral(0),IntLiteral(1)]),IntLiteral(10)),([],[CallStmt(Id('foo'),[CallExpr(Id('goo'),[IntLiteral(1)])]),CallStmt(Id('lmao'),[])])),For(Id('i'),IntLiteral(0),BinaryOp('<',Id('i'),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id('writeln'),[Id('i')])])),Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],([VarDecl(Id('m'),[],IntLiteral(2))],[If([(CallExpr(Id('bool_of_string'),[StringLiteral('True')]), [],[Assign(Id('a'),CallExpr(Id('int_of_string'),[CallExpr(Id('read'),[])])),Assign(Id('b'),BinaryOp('+.',CallExpr(Id('float_of_int'),[Id('a')]),FloatLiteral(2.0)))])],[(),()]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(5)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(6)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(7)]),CallStmt(Id('drawLine'),[IntLiteral(10),IntLiteral(10)]),Assign(ArrayCell(Id('boo'),[IntLiteral(1)]),ArrayCell(Id('arr'),[BinaryOp('+',IntLiteral(10),CallExpr(Id('grrr'),[]))])),CallStmt(Id('foo'),[Id('x'),Id('m')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_program_9(self):
        """test program"""
        input =  """Var: x;
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
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])], ([],[Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])),FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_program_10(self):
        """test program"""
        input =  """Var: x;
                    Function: fact
                        Parameter: n
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.
                        EndBody.

                    Function: sum
                        Parameter: n
                        Body:
                            If n == 0 Then
                                Return 0;
                            Else
                                Return n + sum (n - 1);
                            EndIf.
                        EndBody.

                    Function: main
                        Body:
                            x = 10;
                            fact (x);
                            sum (x);
                        EndBody.
                """ 
        expect = Program([VarDecl(Id('x'),[],None),FuncDecl(Id('fact'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(1))])], ([],[Return(BinaryOp('*',Id('n'),CallExpr(Id('fact'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])), FuncDecl(Id('sum'),[VarDecl(Id('n'),[],None)],([],[If([(BinaryOp('==',Id('n'),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[Return(BinaryOp('+',Id('n'),CallExpr(Id('sum'),[BinaryOp('-',Id('n'),IntLiteral(1))])))]))])) ,FuncDecl(Id('main'),[],([],[Assign(Id('x'),IntLiteral(10)),CallStmt(Id('fact'),[Id('x')]),CallStmt(Id('sum'),[Id('x')])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

