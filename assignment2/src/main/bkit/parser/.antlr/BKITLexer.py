# Generated from c:\Users\Admin\Desktop\ppl\assignment2\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0220\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\7:\u0175\n:\f:\16:\u0178\13:\3")
        buf.write(";\3;\3<\3<\7<\u017e\n<\f<\16<\u0181\13<\3<\6<\u0184\n")
        buf.write("<\r<\16<\u0185\5<\u0188\n<\3=\3=\3=\3=\7=\u018e\n=\f=")
        buf.write("\16=\u0191\13=\3>\3>\3>\3>\7>\u0197\n>\f>\16>\u019a\13")
        buf.write(">\3?\3?\3?\5?\u019f\n?\3@\6@\u01a2\n@\r@\16@\u01a3\3@")
        buf.write("\3@\7@\u01a8\n@\f@\16@\u01ab\13@\3@\6@\u01ae\n@\r@\16")
        buf.write("@\u01af\3@\3@\5@\u01b4\n@\3@\6@\u01b7\n@\r@\16@\u01b8")
        buf.write("\3@\6@\u01bc\n@\r@\16@\u01bd\3@\3@\7@\u01c2\n@\f@\16@")
        buf.write("\u01c5\13@\3@\3@\5@\u01c9\n@\3@\6@\u01cc\n@\r@\16@\u01cd")
        buf.write("\5@\u01d0\n@\3A\3A\5A\u01d4\nA\3B\3B\3B\3B\5B\u01da\n")
        buf.write("B\3C\3C\3D\3D\3D\7D\u01e1\nD\fD\16D\u01e4\13D\3D\3D\3")
        buf.write("E\6E\u01e9\nE\rE\16E\u01ea\3E\3E\3F\3F\3F\3F\7F\u01f3")
        buf.write("\nF\fF\16F\u01f6\13F\3F\3F\3F\3F\3F\3G\3G\3H\3H\3H\7H")
        buf.write("\u0202\nH\fH\16H\u0205\13H\3H\3H\3H\3H\5H\u020b\nH\3H")
        buf.write("\5H\u020e\nH\3I\3I\3I\7I\u0213\nI\fI\16I\u0216\13I\3J")
        buf.write("\3J\3J\3J\7J\u021c\nJ\fJ\16J\u021f\13J\4\u01f4\u021d\2")
        buf.write("K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\2-\2/\27\61")
        buf.write("\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O")
        buf.write("\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s")
        buf.write("9u\2w\2y\2{\2}:\177;\u0081<\u0083\2\u0085\2\u0087=\u0089")
        buf.write(">\u008b?\u008d@\u008fA\u0091B\u0093C\3\2\22\3\2c|\6\2")
        buf.write("\62;C\\aac|\3\2\62;\3\2\63;\4\2ZZzz\4\2\63;CH\4\2\62;")
        buf.write("CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg\4\2--//\t\2))^^ddh")
        buf.write("hppttvv\6\2\f\f$$))^^\5\2\13\f\17\17\"\"\3\2$$\2\u0237")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2")
        buf.write("\2\5\u0097\3\2\2\2\7\u009c\3\2\2\2\t\u00a0\3\2\2\2\13")
        buf.write("\u00a5\3\2\2\2\r\u00ab\3\2\2\2\17\u00b4\3\2\2\2\21\u00b7")
        buf.write("\3\2\2\2\23\u00bc\3\2\2\2\25\u00c3\3\2\2\2\27\u00cb\3")
        buf.write("\2\2\2\31\u00d1\3\2\2\2\33\u00d8\3\2\2\2\35\u00e1\3\2")
        buf.write("\2\2\37\u00e5\3\2\2\2!\u00ee\3\2\2\2#\u00f1\3\2\2\2%\u00fb")
        buf.write("\3\2\2\2\'\u0102\3\2\2\2)\u0107\3\2\2\2+\u010d\3\2\2\2")
        buf.write("-\u0112\3\2\2\2/\u0118\3\2\2\2\61\u011e\3\2\2\2\63\u0120")
        buf.write("\3\2\2\2\65\u0123\3\2\2\2\67\u0125\3\2\2\29\u0128\3\2")
        buf.write("\2\2;\u012a\3\2\2\2=\u012d\3\2\2\2?\u012f\3\2\2\2A\u0132")
        buf.write("\3\2\2\2C\u0134\3\2\2\2E\u0136\3\2\2\2G\u0139\3\2\2\2")
        buf.write("I\u013c\3\2\2\2K\u013f\3\2\2\2M\u0142\3\2\2\2O\u0144\3")
        buf.write("\2\2\2Q\u0146\3\2\2\2S\u0149\3\2\2\2U\u014c\3\2\2\2W\u0150")
        buf.write("\3\2\2\2Y\u0153\3\2\2\2[\u0156\3\2\2\2]\u015a\3\2\2\2")
        buf.write("_\u015e\3\2\2\2a\u0160\3\2\2\2c\u0162\3\2\2\2e\u0164\3")
        buf.write("\2\2\2g\u0166\3\2\2\2i\u0168\3\2\2\2k\u016a\3\2\2\2m\u016c")
        buf.write("\3\2\2\2o\u016e\3\2\2\2q\u0170\3\2\2\2s\u0172\3\2\2\2")
        buf.write("u\u0179\3\2\2\2w\u0187\3\2\2\2y\u0189\3\2\2\2{\u0192\3")
        buf.write("\2\2\2}\u019e\3\2\2\2\177\u01cf\3\2\2\2\u0081\u01d3\3")
        buf.write("\2\2\2\u0083\u01d9\3\2\2\2\u0085\u01db\3\2\2\2\u0087\u01dd")
        buf.write("\3\2\2\2\u0089\u01e8\3\2\2\2\u008b\u01ee\3\2\2\2\u008d")
        buf.write("\u01fc\3\2\2\2\u008f\u01fe\3\2\2\2\u0091\u020f\3\2\2\2")
        buf.write("\u0093\u0217\3\2\2\2\u0095\u0096\7?\2\2\u0096\4\3\2\2")
        buf.write("\2\u0097\u0098\7o\2\2\u0098\u0099\7c\2\2\u0099\u009a\7")
        buf.write("k\2\2\u009a\u009b\7p\2\2\u009b\6\3\2\2\2\u009c\u009d\7")
        buf.write("X\2\2\u009d\u009e\7c\2\2\u009e\u009f\7t\2\2\u009f\b\3")
        buf.write("\2\2\2\u00a0\u00a1\7D\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7f\2\2\u00a3\u00a4\7{\2\2\u00a4\n\3\2\2\2\u00a5\u00a6")
        buf.write("\7D\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\f\3\2\2\2\u00ab\u00ac")
        buf.write("\7E\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\16\3\2\2\2\u00b4\u00b5")
        buf.write("\7F\2\2\u00b5\u00b6\7q\2\2\u00b6\20\3\2\2\2\u00b7\u00b8")
        buf.write("\7G\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\22\3\2\2\2\u00bc\u00bd\7G\2\2\u00bd\u00be")
        buf.write("\7n\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7K\2\2\u00c1\u00c2\7h\2\2\u00c2\24\3\2\2\2\u00c3\u00c4")
        buf.write("\7G\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7f\2\2\u00c6\u00c7")
        buf.write("\7D\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7f\2\2\u00c9\u00ca")
        buf.write("\7{\2\2\u00ca\26\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf\7K\2\2\u00cf\u00d0")
        buf.write("\7h\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\7G\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5\7H\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7t\2\2\u00d7\32\3\2\2\2\u00d8\u00d9")
        buf.write("\7G\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db\u00dc")
        buf.write("\7Y\2\2\u00dc\u00dd\7j\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7g\2\2\u00e0\34\3\2\2\2\u00e1\u00e2")
        buf.write("\7H\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4\36")
        buf.write("\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed \3")
        buf.write("\2\2\2\u00ee\u00ef\7K\2\2\u00ef\u00f0\7h\2\2\u00f0\"\3")
        buf.write("\2\2\2\u00f1\u00f2\7R\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7o\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa$\3\2\2\2\u00fb\u00fc\7T\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7p\2\2\u0101&\3\2\2\2\u0102\u0103")
        buf.write("\7V\2\2\u0103\u0104\7j\2\2\u0104\u0105\7g\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106(\3\2\2\2\u0107\u0108\7Y\2\2\u0108\u0109")
        buf.write("\7j\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c*\3\2\2\2\u010d\u010e\7V\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111\7g\2\2\u0111,\3")
        buf.write("\2\2\2\u0112\u0113\7H\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7n\2\2\u0115\u0116\7u\2\2\u0116\u0117\7g\2\2\u0117.\3")
        buf.write("\2\2\2\u0118\u0119\7G\2\2\u0119\u011a\7p\2\2\u011a\u011b")
        buf.write("\7f\2\2\u011b\u011c\7F\2\2\u011c\u011d\7q\2\2\u011d\60")
        buf.write("\3\2\2\2\u011e\u011f\7-\2\2\u011f\62\3\2\2\2\u0120\u0121")
        buf.write("\7-\2\2\u0121\u0122\7\60\2\2\u0122\64\3\2\2\2\u0123\u0124")
        buf.write("\7/\2\2\u0124\66\3\2\2\2\u0125\u0126\7/\2\2\u0126\u0127")
        buf.write("\7\60\2\2\u01278\3\2\2\2\u0128\u0129\7,\2\2\u0129:\3\2")
        buf.write("\2\2\u012a\u012b\7,\2\2\u012b\u012c\7\60\2\2\u012c<\3")
        buf.write("\2\2\2\u012d\u012e\7^\2\2\u012e>\3\2\2\2\u012f\u0130\7")
        buf.write("^\2\2\u0130\u0131\7\60\2\2\u0131@\3\2\2\2\u0132\u0133")
        buf.write("\7\'\2\2\u0133B\3\2\2\2\u0134\u0135\7#\2\2\u0135D\3\2")
        buf.write("\2\2\u0136\u0137\7(\2\2\u0137\u0138\7(\2\2\u0138F\3\2")
        buf.write("\2\2\u0139\u013a\7~\2\2\u013a\u013b\7~\2\2\u013bH\3\2")
        buf.write("\2\2\u013c\u013d\7?\2\2\u013d\u013e\7?\2\2\u013eJ\3\2")
        buf.write("\2\2\u013f\u0140\7#\2\2\u0140\u0141\7?\2\2\u0141L\3\2")
        buf.write("\2\2\u0142\u0143\7>\2\2\u0143N\3\2\2\2\u0144\u0145\7@")
        buf.write("\2\2\u0145P\3\2\2\2\u0146\u0147\7>\2\2\u0147\u0148\7?")
        buf.write("\2\2\u0148R\3\2\2\2\u0149\u014a\7@\2\2\u014a\u014b\7?")
        buf.write("\2\2\u014bT\3\2\2\2\u014c\u014d\7?\2\2\u014d\u014e\7\61")
        buf.write("\2\2\u014e\u014f\7?\2\2\u014fV\3\2\2\2\u0150\u0151\7>")
        buf.write("\2\2\u0151\u0152\7\60\2\2\u0152X\3\2\2\2\u0153\u0154\7")
        buf.write("@\2\2\u0154\u0155\7\60\2\2\u0155Z\3\2\2\2\u0156\u0157")
        buf.write("\7>\2\2\u0157\u0158\7?\2\2\u0158\u0159\7\60\2\2\u0159")
        buf.write("\\\3\2\2\2\u015a\u015b\7@\2\2\u015b\u015c\7?\2\2\u015c")
        buf.write("\u015d\7\60\2\2\u015d^\3\2\2\2\u015e\u015f\7=\2\2\u015f")
        buf.write("`\3\2\2\2\u0160\u0161\7<\2\2\u0161b\3\2\2\2\u0162\u0163")
        buf.write("\7*\2\2\u0163d\3\2\2\2\u0164\u0165\7+\2\2\u0165f\3\2\2")
        buf.write("\2\u0166\u0167\7]\2\2\u0167h\3\2\2\2\u0168\u0169\7_\2")
        buf.write("\2\u0169j\3\2\2\2\u016a\u016b\7}\2\2\u016bl\3\2\2\2\u016c")
        buf.write("\u016d\7\177\2\2\u016dn\3\2\2\2\u016e\u016f\7\60\2\2\u016f")
        buf.write("p\3\2\2\2\u0170\u0171\7.\2\2\u0171r\3\2\2\2\u0172\u0176")
        buf.write("\t\2\2\2\u0173\u0175\t\3\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177t\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\t\4\2")
        buf.write("\2\u017av\3\2\2\2\u017b\u017f\t\5\2\2\u017c\u017e\5u;")
        buf.write("\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0188\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0184\7\62\2\2\u0183\u0182\3\2\2")
        buf.write("\2\u0184\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0188\3\2\2\2\u0187\u017b\3\2\2\2\u0187")
        buf.write("\u0183\3\2\2\2\u0188x\3\2\2\2\u0189\u018a\7\62\2\2\u018a")
        buf.write("\u018b\t\6\2\2\u018b\u018f\t\7\2\2\u018c\u018e\t\b\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u018f\u0190\3\2\2\2\u0190z\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0193\7\62\2\2\u0193\u0194\t\t\2\2\u0194")
        buf.write("\u0198\t\n\2\2\u0195\u0197\t\13\2\2\u0196\u0195\3\2\2")
        buf.write("\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199|\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019f")
        buf.write("\5w<\2\u019c\u019f\5y=\2\u019d\u019f\5{>\2\u019e\u019b")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019f")
        buf.write("~\3\2\2\2\u01a0\u01a2\5u;\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a9\7\60\2\2\u01a6\u01a8")
        buf.write("\5u;\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01d0\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u01ae\5u;\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b3\t\f\2\2\u01b2\u01b4\t")
        buf.write("\r\2\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6")
        buf.write("\3\2\2\2\u01b5\u01b7\5u;\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("\u01d0\3\2\2\2\u01ba\u01bc\5u;\2\u01bb\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c3\7\60\2\2\u01c0\u01c2")
        buf.write("\5u;\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c8\t\f\2\2\u01c7\u01c9\t\r\2\2")
        buf.write("\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3")
        buf.write("\2\2\2\u01ca\u01cc\5u;\2\u01cb\u01ca\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01d0\3\2\2\2\u01cf\u01a1\3\2\2\2\u01cf\u01ad\3\2\2\2")
        buf.write("\u01cf\u01bb\3\2\2\2\u01d0\u0080\3\2\2\2\u01d1\u01d4\5")
        buf.write("+\26\2\u01d2\u01d4\5-\27\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d4\u0082\3\2\2\2\u01d5\u01d6\7^\2\2\u01d6")
        buf.write("\u01da\t\16\2\2\u01d7\u01d8\7)\2\2\u01d8\u01da\7$\2\2")
        buf.write("\u01d9\u01d5\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u0084\3")
        buf.write("\2\2\2\u01db\u01dc\n\17\2\2\u01dc\u0086\3\2\2\2\u01dd")
        buf.write("\u01e2\7$\2\2\u01de\u01e1\5\u0085C\2\u01df\u01e1\5\u0083")
        buf.write("B\2\u01e0\u01de\3\2\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e4")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7$\2\2")
        buf.write("\u01e6\u0088\3\2\2\2\u01e7\u01e9\t\20\2\2\u01e8\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea")
        buf.write("\u01eb\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed\bE\2\2")
        buf.write("\u01ed\u008a\3\2\2\2\u01ee\u01ef\7,\2\2\u01ef\u01f0\7")
        buf.write(",\2\2\u01f0\u01f4\3\2\2\2\u01f1\u01f3\13\2\2\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f5\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f7\u01f8\7,\2\2\u01f8\u01f9\7,\2\2\u01f9\u01fa\3\2")
        buf.write("\2\2\u01fa\u01fb\bF\2\2\u01fb\u008c\3\2\2\2\u01fc\u01fd")
        buf.write("\13\2\2\2\u01fd\u008e\3\2\2\2\u01fe\u0203\7$\2\2\u01ff")
        buf.write("\u0202\5\u0085C\2\u0200\u0202\5\u0083B\2\u0201\u01ff\3")
        buf.write("\2\2\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u020a\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0206\u0207\7^\2\2\u0207\u020b\n\16\2\2")
        buf.write("\u0208\u0209\7)\2\2\u0209\u020b\n\21\2\2\u020a\u0206\3")
        buf.write("\2\2\2\u020a\u0208\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u020e")
        buf.write("\7$\2\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2\2\2\u020e")
        buf.write("\u0090\3\2\2\2\u020f\u0214\7$\2\2\u0210\u0213\5\u0085")
        buf.write("C\2\u0211\u0213\5\u0083B\2\u0212\u0210\3\2\2\2\u0212\u0211")
        buf.write("\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214")
        buf.write("\u0215\3\2\2\2\u0215\u0092\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0217\u0218\7,\2\2\u0218\u0219\7,\2\2\u0219\u021d\3\2")
        buf.write("\2\2\u021a\u021c\13\2\2\2\u021b\u021a\3\2\2\2\u021c\u021f")
        buf.write("\3\2\2\2\u021d\u021e\3\2\2\2\u021d\u021b\3\2\2\2\u021e")
        buf.write("\u0094\3\2\2\2\u021f\u021d\3\2\2\2!\2\u0176\u017f\u0185")
        buf.write("\u0187\u018f\u0198\u019e\u01a3\u01a9\u01af\u01b3\u01b8")
        buf.write("\u01bd\u01c3\u01c8\u01cd\u01cf\u01d3\u01d9\u01e0\u01e2")
        buf.write("\u01ea\u01f4\u0201\u0203\u020a\u020d\u0212\u0214\u021d")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    VAR = 3
    BODY = 4
    BREAK = 5
    CONTINUE = 6
    DO = 7
    ELSE = 8
    ELSEIF = 9
    ENDBODY = 10
    ENDIF = 11
    ENDFOR = 12
    ENDWHILE = 13
    FOR = 14
    FUNCTION = 15
    IF = 16
    PARAMETER = 17
    RETURN = 18
    THEN = 19
    WHILE = 20
    ENDDO = 21
    ADD = 22
    F_ADD = 23
    SUB = 24
    F_SUB = 25
    MUL = 26
    F_MUL = 27
    DIV = 28
    F_DIV = 29
    REMAIN = 30
    NEG = 31
    AND = 32
    OR = 33
    EQ = 34
    NOT_EQ = 35
    LT = 36
    GT = 37
    LTE = 38
    GTE = 39
    F_NOT_EQ = 40
    F_LT = 41
    F_GT = 42
    F_LTE = 43
    F_GTE = 44
    SEMI = 45
    COLON = 46
    LP = 47
    RP = 48
    LS = 49
    RS = 50
    LB = 51
    RB = 52
    DOT = 53
    COMMA = 54
    ID = 55
    INT_LIT = 56
    FLOAT_LIT = 57
    BOOL_LIT = 58
    STRING_LIT = 59
    WS = 60
    COMMENT = 61
    ERROR_CHAR = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'main'", "'Var'", "'Body'", "'Break'", "'Continue'", 
            "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
            "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
            "'Return'", "'Then'", "'While'", "'EndDo'", "'+'", "'+.'", "'-'", 
            "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "';'", "':'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "WHILE", "ENDDO", "ADD", 
            "F_ADD", "SUB", "F_SUB", "MUL", "F_MUL", "DIV", "F_DIV", "REMAIN", 
            "NEG", "AND", "OR", "EQ", "NOT_EQ", "LT", "GT", "LTE", "GTE", 
            "F_NOT_EQ", "F_LT", "F_GT", "F_LTE", "F_GTE", "SEMI", "COLON", 
            "LP", "RP", "LS", "RS", "LB", "RB", "DOT", "COMMA", "ID", "INT_LIT", 
            "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "WS", "COMMENT", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "VAR", "BODY", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "ADD", "F_ADD", "SUB", 
                  "F_SUB", "MUL", "F_MUL", "DIV", "F_DIV", "REMAIN", "NEG", 
                  "AND", "OR", "EQ", "NOT_EQ", "LT", "GT", "LTE", "GTE", 
                  "F_NOT_EQ", "F_LT", "F_GT", "F_LTE", "F_GTE", "SEMI", 
                  "COLON", "LP", "RP", "LS", "RS", "LB", "RB", "DOT", "COMMA", 
                  "ID", "DIGIT", "DEC", "HEX", "OCT", "INT_LIT", "FLOAT_LIT", 
                  "BOOL_LIT", "ESC", "STR_CHAR", "STRING_LIT", "WS", "COMMENT", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        elif tk == self.STRING_LIT:
            endPos = len(result.text) - 1
            result.text = result.text[1:endPos]
            return result
        else:
            return result;


