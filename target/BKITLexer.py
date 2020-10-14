# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u030e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3=\7=\u0195\n=\f=\16=\u0198\13=\3>\3>\3>\3>\7>\u019e")
        buf.write("\n>\f>\16>\u01a1\13>\3?\3?\3?\5?\u01a6\n?\3@\5@\u01a9")
        buf.write("\n@\3@\6@\u01ac\n@\r@\16@\u01ad\3@\3@\7@\u01b2\n@\f@\16")
        buf.write("@\u01b5\13@\3@\6@\u01b8\n@\r@\16@\u01b9\3@\3@\5@\u01be")
        buf.write("\n@\3@\6@\u01c1\n@\r@\16@\u01c2\3@\6@\u01c6\n@\r@\16@")
        buf.write("\u01c7\3@\3@\7@\u01cc\n@\f@\16@\u01cf\13@\3@\3@\5@\u01d3")
        buf.write("\n@\3@\6@\u01d6\n@\r@\16@\u01d7\5@\u01da\n@\3A\3A\5A\u01de")
        buf.write("\nA\3B\3B\3B\3B\5B\u01e4\nB\3C\3C\3D\3D\3D\7D\u01eb\n")
        buf.write("D\fD\16D\u01ee\13D\3D\3D\3E\3E\7E\u01f4\nE\fE\16E\u01f7")
        buf.write("\13E\3E\3E\7E\u01fb\nE\fE\16E\u01fe\13E\3E\7E\u0201\n")
        buf.write("E\fE\16E\u0204\13E\3E\3E\7E\u0208\nE\fE\16E\u020b\13E")
        buf.write("\3E\3E\7E\u020f\nE\fE\16E\u0212\13E\7E\u0214\nE\fE\16")
        buf.write("E\u0217\13E\3E\7E\u021a\nE\fE\16E\u021d\13E\3E\3E\7E\u0221")
        buf.write("\nE\fE\16E\u0224\13E\3E\7E\u0227\nE\fE\16E\u022a\13E\3")
        buf.write("E\3E\7E\u022e\nE\fE\16E\u0231\13E\3E\3E\7E\u0235\nE\f")
        buf.write("E\16E\u0238\13E\7E\u023a\nE\fE\16E\u023d\13E\3E\7E\u0240")
        buf.write("\nE\fE\16E\u0243\13E\3E\3E\7E\u0247\nE\fE\16E\u024a\13")
        buf.write("E\3E\7E\u024d\nE\fE\16E\u0250\13E\3E\3E\7E\u0254\nE\f")
        buf.write("E\16E\u0257\13E\3E\3E\7E\u025b\nE\fE\16E\u025e\13E\7E")
        buf.write("\u0260\nE\fE\16E\u0263\13E\3E\7E\u0266\nE\fE\16E\u0269")
        buf.write("\13E\3E\3E\7E\u026d\nE\fE\16E\u0270\13E\3E\7E\u0273\n")
        buf.write("E\fE\16E\u0276\13E\3E\3E\7E\u027a\nE\fE\16E\u027d\13E")
        buf.write("\3E\3E\7E\u0281\nE\fE\16E\u0284\13E\7E\u0286\nE\fE\16")
        buf.write("E\u0289\13E\3E\7E\u028c\nE\fE\16E\u028f\13E\3E\3E\7E\u0293")
        buf.write("\nE\fE\16E\u0296\13E\3E\7E\u0299\nE\fE\16E\u029c\13E\3")
        buf.write("E\3E\7E\u02a0\nE\fE\16E\u02a3\13E\3E\3E\7E\u02a7\nE\f")
        buf.write("E\16E\u02aa\13E\7E\u02ac\nE\fE\16E\u02af\13E\5E\u02b1")
        buf.write("\nE\3E\3E\3F\6F\u02b6\nF\rF\16F\u02b7\3F\3F\3G\3G\3G\3")
        buf.write("G\7G\u02c0\nG\fG\16G\u02c3\13G\3G\3G\3G\3G\3G\3H\3H\3")
        buf.write("I\3I\3I\7I\u02cf\nI\fI\16I\u02d2\13I\3I\3I\3I\3I\5I\u02d8")
        buf.write("\nI\3I\5I\u02db\nI\3J\3J\3J\7J\u02e0\nJ\fJ\16J\u02e3\13")
        buf.write("J\3K\3K\3K\3K\7K\u02e9\nK\fK\16K\u02ec\13K\3L\3L\3L\3")
        buf.write("L\3L\3L\7L\u02f4\nL\fL\16L\u02f7\13L\3L\7L\u02fa\nL\f")
        buf.write("L\16L\u02fd\13L\3L\3L\3L\7L\u0302\nL\fL\16L\u0305\13L")
        buf.write("\3L\7L\u0308\nL\fL\16L\u030b\13L\5L\u030d\nL\4\u02c1\u02ea")
        buf.write("\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u\2w\2y\2{\2}<\177=\u0081>\u0083\2\u0085\2\u0087?\u0089")
        buf.write("@\u008bA\u008dB\u008fC\u0091D\u0093E\u0095F\u0097G\3\2")
        buf.write("\23\3\2c|\6\2\62;C\\aac|\3\2\62;\4\2--//\3\2\63;\4\2Z")
        buf.write("Zzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GG")
        buf.write("gg\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\5\2\13\f\17\17")
        buf.write("\"\"\3\2$$\6\2QQZZqqzz\2\u0351\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2\2\7\u00a0")
        buf.write("\3\2\2\2\t\u00a4\3\2\2\2\13\u00a9\3\2\2\2\r\u00af\3\2")
        buf.write("\2\2\17\u00b8\3\2\2\2\21\u00bb\3\2\2\2\23\u00c0\3\2\2")
        buf.write("\2\25\u00c7\3\2\2\2\27\u00cf\3\2\2\2\31\u00d5\3\2\2\2")
        buf.write("\33\u00dc\3\2\2\2\35\u00e5\3\2\2\2\37\u00e9\3\2\2\2!\u00f2")
        buf.write("\3\2\2\2#\u00f5\3\2\2\2%\u00ff\3\2\2\2\'\u0106\3\2\2\2")
        buf.write(")\u010b\3\2\2\2+\u0111\3\2\2\2-\u0116\3\2\2\2/\u011c\3")
        buf.write("\2\2\2\61\u0122\3\2\2\2\63\u0124\3\2\2\2\65\u0127\3\2")
        buf.write("\2\2\67\u0129\3\2\2\29\u012c\3\2\2\2;\u012e\3\2\2\2=\u0131")
        buf.write("\3\2\2\2?\u0133\3\2\2\2A\u0136\3\2\2\2C\u0138\3\2\2\2")
        buf.write("E\u013a\3\2\2\2G\u013d\3\2\2\2I\u0140\3\2\2\2K\u0143\3")
        buf.write("\2\2\2M\u0146\3\2\2\2O\u0148\3\2\2\2Q\u014a\3\2\2\2S\u014d")
        buf.write("\3\2\2\2U\u0150\3\2\2\2W\u0154\3\2\2\2Y\u0157\3\2\2\2")
        buf.write("[\u015a\3\2\2\2]\u015e\3\2\2\2_\u0162\3\2\2\2a\u0164\3")
        buf.write("\2\2\2c\u0166\3\2\2\2e\u0168\3\2\2\2g\u016a\3\2\2\2i\u016c")
        buf.write("\3\2\2\2k\u016e\3\2\2\2m\u0170\3\2\2\2o\u0172\3\2\2\2")
        buf.write("q\u0174\3\2\2\2s\u0176\3\2\2\2u\u017d\3\2\2\2w\u018e\3")
        buf.write("\2\2\2y\u0190\3\2\2\2{\u0199\3\2\2\2}\u01a5\3\2\2\2\177")
        buf.write("\u01a8\3\2\2\2\u0081\u01dd\3\2\2\2\u0083\u01e3\3\2\2\2")
        buf.write("\u0085\u01e5\3\2\2\2\u0087\u01e7\3\2\2\2\u0089\u01f1\3")
        buf.write("\2\2\2\u008b\u02b5\3\2\2\2\u008d\u02bb\3\2\2\2\u008f\u02c9")
        buf.write("\3\2\2\2\u0091\u02cb\3\2\2\2\u0093\u02dc\3\2\2\2\u0095")
        buf.write("\u02e4\3\2\2\2\u0097\u030c\3\2\2\2\u0099\u009a\7?\2\2")
        buf.write("\u009a\4\3\2\2\2\u009b\u009c\7o\2\2\u009c\u009d\7c\2\2")
        buf.write("\u009d\u009e\7k\2\2\u009e\u009f\7p\2\2\u009f\6\3\2\2\2")
        buf.write("\u00a0\u00a1\7X\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7t")
        buf.write("\2\2\u00a3\b\3\2\2\2\u00a4\u00a5\7D\2\2\u00a5\u00a6\7")
        buf.write("q\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8\7{\2\2\u00a8\n\3")
        buf.write("\2\2\2\u00a9\u00aa\7D\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7m\2\2\u00ae\f")
        buf.write("\3\2\2\2\u00af\u00b0\7E\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7g\2\2\u00b7\16")
        buf.write("\3\2\2\2\u00b8\u00b9\7F\2\2\u00b9\u00ba\7q\2\2\u00ba\20")
        buf.write("\3\2\2\2\u00bb\u00bc\7G\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be")
        buf.write("\7u\2\2\u00be\u00bf\7g\2\2\u00bf\22\3\2\2\2\u00c0\u00c1")
        buf.write("\7G\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\u00c5\7K\2\2\u00c5\u00c6\7h\2\2\u00c6\24")
        buf.write("\3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd")
        buf.write("\7f\2\2\u00cd\u00ce\7{\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\7G\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3")
        buf.write("\7K\2\2\u00d3\u00d4\7h\2\2\u00d4\30\3\2\2\2\u00d5\u00d6")
        buf.write("\7G\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7f\2\2\u00d8\u00d9")
        buf.write("\7H\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7t\2\2\u00db\32")
        buf.write("\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7f\2\2\u00df\u00e0\7Y\2\2\u00e0\u00e1\7j\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4\7g\2\2\u00e4\34")
        buf.write("\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8\36\3\2\2\2\u00e9\u00ea\7H\2\2\u00ea\u00eb")
        buf.write("\7w\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1 \3\2\2\2\u00f2\u00f3\7K\2\2\u00f3\u00f4")
        buf.write("\7h\2\2\u00f4\"\3\2\2\2\u00f5\u00f6\7R\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7o\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7t\2\2\u00fe$\3\2\2\2\u00ff\u0100")
        buf.write("\7T\2\2\u0100\u0101\7g\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105\7p\2\2\u0105&\3")
        buf.write("\2\2\2\u0106\u0107\7V\2\2\u0107\u0108\7j\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7p\2\2\u010a(\3\2\2\2\u010b\u010c")
        buf.write("\7Y\2\2\u010c\u010d\7j\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7g\2\2\u0110*\3\2\2\2\u0111\u0112")
        buf.write("\7V\2\2\u0112\u0113\7t\2\2\u0113\u0114\7w\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115,\3\2\2\2\u0116\u0117\7H\2\2\u0117\u0118")
        buf.write("\7c\2\2\u0118\u0119\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b")
        buf.write("\7g\2\2\u011b.\3\2\2\2\u011c\u011d\7G\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7f\2\2\u011f\u0120\7F\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\60\3\2\2\2\u0122\u0123\7-\2\2\u0123\62\3")
        buf.write("\2\2\2\u0124\u0125\7-\2\2\u0125\u0126\7\60\2\2\u0126\64")
        buf.write("\3\2\2\2\u0127\u0128\7/\2\2\u0128\66\3\2\2\2\u0129\u012a")
        buf.write("\7/\2\2\u012a\u012b\7\60\2\2\u012b8\3\2\2\2\u012c\u012d")
        buf.write("\7,\2\2\u012d:\3\2\2\2\u012e\u012f\7,\2\2\u012f\u0130")
        buf.write("\7\60\2\2\u0130<\3\2\2\2\u0131\u0132\7^\2\2\u0132>\3\2")
        buf.write("\2\2\u0133\u0134\7^\2\2\u0134\u0135\7\60\2\2\u0135@\3")
        buf.write("\2\2\2\u0136\u0137\7\'\2\2\u0137B\3\2\2\2\u0138\u0139")
        buf.write("\7#\2\2\u0139D\3\2\2\2\u013a\u013b\7(\2\2\u013b\u013c")
        buf.write("\7(\2\2\u013cF\3\2\2\2\u013d\u013e\7~\2\2\u013e\u013f")
        buf.write("\7~\2\2\u013fH\3\2\2\2\u0140\u0141\7?\2\2\u0141\u0142")
        buf.write("\7?\2\2\u0142J\3\2\2\2\u0143\u0144\7#\2\2\u0144\u0145")
        buf.write("\7?\2\2\u0145L\3\2\2\2\u0146\u0147\7>\2\2\u0147N\3\2\2")
        buf.write("\2\u0148\u0149\7@\2\2\u0149P\3\2\2\2\u014a\u014b\7>\2")
        buf.write("\2\u014b\u014c\7?\2\2\u014cR\3\2\2\2\u014d\u014e\7@\2")
        buf.write("\2\u014e\u014f\7?\2\2\u014fT\3\2\2\2\u0150\u0151\7?\2")
        buf.write("\2\u0151\u0152\7\61\2\2\u0152\u0153\7?\2\2\u0153V\3\2")
        buf.write("\2\2\u0154\u0155\7>\2\2\u0155\u0156\7\60\2\2\u0156X\3")
        buf.write("\2\2\2\u0157\u0158\7@\2\2\u0158\u0159\7\60\2\2\u0159Z")
        buf.write("\3\2\2\2\u015a\u015b\7>\2\2\u015b\u015c\7?\2\2\u015c\u015d")
        buf.write("\7\60\2\2\u015d\\\3\2\2\2\u015e\u015f\7@\2\2\u015f\u0160")
        buf.write("\7?\2\2\u0160\u0161\7\60\2\2\u0161^\3\2\2\2\u0162\u0163")
        buf.write("\7=\2\2\u0163`\3\2\2\2\u0164\u0165\7<\2\2\u0165b\3\2\2")
        buf.write("\2\u0166\u0167\7*\2\2\u0167d\3\2\2\2\u0168\u0169\7+\2")
        buf.write("\2\u0169f\3\2\2\2\u016a\u016b\7]\2\2\u016bh\3\2\2\2\u016c")
        buf.write("\u016d\7_\2\2\u016dj\3\2\2\2\u016e\u016f\7}\2\2\u016f")
        buf.write("l\3\2\2\2\u0170\u0171\7\177\2\2\u0171n\3\2\2\2\u0172\u0173")
        buf.write("\7\60\2\2\u0173p\3\2\2\2\u0174\u0175\7.\2\2\u0175r\3\2")
        buf.write("\2\2\u0176\u017a\t\2\2\2\u0177\u0179\t\3\2\2\u0178\u0177")
        buf.write("\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017bt\3\2\2\2\u017c\u017a\3\2\2\2\u017d")
        buf.write("\u017e\t\4\2\2\u017ev\3\2\2\2\u017f\u0181\t\5\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0186\t\6\2\2\u0183\u0185\5u;\2\u0184\u0183\3\2")
        buf.write("\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u018f\3\2\2\2\u0188\u0186\3\2\2\2\u0189")
        buf.write("\u018b\7\62\2\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2")
        buf.write("\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f")
        buf.write("\3\2\2\2\u018e\u0180\3\2\2\2\u018e\u018a\3\2\2\2\u018f")
        buf.write("x\3\2\2\2\u0190\u0191\7\62\2\2\u0191\u0192\t\7\2\2\u0192")
        buf.write("\u0196\t\b\2\2\u0193\u0195\t\t\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197z\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a")
        buf.write("\7\62\2\2\u019a\u019b\t\n\2\2\u019b\u019f\t\13\2\2\u019c")
        buf.write("\u019e\t\f\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0|\3\2\2")
        buf.write("\2\u01a1\u019f\3\2\2\2\u01a2\u01a6\5w<\2\u01a3\u01a6\5")
        buf.write("y=\2\u01a4\u01a6\5{>\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6~\3\2\2\2\u01a7\u01a9")
        buf.write("\t\5\2\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01d9\3\2\2\2\u01aa\u01ac\5u;\2\u01ab\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b3\7\60\2\2\u01b0\u01b2")
        buf.write("\5u;\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01da\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b8\5u;\2\u01b7\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bb\u01bd\t\r\2\2\u01bc\u01be\t")
        buf.write("\5\2\2\u01bd\u01bc\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0")
        buf.write("\3\2\2\2\u01bf\u01c1\5u;\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01da\3\2\2\2\u01c4\u01c6\5u;\2\u01c5\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9\u01cd\7\60\2\2\u01ca\u01cc")
        buf.write("\5u;\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01d0\u01d2\t\r\2\2\u01d1\u01d3\t\5\2\2")
        buf.write("\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3")
        buf.write("\2\2\2\u01d4\u01d6\5u;\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8")
        buf.write("\u01da\3\2\2\2\u01d9\u01ab\3\2\2\2\u01d9\u01b7\3\2\2\2")
        buf.write("\u01d9\u01c5\3\2\2\2\u01da\u0080\3\2\2\2\u01db\u01de\5")
        buf.write("+\26\2\u01dc\u01de\5-\27\2\u01dd\u01db\3\2\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u0082\3\2\2\2\u01df\u01e0\7^\2\2\u01e0")
        buf.write("\u01e4\t\16\2\2\u01e1\u01e2\7)\2\2\u01e2\u01e4\7$\2\2")
        buf.write("\u01e3\u01df\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u0084\3")
        buf.write("\2\2\2\u01e5\u01e6\n\17\2\2\u01e6\u0086\3\2\2\2\u01e7")
        buf.write("\u01ec\7$\2\2\u01e8\u01eb\5\u0085C\2\u01e9\u01eb\5\u0083")
        buf.write("B\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f0\7$\2\2")
        buf.write("\u01f0\u0088\3\2\2\2\u01f1\u02b0\5k\66\2\u01f2\u01f4\7")
        buf.write("\"\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f8\u01fc\5\u0081A\2\u01f9\u01fb\7\"")
        buf.write("\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u0215\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01ff\u0201\7\"\2\2\u0200\u01ff\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0209")
        buf.write("\5q9\2\u0206\u0208\7\"\2\2\u0207\u0206\3\2\2\2\u0208\u020b")
        buf.write("\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u020c\3\2\2\2\u020b\u0209\3\2\2\2\u020c\u0210\5\u0081")
        buf.write("A\2\u020d\u020f\7\"\2\2\u020e\u020d\3\2\2\2\u020f\u0212")
        buf.write("\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0214\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0202\3\2\2\2")
        buf.write("\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3")
        buf.write("\2\2\2\u0216\u02b1\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021a")
        buf.write("\7\"\2\2\u0219\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b")
        buf.write("\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021e\u0222\5}?\2\u021f\u0221\7\"")
        buf.write("\2\2\u0220\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u023b\3\2\2\2\u0224")
        buf.write("\u0222\3\2\2\2\u0225\u0227\7\"\2\2\u0226\u0225\3\2\2\2")
        buf.write("\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3")
        buf.write("\2\2\2\u0229\u022b\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022f")
        buf.write("\5q9\2\u022c\u022e\7\"\2\2\u022d\u022c\3\2\2\2\u022e\u0231")
        buf.write("\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\u0232\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0236\5}?\2\u0233")
        buf.write("\u0235\7\"\2\2\u0234\u0233\3\2\2\2\u0235\u0238\3\2\2\2")
        buf.write("\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u023a\3")
        buf.write("\2\2\2\u0238\u0236\3\2\2\2\u0239\u0228\3\2\2\2\u023a\u023d")
        buf.write("\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u02b1\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u0240\7\"\2\2")
        buf.write("\u023f\u023e\3\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f\3")
        buf.write("\2\2\2\u0241\u0242\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0241")
        buf.write("\3\2\2\2\u0244\u0248\5\177@\2\u0245\u0247\7\"\2\2\u0246")
        buf.write("\u0245\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2")
        buf.write("\u0248\u0249\3\2\2\2\u0249\u0261\3\2\2\2\u024a\u0248\3")
        buf.write("\2\2\2\u024b\u024d\7\"\2\2\u024c\u024b\3\2\2\2\u024d\u0250")
        buf.write("\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u0251\3\2\2\2\u0250\u024e\3\2\2\2\u0251\u0255\5q9\2\u0252")
        buf.write("\u0254\7\"\2\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2\2\2")
        buf.write("\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0258\3")
        buf.write("\2\2\2\u0257\u0255\3\2\2\2\u0258\u025c\5\177@\2\u0259")
        buf.write("\u025b\7\"\2\2\u025a\u0259\3\2\2\2\u025b\u025e\3\2\2\2")
        buf.write("\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u0260\3")
        buf.write("\2\2\2\u025e\u025c\3\2\2\2\u025f\u024e\3\2\2\2\u0260\u0263")
        buf.write("\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262")
        buf.write("\u02b1\3\2\2\2\u0263\u0261\3\2\2\2\u0264\u0266\7\"\2\2")
        buf.write("\u0265\u0264\3\2\2\2\u0266\u0269\3\2\2\2\u0267\u0265\3")
        buf.write("\2\2\2\u0267\u0268\3\2\2\2\u0268\u026a\3\2\2\2\u0269\u0267")
        buf.write("\3\2\2\2\u026a\u026e\5\u0087D\2\u026b\u026d\7\"\2\2\u026c")
        buf.write("\u026b\3\2\2\2\u026d\u0270\3\2\2\2\u026e\u026c\3\2\2\2")
        buf.write("\u026e\u026f\3\2\2\2\u026f\u0287\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0271\u0273\7\"\2\2\u0272\u0271\3\2\2\2\u0273\u0276")
        buf.write("\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275")
        buf.write("\u0277\3\2\2\2\u0276\u0274\3\2\2\2\u0277\u027b\5q9\2\u0278")
        buf.write("\u027a\7\"\2\2\u0279\u0278\3\2\2\2\u027a\u027d\3\2\2\2")
        buf.write("\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027e\3")
        buf.write("\2\2\2\u027d\u027b\3\2\2\2\u027e\u0282\5\u0087D\2\u027f")
        buf.write("\u0281\7\"\2\2\u0280\u027f\3\2\2\2\u0281\u0284\3\2\2\2")
        buf.write("\u0282\u0280\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0286\3")
        buf.write("\2\2\2\u0284\u0282\3\2\2\2\u0285\u0274\3\2\2\2\u0286\u0289")
        buf.write("\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0288\3\2\2\2\u0288")
        buf.write("\u02b1\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u028c\7\"\2\2")
        buf.write("\u028b\u028a\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3")
        buf.write("\2\2\2\u028d\u028e\3\2\2\2\u028e\u0290\3\2\2\2\u028f\u028d")
        buf.write("\3\2\2\2\u0290\u0294\5\u0089E\2\u0291\u0293\7\"\2\2\u0292")
        buf.write("\u0291\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292\3\2\2\2")
        buf.write("\u0294\u0295\3\2\2\2\u0295\u02ad\3\2\2\2\u0296\u0294\3")
        buf.write("\2\2\2\u0297\u0299\7\"\2\2\u0298\u0297\3\2\2\2\u0299\u029c")
        buf.write("\3\2\2\2\u029a\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b")
        buf.write("\u029d\3\2\2\2\u029c\u029a\3\2\2\2\u029d\u02a1\5q9\2\u029e")
        buf.write("\u02a0\7\"\2\2\u029f\u029e\3\2\2\2\u02a0\u02a3\3\2\2\2")
        buf.write("\u02a1\u029f\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a4\3")
        buf.write("\2\2\2\u02a3\u02a1\3\2\2\2\u02a4\u02a8\5\u0089E\2\u02a5")
        buf.write("\u02a7\7\"\2\2\u02a6\u02a5\3\2\2\2\u02a7\u02aa\3\2\2\2")
        buf.write("\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ac\3")
        buf.write("\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u029a\3\2\2\2\u02ac\u02af")
        buf.write("\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae")
        buf.write("\u02b1\3\2\2\2\u02af\u02ad\3\2\2\2\u02b0\u01f5\3\2\2\2")
        buf.write("\u02b0\u021b\3\2\2\2\u02b0\u0241\3\2\2\2\u02b0\u0267\3")
        buf.write("\2\2\2\u02b0\u028d\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b3")
        buf.write("\5m\67\2\u02b3\u008a\3\2\2\2\u02b4\u02b6\t\20\2\2\u02b5")
        buf.write("\u02b4\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02b5\3\2\2\2")
        buf.write("\u02b7\u02b8\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02ba\b")
        buf.write("F\2\2\u02ba\u008c\3\2\2\2\u02bb\u02bc\7,\2\2\u02bc\u02bd")
        buf.write("\7,\2\2\u02bd\u02c1\3\2\2\2\u02be\u02c0\13\2\2\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02c0\u02c3\3\2\2\2\u02c1\u02c2\3\2\2\2")
        buf.write("\u02c1\u02bf\3\2\2\2\u02c2\u02c4\3\2\2\2\u02c3\u02c1\3")
        buf.write("\2\2\2\u02c4\u02c5\7,\2\2\u02c5\u02c6\7,\2\2\u02c6\u02c7")
        buf.write("\3\2\2\2\u02c7\u02c8\bG\2\2\u02c8\u008e\3\2\2\2\u02c9")
        buf.write("\u02ca\13\2\2\2\u02ca\u0090\3\2\2\2\u02cb\u02d0\7$\2\2")
        buf.write("\u02cc\u02cf\5\u0085C\2\u02cd\u02cf\5\u0083B\2\u02ce\u02cc")
        buf.write("\3\2\2\2\u02ce\u02cd\3\2\2\2\u02cf\u02d2\3\2\2\2\u02d0")
        buf.write("\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d7\3\2\2\2")
        buf.write("\u02d2\u02d0\3\2\2\2\u02d3\u02d4\7^\2\2\u02d4\u02d8\n")
        buf.write("\16\2\2\u02d5\u02d6\7)\2\2\u02d6\u02d8\n\21\2\2\u02d7")
        buf.write("\u02d3\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02da\3\2\2\2")
        buf.write("\u02d9\u02db\7$\2\2\u02da\u02d9\3\2\2\2\u02da\u02db\3")
        buf.write("\2\2\2\u02db\u0092\3\2\2\2\u02dc\u02e1\7$\2\2\u02dd\u02e0")
        buf.write("\5\u0085C\2\u02de\u02e0\5\u0083B\2\u02df\u02dd\3\2\2\2")
        buf.write("\u02df\u02de\3\2\2\2\u02e0\u02e3\3\2\2\2\u02e1\u02df\3")
        buf.write("\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u0094\3\2\2\2\u02e3\u02e1")
        buf.write("\3\2\2\2\u02e4\u02e5\7,\2\2\u02e5\u02e6\7,\2\2\u02e6\u02ea")
        buf.write("\3\2\2\2\u02e7\u02e9\13\2\2\2\u02e8\u02e7\3\2\2\2\u02e9")
        buf.write("\u02ec\3\2\2\2\u02ea\u02eb\3\2\2\2\u02ea\u02e8\3\2\2\2")
        buf.write("\u02eb\u0096\3\2\2\2\u02ec\u02ea\3\2\2\2\u02ed\u02ee\7")
        buf.write("\62\2\2\u02ee\u02ef\t\22\2\2\u02ef\u030d\7\62\2\2\u02f0")
        buf.write("\u02f1\7\62\2\2\u02f1\u02f5\t\7\2\2\u02f2\u02f4\t\b\2")
        buf.write("\2\u02f3\u02f2\3\2\2\2\u02f4\u02f7\3\2\2\2\u02f5\u02f3")
        buf.write("\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02fb\3\2\2\2\u02f7")
        buf.write("\u02f5\3\2\2\2\u02f8\u02fa\n\t\2\2\u02f9\u02f8\3\2\2\2")
        buf.write("\u02fa\u02fd\3\2\2\2\u02fb\u02f9\3\2\2\2\u02fb\u02fc\3")
        buf.write("\2\2\2\u02fc\u030d\3\2\2\2\u02fd\u02fb\3\2\2\2\u02fe\u02ff")
        buf.write("\7\62\2\2\u02ff\u0303\t\n\2\2\u0300\u0302\t\13\2\2\u0301")
        buf.write("\u0300\3\2\2\2\u0302\u0305\3\2\2\2\u0303\u0301\3\2\2\2")
        buf.write("\u0303\u0304\3\2\2\2\u0304\u0309\3\2\2\2\u0305\u0303\3")
        buf.write("\2\2\2\u0306\u0308\n\f\2\2\u0307\u0306\3\2\2\2\u0308\u030b")
        buf.write("\3\2\2\2\u0309\u0307\3\2\2\2\u0309\u030a\3\2\2\2\u030a")
        buf.write("\u030d\3\2\2\2\u030b\u0309\3\2\2\2\u030c\u02ed\3\2\2\2")
        buf.write("\u030c\u02f0\3\2\2\2\u030c\u02fe\3\2\2\2\u030d\u0098\3")
        buf.write("\2\2\2G\2\u017a\u0180\u0186\u018c\u018e\u0196\u019f\u01a5")
        buf.write("\u01a8\u01ad\u01b3\u01b9\u01bd\u01c2\u01c7\u01cd\u01d2")
        buf.write("\u01d7\u01d9\u01dd\u01e3\u01ea\u01ec\u01f5\u01fc\u0202")
        buf.write("\u0209\u0210\u0215\u021b\u0222\u0228\u022f\u0236\u023b")
        buf.write("\u0241\u0248\u024e\u0255\u025c\u0261\u0267\u026e\u0274")
        buf.write("\u027b\u0282\u0287\u028d\u0294\u029a\u02a1\u02a8\u02ad")
        buf.write("\u02b0\u02b7\u02c1\u02ce\u02d0\u02d7\u02da\u02df\u02e1")
        buf.write("\u02ea\u02f5\u02fb\u0303\u0309\u030c\3\b\2\2")
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


