import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # ---------- test identifiers ----------------
    def test_lower_identifier_101(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_identifier_102(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a_102", "a_102,<EOF>", 102))

    def test_lower_identifier_103(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aA_", "aA_,<EOF>", 103))

    def test_lower_identifier_104(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("z", "z,<EOF>", 104))

    def test_lower_identifier_105(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("zA_102", "zA_102,<EOF>", 105))

    # test keywords
    def test_lower_upper_id_106(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 106))

    def test_lower_upper_id_107(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Function Parameter Body EndBody", "Function,Parameter,Body,EndBody,<EOF>", 107))

    def test_lower_upper_id_108(self):
        self.assertTrue(TestLexer.checkLexeme(
            "While (x != 0 ) Do x = x - 1 EndWhile.", "While,(,x,!=,0,),Do,x,=,x,-,1,EndWhile,.,<EOF>", 108))

    def test_lower_upper_id_109(self):
        self.assertTrue(TestLexer.checkLexeme(
            "For Do EndFor", "For,Do,EndFor,<EOF>", 109))

    def test_lower_upper_id_110(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Do While EndDo", "Do,While,EndDo,<EOF>", 110))

    def test_lower_upper_id_111(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Return Break Continue", "Return,Break,Continue,<EOF>", 111))

    def test_lower_upper_id_112(self):
        self.assertTrue(TestLexer.checkLexeme(
            "If ElseIf Else EndIf", "If,ElseIf,Else,EndIf,<EOF>", 112))

    def test_lower_upper_id_113(self):
        self.assertTrue(TestLexer.checkLexeme(
            "True False", "True,False,<EOF>", 113))

    # -----------test keywords uppercase error---------

    def test_wrong_keyword_token_114(self):
        self.assertTrue(TestLexer.checkLexeme(
            "FuNction", "Error Token F", 114))

    def test_wrong_keyword_token_115(self):
        self.assertTrue(TestLexer.checkLexeme(
            "WhiLe", "Error Token W", 115))

    def test_wrong_keyword_token_116(self):
        self.assertTrue(TestLexer.checkLexeme(
            "EndWhILE", "Error Token E", 116))

    def test_wrong_keyword_token_117(self):
        self.assertTrue(TestLexer.checkLexeme(
            "FOR", "Error Token F", 117))

    def test_wrong_keyword_token_118(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ENDfor", "Error Token E", 118))

    def test_wrong_keyword_token_119(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ReTuRN", "Error Token R", 119))

    def test_wrong_keyword_token_120(self):
        self.assertTrue(TestLexer.checkLexeme(
            "BREAk", "Error Token B", 120))

    # -----------test operators----------
    def test_operator_121(self):
        self.assertTrue(TestLexer.checkLexeme(
            "+ +. - -. * *. \\ \\. %", "+,+.,-,-.,*,*.,\,\.,%,<EOF>", 121))

    def test_operator_122(self):
        self.assertTrue(TestLexer.checkLexeme(
            "! && || == !=", "!,&&,||,==,!=,<EOF>", 122))

    def test_operator_123(self):
        self.assertTrue(TestLexer.checkLexeme(
            "< > <= >= >. <. >=. <=. ", "<,>,<=,>=,>.,<.,>=.,<=.,<EOF>", 123))

    # -----------test separators--------
    def test_separator_124(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{{(()())}}}}", "{,{,{,(,(,),(,),),},},},},<EOF>", 124))

    def test_separator_125(self):
        self.assertTrue(TestLexer.checkLexeme(
            "[[[]]]] {{{{}}}}", "[,[,[,],],],],{,{,{,{,},},},},<EOF>", 125))

    def test_separator_126(self):
        self.assertTrue(TestLexer.checkLexeme(
            ".,...,..;:::::,", ".,,,.,.,.,,,.,.,;,:,:,:,:,:,,,<EOF>", 126))

    # --------test error character oken--------
    def test_wrong_token_127(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 127))

    def test_wrong_token_128(self):
        self.assertTrue(TestLexer.checkLexeme(
            "aA@", "aA,Error Token @", 128))

    def test_wrong_token_129(self):
        self.assertTrue(TestLexer.checkLexeme(
            "#include", "Error Token #", 129))

    def test_wrong_token_130(self):
        self.assertTrue(TestLexer.checkLexeme(
            "abc$1000", "abc,Error Token $", 130))

    def test_wrong_token_131(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{`abc$1000`", "{,Error Token `", 131))

    def test_wrong_token_132(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: i = a*2^10", "Var,:,i,=,a,*,2,Error Token ^", 132))

    def test_wrong_token_133(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: a = ~a;", "Var,:,a,=,Error Token ~", 133))

    # ---------test int literals------------
    def test_int_dec_literal_134(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: k = +5556", "Var,:,k,=,+5556,<EOF>", 134))

    def test_int_dec_literal_135(self):
        self.assertTrue(TestLexer.checkLexeme(
            "-5556", "-5556,<EOF>", 135))

    def test_int_dec_literal_136(self):
        self.assertTrue(TestLexer.checkLexeme(
            "000", "000,<EOF>", 136))

    def test_int_hex_literal_137(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0xFF", "0xFF,<EOF>", 137))

    def test_int_hex_literal_138(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0XABC", "0XABC,<EOF>", 138))

    def test_int_hex_literal_139(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0X12ABC", "0X12ABC,<EOF>", 139))

    def test_int_hex_literal_140(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0X11333", "0X11333,<EOF>", 140))

    def test_int_hex_literal_error_141(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0XAaBb", "Error Token 0XAa", 141))

    def test_int_hex_literal_error_142(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0X1a2b", "Error Token 0X1a", 142))

    def test_int_hex_literal_error_143(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0x1a2b", "Error Token 0x1a", 143))

    def test_int_hex_literal_error_144(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0xZBZZZ", "Error Token 0xZ", 144))

    def test_int_oct_literal_145(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o567", "0o567,<EOF>", 145))

    def test_int_oct_literal_146(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0O124", "0O124,<EOF>", 146))

    def test_int_oct_literal_error_147(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o589", "Error Token 0o589", 147))

    def test_int_oct_literal_error_148(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o5aa", "Error Token 0o5aa", 148))

    def test_int_oct_literal_error_149(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0oAB5", "Error Token 0oAB", 149))

    # def test_integer_104(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    # def test_illegal_escape_105(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    # def test_illegal_escape_106(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "\\k\\m"  """, """Illegal Escape In String: \\k""", 126))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "abc def  """, """Unclosed String: abc def  """, 106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    # def test_normal_string(self):
    #     """test normal string"""
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ "abdef"  """, """abdef,<EOF>""", 108))

    # def test_hex_interger_1(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0xFF""", """0xFF,<EOF>""", 109))

    # def test_hex_interger_2(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0XABC""", """0XABC,<EOF>""", 110))

    # def test_dec_interger_1(self):
    #     self.assertTrue(TestLexer.checkLexeme("""0""", """0,<EOF>""", 111))

    # def test_dec_interger_2(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """9991""", """9991,<EOF>""", 112))

    # def test_oct_interger_1(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0o567""", """0o567,<EOF>""", 113))

    # def test_oct_interger_2(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0O77""", """0O77,<EOF>""", 114))

    # # errors for interger literal
    # def test_dec_interger_with_error(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0567""", """Error Token 0""", 115))

    # # catch error of ID first
    # def test_hex_interger_with_error(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0xz""", """Error Token 0xz""", 116))

    # def test_oct_interger_with_error(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """0o89""", """Error Token 0o89""", 117))

    # # test array
    # def test_normal_array_1(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """{5, 6, 7}""", """{5, 6, 7},<EOF>""", 118))

    # def test_normal_array_2(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """ {{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}} """, """{{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}},<EOF>""", 119))

    # def test_normal_array_3(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """{5.6,5E-10,6.03}""", """{5.6,5E-10,6.03},<EOF>""", 120))

    # def test_empty_array(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """{,}""", """{,}""", 125))

    # def test_error_array(self):
    #     self.assertTrue(TestLexer.checkLexeme(
    #         """{5.6,TRUE,6.03}""", """{,5.6,,,Error Token T""", 121))

    # # test comment
    # def test_normal_single_comment(self):
    #     self.assertTrue(TestLexer.checkLexeme("""**This line will be ignore**9990""",
    #                                           """9990,<EOF>""", 122))

    # def test_normal_block_comment(self):
    #     self.assertTrue(TestLexer.checkLexeme("""**This line will be ignore\n*This is a\n* multi-line\n* comment.**"somestring" """,
    #                                           """somestring,<EOF>""", 123))

    # def test_unclosed_comment(self):
    #     self.assertTrue(TestLexer.checkLexeme("""**This line will be ignore9990""",
    #                                           """Unterminated Comment""", 124))

    # def test_unclosed_comment_1(self):
    #     self.assertTrue(TestLexer.checkLexeme("""** ***""",
    #                                           """*,<EOF>""", 125))
