;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Jan 05 07:24:45 ICT 2021

.source Main.java
.class public Main
.super java/lang/Object


.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this LMain; from Label0 to Label1

Label0:
.line 1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 2
.limit locals 1
.var 0 is args [Ljava/lang/String; from Label0 to Label1

Label0:
.line 3
	getstatic java.lang.System.out Ljava/io/PrintStream;
	iconst_2
	invokestatic Main/foo(I)I
	invokevirtual java/io/PrintStream/print(I)V
Label1:
.line 4
	return

.end method

.method static foo(I)I
.limit stack 2
.limit locals 1
.var 0 is a I from Label2 to Label3

Label2:
.line 7
	iload_0
	iconst_3
	if_icmple Label0
.line 8
	iconst_1
	ireturn
Label0:
.line 9
	iload_0
	iconst_2
	if_icmpge Label1
.line 10
	iconst_2
	ireturn
Label1:
.line 12
	iconst_3
Label3:
	ireturn

.end method
