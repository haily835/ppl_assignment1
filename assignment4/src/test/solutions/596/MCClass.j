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
.var 1 is a Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	ifgt Label4
	iconst_3
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	ifgt Label6
	iconst_1
	iconst_0
	idiv
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	istore_1
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method
