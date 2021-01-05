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
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	invokestatic MCClass/fibonacci(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static fibonacci(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
Label5:
	iconst_0
	ireturn
Label6:
	goto Label2
Label2:
	iload_0
	iconst_1
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
Label10:
	iconst_1
	ireturn
Label11:
	goto Label7
Label7:
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fibonacci(I)I
	iload_0
	iconst_2
	isub
	invokestatic MCClass/fibonacci(I)I
	iadd
	ireturn
Label1:
.limit stack 7
.limit locals 1
.end method
