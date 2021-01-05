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
.var 1 is r F from Label0 to Label1
.var 2 is v F from Label0 to Label1
Label0:
	ldc 10.0
	fstore_1
	ldc 0.0
	fstore_2
	ldc 4.0
	ldc 3.0
	fdiv
	ldc 3.14
	fmul
	fload_1
	fmul
	fload_1
	fmul
	fload_1
	fmul
	fstore_2
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method
