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
        expect = str()
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

    def test_locla_variable_with_outside_scope_15(self):
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
        self.assertTrue(TestChecker.test(input,expect,414))

    # def test_redeclare_function(self):
    #     """Simple program: main"""
    #     input = Program([
    #         VarDecl(Id("a"), [], IntLiteral(3)),
    #         VarDecl(Id("b"), [3], ArrayLiteral([IntLiteral(3), IntLiteral(5), IntLiteral(6)])),
    #         FuncDecl(
    #             Id("foo"), 
    #             [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
    #             (
    #                 [VarDecl(Id("c"),[],None), VarDecl(Id("d"),[],None)],
    #                 [CallStmt(Id("foo"),[IntLiteral(3), FloatLiteral(4.0)])]
    #             )
    #         ),
    #         FuncDecl(
    #             Id("foo"), 
    #             [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
    #             (
    #                 [VarDecl(Id("c"),[],None), VarDecl(Id("d"),[],None)],
    #                 [CallStmt(Id("foo"),[IntLiteral(3), FloatLiteral(4.0)])]
    #             )
    #         )
    #     ])
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numof_param_stmt(self):
    #     """Complex program"""
    #     input = Program([
    #         FuncDecl(
    #             Id("main"), 
    #             [],
    #             (
    #                 [],
    #                 [CallStmt(Id("printStrLn"),[])]
    #             )
    #         )
    #     ])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,403))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_if_scope_1(self):
    #     input = Program([
    #         FuncDecl(
    #             Id("main"), 
    #             [],
    #             (
    #                 [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
    #                 [
    #                     If(
    #                         [
    #                             (Id("a"), 
    #                             [VarDecl(Id("b"),[],None), VarDecl(Id("c"),[],None)], [Assign(Id("b"), IntLiteral(3))])
    #                         ],
    #                         ([],[])
    #                     )
    #                 ]
    #             )
    #         )
    #     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_if_scope_2(self):
    #     input = Program([
    #         FuncDecl(
    #             Id("main"), 
    #             [],
    #             (
    #                 [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
    #                 [
    #                     If(
    #                         [
    #                             (Id("a"), [VarDecl(Id("b"),[],None), VarDecl(Id("c"),[],None)], [Assign(Id("b"), IntLiteral(3))]),
    #                             (Id("a"), [VarDecl(Id("b"),[],None), VarDecl(Id("c"),[],None)], [Assign(Id("b"), IntLiteral(3))]),
    #                             (Id("a"), [VarDecl(Id("b"),[],None), VarDecl(Id("c"),[],None)], [Assign(Id("b"), IntLiteral(3))])
    #                         ],
    #                         ([VarDecl(Id("b"),[],None), VarDecl(Id("c"),[],None)],[Assign(Id("b"), IntLiteral(3))])
    #                     )
    #                 ]
    #             )
    #         )
    #     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,409))
    
    # def test_normal_function(self):
    #     """Simple program: main"""
    #     input = Program([
    #         VarDecl(Id("a"), [], IntLiteral(3)),
    #         VarDecl(Id("b"), [3], ArrayLiteral([IntLiteral(3), IntLiteral(5), IntLiteral(6)])),
    #         FuncDecl(
    #             Id("foo"), 
    #             [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
    #             (
    #                 [VarDecl(Id("c"),[],None), VarDecl(Id("d"),[],None)],
    #                 [CallStmt(Id("foo"),[IntLiteral(3), FloatLiteral(4.0)])]
    #             )
    #         )
    #     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,400))


    # def test_function_return_infer(self):
    #     """Simple program: main"""
    #     input = Program([
    #         FuncDecl(
    #             Id("foo"), 
    #             [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
    #             (
    #                 [],
    #                 []
    #             )
    #         ),
    #         FuncDecl(
    #             Id("foo2"), 
    #             [],
    #             (
    #                 [],
    #                 [Assign(Id("a"), IntLiteral(5))]
    #             )
    #         )
    #     ])
    #     expect = str(Undeclared(Identifier(), "a"))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    