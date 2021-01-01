import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
                    CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    	expect = "120"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_simple_function(self):
        input = Program([FuncDecl(Id("main"), [VarDecl(Id("args"), [], None)], ([VarDecl(Id("b"), [], IntLiteral(3))],[ Return(None)]))])
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_simple_function_2(self):
        input = """
        Function: main
        Body:
            foo(True);
        EndBody.

        Function: foo
        Parameter: a
        Body:
            Return;
        EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_array_function(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a[2][2]={{1,2}, {3,4}};
        EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_array_2(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a[2]={1,2};
        EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_array_3(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a[2][2][2]={{{1,2},{3,4}},{{5,6},{7,8}}};
        EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,506))



    def test_compare_1(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a = 123;
            print(string_of_bool(True));
            Return;
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_function_ret_1(self):
        input = """
        Function: main
        Parameter: args
        Body:
            print(string_of_int(2));
            Return;
        EndBody.
        Function: foo
        Body:
            Return 3;
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_if_1(self):
        input = """
        Function: main
        Parameter: args
        Body:
            If False Then
                print("1");
            ElseIf True Then
                print("2");
            EndIf.
            Return;
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_if_2(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a = 3;
            If False Then
                print("1");
            ElseIf True Then
                print(string_of_int(a));
            EndIf.
            Return;
        EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_if_3(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a = 3;
            If True Then
                Var: a = 1;
                print(string_of_int(a));
            EndIf.
            
            Return;
        EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_if_4(self):
        input = """
        Function: main
        Parameter: args
        Body:
            Var: a = 3;
            If True Then
                Var: a = 1;
                print(string_of_int(a));
            EndIf.
            If True Then
                print(string_of_int(a));
            EndIf.
            Return;
        EndBody.
        """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_if_5(self):
        input = """
        Function: main
        Body:
            If True Then
                Var: a = 1;
                print(string_of_int(a));
            Else
                Var: a = 5;
                print(string_of_int(a));
            EndIf.
        EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_if_6(self):
        input = """
        Function: main
        Parameter: args
        Body:
            If False Then
                Var: a = 1;
                print(string_of_int(a));
            ElseIf False Then
                Var: a = 2;
                print(string_of_int(a));
            ElseIf False Then
                Var: a = 3;
                print(string_of_int(a));
            ElseIf True Then
                Var: a = 4;
                print(string_of_int(a));
            Else
                Var: a = 5;
                print(string_of_int(a));
            EndIf.
            Return;
        EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,514))


