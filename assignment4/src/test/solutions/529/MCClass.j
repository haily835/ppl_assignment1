.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I

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
	putstatic MCClass.a [I
	return
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.a [I
	invokestatic MCClass/printArray1([I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static printArray1([I)V
.var 0 is a [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_0
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
	iconst_1
	iload_1
Label2:
	iadd
	istore_1
	goto Label4
Label3:
	return
Label1:
.limit stack 4
.limit locals 2
.end method
