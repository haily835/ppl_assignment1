import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_call_1(self):
        input = """
                Function: main
                Body: 
                If True Then
                    Return 1;
                EndIf.
                EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,400))