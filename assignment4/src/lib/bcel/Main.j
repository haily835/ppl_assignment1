;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Mon Jan 04 09:16:32 ICT 2021

.source Main.java
.class public Main
.super java/lang/Object

.field static a [[I

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
.limit stack 3
.limit locals 1
.var 0 is args [Ljava/lang/String; from Label0 to Label1

Label0:
.line 4
	getstatic java.lang.System.out Ljava/io/PrintStream;
	getstatic Main.a [[I
	iconst_0
	aaload
	iconst_0
	iaload
	invokevirtual java/io/PrintStream/print(I)V
Label1:
.line 5
	return

.end method

.method static <clinit>()V
.limit stack 7
.limit locals 0

.line 2
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	putstatic Main.a [[I
	return

.end method
