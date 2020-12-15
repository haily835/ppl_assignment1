import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_call_78(self):
        input = """
                Function: main
                Parameter: y
                Body: 
                main(3.3);
                y = 4;
                EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,478))