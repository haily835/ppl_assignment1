import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_normal_string(self):
        """test normal string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abdef"  """, """abdef,<EOF>""", 108))

    def test_hex_interger_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0xFF""", """0xFF,<EOF>""", 109))

    def test_hex_interger_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0XABC""", """0XABC,<EOF>""", 110))

    def test_dec_interger_1(self):
        self.assertTrue(TestLexer.checkLexeme("""0""", """0,<EOF>""", 111))

    def test_dec_interger_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """9991""", """9991,<EOF>""", 112))

    def test_oct_interger_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0o567""", """0o567,<EOF>""", 113))

    def test_oct_interger_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0O77""", """0O77,<EOF>""", 114))

    # errors for interger literal
    def test_dec_interger_with_error(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0567""", """Error Token 0""", 115))

    # catch error of ID first
    def test_hex_interger_with_error(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0xz""", """Error Token 0""", 116))

    def test_oct_interger_with_error(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0o89""", """Error Token 0""", 117))
