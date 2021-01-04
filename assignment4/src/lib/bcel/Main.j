;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Sun Jan 03 22:33:23 ICT 2021

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
.var 1 is a [[[Z from Label2 to Label1

Label0:
.line 3
	iconst_2
	anewarray [[Z
	dup
	iconst_0
	iconst_2
	anewarray [Z
	dup
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [Z
	dup
	iconst_0
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	aastore
	astore_1
Label2:
.line 4
	getstatic java.lang.System.out Ljava/io/PrintStream;
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	baload
	invokevirtual java/io/PrintStream/print(Z)V
Label1:
.line 5
	return

.end method
