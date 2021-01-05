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
# Function: fact
# Parameter: n
# Body:
# If n == 0 Then
# Return 1;
# Else
# Return n*fact (n - 1);
# EndIf.
# EndBody.

# Function: main
# Body:
# x = 10;
# print(string_of_int(fact(x)));
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

#     def test_array_cell_5(self):
#         input = """

# Var: a[2][2] = {{1,2},{3,4}};
# Var: i = 0, j = 0;
# Function: main
# Body:
# For( i = 0, i < 2, 1) Do
#     For(j = 0, j < 2, 1) Do
#         print(string_of_int(a[i][j]));
#     EndFor.
# EndFor.
# EndBody.
#         """
#         expect = "1234"
#         self.assertTrue(TestCodeGen.test(input,expect,527))

#     def test_array_cell_6(self):
#         input = """

# Var: a[2][2][2] = {{{1,2},{3,4}}, {{5,6},{7,8}}};
# Var: i = 0, j = 0, k = 0;
# Function: main
# Body:
# For( i = 0, i < 2, 1) Do
#     For(j = 0, j < 2, 1) Do
#         For(k = 0, k < 2, 1) Do
#             print(string_of_int(a[i][j][k]));
#         EndFor.
#     EndFor.
# EndFor.
# EndBody.
#         """
#         expect = "12345678"
#         self.assertTrue(TestCodeGen.test(input,expect,528))


#     def test_array_cell_7(self):
#         input = """
# Var: a[2] = {1,2};

# Function: main
# Body:
# printArray1(a);
# EndBody.

# Function: printArray1
# Parameter: a
# Body:
# Var: i = 0;
# For( i = 0, i < 2, 1) Do
#     print(string_of_int(a[i]));
# EndFor.
# Return;
# EndBody.
#         """
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input,expect,529))

#     def test_binary_1(self):
#         input = """
# Function: main
# Body:
# print(string_of_int((1+2)*2));
# EndBody.
#         """
#         expect = "6"
#         self.assertTrue(TestCodeGen.test(input,expect,530))
    
#     def test_binary_2(self):
#         input = """
# Function: main
# Body:
# print(string_of_int((1+2+2)*2*2));
# EndBody.
#         """
#         expect = "20"
#         self.assertTrue(TestCodeGen.test(input,expect,531))

#     def test_binary_3(self):
#         input = """
# Function: main
# Body:
# print(string_of_int((1-2-2)*2*2));
# EndBody.
#         """
#         expect = "-12"
#         self.assertTrue(TestCodeGen.test(input,expect,532))

#     def test_binary_4(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(15 % 2 % 2));
# EndBody.
#         """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,533))


#     def test_binary_5(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(15 \\ 2 \\ 2));
# EndBody.
#         """
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,534))

#     def test_binary_6(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(-5 + 2));
# EndBody.
#         """
#         expect = "-3"
#         self.assertTrue(TestCodeGen.test(input,expect,535))

#     def test_binary_7(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(-.5.0 +. 2.0));
# EndBody.
#         """
#         expect = "-3.0"
#         self.assertTrue(TestCodeGen.test(input,expect,536))

#     def test_binary_8(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(5.0 *. 2.0));
# EndBody.
#         """
#         expect = "10.0"
#         self.assertTrue(TestCodeGen.test(input,expect,537))

#     def test_binary_9(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(5.0 *. 2.0 *. 2.0 -. 3.0));
# EndBody.
#         """
#         expect = "17.0"
#         self.assertTrue(TestCodeGen.test(input,expect,538))

#     def test_binary_10(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(5.0 +. 2.0 +. 2.0 -. 3.0));
# EndBody.
#         """
#         expect = "6.0"
#         self.assertTrue(TestCodeGen.test(input,expect,539))
            
#     def test_binary_11(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(5.0 \\. 2.0));
# EndBody.
#         """
#         expect = "2.5"
#         self.assertTrue(TestCodeGen.test(input,expect,540))

#     def test_binary_12(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(5.0 \\. 2.0 \\. 0.5));
# EndBody.
#         """
#         expect = "5.0"
#         self.assertTrue(TestCodeGen.test(input,expect,541))

#     def test_binary_13(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(-15.0 \\. 2.0));
# EndBody.
#         """
#         expect = "-7.5"
#         self.assertTrue(TestCodeGen.test(input,expect,542))

#     def test_binary_14(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(float_to_int(1) +. 2.0));
# EndBody.
#         """
#         expect = "3.0"
#         self.assertTrue(TestCodeGen.test(input,expect,543))

#     def test_binary_15(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(int_of_float(1.0) * 2));
# EndBody.
#         """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,544))

#     def test_binary_16(self):
#         input = """
# Function: main
# Body:
# print(string_of_float(float_of_string("1.0") * 2.0));
# EndBody.
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,545))

#     def test_binary_17(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(int_of_string("1") * 2));
# EndBody.
#         """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,546))

#     def test_boolean(self):
#         input = """
# Function: main
# Body:
# print(string_of_bool(bool_of_string("True")));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,547))

#     def test_boolean_2(self):
#         input = """
# Function: main
# Body:
# Var: a = 0;
# Var: b = 0;
# If bool_of_string("True") Then
#     a = int_of_string(read());
#     b = float_to_int(a) + 2.0;
#     print(string_of_float(b));
# EndIf.
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,548))

#     def test_sum_array(self):
#         input = """
# Function: main
# Body:
# Var: a[5] = {1,2,3,4,5};
# print(string_of_int(sum(a, 5)));
# EndBody.

# Function: sum
# Parameter: a, size
# Body:
# Var: i = 0;
# Var: result = 0;
# For(i = 0, i < size, 1) Do
#     result = result + a[i];
# EndFor.
# Return result;
# EndBody.
#         """
#         expect = "15"
#         self.assertTrue(TestCodeGen.test(input,expect,549))


#     def test_return_ele(self):
#         input = """
# Var: i = 0;
# Function: main
# Body:
# For( i = 0, i < 3, 1 ) Do
#     print(createArr(i));
# EndFor.
# EndBody.

# Function: createArr
# Parameter: i
# Body:
# Var: a[3] = {"Happy ", "new ", "year"};
# Return a[i];
# EndBody.
#         """
#         expect = "Happy new year"
#         self.assertTrue(TestCodeGen.test(input,expect,550))

#     def test_do_while_1(self):
#         input = """
# Var: i = 0;
# Function: main
# Body:
# Do 
#     print(string_of_int(i));
#     i = i + 1;
# While i < 5
# EndDo.
# EndBody.
#         """
#         expect = "01234"
#         self.assertTrue(TestCodeGen.test(input,expect,551))

#     def test_while(self):
#         input = """
# Var: i = 0;
# Function: main
# Body:
# While i < 5 Do
#     print(string_of_int(i));
#     i = i + 1;
# EndWhile.
# EndBody.
#         """
#         expect = "01234"
#         self.assertTrue(TestCodeGen.test(input,expect,552))

#     def test_do_while_2(self):
#         input = """
# Var: i = 0;
# Function: main
# Body:
# Do 
#     print(string_of_int(i));
#     i = i + 1;
# While False
# EndDo.
# EndBody.
#         """
#         expect = "0"
#         self.assertTrue(TestCodeGen.test(input,expect,553))

#     def test_break_while_1(self):
#         input = """
# Var: i = 0;
# Function: main
# Body:
# While i < 10 Do
#     If i == 5 Then
#         Break;
#     EndIf.
#     print(string_of_int(i));
#     i = i + 1;
# EndWhile.
# EndBody.
#         """
#         expect = "01234"
#         self.assertTrue(TestCodeGen.test(input,expect,554))

#     def test_break_while_2(self):
#         input = """
# Var: i = 0, j = 0;
# Function: main
# Body:
# Var: a[2][2] = {{1,2}, {3,4}};
# While i < 2 Do
#     While j < 2 Do
#         print(string_of_int(a[i][j]));
#         j = j + 1;
#     EndWhile.
#     If i == 1 Then
#         Break;
#     EndIf.
#     i = i + 1;
# EndWhile.
# EndBody.
#         """
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input,expect,555))


#     def test_continue_1(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {"a", "b", "c"}, i = 0;
# For( i = 0, i < 3, 1 ) Do
#     If i == 1 Then
#         Continue;
#     EndIf.
#     print(a[i]);
# EndFor.
# EndBody.
#         """
#         expect = "ac"
#         self.assertTrue(TestCodeGen.test(input,expect,556))

#     def test_continue_2(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {"a", "b", "c"}, i = 0;
# While i < 3 Do
#     If i == 1 Then
#         i = i + 1;
#         Continue;
#     Else
#         print(a[i]);
#         i = i + 1;
#     EndIf.
# EndWhile.
# EndBody.
#         """
#         expect = "ac"
#         self.assertTrue(TestCodeGen.test(input,expect,557))

#     def test_continue_3(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {"a", "b", "c"}, i = 0;
# Do
#     If i == 1 Then
#         i = i + 1;
#         Continue;
#     Else
#         print(a[i]);
#         i = i + 1;
#     EndIf.
# While i < 3
# EndDo.
# EndBody.
#         """
#         expect = "ac"
#         self.assertTrue(TestCodeGen.test(input,expect,558))

#     def test_binary_logical_1(self):
#         input = """
# Function: main
# Body:
# print(string_of_bool((3 < 4) && (3.0 <. 4.0)));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,559))

#     def test_binary_logical_2(self):
#         input = """
# Var: b = 3, c = 4;
# Function: main
# Body:
# print(string_of_bool(b == c));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,560))

#     def test_binary_logical__2(self):
#         input = """
# Var: b = 3, c = 4;
# Function: main
# Body:
# print(string_of_bool(b != c));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,561))

#     def test_binary_logical_3(self):
#         input = """
# Var: b = 3, c = 4;
# Function: main
# Body:
# print(string_of_bool(b <= c));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,562))

#     def test_binary_logical_4(self):
#         input = """
# Var: b = 3, c = 4;
# Function: main
# Body:
# print(string_of_bool(b >= c));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,563))

#     def test_binary_logical_5(self):
#         input = """
# Var: b = 3, c = 4;
# Function: main
# Body:
# print(string_of_bool(b > c));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,564))

#     def test_binary_logical_6(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool(b >. c));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,565))

#     def test_binary_logical_7(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool(b >=. c));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,566))

#     def test_binary_logical_8(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool(b <=. c));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,567))

#     def test_binary_logical_9(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool(b =/= c));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,568))

#     def test_binary_logical_10(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool((b =/= c) || (b <=. c) || (b <. c)));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,569))

#     def test_binary_logical_11(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool((b =/= c) && (b <=. c) && (b <. c)));
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,570))  

#     def test_not(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool(!(b =/= c)));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,571))  

#     def test_not_1(self):
#         input = """
# Var: b = 3.0, c = 4.0;
# Function: main
# Body:
# print(string_of_bool(!(b =/= c) || False));
# EndBody.
#         """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,572))  

#     def test_multiple_para(self):
#         input = """
# Function: main
# Body:
# Var: a = 5, b = 6;
# print(string_of_bool(isSmaller(a,b)));
# EndBody.

# Function: isSmaller
# Parameter: a, b
# Body:
#     Return a < b;
# EndBody.
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,573))

#     def test_array_cell_1(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {1,2,3};
# a[2] = 5;
# print(string_of_int(a[2]));
# EndBody.

#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,574))  

#     def test_array_cell_2(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {1,2,3};
# a[2] = 5;
# a[1] = a[2];
# print(string_of_int(a[1]));
# EndBody.

#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,575)) 

#     def test_array_cell_3(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {1,2,3};
# a[1] = a[1] * a[1];
# print(string_of_int(a[1]));
# EndBody.
#         """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,576))

#     def test_array_cell_4(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {1,2,3};
# a[2] = 5;
# a[1*1+0] = a[2] * a[1] * a[1];
# print(string_of_int(a[1]));
# EndBody.

#         """
#         expect = "20"
#         self.assertTrue(TestCodeGen.test(input,expect,577))

#     def test_do_while_3(self):
#         input = """
# Function: main
# Body:
# Var: a = 0, iSum = 0;
# Do 
#     a = a + 1;
#     If a % 2 == 0 Then
#         Continue;
#     EndIf.
#     iSum = iSum + a;
# While a < 20
# EndDo.
# print(string_of_int(iSum));
# EndBody.
#         """
#         expect = "100"
#         self.assertTrue(TestCodeGen.test(input,expect,578))

#     def test_return_in_for_4(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(foo()));
# EndBody.

# Function: foo
# Body:
# Var: i = 0;
# For(i = 0, i<3, 1) Do
#     If i == 2 Then
#         Return i;
#     EndIf.
# EndFor.
# Return 5;
# EndBody.
#         """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,579))

#     def test_return_in_if(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(foo()));
# EndBody.

# Function: foo
# Body:
# Var: i = 5;
# If i == 2 Then
#     Return i;
# EndIf.
# Return 4;
# EndBody.
#         """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,580))

#     def test_func_expr_1(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(foo() + foo1()));
# EndBody.

# Function: foo
# Body:
# Var: i = 5;
# If i == 2 Then
#     Return i;
# EndIf.
# Return 4;
# EndBody.

# Function: foo1
# Body:
# Return 6;
# EndBody.
#         """
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,581))

#     def test_nested_func_expr_1(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(incr(3)));
# EndBody.

# Function: incr
# Parameter: a
# Body:
# Return a + 1;
# EndBody.
#         """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,582))

#     def test_nested_func_expr_2(self):
#         input = """
# Function: main
# Body:
# Var: a[3] = {1,2,3};
# a = incrArr(a,3);
# EndBody.

# Function: incrArr
# Parameter: a,size
# Body:
# Var: i = 0;
# For( i = 0, i < size, 1 ) Do
#     a[i] = a[i] + 1;
# EndFor.
# Return a;
# EndBody.
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,583))

#     def test_nested_func_expr_3(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(double(incr(3))));
# EndBody.

# Function: incr
# Parameter: a
# Body:
# Return a + 1;
# EndBody.

# Function: double
# Parameter: a
# Body:
# Return 2*a;
# EndBody.
#         """
#         expect = "8"
#         self.assertTrue(TestCodeGen.test(input,expect,584))


#     def test_nested_func_expr_4(self):
#         input = """
# Function: main
# Body:
# print(string_of_int(square(double(incr(3)))));
# EndBody.

# Function: incr
# Parameter: a
# Body:
# Return a + 1;
# EndBody.

# Function: double
# Parameter: a
# Body:
# Return 2*a;
# EndBody.

# Function: square
# Parameter: a
# Body:
# Return a*a;
# EndBody.
#         """
#         expect = "64"
#         self.assertTrue(TestCodeGen.test(input,expect,585))
