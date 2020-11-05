import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
Function: main
Body:
Var:x = 5;
EndBody."""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_simple_program_1(self):
        """Simple program: int main() {} """
        input = """
Function: main
Body:
Var:x[5] = 5;
x[8] = 5;
EndBody."""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
