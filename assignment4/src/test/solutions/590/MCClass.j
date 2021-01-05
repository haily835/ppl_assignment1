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
Label0:
	iconst_2
	istore_1
	iload_1
	iconst_5
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
Label6:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
Label12:
	iload_1
	iconst_2
	imul
	istore_1
Label13:
	goto Label9
Label8:
Label14:
	iload_1
	iconst_2
	idiv
	istore_1
Label15:
Label9:
Label7:
	goto Label3
Label2:
Label16:
	bipush 11
	istore_1
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
Label22:
	iload_1
	iconst_3
	imul
	istore_1
Label23:
	goto Label19
Label18:
Label24:
	iload_1
	iconst_3
	imul
	iconst_2
	idiv
	istore_1
Label25:
Label19:
Label17:
Label3:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
.limit locals 2
.end method
