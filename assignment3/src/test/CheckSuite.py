import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

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


    def test_function_return_infer(self):
        """Simple program: main"""
        input = Program([
            FuncDecl(
                Id("foo"), 
                [VarDecl(Id("a"),[],None), VarDecl(Id("b"),[],None)],
                (
                    [],
                    []
                )
            ),
            FuncDecl(
                Id("foo2"), 
                [],
                (
                    [],
                    [Assign(Id("a"), IntLiteral(5))]
                )
            )
        ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

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
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))