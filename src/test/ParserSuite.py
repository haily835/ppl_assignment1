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

    def test_declare_without_colon(self):
        input = """Function: main\n\tBody:\n\t\tVar: c d = 6, e, f\n\tEndBody."""
        expect = "Error on line 3 col 9: d"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_array_declare_1(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[5];\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_array_declare_2(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[5][4];\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_array_declare_with_initial_1(self):
        input = """Function: main\n\tBody:\n\t\tVar: a[5] = {1,4,3,2,0};\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_array_declare_with_initial_2(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2][3]={{1,2,3},{4,5,6}};\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_mix_composite_scale_var(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2][3], m, n;\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_mix_composite_scale_var_with_init(self):
        input = """Function: main\n\tBody:\n\t\tVar: b[2] = {1,2}, m=6, n="string";\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_error_declare_array_1(self):
        """mising close square bracket"""
        input = """Function: main\n\tBody:\n\t\tVar: b[2, m, n;\n\tEndBody."""
        expect = "Error on line 3 col 10: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_stmt_expression(self):
        input = """Function: main\n\tBody:\n\t\ta[3] = 4*5 + foo(3);\n\tEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
