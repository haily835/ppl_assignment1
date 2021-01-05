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
.var 2 is b Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_0
	istore_2
	iconst_1
	ifle Label2
	iload_2
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	iconst_0
	idiv
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_1
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
