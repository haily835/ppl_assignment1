;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Wed Dec 30 19:29:42 ICT 2020

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
.limit stack 10
.limit locals 2
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[[I from Label1 to Label1

Label0:
.line 3
	iconst_2
	anewarray [[I
	dup
	iconst_0
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
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 6
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	aastore
	aastore
	astore_1
Label1:
.line 4
	return

.end method
