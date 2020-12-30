import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """Function: main
    #                Body: 
    #                     print(string_of_int(120));
    #                EndBody."""
    #     expect = "120"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],([],[
    # 			CallStmt(Id("print"),[
    #                 CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    # 	expect = "120"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
        
    # def test_simple_function(self):
    #     input = Program([FuncDecl(Id("main"), [VarDecl(Id("args"), [], None)], ([VarDecl(Id("b"), [], IntLiteral(3))],[ Return(None)]))])
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def test_simple_function(self):
    #     input = """
    #     Function: main
    #     Parameter: args
    #     Body:
    #         foo(True);
    #     EndBody.

    #     Function: foo
    #     Parameter: a
    #     Body:
    #         Return;
    #     EndBody.
    #     """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_array_function(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a[2][2]={{1,2}, {3,4}};
        EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_int2_ast(self):
    # 	input = Program([VarDecl(Id("a"), [], IntLiteral(3))])
    # 	expect = ""
    # 	self.assertTrue(TestCodeGen.test(input,expect,502))

