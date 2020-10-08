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

    def test_illegal_escape_1(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_illegal_escape_2(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\\k\\m"  """, """Illegal Escape In String: \\k""", 126))

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
            """0xz""", """Error Token 0xz""", 116))

    def test_oct_interger_with_error(self):
        self.assertTrue(TestLexer.checkLexeme(
            """0o89""", """Error Token 0o89""", 117))

    # test array
    def test_normal_array_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5, 6, 7}""", """{5, 6, 7},<EOF>""", 118))

    def test_normal_array_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ {{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}} """, """{{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}},<EOF>""", 119))

    def test_normal_array_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5.6,5E-10,6.03}""", """{5.6,5E-10,6.03},<EOF>""", 120))

    def test_empty_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{,}""", """{,}""", 125))

    def test_error_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5.6,TRUE,6.03}""", """{,5.6,,,Error Token T""", 121))

    # test comment
    def test_normal_single_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""**This line will be ignore**9990""",
                                              """9990,<EOF>""", 122))

    def test_normal_block_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""**This line will be ignore\n*This is a\n* multi-line\n* comment.**"somestring" """,
                                              """somestring,<EOF>""", 123))

    def test_unclosed_comment(self):
        self.assertTrue(TestLexer.checkLexeme("""**This line will be ignore9990""",
                                              """Unterminated Comment""", 124))

    def test_unclosed_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("""** ***""",
                                              """Unterminated Comment""", 125))
