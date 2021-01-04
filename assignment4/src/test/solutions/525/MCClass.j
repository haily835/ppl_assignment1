.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "String"
	aastore
	dup
	iconst_1
	ldc "var"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "3"
	aastore
	dup
	iconst_1
	ldc "trign"
	aastore
	aastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
.limit locals 2
.end method

.method public <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method
