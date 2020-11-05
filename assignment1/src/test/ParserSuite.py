# Student ID: 1852348
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Function: main\n\tBody:\n\t\tVar: x;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    # -------- test variable declaration -------------
    def test_declare_with_initial_1(self):
        input = """Function: main\n\tBody:\n\t\tVar: x = 1;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_declare_multiple_var(self):
        input = """Function: main\n\tBody:\n\t\tVar: c, d, e, f;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_declare_multiple_with_initial(self):
        input = """Function: main\n\tBody:\n\t\tVar: c, d = 6, e, f=7;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_declare_multiple_with_initial_types(self):
        input = """Function: main\n\tBody:\n\t\tVar: c = True, d = "string", e=0.9, f=7;\n\tEndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    # ------------error variable declare cases-------
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Function: main\n\tBody:\n\t\tVar: ;\n\tEndBody."""
        expect = "Error on line 3 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_declare_without_semi(self):
        input = """Function: main\n\tBody:\n\t\tVar: c\n\tEndBody."""
        expect = "Error on line 4 col 1: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_declare_without_var(self):
        input = """Function: main\n\tBody:\n\t\t c\n\tEndBody."""
        expect = "Error on line 4 col 1: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_var_declare_without_comma(self):
        input = """Function: main\n\tBody:\n\t\tVar: c d = 6, e, f\n\tEndBody."""
        expect = "Error on line 3 col 9: d"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_var_declare_without_colon(self):
        input = """Function: main\n\tBody:\n\t\tVar c d = 6, e, f\n\tEndBody."""
        expect = "Error on line 3 col 6: c"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_array_declare_1(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[5];\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_array_declare_2(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[5][4];\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_array_declare_with_initial_1(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[5] = {1,4,3,2,0};\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_array_declare_with_initial_2(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2][3]={{1,2,3},{4,5,6}};\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_mix_composite_scale_var(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2][3], m, n;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_mix_composite_scale_var_with_init(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2] = {1,2}, m=6, n="string";\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_error_declare_array_1(self):
        """mising close square bracket"""
        input = """Function: main\n\tBody:\n\t\tVar: b[2, m, n;\n\tEndBody."""
        expect = "Error on line 3 col 10: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_declare_array_with_wrong_initial(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2] = {2, "String"}, m, n;\n\tEndBody."""
        expect = "Error on line 3 col 18: String"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_error_declare_array_2(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2[3] = {2, "String"}, m, n;\n\tEndBody."""
        expect = "Error on line 3 col 10: ["
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_error_declare_array_3(self):
        input = """Function: main\n\tBody:\n\t\tVar: A[2][3], n;\n\tEndBody."""
        expect = "A"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_error_declare_array_4(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[][3], m, n;\n\tEndBody."""
        expect = "Error on line 3 col 9: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    # --------------expression----------------------
    # test ary of operator
    def test_error_ary_1(self):
        input = """Function: main\n\tBody:\n\t\ta = a!;\n\tEndBody."""
        expect = "Error on line 3 col 7: !"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_error_ary_2(self):
        input = """Function: main\n\tBody:\n\t\ta = *;\n\tEndBody."""
        expect = "Error on line 3 col 6: *"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_error_ary_3(self):
        input = """Function: main\n\tBody:\n\t\tb = b[3]b;\n\tEndBody."""
        expect = "Error on line 3 col 10: b"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_error_ary_4(self):
        input = """Function: main\n\tBody:\n\t\tb = b-;\n\tEndBody."""
        expect = "Error on line 3 col 8: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_error_ary_5(self):
        input = """Function: main\n\tBody:\n\t\tb!=;\n\tEndBody."""
        expect = "Error on line 3 col 3: !="
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_ary_1(self):
        input = """Function: main\n\tBody:\n\t\ta = a != a + b * c + (a\\b) + !h;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_ary_2(self):
        input = """Function: main\n\tBody:\n\t\tc = (a != b); c = a == b;d = a < b;d = a > b;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    # test association of operators
    def test_assoc_1(self):
        input = """Function: main\n\tBody:\n\t\ta = 1 + 2 + (3*4); \n\t\tc = 1 * 3 * 4;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_wrong_assoc_1(self):
        input = """Function: main\n\tBody:\n\t\tk = (a == c == d);\n\tEndBody."""
        expect = "Error on line 3 col 14: =="
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_wrong_assoc_2(self):
        input = """Function: main\n\tBody:\n\t\tk = a < c < d\n\tEndBody."""
        expect = "Error on line 3 col 12: <"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_wrong_assoc_3(self):
        input = """Function: main\n\tBody:\n\t\tk = a <. c <. d;\n\tEndBody."""
        expect = "Error on line 3 col 13: <."
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    # test parentheses
    def test_parentheses_expression_1(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\tk = (a <. c) <. d;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_parentheses_expression_2(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\tk = (a == c) == (k == h);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_nested_parentheses_expression(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\tk = (a == c) == ((k == h) == (y == t));\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_parentheses_expression_with_error(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\tk = (a == c) == (k == h) == (y == t);\n\tEndBody."""
        expect = "Error on line 3 col 27: =="
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_parentheses__with_error(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\tk = (a == c == (k == h) == (y == t);\n\tEndBody."""
        expect = "Error on line 3 col 14: =="
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    # test expression function call
    def test_function_call(self):
        input = """Function: main\n\tBody:\n\t\ta = foo();\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_function_call_with_single_argument(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\ta = foo(5);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_function_call_with_multiple_arguments(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\ta = foo(5,"string", True);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_function_call_with_expression_arguments(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\ta = foo(5 + 4 * 3 \ 5,"string", True);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_function_call_with_expression_arguments_1(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\ta = foo((5 + 4) * (3 \ 5),"string", True);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_function_call_with_other_operators(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\ta = foo(True) * incr(5) + decr(6);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_nested_function_call(self):
        """This should raise no error"""
        input = """Function: main\n\tBody:\n\t\ta = foo(True,incr(5), incr(6));\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_function_call_with_error(self):
        input = """Function: main\n\tBody:\n\t\ta = foo(True,incr(5), incr(6);\n\tEndBody."""
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_function_call_with_error_2(self):
        input = """Function: main\n\tBody:\n\t\ta = foo(True;incr(5), incr(6));\n\tEndBody."""
        expect = "Error on line 3 col 14: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    # test index operator
    def test_idx_operator_expression(self):
        input = """Function: main\n\tBody:\n\t\ta[3] = 4*5 + foo(3);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_idx_operator_expression_1(self):
        input = """Function: main\n\tBody:\n\t\tc = a[b[2]] + 4;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_idx_operator_expression_2(self):
        input = """Function: main\n\tBody:\n\t\tc = a[foo(3)] + 4;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_idx_operator_expression_3(self):
        input = """Function: main\n\tBody:\n\t\tc = a[(4*3) + 5 + foo("string")] + 4;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_idx_operator_expression_4(self):
        input = """Function: main\n\tBody:\n\t\tc = a[8][6][9] + 4;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    # ----------------function declaration------------------
    # test fucntion declaration Parameter part
    def test_normal_function_declaration_1(self):
        input = """Function: foo
Parameter: a[5], c
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_normal_multiple_function_declarations(self):
        input = """Function: foo
Parameter: a[5], c, b[6][7]
Body:
EndBody.

Function: foo1
Parameter: a[5], c, b[6][7], d
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_function_decl_empty_para_errors(self):
        input = """Function: foo
Parameter:
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = "Error on line 3 col 0: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_function_decl_para_separator_errors(self):
        input = """Function: foo
Parameter: a[5]; c
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_function_decl_para_with_initial_errors(self):
        input = """Function: foo
Parameter: a[5], c = 0
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = "Error on line 2 col 19: ="
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_function_decl_without_parameters(self):
        input = """Function: foo
Body:
EndBody.

Function: main
Body:
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    # ----------- test function body part ------------
    def test_function_decl_without_body(self):
        input = """Function: foo
Parameter: x, y, z
x = 5;

Function: main
Body:
EndBody."""
        expect = "Error on line 3 col 0: x"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_function_decl_without_body_closing(self):
        input = """Function: foo
Parameter: x, y, z
Body:
    x = 5;

Function: main
Body:
EndBody."""
        expect = "Error on line 6 col 0: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_function_decl_without_identifier(self):
        input = """Function:
Parameter: x, y, z
Body:
    x = 5;
Endbody.

Function: main
Body:
EndBody."""
        expect = "Error on line 2 col 0: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_function_normal_body(self):
        input = """Function: foo
Parameter: y
Body:
    Var: x, sum = 0;
    x = x + 1;
EndBody.

Function: main
Body:
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_function_error_body(self):
        input = """Function: foo
Parameter: y
Body:
    x = 5;
    Var: x, sum = 0;
    x = x + 1;
    While (x < 10) Do
        sum = sum + x;
    EndWhile.
EndBody.

Function: main
Body:
EndBody."""
        expect = "Error on line 5 col 4: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_nested_function_declaration_error(self):
        input = """Function: foo
Parameter: y
Body:
    Var: x, sum = 0;
    x = x + 1;
    Function: fooIn
    Parameter: y
    Body:
    EndBody.
EndBody.

Function: main
Body:
EndBody."""
        expect = "Error on line 6 col 4: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    # ----------- test statements---------------------
    # ----------- while statement ----------

    def test_normal_while_stmt(self):
        input = """Function: main
Body:
    While (x < 10) Do
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_normal_nested_while_stmt(self):
        input = """Function: main
Body:
    While (x < 10) Do
        sum = sum + x;
        While( z > 10 ) Do
            z = z - 1;
        EndWhile.
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_complex_condition_while_stmt(self):
        input = """Function: main
Body:
    While (x < 10) && (x != 0) Do
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_while_stmt_syntax_error_1(self):
        input = """Function: main
Body:
    While (x < 10)
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = "Error on line 3 col 4: While"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_while_stmt_syntax_error_2(self):
        input = """Function: main
Body:
    While (x < 10) Do
        sum = sum + x;
    
EndBody."""
        expect = "Error on line 6 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_nested_while_stmt_syntax_error_2(self):
        input = """Function: main
Body:
    While (x < 10) Do
        sum = sum + x;
        While ( z > 10 ) Do
            z = z - 1;
    EndWhile.
    
EndBody."""
        expect = "Error on line 9 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    # ------------if stmt----------------
    def test_if_stmt(self):
        input = """Function: main
Body:
    Var: x, sum;
    If (x < 10) Then
    ElseIf (x % 2) == 0 Then sum = sum + x;
    Else sum = sum - x;
    EndIf.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_nested_if_stmt(self):
        input = """Function: main
Body:
    Var: x, sum;
    If (x < 10) Then
    ElseIf (x % 2) == 0 Then If(sum < 0) Then sum = 0; EndIf.
    Else sum = sum - x;
    EndIf.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_if_stmt_error(self):
        input = """Function: main
Body:
    Var: x, sum;
    If (x < 10) Then
    ElseIf (x % 2) == 0 Then If(sum < 0) Then sum = 0; EndIf.
    Else sum = sum - x;
    
    
EndBody."""
        expect = "Error on line 9 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_if_stmt_with_many_elseif(self):
        input = """Function: main
Body:
    Var: x, sum;
    If (x < 10) Then
    ElseIf (x % 2) == 0 Then If(sum < 0) Then sum = 0; EndIf.
    ElseIf (x % 3) == 0 Then If(sum < 0) Then sum = 1; EndIf.
    ElseIf (x % 4) == 0 Then If(sum < 0) Then sum = 2; EndIf.
    Else sum = sum - x;
    EndIf.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    # ------------for stmt----------------
    def test_for_stmt(self):
        input = """Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_nested_for_stmt(self):
        input = """Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
        EndFor.
    EndFor.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_nested_for_stmt_complex_arg(self):
        input = """Function: main
Body:
    Var: i;
    For (i = 1, (i < 10) && (i % 2 == 0), 2*3) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_for_error_1(self):
        input = """Function: main
Body:
    Var: i;
    For (i = 1, (i < 10) && (i % 2 == 0), 2*3)
        printLn(i);
    EndFor.
    
EndBody."""
        expect = "Error on line 5 col 8: printLn"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_for_error_without_condition(self):
        input = """Function: main
Body:
    Var: i;
    For (i = 1, 2*3) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = "Error on line 4 col 19: )"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_nested_for_error(self):
        input = """Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
    EndFor.
    
EndBody."""
        expect = "Error on line 9 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    # ------------do while stmt----------------
    def test_dowhile_stmt(self):
        input = """Function: main
Body:
    Var: i;
    Do
        i = i + 1;
    While i < 20
    EndDo.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_nested_dowhile_stmt(self):
        input = """Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
        Do
            j = j - 1;
        While j > 0
        EndDo.
    While i < 20
    EndDo.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_nested_while_in_dowhile_stmt(self):
        input = """Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
        While j > 0 Do
            j = j - 1;
        EndWhile.
    While i < 20
    EndDo.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_dowhile_error(self):
        input = """Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
    While i < 20 Do
        i = i + 1;
    EndWhile.
    EndDo.
    
EndBody."""
        expect = "Error on line 9 col 4: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    # -----break statement------
    def test_break_stmt(self):
        input = """Function: main
Body:
    Var: i;
    Do
        i = i + 1;
        If ( i == 10 ) Then Break; EndIf.
    While i < 20
    EndDo.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    # -----continue statement------
    def test_continue_stmt(self):
        input = """Function: main
Body:
    Var: i;
    
    For (i = 0, i < 10, 1) Do
        If i % 2 == 0 Then Continue; EndIf.
    EndFor.
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    # ------assign statement --------
    def test_assign_stmt(self):
        input = """Function: main
Body:
    Var: i;
    v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_assign_error_1(self):
        input = """Function: main
Body:
    Var: i,j;
    i = j = 5;
EndBody."""
        expect = "Error on line 4 col 10: ="
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_assign_error_2(self):
        input = """Function: main
Body:
    Var: i,j;
    i = 6
EndBody."""
        expect = "Error on line 5 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    # ------return statement----------
    def test_simple_return_stmt(self):
        input = """Function: double
Parameter: a
Body:
    Return 2*a;
EndBody.

Function: main
Body:
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_return_stmt(self):
        input = """Var: x;
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_return_stmt_without_expr(self):
        input = """Function: foo
Parameter: a
Body:
    Return;
EndBody.

Function: main
Body:
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    # -----------test mixing statements-----------
    def test_mix_stmt_1(self):
        input = """Function: main
Body:
    Var: arr[2][3] = {{2,3,5},{6,7,8}};
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            printLn(arr[i][j]);
            sum = sum + arr[i][j];
        EndFor.
        i = i + 1;
    EndWhile.
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_mix_stmt_2(self):
        input = """Function: main
Body:
    Var: arrA[2][3] = {{2,3,5},{6,7,8}};
    Var: arrB[2][3] = {{2,3,5},{6,7,8}};
    Var: isEqual = True;
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            If((arrA[i][j]) != (arrB[i][j])) Then
                isEqual = False;
                Break;
            EndIf.
        EndFor.
        i = i + 1;
    EndWhile.
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_mix_stmt_error(self):
        input = """Function: main
Body:
    Var: arr[2][3] = {{2,3,5},{6,7,8}};
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            printLn(arr[i][j]);
            sum = sum + arr[i][j];
        EndWhile.
        i = i + 1;
    EndFor.
EndBody.
"""
        expect = "Error on line 9 col 8: EndWhile"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    # -----------test complex program------------

    def test_complex_program_1(self):
        input = """** Gobal variable declaration **
Var: a,b,c;
** Function declaration **
Function: printArray
Parameter: a, size
Body:
    ** Local variable declaration **
    Var: i;
    For (i = 0, i < size, 1) Do
        printLn(a[i]);
    EndFor.
EndBody.

Function: main
Body:
    Var: a[5] = {5,6,7,8,9};
    printArray(a,5);
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_complex_program_without_main_error(self):
        input = """** Gobal variable declaration **
Var: a,b,c;
** Function declaration **
Function: printArray
Parameter: a, size
Body:
    ** Local variable declaration **
    Var: i;
    For (i = 0, i < size, 1) Do
        printLn(a[i]);
    EndFor.
EndBody.
"""
        expect = "Error on line 13 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    # error when global declare after function declare
    def test_complex_program_global_declare(self):
        input = """** Function declaration **
Function: printArray
Parameter: a, size
Body:
    ** Local variable declaration **
    Var: i;
    For (i = 0, i < size, 1) Do
        printLn(a[i]);
    EndFor.
EndBody.

** Gobal variable declaration **
Var: a,b,c;

Function: main
Body:
    Var: a[5] = {5,6,7,8,9};
    printArray(a,5);
EndBody.
"""
        expect = "Error on line 13 col 0: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    # detect error when initial value is not a literal but expression
    def test_complex_program_2_error(self):
        input = """Function: binarySearch
Parameter: arr[10], l, r, x 
Body:
    If (r >= l) Then
        Var: mid = l + (r - l) \ 2;
        ** If the element is present at the middle 
         itself **
        If ((arr[mid]) == x) Then
            Return mid;
        EndIf.
  
        ** If element is smaller than mid, then 
        it can only be present in left subarray **
        If ((arr[mid]) > x) Then
            Return binarySearch(arr, l, mid - 1, x); 
        EndIf.

        ** Else the element can only be present 
        in right subarray **
        Return binarySearch(arr, mid + 1, r, x); 
    EndIf.
  
    ** We reach here when element is not 
    present in array **
    Return -1; 
EndBody.
  
Function: main
Body:
    Var: arr[5] = { 2, 3, 4, 10, 40 }; 
    Var: x = 10; 
    Var: n , result;
    n = sizeof(arr) \ sizeof(arr[0]); 
    result = binarySearch(arr, 0, n - 1, x);
    If (result == -1) Then 
        printLn("Element is not present in array");
    Else
        printLn("Element is present at index: ");
        printLn(result); 
    EndIf.
EndBody.
"""
        expect = "Error on line 5 col 19: l"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    # detect an if statement is not closed using EndIf.
    def test_complex_program_2_error_1(self):
        input = """Function: binarySearch
Parameter: arr[10], l, r, x 
Body:
    If (r >= l) Then
        Var: mid;
        mid = l + (r - l) \ 2;
        ** If the element is present at the middle 
         itself **
        If ((arr[mid]) == x) Then
            Return mid;
        ** not closing here **
  
        ** If element is smaller than mid, then 
        it can only be present in left subarray **
        If ((arr[mid]) > x) Then
            Return binarySearch(arr, l, mid - 1, x); 
        EndIf.

        ** Else the element can only be present 
        in right subarray **
        Return binarySearch(arr, mid + 1, r, x); 
    EndIf.
  
    ** We reach here when element is not 
    present in array **
    Return -1; 
EndBody.
  
Function: main
Body:
    Var: arr[5] = { 2, 3, 4, 10, 40 }; 
    Var: x = 10; 
    Var: n , result;
    n = sizeof(arr) \ sizeof(arr[0]); 
    result = binarySearch(arr, 0, n - 1, x);
    If (result == -1) Then 
        printLn("Element is not present in array");
    Else
        printLn("Element is present at index: ");
        printLn(result); 
    EndIf.
EndBody.
"""
        expect = "Error on line 27 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_complex_program_2_without_error(self):
        input = """Function: binarySearch
Parameter: arr[10], l, r, x 
Body:
    If (r >= l) Then
        Var: mid;
        mid = l + (r - l) \ 2;
        ** If the element is present at the middle 
         itself **
        If ((arr[mid]) == x) Then
            Return mid;
        EndIf.
  
        ** If element is smaller than mid, then 
        it can only be present in left subarray **
        If ((arr[mid]) > x) Then
            Return binarySearch(arr, l, mid - 1, x); 
        EndIf.

        ** Else the element can only be present 
        in right subarray **
        Return binarySearch(arr, mid + 1, r, x); 
    EndIf.
  
    ** We reach here when element is not 
    present in array **
    Return -1; 
EndBody.
  
Function: main
Body:
    Var: arr[5] = { 2, 3, 4, 10, 40 }; 
    Var: x = 10; 
    Var: n , result;
    n = sizeof(arr) \ sizeof(arr[0]); 
    result = binarySearch(arr, 0, n - 1, x);
    If (result == -1) Then 
        printLn("Element is not present in array");
    Else
        printLn("Element is present at index: ");
        printLn(result); 
    EndIf.
EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    # ------test array -------


    def test_array_1(self):
        input = """Function: main
Body:
    a[3] = {True, False, True};
    b[3] = {567, 0x567, 0O345};
    c[3] = {{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}};
    d[3] = {5.6,5E-10,6.03};

EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))
    
    def test_array_error_2(self):
        input = """Function: main
Body:
    a[3] = {True,{"True"},{"True", "False"}};
EndBody.
"""
        expect = "Error on line 3 col 17: {"
        self.assertTrue(TestParser.checkParser(input, expect, 302))
    
    def test_array_error_3(self):
        input = """Function: main
Body:
    a[3] = {5.6,"TRUE",6.03};
EndBody.
"""
        expect = "Error on line 3 col 16: TRUE"
        self.assertTrue(TestParser.checkParser(input, expect, 303))