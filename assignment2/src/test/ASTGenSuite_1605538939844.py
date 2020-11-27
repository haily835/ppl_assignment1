import unittest
from TestUtils import TestAST
from AntiAST import *

class ASTGenSuite(unittest.TestCase):

    # test var declare
    def test_1_vardecl(self):
        """Simple program: int main() {} """
        input= """
Function: main
Body:
Var:x = 5;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_2_vardecl(self):
        input = """
Function: main
Body:
Var: b[2][3] = {{2,3,4},{4,5,6}};
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_3_vardecl(self):
        input = """
Function: main
Body:
Var: c, d = 6, e, f;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_4_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10];
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_5_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_6_vardecl(self):
        input = """
Function: main
Body:
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var:x = 5;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # global var decl
    def test_7_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_8_vardecl(self):
        input = """
Var: m, n[10] = {1,2,4,5,6,7,8,9,10};
Function: main
Body:
Var: a = 5, c = 6, d;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_9_vardecl(self):
        input = """
Var: m, n[10] = {True,False,True,False,True,False,True,False,True};
Function: main
Body:
Var: a = "string", c = 567e-11, d;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_10_vardecl(self):
        input = """
Var: m, n[10];
Function: another
Body:
Var: a,b,c = 10;
EndBody.
Function: main
Body:
Var: a,b,c = 10;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

# test simple expression
    def test_11_expr_simple(self):
        input = """Function: main
Body:
    a = 3 + 4;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_12_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 +. 4.6;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_13_expr_simple(self):
        input = """Function: main
Body:
    a = 3 - 4;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_14_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 -. 4.6;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_15_expr_simple(self):
        input = """Function: main
Body:
    a = 3*4;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_16_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 *. 4.6;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_17_expr_simple(self):
        input = """Function: main
Body:
    a = 3 \\ 4;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_18_expr_simple(self):
        input = """Function: main
Body:
    a = 3.0 \\. 4.6;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_19_expr_simple(self):
        input = """Function: main
Body:
    a = 3 % 4;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_20_expr_simple(self):
        input = """Function: main
Body:
    a = !foo(x);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_21_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) && True;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_22_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) || True;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_23_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) == True;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_24_expr_simple(self):
        input = """Function: main
Body:
    a = foo(x) != True;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_25_expr_simple(self):
        input = """Function: main
Body:
    a = 4 < 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_26_expr_simple(self):
        input = """Function: main
Body:
    a = 4 > 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_27_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <= 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_28_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >= 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_29_expr_simple(self):
        input = """Function: main
Body:
    a = 4 =/= 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_30_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <. 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_31_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >. 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_32_expr_simple(self):
        input = """Function: main
Body:
    a = 4 >=. 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_33_expr_simple(self):
        input = """Function: main
Body:
    a = 4 <=. 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_34_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 + 2 - 4 + 6;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_35_expr(self):
        input = """
Function: main
Body:
a = 10 + 2 * 2;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_36_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_37_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - 2 && 3 || 4 && 6;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_38_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + 2 - (2 && 3);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_39_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_40_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = b + c[0] && 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_41_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 + foo(x, 6+7*8);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_42_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = 10 + (2 - 2) && 3 == e * 2 + 4[0];
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_43_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = !(-10 + (2 - 2)) && 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_44_expr(self):
        input = """
Function: main
Body:
Var: b,c = 10;
a = (!foo(-10 + (2 - 2)) && 3)[5+5];
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_45_expr(self):
        input = """
Function: main
Body:
a = b[1][2] + (c[1])[3] ;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_46_expr(self):
        input = """
Function: main
Body:
a = -.b[1][2] +. (c[1])[3] * foo(f(x), y);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_47_expr(self):
        input = """
Function: main
Body:
a = ---a;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_48_expr(self):
        input = """
Function: main
Body:
a = b[foo(x)][2][3][4];
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_49_expr(self):
        input = """
Function: main
Body:
a = !!!!!b[foo(x)][2][3][4];
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_50_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || b || d || k;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_51_expr(self):
        input = """
Function: main
Body:
a = a*b*c*.d\\d\\.c && a || (b || d || k);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_52_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))));
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_53_expr(self):
        input = """
Function: main
Body:
a = foo(b, foo(c, foo(d, f(k))))[6\\7][a[2]];
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_54_expr(self):
        input = """
Function: main
Body:
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_55_expr(self):
        input = """
Function: main
Body:
v = foo() + !(foo() * a[4][5][6]);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_56_expr(self):
        input = """
Function: main
Body:
v = foo(124, a[3][6], a && b);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_57_expr(self):
        input = """
Function: main
Body:
v = !!!!!-------.-.-.-.a%b;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_58_expr(self):
        input = """
Function: main
Body:
v = a != ((b != c) != d);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_59_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_60_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
Else 
        Break;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    def test_61_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        Var: a = 10;
        x = x + 1;
ElseIf x > 20 Then
        Var: x = 5;
        Break;
Else 
        Var: x = 6;
        Continue;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_62_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then x = x + 1;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then Break;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_63_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        Var: a = 0;
        x = x + 1;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then Break;
ElseIf x > 20 Then 
        Break;
        If x > 50 Then Continue; EndIf.
Else
        Var: b = 0;
        Continue;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,362))


    def test_64_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
ElseIf x > 20 Then
        If x > 50 Then Continue; EndIf.
        Break;
ElseIf x > 20 Then
        If x > 50 Then Continue; EndIf.
        Break;
ElseIf x > 20 Then
        Var: a[1] = {1};
        Break;
        If x > 50 Then Continue; EndIf.
Else
        Continue;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_65_if(self):
        input = """
Function: main
Body:
Var: x = 0;
If x < 20 Then
        x = x + 1;
ElseIf x > 20 Then
        If x > 50 Then
                If x < 30 Then Break; ElseIf x > 50 Then Var: a = 10; x = x + 1; Else x = x - 1; EndIf.
        EndIf.
        Continue;
        Break;
ElseIf x > 20 Then
        If x > 50 Then Continue; EndIf.
        Break;
ElseIf x > 20 Then
        Break;
        If x > 50 Then Continue; ElseIf (x < 80) Then Break; EndIf.
Else
        Continue;
EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_66_while(self):
        input = """
Function: main
Body:
While x < 20 Do x = x + 1; EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_67_while(self):
        input = """
Function: main
Body:
    While (x < 10) Do
        sum = sum + x;
        While( z > 10 ) Do
            z = z - 1;
        EndWhile.
    EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_68_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        sum = sum + x;
    EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_69_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        Var: sum = 0, a[3];
        sum = sum + x;
        While ( x % 2 == 0 ) Do
                Var: k = 0;
                sum = sum - x;
        EndWhile. 
    EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_70_while(self):
        input = """
Function: main
Body:
    While (x < 10) && (x != 0) && foo(x,y) Do
        Var: sum = 0, a[3];
        sum = sum + x;
        While ( x % 2 == 0 ) Do
                Var: k = 0;
                sum = sum - x;
                Break;
        EndWhile. 
        While ( k % 2 == 0 ) Do
                Var: k = 0;
                sum = sum - x;
                Break;
        EndWhile. 
        Continue;
    EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_71_dowhile(self):
        input = """
Function: main
Body:
    Var: i;
    Do
        i = i + 1;
    While i < 20
    EndDo.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
        
    def test_72_dowhile(self):
        input = """
Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
        Do
            j = j - 1;
        While j > 0
        EndDo.
    While i < 20
    EndDo.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_73_dowhile(self):
        input = """
Function: main
Body:
    Var: i = 0, j = 10;
    Do
        i = i + 1;
        Do
            j = j - 1;
        While j > 0
        EndDo.
        Do
            j = j - 1;
            Do
            j = j - 1;
            While j > 0
            EndDo.
        While j > 0
        EndDo.
    While i < 20
    EndDo.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_74_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_75_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        Var: isEqual = True;
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
        EndFor.
    EndFor.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_76_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, (i < 10) && (i % 2 == 0), 2*3) Do
        printLn(i);
    EndFor.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_77_for(self):
        input = """
Function: main
Body:
    Var: i;
    For (i = 1, i < 10, 2) Do
        For (j = 1, j < 10, 3) Do
            Var: j;
            printLn(i*j);
        EndFor.
        For (j = 1, j < 10, 3) Do
            Var: isFalse = True;
            printLn(i*j);
        EndFor.
        For (j = 1, j < 10, 3) Do
            printLn(i*j);
            For (j = 1, j < 10, 3) Do
            printLn(i*j);
            EndFor.
        EndFor.
    EndFor.
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
        

    def test_78_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5);
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_79_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5,"string", True);
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_80_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(5 + 4 * 3 \\ 5,"string", True);
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_81_callstmt(self):
        input = """
Function: main
Body:
    Var: i;
    foo(True,incr(5), incr(6));
    
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_82_return_stmt(self):
        input = """
Function: main
Body:
    Var: i;
    Return i * 2 * 3;  
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_83_return_stmt(self):
        input = """
Function: main
Body:
    Return foo(True,incr(5), incr(6));  
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_84_return_stmt(self):
        input = """
Function: main
Body:
    Return;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_85_break_stmt(self):
        input = """
Function: main
Body:
    Break;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_86_continue_stmt(self):
        input = """
Function: main
Body:
    Continue;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_87_mixstmt(self):
        input = """
Function: main
Body:
    Var: arr[2][3] = {{2,3,5},{6,7,8}};
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            printLn(arr[i][j]);
            sum = sum + arr[i][j];
        EndFor.
        i = i + 1;
    EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_88_mixstmt(self):
        input = """
Function: main
Body:
    Var: arrA[2][3] = {{2,3,5},{6,7,8}};
    Var: arrB[2][3] = {{2,3,5},{6,7,8}};
    Var: isEqual = True;
    Var: i = 0, j, sum;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            If((arrA[i][j]) != (arrB[i][j])) Then
                isEqual = False;
                Break;
            EndIf.
        EndFor.
        i = i + 1;
    EndWhile.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_89_mixstmt(self):
        input = """
Function: main
Body:
    Var: arrA[2][3] = {{2,3,5},{6,7,8}};
    While i < 2 Do
        Var: isEqual = True;
        For (j = 0, j < 3, 1) Do
            If((arrA[i][j]) != (arrB[i][j])) Then
                Var: isEqual = True;
                isEqual = False;
                Do
                    j = j - 1;
                    While j > 0
                EndDo.
                Break;
                foo();
            EndIf.
        EndFor.
        i = i + 1;
    EndWhile.
    Return i + 3;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_90_function_declaration(self):
        input = """Function: foo
Parameter: a[5], c
Body:
EndBody.
Function: main
Body:
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_91_function_declaration(self):
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
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_92_function_declaration(self):
        input = """Function: foo
Parameter: a[5], c
Body:
    Var: x,y,z;
EndBody.
Function: main
Body:
    Var: k,m,n,o;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_93_function_declaration(self):
        input = """
Function: foo
Parameter: a[5], c
Body:
    Var: x,y,z;
    While i < 2 Do
        For (j = 0, j < 3, 1) Do
            printLn(arr[i][j]);
            sum = sum + arr[i][j];
        EndFor.
        i = i + 1;
    EndWhile.
EndBody.
Function: main
Parameter: d[5], e
Body:
    Var: k,m,n,o;
    For (j = 1, j < 10, 3) Do
            Var: j;
            printLn(i*j);
    EndFor.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_94_function_declaration(self):
        input = """
Function: foo
Parameter: a[5], c
Body:
EndBody.
**Main function**
Function: main
Body:
**Comment
Comment**
Var: arrA[2][3] = {{2,3,5},{6,7,8}};
Var: arrB[2][3] = {{2,3,5},{6,7,8}};
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_95_array(self):
        input = """Function: main
Body:
    a[3] = {True, False, True};
    d[3] = {5.6,5E-10,6.03};
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_96_array(self):
        input = """
Function: main
Body:
    c[3] = {{"a" ,"b", "c"},{"e" ,"r", "h"},{"k","s","m"}};
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_97_array(self):
        input = """
Function: main
Body:
    a[3*b[2][3][4]] = 5;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_98_array(self):
        input = """
Function: main
Body:
    (a + foo())[1] = a[3][4];
    4[1] = 5;
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_99_complex_program(self):
        input = """
Function: binarySearch
Parameter: arr[10], l, r, x 
Body:
    If (r >= l) Then
        Var: mid;
        mid = l + (r - l) \ 2;
        ** If the element is present at the middle 
         itself **
        If ((arr[mid]) == x) Then
            Return mid;
        EndIf.
  
        ** If element is smaller than mid, then 
        it can only be present in left subarray **
        If ((arr[mid]) > x) Then
            Return binarySearch(arr, l, mid - 1, x); 
        EndIf.
        ** Else the element can only be present 
        in right subarray **
        Return binarySearch(arr, mid + 1, r, x); 
    EndIf.
  
    ** We reach here when element is not 
    present in array **
    Return -1; 
EndBody.
  
Function: main
Body:
    Var: arr[5] = { 2, 3, 4, 10, 40 }; 
    Var: x = 10; 
    Var: n , result;
    n = sizeof(arr) \ sizeof(arr[0]); 
    result = binarySearch(arr, 0, n - 1, x);
    If (result == -1) Then 
        printLn("Element is not present in array");
    Else
        printLn("Element is present at index: ");
        printLn(result); 
    EndIf.
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))


    def test_100_complex_program(self):
        input = """
** Gobal variable declaration **
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
"""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_101_complex_program(self):
        input = """Var: x;
Function: fact
Parameter: n
Body:
    If n == 0 Then
        Return 1;
    Else
        Return n * fact (n - 1);
    EndIf.
EndBody.
Function: main
Body:
    x = 10;
    fact (x);
EndBody."""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
