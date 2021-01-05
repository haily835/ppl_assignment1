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
.var 1 is a I from Label0 to Label1
.var 2 is iSum I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_2
Label4:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 17
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
Label10:
	goto Label3
Label11:
	goto Label7
Label7:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label12
Label15:
	goto Label2
Label16:
	goto Label12
Label12:
	iload_2
	iload_1
	iadd
	istore_2
Label6:
Label2:
	iload_1
	bipush 20
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label3
	goto Label4
Label3:
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 3
.end method
