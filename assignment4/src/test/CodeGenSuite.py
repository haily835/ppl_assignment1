import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
#     def test_int(self):
#         """Simple program: int main() {} """
#         input = """Function: main
#                    Body: 
#                         print(string_of_int(120));
#                    EndBody."""
#         expect = "120"
#         self.assertTrue(TestCodeGen.test(input,expect,500))

#     def test_int_ast(self):
#     	input = Program([
#     		FuncDecl(Id("main"),[],([],[
#     			CallStmt(Id("print"),[
#                     CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
#     	expect = "120"
#     	self.assertTrue(TestCodeGen.test(input,expect,501))
        
#     def test_simple_function(self):
#         input = Program([FuncDecl(Id("main"), [VarDecl(Id("args"), [], None)], ([VarDecl(Id("b"), [], IntLiteral(3))],[ Return(None)]))])
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,502))

#     def test_simple_function_2(self):
#         input = """
#         Function: main
#         Body:
#             foo(True);
#         EndBody.

#         Function: foo
#         Parameter: a
#         Body:
#             Return;
#         EndBody.
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,503))

#     def test_array_function(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a[2][2]={{1,2}, {3,4}};
#         EndBody.
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,504))

#     def test_array_2(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a[2]={1,2};
#         EndBody.
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,505))

#     def test_array_3(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a[2][2][2]={{{1,2},{3,4}},{{5,6},{7,8}}};
#         EndBody.
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,506))



#     def test_compare_1(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a = 123;
#             print(string_of_bool(True));
#             Return;
#         EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,507))

#     def test_function_ret_1(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             print(string_of_int(2));
#             Return;
#         EndBody.
#         Function: foo
#         Body:
#             Return 3;
#         EndBody.
#         """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,508))

#     def test_if_1(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             If False Then
#                 print("1");
#             ElseIf True Then
#                 print("2");
#             EndIf.
#             Return;
#         EndBody.
#         """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,509))

#     def test_if_2(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a = 3;
#             If False Then
#                 print("1");
#             ElseIf True Then
#                 print(string_of_int(a));
#             EndIf.
#             Return;
#         EndBody.
#         """
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,510))

#     def test_if_3(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a = 3;
#             If True Then
#                 Var: a = 1;
#                 print(string_of_int(a));
#             EndIf.
            
#             Return;
#         EndBody.
#         """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,511))

#     def test_if_4(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: a = 3;
#             If True Then
#                 Var: a = 1;
#                 print(string_of_int(a));
#             EndIf.
#             If True Then
#                 print(string_of_int(a));
#             EndIf.
#             Return;
#         EndBody.
#         """
#         expect = "13"
#         self.assertTrue(TestCodeGen.test(input,expect,512))

#     def test_if_5(self):
#         input = """
#         Function: main
#         Body:
#             If True Then
#                 Var: a = 1;
#                 print(string_of_int(a));
#             Else
#                 Var: a = 5;
#                 print(string_of_int(a));
#             EndIf.
#         EndBody.
#         """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,513))

#     def test_if_6(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             If False Then
#                 Var: a = 1;
#                 print(string_of_int(a));
#             ElseIf False Then
#                 Var: a = 2;
#                 print(string_of_int(a));
#             ElseIf False Then
#                 Var: a = 3;
#                 print(string_of_int(a));
#             ElseIf False Then
#                 Var: a = 4;
#                 print(string_of_int(a));
#             Else
#                 Var: a = 5;
#                 print(string_of_int(a));
#             EndIf.
#             Return;
#         EndBody.
#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,514))

#     def test_for_1(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: i = 0;
#             For( i = 1, i < 5, 1) Do
#                 print(string_of_int(i));
#             EndFor.
#         EndBody.
#         """
#         expect = "1234"
#         self.assertTrue(TestCodeGen.test(input,expect,515))

#     def test_for_2(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: i = 0;
#             For( i = 1, i < 5, 1) Do
#                 Var: a = 0;
#                 a = i;
#                 print(string_of_int(a));
#             EndFor.
#         EndBody.
#         """
#         expect = "1234"
#         self.assertTrue(TestCodeGen.test(input,expect,516))
    
#     def test_for_3(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: i = 0, j = 0;
#             For( i = 0, i < 3, 1) Do
#                 For( j = 0, j < 3, 1) Do
#                     print(string_of_int(3));
#                 EndFor.
#             EndFor.
#         EndBody.
#         """
#         expect = "333333333"
#         self.assertTrue(TestCodeGen.test(input,expect,517))

#     def test_for_4(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: i = 0;
#             For( i = 0, i < 9, 1) Do
#                 If i % 2 == 0 Then
#                     print(string_of_int(i));
#                 EndIf.
#             EndFor.
#         EndBody.
#         """
#         expect = "02468"
#         self.assertTrue(TestCodeGen.test(input,expect,518))

#     def test_for_5(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: i = 0;
#             For( i = 0, i < 9, 1) Do
#                 Var: i = 5;
#                 print(string_of_int(i));
#             EndFor.
#         EndBody.
#         """
#         expect = "555555555"
#         self.assertTrue(TestCodeGen.test(input,expect,519))


#     def test_while_1(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             Var: i = 0;
#             While i < 5 Do
#                 print(string_of_int(i));
#                 i = i + 1;
#             EndWhile.
#         EndBody.
#         """
#         expect = "01234"
#         self.assertTrue(TestCodeGen.test(input,expect,520))

#     def test_while_2(self):
#         input = """
#         Function: main
#         Parameter: args
#         Body:
#             While True Do
#                 print(string_of_int(1));
#                 Break;
#             EndWhile.
#         EndBody.
#         """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,521))

#     def test_call_expr_1(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(foo(2)));
# EndBody.

# Function: foo
# Parameter: a
# Body:
# Return 3;
# EndBody.
#         """
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,522))
        
#     def test_recursive_1(self):
#         input = """
# Var: x = 0;

# Function: main
# Body:
# x = 10;
# print(string_of_int(fact(x)));
# EndBody.

# Function: fact
# Parameter: n
# Body:
# If n == 0 Then
# Return 1;
# ElseIf n!=0 Then
# Return n*fact (n - 1);
# EndIf.
# EndBody.
#         """
#         expect = "3628800"
#         self.assertTrue(TestCodeGen.test(input,expect,523))

#     def test_arraycell_1(self):
#         input = """
# Function: main
# Body:
# Var: a[2][2] = {{1,2},{3,4}};
# print(string_of_int(a[0][1]));
# EndBody.
#         """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,524))

#     def test_array_cell_2(self):
#         input = """
# Function: main
# Body:
# Var: a[2][2] = {{"String","var"},{"3","trign"}};
# print(a[0][0]);
# EndBody.
#         """
#         expect = "String"
#         self.assertTrue(TestCodeGen.test(input,expect,525))

#     def test_array_cell_3(self):
#         input = """
# Function: main
# Body:
# Var: a[2][2][2] = {{{True, False},{True,False}},{{True, False},{True, False}}};
# print(string_of_bool(a[0][0][1]));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,526))

#     def test_array_cell_4(self):
#         input = """
# Var: a[5] = {1,2,3,4,5};
# Function: main
# Body:
# Var: i = 0;
# For(i = 0, i < 5, 1) Do
#     print(string_of_int(a[i]));
# EndFor.
# EndBody.
#         """
#         expect = "12345"
#         self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_array_cell_5(self):
        input = """
Var: a[2][2] = {{1,2},{3,4}};
Var: i = 0, j = 0;
Function: main
Body:
For(i = 0, i < 2, 1) Do
    For(j = 0, j < 2, 1) Do
        print(string_of_int(a[i][j]));
    EndFor.
EndFor.
EndBody.
        """
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input,expect,527))