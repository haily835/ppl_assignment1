# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0308\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\7:\u0179\n:\f:\16:\u017c")
        buf.write("\13:\3;\3;\3<\3<\7<\u0182\n<\f<\16<\u0185\13<\3<\6<\u0188")
        buf.write("\n<\r<\16<\u0189\5<\u018c\n<\3=\3=\3=\3=\7=\u0192\n=\f")
        buf.write("=\16=\u0195\13=\3>\3>\3>\3>\7>\u019b\n>\f>\16>\u019e\13")
        buf.write(">\3?\3?\3?\5?\u01a3\n?\3@\6@\u01a6\n@\r@\16@\u01a7\3@")
        buf.write("\3@\7@\u01ac\n@\f@\16@\u01af\13@\3@\6@\u01b2\n@\r@\16")
        buf.write("@\u01b3\3@\3@\5@\u01b8\n@\3@\6@\u01bb\n@\r@\16@\u01bc")
        buf.write("\3@\6@\u01c0\n@\r@\16@\u01c1\3@\3@\7@\u01c6\n@\f@\16@")
        buf.write("\u01c9\13@\3@\3@\5@\u01cd\n@\3@\6@\u01d0\n@\r@\16@\u01d1")
        buf.write("\5@\u01d4\n@\3A\3A\5A\u01d8\nA\3B\3B\3B\3B\5B\u01de\n")
        buf.write("B\3C\3C\3D\3D\3D\7D\u01e5\nD\fD\16D\u01e8\13D\3D\3D\3")
        buf.write("E\3E\7E\u01ee\nE\fE\16E\u01f1\13E\3E\3E\7E\u01f5\nE\f")
        buf.write("E\16E\u01f8\13E\3E\7E\u01fb\nE\fE\16E\u01fe\13E\3E\3E")
        buf.write("\7E\u0202\nE\fE\16E\u0205\13E\3E\3E\7E\u0209\nE\fE\16")
        buf.write("E\u020c\13E\7E\u020e\nE\fE\16E\u0211\13E\3E\7E\u0214\n")
        buf.write("E\fE\16E\u0217\13E\3E\3E\7E\u021b\nE\fE\16E\u021e\13E")
        buf.write("\3E\7E\u0221\nE\fE\16E\u0224\13E\3E\3E\7E\u0228\nE\fE")
        buf.write("\16E\u022b\13E\3E\3E\7E\u022f\nE\fE\16E\u0232\13E\7E\u0234")
        buf.write("\nE\fE\16E\u0237\13E\3E\7E\u023a\nE\fE\16E\u023d\13E\3")
        buf.write("E\3E\7E\u0241\nE\fE\16E\u0244\13E\3E\7E\u0247\nE\fE\16")
        buf.write("E\u024a\13E\3E\3E\7E\u024e\nE\fE\16E\u0251\13E\3E\3E\7")
        buf.write("E\u0255\nE\fE\16E\u0258\13E\7E\u025a\nE\fE\16E\u025d\13")
        buf.write("E\3E\7E\u0260\nE\fE\16E\u0263\13E\3E\3E\7E\u0267\nE\f")
        buf.write("E\16E\u026a\13E\3E\7E\u026d\nE\fE\16E\u0270\13E\3E\3E")
        buf.write("\7E\u0274\nE\fE\16E\u0277\13E\3E\3E\7E\u027b\nE\fE\16")
        buf.write("E\u027e\13E\7E\u0280\nE\fE\16E\u0283\13E\3E\7E\u0286\n")
        buf.write("E\fE\16E\u0289\13E\3E\3E\7E\u028d\nE\fE\16E\u0290\13E")
        buf.write("\3E\7E\u0293\nE\fE\16E\u0296\13E\3E\3E\7E\u029a\nE\fE")
        buf.write("\16E\u029d\13E\3E\3E\7E\u02a1\nE\fE\16E\u02a4\13E\7E\u02a6")
        buf.write("\nE\fE\16E\u02a9\13E\5E\u02ab\nE\3E\3E\3F\6F\u02b0\nF")
        buf.write("\rF\16F\u02b1\3F\3F\3G\3G\3G\3G\7G\u02ba\nG\fG\16G\u02bd")
        buf.write("\13G\3G\3G\3G\3G\3G\3H\3H\3I\3I\3I\7I\u02c9\nI\fI\16I")
        buf.write("\u02cc\13I\3I\3I\3I\3I\5I\u02d2\nI\3I\5I\u02d5\nI\3J\3")
        buf.write("J\3J\7J\u02da\nJ\fJ\16J\u02dd\13J\3K\3K\3K\3K\7K\u02e3")
        buf.write("\nK\fK\16K\u02e6\13K\3L\3L\3L\3L\3L\3L\7L\u02ee\nL\fL")
        buf.write("\16L\u02f1\13L\3L\7L\u02f4\nL\fL\16L\u02f7\13L\3L\3L\3")
        buf.write("L\7L\u02fc\nL\fL\16L\u02ff\13L\3L\7L\u0302\nL\fL\16L\u0305")
        buf.write("\13L\5L\u0307\nL\4\u02bb\u02e4\2M\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{\2}<\177=\u0081")
        buf.write(">\u0083\2\u0085\2\u0087?\u0089@\u008bA\u008dB\u008fC\u0091")
        buf.write("D\u0093E\u0095F\u0097G\3\2\23\3\2c|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\3\2\63;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\63")
        buf.write("9\3\2\629\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\7\2\n\f\16")
        buf.write("\17$$))^^\5\2\13\f\17\17\"\"\3\2$$\6\2QQZZqqzz\2\u0349")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2")
        buf.write("\2\5\u009b\3\2\2\2\7\u00a0\3\2\2\2\t\u00a4\3\2\2\2\13")
        buf.write("\u00a9\3\2\2\2\r\u00af\3\2\2\2\17\u00b8\3\2\2\2\21\u00bb")
        buf.write("\3\2\2\2\23\u00c0\3\2\2\2\25\u00c7\3\2\2\2\27\u00cf\3")
        buf.write("\2\2\2\31\u00d5\3\2\2\2\33\u00dc\3\2\2\2\35\u00e5\3\2")
        buf.write("\2\2\37\u00e9\3\2\2\2!\u00f2\3\2\2\2#\u00f5\3\2\2\2%\u00ff")
        buf.write("\3\2\2\2\'\u0106\3\2\2\2)\u010b\3\2\2\2+\u0111\3\2\2\2")
        buf.write("-\u0116\3\2\2\2/\u011c\3\2\2\2\61\u0122\3\2\2\2\63\u0124")
        buf.write("\3\2\2\2\65\u0127\3\2\2\2\67\u0129\3\2\2\29\u012c\3\2")
        buf.write("\2\2;\u012e\3\2\2\2=\u0131\3\2\2\2?\u0133\3\2\2\2A\u0136")
        buf.write("\3\2\2\2C\u0138\3\2\2\2E\u013a\3\2\2\2G\u013d\3\2\2\2")
        buf.write("I\u0140\3\2\2\2K\u0143\3\2\2\2M\u0146\3\2\2\2O\u0148\3")
        buf.write("\2\2\2Q\u014a\3\2\2\2S\u014d\3\2\2\2U\u0150\3\2\2\2W\u0154")
        buf.write("\3\2\2\2Y\u0157\3\2\2\2[\u015a\3\2\2\2]\u015e\3\2\2\2")
        buf.write("_\u0162\3\2\2\2a\u0164\3\2\2\2c\u0166\3\2\2\2e\u0168\3")
        buf.write("\2\2\2g\u016a\3\2\2\2i\u016c\3\2\2\2k\u016e\3\2\2\2m\u0170")
        buf.write("\3\2\2\2o\u0172\3\2\2\2q\u0174\3\2\2\2s\u0176\3\2\2\2")
        buf.write("u\u017d\3\2\2\2w\u018b\3\2\2\2y\u018d\3\2\2\2{\u0196\3")
        buf.write("\2\2\2}\u01a2\3\2\2\2\177\u01d3\3\2\2\2\u0081\u01d7\3")
        buf.write("\2\2\2\u0083\u01dd\3\2\2\2\u0085\u01df\3\2\2\2\u0087\u01e1")
        buf.write("\3\2\2\2\u0089\u01eb\3\2\2\2\u008b\u02af\3\2\2\2\u008d")
        buf.write("\u02b5\3\2\2\2\u008f\u02c3\3\2\2\2\u0091\u02c5\3\2\2\2")
        buf.write("\u0093\u02d6\3\2\2\2\u0095\u02de\3\2\2\2\u0097\u0306\3")
        buf.write("\2\2\2\u0099\u009a\7?\2\2\u009a\4\3\2\2\2\u009b\u009c")
        buf.write("\7o\2\2\u009c\u009d\7c\2\2\u009d\u009e\7k\2\2\u009e\u009f")
        buf.write("\7p\2\2\u009f\6\3\2\2\2\u00a0\u00a1\7X\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7t\2\2\u00a3\b\3\2\2\2\u00a4\u00a5")
        buf.write("\7D\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8")
        buf.write("\7{\2\2\u00a8\n\3\2\2\2\u00a9\u00aa\7D\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7m\2\2\u00ae\f\3\2\2\2\u00af\u00b0\7E\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\16\3\2\2\2\u00b8\u00b9\7F\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7G\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7g\2\2\u00bf\22")
        buf.write("\3\2\2\2\u00c0\u00c1\7G\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7K\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\24\3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7{\2\2\u00ce\26")
        buf.write("\3\2\2\2\u00cf\u00d0\7G\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2\u00d3\7K\2\2\u00d3\u00d4\7h\2\2\u00d4\30")
        buf.write("\3\2\2\2\u00d5\u00d6\7G\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7H\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\32\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7f\2\2\u00df\u00e0\7Y\2\2\u00e0\u00e1")
        buf.write("\7j\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\36\3\2\2\2\u00e9\u00ea")
        buf.write("\7H\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7e\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1 \3\2\2\2\u00f2\u00f3")
        buf.write("\7K\2\2\u00f3\u00f4\7h\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7R\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7o\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7t\2\2\u00fe$\3")
        buf.write("\2\2\2\u00ff\u0100\7T\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105&\3\2\2\2\u0106\u0107\7V\2\2\u0107\u0108")
        buf.write("\7j\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a(\3")
        buf.write("\2\2\2\u010b\u010c\7Y\2\2\u010c\u010d\7j\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7n\2\2\u010f\u0110\7g\2\2\u0110*\3")
        buf.write("\2\2\2\u0111\u0112\7V\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7w\2\2\u0114\u0115\7g\2\2\u0115,\3\2\2\2\u0116\u0117")
        buf.write("\7H\2\2\u0117\u0118\7c\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7u\2\2\u011a\u011b\7g\2\2\u011b.\3\2\2\2\u011c\u011d")
        buf.write("\7G\2\2\u011d\u011e\7p\2\2\u011e\u011f\7f\2\2\u011f\u0120")
        buf.write("\7F\2\2\u0120\u0121\7q\2\2\u0121\60\3\2\2\2\u0122\u0123")
        buf.write("\7-\2\2\u0123\62\3\2\2\2\u0124\u0125\7-\2\2\u0125\u0126")
        buf.write("\7\60\2\2\u0126\64\3\2\2\2\u0127\u0128\7/\2\2\u0128\66")
        buf.write("\3\2\2\2\u0129\u012a\7/\2\2\u012a\u012b\7\60\2\2\u012b")
        buf.write("8\3\2\2\2\u012c\u012d\7,\2\2\u012d:\3\2\2\2\u012e\u012f")
        buf.write("\7,\2\2\u012f\u0130\7\60\2\2\u0130<\3\2\2\2\u0131\u0132")
        buf.write("\7^\2\2\u0132>\3\2\2\2\u0133\u0134\7^\2\2\u0134\u0135")
        buf.write("\7\60\2\2\u0135@\3\2\2\2\u0136\u0137\7\'\2\2\u0137B\3")
        buf.write("\2\2\2\u0138\u0139\7#\2\2\u0139D\3\2\2\2\u013a\u013b\7")
        buf.write("(\2\2\u013b\u013c\7(\2\2\u013cF\3\2\2\2\u013d\u013e\7")
        buf.write("~\2\2\u013e\u013f\7~\2\2\u013fH\3\2\2\2\u0140\u0141\7")
        buf.write("?\2\2\u0141\u0142\7?\2\2\u0142J\3\2\2\2\u0143\u0144\7")
        buf.write("#\2\2\u0144\u0145\7?\2\2\u0145L\3\2\2\2\u0146\u0147\7")
        buf.write(">\2\2\u0147N\3\2\2\2\u0148\u0149\7@\2\2\u0149P\3\2\2\2")
        buf.write("\u014a\u014b\7>\2\2\u014b\u014c\7?\2\2\u014cR\3\2\2\2")
        buf.write("\u014d\u014e\7@\2\2\u014e\u014f\7?\2\2\u014fT\3\2\2\2")
        buf.write("\u0150\u0151\7?\2\2\u0151\u0152\7\61\2\2\u0152\u0153\7")
        buf.write("?\2\2\u0153V\3\2\2\2\u0154\u0155\7>\2\2\u0155\u0156\7")
        buf.write("\60\2\2\u0156X\3\2\2\2\u0157\u0158\7@\2\2\u0158\u0159")
        buf.write("\7\60\2\2\u0159Z\3\2\2\2\u015a\u015b\7>\2\2\u015b\u015c")
        buf.write("\7?\2\2\u015c\u015d\7\60\2\2\u015d\\\3\2\2\2\u015e\u015f")
        buf.write("\7@\2\2\u015f\u0160\7?\2\2\u0160\u0161\7\60\2\2\u0161")
        buf.write("^\3\2\2\2\u0162\u0163\7=\2\2\u0163`\3\2\2\2\u0164\u0165")
        buf.write("\7<\2\2\u0165b\3\2\2\2\u0166\u0167\7*\2\2\u0167d\3\2\2")
        buf.write("\2\u0168\u0169\7+\2\2\u0169f\3\2\2\2\u016a\u016b\7]\2")
        buf.write("\2\u016bh\3\2\2\2\u016c\u016d\7_\2\2\u016dj\3\2\2\2\u016e")
        buf.write("\u016f\7}\2\2\u016fl\3\2\2\2\u0170\u0171\7\177\2\2\u0171")
        buf.write("n\3\2\2\2\u0172\u0173\7\60\2\2\u0173p\3\2\2\2\u0174\u0175")
        buf.write("\7.\2\2\u0175r\3\2\2\2\u0176\u017a\t\2\2\2\u0177\u0179")
        buf.write("\t\3\2\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bt\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017d\u017e\t\4\2\2\u017ev\3\2\2\2\u017f")
        buf.write("\u0183\t\5\2\2\u0180\u0182\5u;\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u018c\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0188\7")
        buf.write("\62\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2")
        buf.write("\u018b\u017f\3\2\2\2\u018b\u0187\3\2\2\2\u018cx\3\2\2")
        buf.write("\2\u018d\u018e\7\62\2\2\u018e\u018f\t\6\2\2\u018f\u0193")
        buf.write("\t\7\2\2\u0190\u0192\t\b\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194z\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0197\7\62\2")
        buf.write("\2\u0197\u0198\t\t\2\2\u0198\u019c\t\n\2\2\u0199\u019b")
        buf.write("\t\13\2\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d|\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u01a3\5w<\2\u01a0\u01a3\5y=\2\u01a1")
        buf.write("\u01a3\5{>\2\u01a2\u019f\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3~\3\2\2\2\u01a4\u01a6\5u;\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ad\7")
        buf.write("\60\2\2\u01aa\u01ac\5u;\2\u01ab\u01aa\3\2\2\2\u01ac\u01af")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01d4\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2\5u;\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\t")
        buf.write("\f\2\2\u01b6\u01b8\t\r\2\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01bb\5u;\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01d4\3\2\2\2\u01be\u01c0\5u;\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c7\7")
        buf.write("\60\2\2\u01c4\u01c6\5u;\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9")
        buf.write("\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cc\t\f\2\2")
        buf.write("\u01cb\u01cd\t\r\2\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3")
        buf.write("\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01d0\5u;\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01a5\3\2\2\2")
        buf.write("\u01d3\u01b1\3\2\2\2\u01d3\u01bf\3\2\2\2\u01d4\u0080\3")
        buf.write("\2\2\2\u01d5\u01d8\5+\26\2\u01d6\u01d8\5-\27\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u0082\3\2\2\2\u01d9")
        buf.write("\u01da\7^\2\2\u01da\u01de\t\16\2\2\u01db\u01dc\7)\2\2")
        buf.write("\u01dc\u01de\7$\2\2\u01dd\u01d9\3\2\2\2\u01dd\u01db\3")
        buf.write("\2\2\2\u01de\u0084\3\2\2\2\u01df\u01e0\n\17\2\2\u01e0")
        buf.write("\u0086\3\2\2\2\u01e1\u01e6\7$\2\2\u01e2\u01e5\5\u0085")
        buf.write("C\2\u01e3\u01e5\5\u0083B\2\u01e4\u01e2\3\2\2\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e9\u01ea\7$\2\2\u01ea\u0088\3\2\2\2\u01eb\u02aa\5")
        buf.write("k\66\2\u01ec\u01ee\7\"\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1")
        buf.write("\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f6\5\u0081")
        buf.write("A\2\u01f3\u01f5\7\"\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8")
        buf.write("\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u020f\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fb\7\"\2\2")
        buf.write("\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc")
        buf.write("\3\2\2\2\u01ff\u0203\5q9\2\u0200\u0202\7\"\2\2\u0201\u0200")
        buf.write("\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3\2\2\2")
        buf.write("\u0206\u020a\5\u0081A\2\u0207\u0209\7\"\2\2\u0208\u0207")
        buf.write("\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020d\u01fc\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u020f\u0210\3\2\2\2\u0210\u02ab\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0212\u0214\7\"\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021c\5")
        buf.write("}?\2\u0219\u021b\7\"\2\2\u021a\u0219\3\2\2\2\u021b\u021e")
        buf.write("\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\u0235\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0221\7\"\2\2")
        buf.write("\u0220\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3")
        buf.write("\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0222")
        buf.write("\3\2\2\2\u0225\u0229\5q9\2\u0226\u0228\7\"\2\2\u0227\u0226")
        buf.write("\3\2\2\2\u0228\u022b\3\2\2\2\u0229\u0227\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u022c\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022c\u0230\5}?\2\u022d\u022f\7\"\2\2\u022e\u022d\3\2")
        buf.write("\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0233")
        buf.write("\u0222\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236\u02ab\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u023a\7\"\2\2\u0239\u0238\3\2\2\2\u023a\u023d")
        buf.write("\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u023e\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u0242\5\177@")
        buf.write("\2\u023f\u0241\7\"\2\2\u0240\u023f\3\2\2\2\u0241\u0244")
        buf.write("\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write("\u025b\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u0247\7\"\2\2")
        buf.write("\u0246\u0245\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3")
        buf.write("\2\2\2\u0248\u0249\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248")
        buf.write("\3\2\2\2\u024b\u024f\5q9\2\u024c\u024e\7\"\2\2\u024d\u024c")
        buf.write("\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2")
        buf.write("\u0252\u0256\5\177@\2\u0253\u0255\7\"\2\2\u0254\u0253")
        buf.write("\3\2\2\2\u0255\u0258\3\2\2\2\u0256\u0254\3\2\2\2\u0256")
        buf.write("\u0257\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2")
        buf.write("\u0259\u0248\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u0259\3")
        buf.write("\2\2\2\u025b\u025c\3\2\2\2\u025c\u02ab\3\2\2\2\u025d\u025b")
        buf.write("\3\2\2\2\u025e\u0260\7\"\2\2\u025f\u025e\3\2\2\2\u0260")
        buf.write("\u0263\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2")
        buf.write("\u0262\u0264\3\2\2\2\u0263\u0261\3\2\2\2\u0264\u0268\5")
        buf.write("\u0087D\2\u0265\u0267\7\"\2\2\u0266\u0265\3\2\2\2\u0267")
        buf.write("\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0268\u0269\3\2\2\2")
        buf.write("\u0269\u0281\3\2\2\2\u026a\u0268\3\2\2\2\u026b\u026d\7")
        buf.write("\"\2\2\u026c\u026b\3\2\2\2\u026d\u0270\3\2\2\2\u026e\u026c")
        buf.write("\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0271\3\2\2\2\u0270")
        buf.write("\u026e\3\2\2\2\u0271\u0275\5q9\2\u0272\u0274\7\"\2\2\u0273")
        buf.write("\u0272\3\2\2\2\u0274\u0277\3\2\2\2\u0275\u0273\3\2\2\2")
        buf.write("\u0275\u0276\3\2\2\2\u0276\u0278\3\2\2\2\u0277\u0275\3")
        buf.write("\2\2\2\u0278\u027c\5\u0087D\2\u0279\u027b\7\"\2\2\u027a")
        buf.write("\u0279\3\2\2\2\u027b\u027e\3\2\2\2\u027c\u027a\3\2\2\2")
        buf.write("\u027c\u027d\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c\3")
        buf.write("\2\2\2\u027f\u026e\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f")
        buf.write("\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u02ab\3\2\2\2\u0283")
        buf.write("\u0281\3\2\2\2\u0284\u0286\7\"\2\2\u0285\u0284\3\2\2\2")
        buf.write("\u0286\u0289\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0288\3")
        buf.write("\2\2\2\u0288\u028a\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u028e")
        buf.write("\5\u0089E\2\u028b\u028d\7\"\2\2\u028c\u028b\3\2\2\2\u028d")
        buf.write("\u0290\3\2\2\2\u028e\u028c\3\2\2\2\u028e\u028f\3\2\2\2")
        buf.write("\u028f\u02a7\3\2\2\2\u0290\u028e\3\2\2\2\u0291\u0293\7")
        buf.write("\"\2\2\u0292\u0291\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292")
        buf.write("\3\2\2\2\u0294\u0295\3\2\2\2\u0295\u0297\3\2\2\2\u0296")
        buf.write("\u0294\3\2\2\2\u0297\u029b\5q9\2\u0298\u029a\7\"\2\2\u0299")
        buf.write("\u0298\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299\3\2\2\2")
        buf.write("\u029b\u029c\3\2\2\2\u029c\u029e\3\2\2\2\u029d\u029b\3")
        buf.write("\2\2\2\u029e\u02a2\5\u0089E\2\u029f\u02a1\7\"\2\2\u02a0")
        buf.write("\u029f\3\2\2\2\u02a1\u02a4\3\2\2\2\u02a2\u02a0\3\2\2\2")
        buf.write("\u02a2\u02a3\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3")
        buf.write("\2\2\2\u02a5\u0294\3\2\2\2\u02a6\u02a9\3\2\2\2\u02a7\u02a5")
        buf.write("\3\2\2\2\u02a7\u02a8\3\2\2\2\u02a8\u02ab\3\2\2\2\u02a9")
        buf.write("\u02a7\3\2\2\2\u02aa\u01ef\3\2\2\2\u02aa\u0215\3\2\2\2")
        buf.write("\u02aa\u023b\3\2\2\2\u02aa\u0261\3\2\2\2\u02aa\u0287\3")
        buf.write("\2\2\2\u02ab\u02ac\3\2\2\2\u02ac\u02ad\5m\67\2\u02ad\u008a")
        buf.write("\3\2\2\2\u02ae\u02b0\t\20\2\2\u02af\u02ae\3\2\2\2\u02b0")
        buf.write("\u02b1\3\2\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2")
        buf.write("\u02b2\u02b3\3\2\2\2\u02b3\u02b4\bF\2\2\u02b4\u008c\3")
        buf.write("\2\2\2\u02b5\u02b6\7,\2\2\u02b6\u02b7\7,\2\2\u02b7\u02bb")
        buf.write("\3\2\2\2\u02b8\u02ba\13\2\2\2\u02b9\u02b8\3\2\2\2\u02ba")
        buf.write("\u02bd\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bb\u02b9\3\2\2\2")
        buf.write("\u02bc\u02be\3\2\2\2\u02bd\u02bb\3\2\2\2\u02be\u02bf\7")
        buf.write(",\2\2\u02bf\u02c0\7,\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2")
        buf.write("\bG\2\2\u02c2\u008e\3\2\2\2\u02c3\u02c4\13\2\2\2\u02c4")
        buf.write("\u0090\3\2\2\2\u02c5\u02ca\7$\2\2\u02c6\u02c9\5\u0085")
        buf.write("C\2\u02c7\u02c9\5\u0083B\2\u02c8\u02c6\3\2\2\2\u02c8\u02c7")
        buf.write("\3\2\2\2\u02c9\u02cc\3\2\2\2\u02ca\u02c8\3\2\2\2\u02ca")
        buf.write("\u02cb\3\2\2\2\u02cb\u02d1\3\2\2\2\u02cc\u02ca\3\2\2\2")
        buf.write("\u02cd\u02ce\7^\2\2\u02ce\u02d2\n\16\2\2\u02cf\u02d0\7")
        buf.write(")\2\2\u02d0\u02d2\n\21\2\2\u02d1\u02cd\3\2\2\2\u02d1\u02cf")
        buf.write("\3\2\2\2\u02d2\u02d4\3\2\2\2\u02d3\u02d5\7$\2\2\u02d4")
        buf.write("\u02d3\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u0092\3\2\2\2")
        buf.write("\u02d6\u02db\7$\2\2\u02d7\u02da\5\u0085C\2\u02d8\u02da")
        buf.write("\5\u0083B\2\u02d9\u02d7\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da")
        buf.write("\u02dd\3\2\2\2\u02db\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2")
        buf.write("\u02dc\u0094\3\2\2\2\u02dd\u02db\3\2\2\2\u02de\u02df\7")
        buf.write(",\2\2\u02df\u02e0\7,\2\2\u02e0\u02e4\3\2\2\2\u02e1\u02e3")
        buf.write("\13\2\2\2\u02e2\u02e1\3\2\2\2\u02e3\u02e6\3\2\2\2\u02e4")
        buf.write("\u02e5\3\2\2\2\u02e4\u02e2\3\2\2\2\u02e5\u0096\3\2\2\2")
        buf.write("\u02e6\u02e4\3\2\2\2\u02e7\u02e8\7\62\2\2\u02e8\u02e9")
        buf.write("\t\22\2\2\u02e9\u0307\7\62\2\2\u02ea\u02eb\7\62\2\2\u02eb")
        buf.write("\u02ef\t\6\2\2\u02ec\u02ee\t\7\2\2\u02ed\u02ec\3\2\2\2")
        buf.write("\u02ee\u02f1\3\2\2\2\u02ef\u02ed\3\2\2\2\u02ef\u02f0\3")
        buf.write("\2\2\2\u02f0\u02f5\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f2\u02f4")
        buf.write("\n\b\2\2\u02f3\u02f2\3\2\2\2\u02f4\u02f7\3\2\2\2\u02f5")
        buf.write("\u02f3\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u0307\3\2\2\2")
        buf.write("\u02f7\u02f5\3\2\2\2\u02f8\u02f9\7\62\2\2\u02f9\u02fd")
        buf.write("\t\t\2\2\u02fa\u02fc\t\n\2\2\u02fb\u02fa\3\2\2\2\u02fc")
        buf.write("\u02ff\3\2\2\2\u02fd\u02fb\3\2\2\2\u02fd\u02fe\3\2\2\2")
        buf.write("\u02fe\u0303\3\2\2\2\u02ff\u02fd\3\2\2\2\u0300\u0302\n")
        buf.write("\13\2\2\u0301\u0300\3\2\2\2\u0302\u0305\3\2\2\2\u0303")
        buf.write("\u0301\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0307\3\2\2\2")
        buf.write("\u0305\u0303\3\2\2\2\u0306\u02e7\3\2\2\2\u0306\u02ea\3")
        buf.write("\2\2\2\u0306\u02f8\3\2\2\2\u0307\u0098\3\2\2\2E\2\u017a")
        buf.write("\u0183\u0189\u018b\u0193\u019c\u01a2\u01a7\u01ad\u01b3")
        buf.write("\u01b7\u01bc\u01c1\u01c7\u01cc\u01d1\u01d3\u01d7\u01dd")
        buf.write("\u01e4\u01e6\u01ef\u01f6\u01fc\u0203\u020a\u020f\u0215")
        buf.write("\u021c\u0222\u0229\u0230\u0235\u023b\u0242\u0248\u024f")
        buf.write("\u0256\u025b\u0261\u0268\u026e\u0275\u027c\u0281\u0287")
        buf.write("\u028e\u0294\u029b\u02a2\u02a7\u02aa\u02b1\u02bb\u02c8")
        buf.write("\u02ca\u02d1\u02d4\u02d9\u02db\u02e4\u02ef\u02f5\u02fd")
        buf.write("\u0303\u0306\3\b\2\2")
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
    TRUE = 21
    FALSE = 22
    ENDDO = 23
    ADD = 24
    F_ADD = 25
    SUB = 26
    F_SUB = 27
    MUL = 28
    F_MUL = 29
    DIV = 30
    F_DIV = 31
    REMAIN = 32
    NEG = 33
    AND = 34
    OR = 35
    EQ = 36
    NOT_EQ = 37
    LT = 38
    GT = 39
    LTE = 40
    GTE = 41
    F_NOT_EQ = 42
    F_LT = 43
    F_GT = 44
    F_LTE = 45
    F_GTE = 46
    SEMI = 47
    COLON = 48
    LP = 49
    RP = 50
    LS = 51
    RS = 52
    LB = 53
    RB = 54
    DOT = 55
    COMMA = 56
    ID = 57
    INT_LIT = 58
    FLOAT_LIT = 59
    BOOL_LIT = 60
    STRING_LIT = 61
    ARRAY_LIT = 62
    WS = 63
    COMMENT = 64
    ERROR_CHAR = 65
    ILLEGAL_ESCAPE = 66
    UNCLOSE_STRING = 67
    UNTERMINATED_COMMENT = 68
    ERROR_INTLIT = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'main'", "'Var'", "'Body'", "'Break'", "'Continue'", 
            "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
            "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
            "'Return'", "'Then'", "'While'", "'True'", "'False'", "'EndDo'", 
            "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "';'", 
            "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "WHILE", "TRUE", "FALSE", 
            "ENDDO", "ADD", "F_ADD", "SUB", "F_SUB", "MUL", "F_MUL", "DIV", 
            "F_DIV", "REMAIN", "NEG", "AND", "OR", "EQ", "NOT_EQ", "LT", 
            "GT", "LTE", "GTE", "F_NOT_EQ", "F_LT", "F_GT", "F_LTE", "F_GTE", 
            "SEMI", "COLON", "LP", "RP", "LS", "RS", "LB", "RB", "DOT", 
            "COMMA", "ID", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
            "ARRAY_LIT", "WS", "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_INTLIT" ]

    ruleNames = [ "T__0", "T__1", "VAR", "BODY", "BREAK", "CONTINUE", "DO", 
                  "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                  "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "ADD", "F_ADD", "SUB", 
                  "F_SUB", "MUL", "F_MUL", "DIV", "F_DIV", "REMAIN", "NEG", 
                  "AND", "OR", "EQ", "NOT_EQ", "LT", "GT", "LTE", "GTE", 
                  "F_NOT_EQ", "F_LT", "F_GT", "F_LTE", "F_GTE", "SEMI", 
                  "COLON", "LP", "RP", "LS", "RS", "LB", "RB", "DOT", "COMMA", 
                  "ID", "DIGIT", "DEC", "HEX", "OCT", "INT_LIT", "FLOAT_LIT", 
                  "BOOL_LIT", "ESC", "STR_CHAR", "STRING_LIT", "ARRAY_LIT", 
                  "WS", "COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "ERROR_INTLIT" ]

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
        elif tk == self.ARRAY_LIT:
            result.text = result.text.replace(" ", "")
        elif tk == self.ERROR_INTLIT:
            raise ErrorToken(result.text)
        else:
            return result;


