# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u02fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\13:\3;\3;\3<\5<\u0181\n<\3<\3<\7<\u0185\n<\f<\16<\u0188")
        buf.write("\13<\3<\6<\u018b\n<\r<\16<\u018c\5<\u018f\n<\3=\3=\3=")
        buf.write("\6=\u0194\n=\r=\16=\u0195\3>\3>\3>\6>\u019b\n>\r>\16>")
        buf.write("\u019c\3?\3?\3?\5?\u01a2\n?\3@\5@\u01a5\n@\3@\6@\u01a8")
        buf.write("\n@\r@\16@\u01a9\3@\3@\7@\u01ae\n@\f@\16@\u01b1\13@\3")
        buf.write("@\6@\u01b4\n@\r@\16@\u01b5\3@\3@\3@\6@\u01bb\n@\r@\16")
        buf.write("@\u01bc\3@\6@\u01c0\n@\r@\16@\u01c1\3@\3@\6@\u01c6\n@")
        buf.write("\r@\16@\u01c7\3@\3@\3@\6@\u01cd\n@\r@\16@\u01ce\5@\u01d1")
        buf.write("\n@\3A\3A\5A\u01d5\nA\3B\3B\3B\3B\5B\u01db\nB\3C\3C\3")
        buf.write("D\3D\3D\7D\u01e2\nD\fD\16D\u01e5\13D\3D\3D\3E\3E\7E\u01eb")
        buf.write("\nE\fE\16E\u01ee\13E\3E\3E\7E\u01f2\nE\fE\16E\u01f5\13")
        buf.write("E\3E\7E\u01f8\nE\fE\16E\u01fb\13E\3E\3E\7E\u01ff\nE\f")
        buf.write("E\16E\u0202\13E\3E\3E\7E\u0206\nE\fE\16E\u0209\13E\7E")
        buf.write("\u020b\nE\fE\16E\u020e\13E\3E\7E\u0211\nE\fE\16E\u0214")
        buf.write("\13E\3E\3E\7E\u0218\nE\fE\16E\u021b\13E\3E\7E\u021e\n")
        buf.write("E\fE\16E\u0221\13E\3E\3E\7E\u0225\nE\fE\16E\u0228\13E")
        buf.write("\3E\3E\7E\u022c\nE\fE\16E\u022f\13E\7E\u0231\nE\fE\16")
        buf.write("E\u0234\13E\3E\7E\u0237\nE\fE\16E\u023a\13E\3E\3E\7E\u023e")
        buf.write("\nE\fE\16E\u0241\13E\3E\7E\u0244\nE\fE\16E\u0247\13E\3")
        buf.write("E\3E\7E\u024b\nE\fE\16E\u024e\13E\3E\3E\7E\u0252\nE\f")
        buf.write("E\16E\u0255\13E\7E\u0257\nE\fE\16E\u025a\13E\3E\7E\u025d")
        buf.write("\nE\fE\16E\u0260\13E\3E\3E\7E\u0264\nE\fE\16E\u0267\13")
        buf.write("E\3E\7E\u026a\nE\fE\16E\u026d\13E\3E\3E\7E\u0271\nE\f")
        buf.write("E\16E\u0274\13E\3E\3E\7E\u0278\nE\fE\16E\u027b\13E\7E")
        buf.write("\u027d\nE\fE\16E\u0280\13E\3E\7E\u0283\nE\fE\16E\u0286")
        buf.write("\13E\3E\3E\7E\u028a\nE\fE\16E\u028d\13E\3E\7E\u0290\n")
        buf.write("E\fE\16E\u0293\13E\3E\3E\7E\u0297\nE\fE\16E\u029a\13E")
        buf.write("\3E\3E\7E\u029e\nE\fE\16E\u02a1\13E\7E\u02a3\nE\fE\16")
        buf.write("E\u02a6\13E\5E\u02a8\nE\3E\3E\3F\6F\u02ad\nF\rF\16F\u02ae")
        buf.write("\3F\3F\3G\3G\3G\3G\7G\u02b7\nG\fG\16G\u02ba\13G\3G\3G")
        buf.write("\3G\3G\3G\3H\3H\3I\3I\3I\7I\u02c6\nI\fI\16I\u02c9\13I")
        buf.write("\3I\3I\3I\5I\u02ce\nI\3J\3J\3J\7J\u02d3\nJ\fJ\16J\u02d6")
        buf.write("\13J\3K\3K\3K\3K\7K\u02dc\nK\fK\16K\u02df\13K\3L\3L\3")
        buf.write("L\7L\u02e4\nL\fL\16L\u02e7\13L\3L\7L\u02ea\nL\fL\16L\u02ed")
        buf.write("\13L\3L\3L\3L\7L\u02f2\nL\fL\16L\u02f5\13L\3L\7L\u02f8")
        buf.write("\nL\fL\16L\u02fb\13L\5L\u02fd\nL\4\u02b8\u02dd\2M\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2")
        buf.write("w\2y\2{\2}<\177=\u0081>\u0083\2\u0085\2\u0087?\u0089@")
        buf.write("\u008bA\u008dB\u008fC\u0091D\u0093E\u0095F\u0097G\3\2")
        buf.write("\17\3\2c|\6\2\62;C\\aac|\3\2\62;\4\2--//\3\2\63;\4\2Z")
        buf.write("Zzz\4\2\62;CH\4\2QQqq\3\2\629\4\2GGgg\t\2))^^ddhhpptt")
        buf.write("vv\7\2\n\f\16\17$$))^^\5\2\13\f\17\17\"\"\2\u033d\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
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
        buf.write("u\u017d\3\2\2\2w\u018e\3\2\2\2y\u0190\3\2\2\2{\u0197\3")
        buf.write("\2\2\2}\u01a1\3\2\2\2\177\u01a4\3\2\2\2\u0081\u01d4\3")
        buf.write("\2\2\2\u0083\u01da\3\2\2\2\u0085\u01dc\3\2\2\2\u0087\u01de")
        buf.write("\3\2\2\2\u0089\u01e8\3\2\2\2\u008b\u02ac\3\2\2\2\u008d")
        buf.write("\u02b2\3\2\2\2\u008f\u02c0\3\2\2\2\u0091\u02c2\3\2\2\2")
        buf.write("\u0093\u02cf\3\2\2\2\u0095\u02d7\3\2\2\2\u0097\u02fc\3")
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
        buf.write("\u0181\t\5\2\2\u0180\u017f\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0186\t\6\2\2\u0183\u0185\5")
        buf.write("u;\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018f\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0189\u018b\7\62\2\2\u018a\u0189\3\2\2")
        buf.write("\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u0180\3\2\2\2\u018e")
        buf.write("\u018a\3\2\2\2\u018fx\3\2\2\2\u0190\u0191\7\62\2\2\u0191")
        buf.write("\u0193\t\7\2\2\u0192\u0194\t\b\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196z\3\2\2\2\u0197\u0198\7\62\2\2\u0198\u019a")
        buf.write("\t\t\2\2\u0199\u019b\t\n\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d|\3\2\2\2\u019e\u01a2\5w<\2\u019f\u01a2\5y=\2\u01a0")
        buf.write("\u01a2\5{>\2\u01a1\u019e\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2~\3\2\2\2\u01a3\u01a5\t\5\2\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01d0\3\2\2\2")
        buf.write("\u01a6\u01a8\5u;\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2")
        buf.write("\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab\u01af\7\60\2\2\u01ac\u01ae\5u;\2\u01ad")
        buf.write("\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01d1\3\2\2\2\u01b1\u01af\3")
        buf.write("\2\2\2\u01b2\u01b4\5u;\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b8\t\13\2\2\u01b8\u01ba\t\5\2")
        buf.write("\2\u01b9\u01bb\5u;\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01d1")
        buf.write("\3\2\2\2\u01be\u01c0\5u;\2\u01bf\u01be\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01c5\7\60\2\2\u01c4\u01c6\5u;\2")
        buf.write("\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca")
        buf.write("\t\13\2\2\u01ca\u01cc\t\5\2\2\u01cb\u01cd\5u;\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01a7\3")
        buf.write("\2\2\2\u01d0\u01b3\3\2\2\2\u01d0\u01bf\3\2\2\2\u01d1\u0080")
        buf.write("\3\2\2\2\u01d2\u01d5\5+\26\2\u01d3\u01d5\5-\27\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u0082\3\2\2\2")
        buf.write("\u01d6\u01d7\7^\2\2\u01d7\u01db\t\f\2\2\u01d8\u01d9\7")
        buf.write(")\2\2\u01d9\u01db\7$\2\2\u01da\u01d6\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u0084\3\2\2\2\u01dc\u01dd\n\r\2\2\u01dd")
        buf.write("\u0086\3\2\2\2\u01de\u01e3\7$\2\2\u01df\u01e2\5\u0085")
        buf.write("C\2\u01e0\u01e2\5\u0083B\2\u01e1\u01df\3\2\2\2\u01e1\u01e0")
        buf.write("\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3")
        buf.write("\u01e4\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e6\u01e7\7$\2\2\u01e7\u0088\3\2\2\2\u01e8\u02a7\5")
        buf.write("k\66\2\u01e9\u01eb\7\"\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f3\5\u0081")
        buf.write("A\2\u01f0\u01f2\7\"\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f5")
        buf.write("\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u020c\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f8\7\"\2\2")
        buf.write("\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01f9")
        buf.write("\3\2\2\2\u01fc\u0200\5q9\2\u01fd\u01ff\7\"\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0203\u0207\5\u0081A\2\u0204\u0206\7\"\2\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0208\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2")
        buf.write("\u020a\u01f9\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3")
        buf.write("\2\2\2\u020c\u020d\3\2\2\2\u020d\u02a8\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020f\u0211\7\"\2\2\u0210\u020f\3\2\2\2\u0211")
        buf.write("\u0214\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213\3\2\2\2")
        buf.write("\u0213\u0215\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0219\5")
        buf.write("}?\2\u0216\u0218\7\"\2\2\u0217\u0216\3\2\2\2\u0218\u021b")
        buf.write("\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a")
        buf.write("\u0232\3\2\2\2\u021b\u0219\3\2\2\2\u021c\u021e\7\"\2\2")
        buf.write("\u021d\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d\3")
        buf.write("\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222\3\2\2\2\u0221\u021f")
        buf.write("\3\2\2\2\u0222\u0226\5q9\2\u0223\u0225\7\"\2\2\u0224\u0223")
        buf.write("\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0229\u022d\5}?\2\u022a\u022c\7\"\2\2\u022b\u022a\3\2")
        buf.write("\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u0230")
        buf.write("\u021f\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0232\u0233\3\2\2\2\u0233\u02a8\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0235\u0237\7\"\2\2\u0236\u0235\3\2\2\2\u0237\u023a")
        buf.write("\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239")
        buf.write("\u023b\3\2\2\2\u023a\u0238\3\2\2\2\u023b\u023f\5\177@")
        buf.write("\2\u023c\u023e\7\"\2\2\u023d\u023c\3\2\2\2\u023e\u0241")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240")
        buf.write("\u0258\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0244\7\"\2\2")
        buf.write("\u0243\u0242\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243\3")
        buf.write("\2\2\2\u0245\u0246\3\2\2\2\u0246\u0248\3\2\2\2\u0247\u0245")
        buf.write("\3\2\2\2\u0248\u024c\5q9\2\u0249\u024b\7\"\2\2\u024a\u0249")
        buf.write("\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024c")
        buf.write("\u024d\3\2\2\2\u024d\u024f\3\2\2\2\u024e\u024c\3\2\2\2")
        buf.write("\u024f\u0253\5\177@\2\u0250\u0252\7\"\2\2\u0251\u0250")
        buf.write("\3\2\2\2\u0252\u0255\3\2\2\2\u0253\u0251\3\2\2\2\u0253")
        buf.write("\u0254\3\2\2\2\u0254\u0257\3\2\2\2\u0255\u0253\3\2\2\2")
        buf.write("\u0256\u0245\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3")
        buf.write("\2\2\2\u0258\u0259\3\2\2\2\u0259\u02a8\3\2\2\2\u025a\u0258")
        buf.write("\3\2\2\2\u025b\u025d\7\"\2\2\u025c\u025b\3\2\2\2\u025d")
        buf.write("\u0260\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025f\3\2\2\2")
        buf.write("\u025f\u0261\3\2\2\2\u0260\u025e\3\2\2\2\u0261\u0265\5")
        buf.write("\u0087D\2\u0262\u0264\7\"\2\2\u0263\u0262\3\2\2\2\u0264")
        buf.write("\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2")
        buf.write("\u0266\u027e\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u026a\7")
        buf.write("\"\2\2\u0269\u0268\3\2\2\2\u026a\u026d\3\2\2\2\u026b\u0269")
        buf.write("\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026e\3\2\2\2\u026d")
        buf.write("\u026b\3\2\2\2\u026e\u0272\5q9\2\u026f\u0271\7\"\2\2\u0270")
        buf.write("\u026f\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2")
        buf.write("\u0272\u0273\3\2\2\2\u0273\u0275\3\2\2\2\u0274\u0272\3")
        buf.write("\2\2\2\u0275\u0279\5\u0087D\2\u0276\u0278\7\"\2\2\u0277")
        buf.write("\u0276\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2")
        buf.write("\u0279\u027a\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027c\u026b\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c")
        buf.write("\3\2\2\2\u027e\u027f\3\2\2\2\u027f\u02a8\3\2\2\2\u0280")
        buf.write("\u027e\3\2\2\2\u0281\u0283\7\"\2\2\u0282\u0281\3\2\2\2")
        buf.write("\u0283\u0286\3\2\2\2\u0284\u0282\3\2\2\2\u0284\u0285\3")
        buf.write("\2\2\2\u0285\u0287\3\2\2\2\u0286\u0284\3\2\2\2\u0287\u028b")
        buf.write("\5\u0089E\2\u0288\u028a\7\"\2\2\u0289\u0288\3\2\2\2\u028a")
        buf.write("\u028d\3\2\2\2\u028b\u0289\3\2\2\2\u028b\u028c\3\2\2\2")
        buf.write("\u028c\u02a4\3\2\2\2\u028d\u028b\3\2\2\2\u028e\u0290\7")
        buf.write("\"\2\2\u028f\u028e\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f")
        buf.write("\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0294\3\2\2\2\u0293")
        buf.write("\u0291\3\2\2\2\u0294\u0298\5q9\2\u0295\u0297\7\"\2\2\u0296")
        buf.write("\u0295\3\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296\3\2\2\2")
        buf.write("\u0298\u0299\3\2\2\2\u0299\u029b\3\2\2\2\u029a\u0298\3")
        buf.write("\2\2\2\u029b\u029f\5\u0089E\2\u029c\u029e\7\"\2\2\u029d")
        buf.write("\u029c\3\2\2\2\u029e\u02a1\3\2\2\2\u029f\u029d\3\2\2\2")
        buf.write("\u029f\u02a0\3\2\2\2\u02a0\u02a3\3\2\2\2\u02a1\u029f\3")
        buf.write("\2\2\2\u02a2\u0291\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2")
        buf.write("\3\2\2\2\u02a4\u02a5\3\2\2\2\u02a5\u02a8\3\2\2\2\u02a6")
        buf.write("\u02a4\3\2\2\2\u02a7\u01ec\3\2\2\2\u02a7\u0212\3\2\2\2")
        buf.write("\u02a7\u0238\3\2\2\2\u02a7\u025e\3\2\2\2\u02a7\u0284\3")
        buf.write("\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02aa\5m\67\2\u02aa\u008a")
        buf.write("\3\2\2\2\u02ab\u02ad\t\16\2\2\u02ac\u02ab\3\2\2\2\u02ad")
        buf.write("\u02ae\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02af\3\2\2\2")
        buf.write("\u02af\u02b0\3\2\2\2\u02b0\u02b1\bF\2\2\u02b1\u008c\3")
        buf.write("\2\2\2\u02b2\u02b3\7,\2\2\u02b3\u02b4\7,\2\2\u02b4\u02b8")
        buf.write("\3\2\2\2\u02b5\u02b7\13\2\2\2\u02b6\u02b5\3\2\2\2\u02b7")
        buf.write("\u02ba\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b8\u02b6\3\2\2\2")
        buf.write("\u02b9\u02bb\3\2\2\2\u02ba\u02b8\3\2\2\2\u02bb\u02bc\7")
        buf.write(",\2\2\u02bc\u02bd\7,\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf")
        buf.write("\bG\2\2\u02bf\u008e\3\2\2\2\u02c0\u02c1\13\2\2\2\u02c1")
        buf.write("\u0090\3\2\2\2\u02c2\u02c7\7$\2\2\u02c3\u02c6\5\u0085")
        buf.write("C\2\u02c4\u02c6\5\u0083B\2\u02c5\u02c3\3\2\2\2\u02c5\u02c4")
        buf.write("\3\2\2\2\u02c6\u02c9\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c7")
        buf.write("\u02c8\3\2\2\2\u02c8\u02ca\3\2\2\2\u02c9\u02c7\3\2\2\2")
        buf.write("\u02ca\u02cb\7^\2\2\u02cb\u02cd\n\f\2\2\u02cc\u02ce\7")
        buf.write("$\2\2\u02cd\u02cc\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u0092")
        buf.write("\3\2\2\2\u02cf\u02d4\7$\2\2\u02d0\u02d3\5\u0085C\2\u02d1")
        buf.write("\u02d3\5\u0083B\2\u02d2\u02d0\3\2\2\2\u02d2\u02d1\3\2")
        buf.write("\2\2\u02d3\u02d6\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d4\u02d5")
        buf.write("\3\2\2\2\u02d5\u0094\3\2\2\2\u02d6\u02d4\3\2\2\2\u02d7")
        buf.write("\u02d8\7,\2\2\u02d8\u02d9\7,\2\2\u02d9\u02dd\3\2\2\2\u02da")
        buf.write("\u02dc\13\2\2\2\u02db\u02da\3\2\2\2\u02dc\u02df\3\2\2")
        buf.write("\2\u02dd\u02de\3\2\2\2\u02dd\u02db\3\2\2\2\u02de\u0096")
        buf.write("\3\2\2\2\u02df\u02dd\3\2\2\2\u02e0\u02e1\7\62\2\2\u02e1")
        buf.write("\u02e5\t\7\2\2\u02e2\u02e4\t\b\2\2\u02e3\u02e2\3\2\2\2")
        buf.write("\u02e4\u02e7\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e5\u02e6\3")
        buf.write("\2\2\2\u02e6\u02eb\3\2\2\2\u02e7\u02e5\3\2\2\2\u02e8\u02ea")
        buf.write("\n\b\2\2\u02e9\u02e8\3\2\2\2\u02ea\u02ed\3\2\2\2\u02eb")
        buf.write("\u02e9\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02fd\3\2\2\2")
        buf.write("\u02ed\u02eb\3\2\2\2\u02ee\u02ef\7\62\2\2\u02ef\u02f3")
        buf.write("\t\t\2\2\u02f0\u02f2\t\n\2\2\u02f1\u02f0\3\2\2\2\u02f2")
        buf.write("\u02f5\3\2\2\2\u02f3\u02f1\3\2\2\2\u02f3\u02f4\3\2\2\2")
        buf.write("\u02f4\u02f9\3\2\2\2\u02f5\u02f3\3\2\2\2\u02f6\u02f8\n")
        buf.write("\n\2\2\u02f7\u02f6\3\2\2\2\u02f8\u02fb\3\2\2\2\u02f9\u02f7")
        buf.write("\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02fd\3\2\2\2\u02fb")
        buf.write("\u02f9\3\2\2\2\u02fc\u02e0\3\2\2\2\u02fc\u02ee\3\2\2\2")
        buf.write("\u02fd\u0098\3\2\2\2D\2\u017a\u0180\u0186\u018c\u018e")
        buf.write("\u0195\u019c\u01a1\u01a4\u01a9\u01af\u01b5\u01bc\u01c1")
        buf.write("\u01c7\u01ce\u01d0\u01d4\u01da\u01e1\u01e3\u01ec\u01f3")
        buf.write("\u01f9\u0200\u0207\u020c\u0212\u0219\u021f\u0226\u022d")
        buf.write("\u0232\u0238\u023f\u0245\u024c\u0253\u0258\u025e\u0265")
        buf.write("\u026b\u0272\u0279\u027e\u0284\u028b\u0291\u0298\u029f")
        buf.write("\u02a4\u02a7\u02ae\u02b8\u02c5\u02c7\u02cd\u02d2\u02d4")
        buf.write("\u02dd\u02e5\u02eb\u02f3\u02f9\u02fc\3\b\2\2")
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
        elif tk == self.ERROR_INTLIT:
            raise ErrorToken(result.text)
        else:
            return result;


