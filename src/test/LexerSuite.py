# Student ID: 1852348
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
            "Var: k = +5556", "Var,:,k,=,+,5556,<EOF>", 134))

    def test_int_dec_literal_135(self):
        self.assertTrue(TestLexer.checkLexeme(
            "-5556", "-,5556,<EOF>", 135))

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

    def test_int_hex_literal_error_145(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0x0BZZZ", "Error Token 0x0", 145))

    def test_int_oct_literal_146(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o567", "0o567,<EOF>", 146))

    def test_int_oct_literal_147(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0O124", "0O124,<EOF>", 147))

    def test_int_oct_literal_error_148(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o589", "Error Token 0o589", 148))

    def test_int_oct_literal_error_149(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o5aa", "Error Token 0o5aa", 149))

    def test_int_oct_literal_error_150(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0oAB5", "Error Token 0oAB", 150))

    def test_int_oct_literal_error_151(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o0AB5", "Error Token 0o0", 151))

    # -------- test float literals ----------

    def test_float_literal_152(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.03", "12.03,<EOF>", 152))

    def test_float_literal_153(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.", "12.,<EOF>", 153))

    def test_float_literal_154(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.0e3", "12.0e3,<EOF>", 154))

    def test_float_literal_155(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12e3", "12e3,<EOF>", 155))

    def test_float_literal_156(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.e5", "12.e5,<EOF>", 156))

    def test_float_literal_157(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.0e3", "12.0e3,<EOF>", 157))

    def test_float_literal_158(self):
        self.assertTrue(TestLexer.checkLexeme(
            "120000e-1", "120000e-1,<EOF>", 158))

    def test_float_literal_error_159(self):
        self.assertTrue(TestLexer.checkLexeme(
            ".03", ".,0,3,<EOF>", 159))

    def test_float_literal_error_160(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.abc", "12.,abc,<EOF>", 160))

    def test_float_literal_error_161(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.e", "12.,e,<EOF>", 161))

    # ----------test string literals------------

    def test_normal_string_162(self):
        """test normal string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abdef"  """, """abdef,<EOF>""", 162))

    def test_normal_string_163(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "a@2sow3##"  """, """a@2sow3##,<EOF>""", 163))

    def test_normal_string_with_escape_164(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ Var: x = "a\\b\\f\\r\\t\\n"  """, "Var,:,x,=,a\\b\\f\\r\\t\\n,<EOF>", 164))

    def test_normal_string_with_escape_165(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 165))

    def test_normal_string_with_escape_166(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n '"def '""  """, """ab'"c\\n '"def '",<EOF>""", 166))

    def test_normal_string_with_escape_167(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\\\\\\\\\n def"  """, """ab'"c\\\\\\\\\\n def,<EOF>""", 167))

    def test_normal_string_with_escape_168(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'" \\'def\\'"  """, """ab'" \\'def\\',<EOF>""", 168))

    def test_illegal_escape_169(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 169))

    def test_illegal_escape_170(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\" def"  """, """Illegal Escape In String: abc\\\"""", 170))

    def test_illegal_escape_171(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc' def"  """, """Illegal Escape In String: abc\' """, 171))

    def test_illegal_escape_172(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc"' def"  """, """abc,Error Token '""", 172))

    def test_illegal_escape_173(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "\B \RaiL\\n\\k\\m"  """, """Illegal Escape In String: \B""", 173))

    def test_unterminated_string_174(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 174))

    def test_unterminated_string_175(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def\\'  """, """Unclosed String: abc def\\'  """, 175))

    def test_unterminated_string_176(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ """""""  """, """Unclosed String:   """, 176))

    def test_unterminated_string_177(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def" "'"  """, """abc def,Unclosed String: '"  """, 177))

    def test_unterminated_string_178(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def" "'"'"'"'"  """, """abc def,Unclosed String: '"'"'"'"  """, 178))

    # ------------test boolean literals--------

    def test_bool_literal_179(self):
        self.assertTrue(TestLexer.checkLexeme(
            """Var: x = True, y = False;""", """Var,:,x,=,True,,,y,=,False,;,<EOF>""", 179))

    def test_bool_literal_180(self):
        self.assertTrue(TestLexer.checkLexeme(
            """Var: x = TRue;""", """Var,:,x,=,Error Token T""", 180))

    # ------------test array literals------------
    def test_normal_array_181(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5,6,7}""", """{5,6,7},<EOF>""", 181))

    def test_normal_array_space_182(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5, 6, 7}""", """{5,6,7},<EOF>""", 182))

    def test_normal_array_183(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ {{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}} """, """{{"a","b","c"},{"e","r","h"},{"k","s","m"}},<EOF>""", 183))

    def test_normal_array_184(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5.6,5E-10,6.03}""", """{5.6,5E-10,6.03},<EOF>""", 184))

    def test_normal_array_185(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5}""", """{5},<EOF>""", 185))

    def test_normal_array_186(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{True, False, True}""", """{True,False,True},<EOF>""", 186))

    def test_normal_array_187(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{567, 0x567, 0O345}""", """{567,0x567,0O345},<EOF>""", 187))

    def test_error_array_188(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{True,{"True"},{"True", "False"}}""", """{,True,,,{"True"},,,{"True","False"},},<EOF>""", 188))

    def test_error_array_189(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5.6,"TRUE",6.03}""", """{,5.6,,,TRUE,,,6.03,},<EOF>""", 189))

    def test_error_array_190(self):
        self.assertTrue(TestLexer.checkLexeme(
            """{5.6,TRUE,6.03}""", """{,5.6,,,Error Token T""", 190))

    # ----------test comment----------
    def test_normal_single_comment_191(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**This line will be ignore**9990""", """9990,<EOF>""", 191))

    def test_normal_block_comment_192(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**This line will be ignore\n*This is a\n* multi-line\n* comment.**"somestring" """, """somestring,<EOF>""", 192))

    def test_normal_comment_193(self):
        self.assertTrue(TestLexer.checkLexeme(
            """** ***""", """*,<EOF>""", 193))

    def test_normal_comment_194(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ " ** ** " """, """ ** ** ,<EOF>""", 194))

    def test_normal_comment_195(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ ** "string" ** " ** ** " """, """ ** ** ,<EOF>""", 195))

    def test_unclosed_comment_196(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ **"Some*""", """Unterminated Comment""", 196))

    def test_unclosed_comment_197(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ **"Some**string"** """, """string,Unclosed String: ** """, 197))

    def test_unclosed_comment_198(self):
        self.assertTrue(TestLexer.checkLexeme(
            """**This line will be ignore9990""", """Unterminated Comment""", 198))

    def test_unclosed_comment_199(self):
        self.assertTrue(TestLexer.checkLexeme(
            """******"****""", """Unterminated Comment""", 199))

# ---------Test simple program-------
    def test_simple_program_200(self):
        self.assertTrue(TestLexer.checkLexeme(
            """** Gobal variable declaration **
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
""", """Var,:,a,,,b,,,c,;,Function,:,printArray,Parameter,:,a,,,size,Body,:,Var,:,i,;,For,(,i,=,0,,,i,<,size,,,1,),Do,printLn,(,a,[,i,],),;,EndFor,.,EndBody,.,Function,:,main,Body,:,Var,:,a,[,5,],=,{5,6,7,8,9},;,printArray,(,a,,,5,),;,EndBody,.,<EOF>""", 200))
