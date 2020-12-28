;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Fri Dec 25 16:29:47 ICT 2020

.source Main.java
.class public Main
.super java/lang/Object

.field  a I

.method public <init>()V
.limit stack 2
.limit locals 1
.var 0 is this LMain; from Label0 to Label1

Label0:
.line 1
	aload_0
	invokespecial java/lang/Object/<init>()V
.line 2
	aload_0
	iconst_5
	putfield Main.a I
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 2
.limit locals 1
.var 0 is args [Ljava/lang/String; from Label0 to Label1

Label0:
.line 4
	getstatic java.lang.System.out Ljava/io/PrintStream;
	ldc "Hello World"
	invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
Label1:
.line 5
	return

.end method

.method public foo(I)I
.limit stack 2
.limit locals 2
.var 0 is this LMain; from Label0 to Label1
.var 1 is b I from Label0 to Label1

Label0:
.line 8
	aload_0
	getfield Main.a I
	iload_1
	iadd
Label1:
	ireturn

.end method
