;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Sat Jan 02 14:52:07 ICT 2021

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
.limit locals 2
.var 0 is args [Ljava/lang/String; from Label2 to Label0
.var 1 is i I from Label1 to Label0

Label2:
.line 3
	iconst_0
	istore_1
Label1:
	iload_1
	iconst_5
	if_icmpge Label0
.line 4
	getstatic java.lang.System.out Ljava/io/PrintStream;
	iload_1
	invokevirtual java/io/PrintStream/println(I)V
.line 3
	iinc 1 1
	goto Label1
Label0:
.line 6
	return

.end method
