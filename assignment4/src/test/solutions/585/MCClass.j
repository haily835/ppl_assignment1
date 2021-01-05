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
Label0:
	iconst_3
	invokestatic MCClass/incr(I)I
	invokestatic MCClass/double(I)I
	invokestatic MCClass/square(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static incr(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static double(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iconst_2
	iload_0
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static square(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method
