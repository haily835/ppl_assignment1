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
.var 1 is a [Ljava/lang/String; from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "a"
	aastore
	dup
	iconst_1
	ldc "b"
	aastore
	dup
	iconst_2
	ldc "c"
	aastore
	astore_1
	iconst_0
	istore_2
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_2
	iconst_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	goto Label2
Label13:
	goto Label9
Label9:
	aload_1
	iload_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 9
.limit locals 3
.end method
