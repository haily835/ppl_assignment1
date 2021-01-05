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

.method public <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
.var 2 is y F from Label0 to Label1
Label0:
	ldc 10.0
	fstore_1
	ldc 4.0
	fstore_2
	ldc 2.0
	fload_1
	fadd
	ldc 4.0
	fload_2
	fdiv
	invokestatic MCClass/foo(FF)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static foo(FF)V
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fadd
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
.limit stack 2
.limit locals 2
.end method
