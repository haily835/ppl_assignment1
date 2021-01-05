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
	invokestatic MCClass/foo()I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo()I
.var 0 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_0
	iconst_0
	istore_0
Label4:
	iload_0
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_0
	iconst_2
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	iload_0
	ireturn
Label13:
	goto Label9
Label9:
Label8:
Label2:
	iconst_1
	iload_0
	iadd
	istore_0
	goto Label4
Label3:
	iconst_5
	ireturn
Label1:
.limit stack 6
.limit locals 1
.end method
