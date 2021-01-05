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
.var 1 is a [I from Label0 to Label1
Label0:
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
	aload_1
	iconst_5
	invokestatic MCClass/sum([II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static sum([II)I
.var 0 is a [I from Label0 to Label1
.var 1 is size I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is result I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iconst_0
	istore_3
	iconst_0
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_3
	aload_0
	iload_2
	iaload
	iadd
	istore_3
Label8:
Label2:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label4
Label3:
	iload_3
	ireturn
Label1:
.limit stack 6
.limit locals 4
.end method
