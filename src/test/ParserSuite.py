import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Function: main\n\tBody:\n\t\tVar: x;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

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

    # error variable declare cases
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

    def test_declare_without_comma(self):
        input = """Function: main\n\tBody:\n\t\tVar: c d = 6, e, f\n\tEndBody."""
        expect = "Error on line 3 col 9: d"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_declare_without_colon(self):
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
        expect = "Error on line 3 col 14: {"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_error_declare_array_2(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2[3] = {2, "String"}, m, n;\n\tEndBody."""
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_error_declare_array_3(self):
        input = """Function: main\n\tBody:\n\t\tVar: A[2][3], n;\n\tEndBody."""
        expect = "A"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_error_declare_array_4(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[][3], m, n;\n\tEndBody."""
        expect = "Error on line 3 col 9: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    # test ary of operator
    def test_error_ary_1(self):
        input = """Function: main\n\tBody:\n\t\ta = a!b;\n\tEndBody."""
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
        expect = "Error on line 2 col 0: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

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
    # test function declaration Body part variable declare

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

    def test_nested_function_error(self):
        input = """Function: foo
Parameter: y
Body:
    Var: x, sum = 0;
    x = x + 1;
    While (x < 10) Do
        sum = sum + x;
    EndWhile.
    Function: fooInside
    Parameter: y
    Body:
    EndBody.
EndBody.

Function: main
Body:
EndBody."""
        expect = "Error on line 9 col 4: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
