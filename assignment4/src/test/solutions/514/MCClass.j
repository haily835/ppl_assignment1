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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	ifle Label2
.var 1 is a I from Label7 to Label8
Label7:
	iconst_1
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
	goto Label6
Label2:
	iconst_0
	ifle Label3
.var 1 is a I from Label9 to Label10
Label9:
	iconst_2
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label10:
	goto Label6
Label3:
	iconst_0
	ifle Label4
.var 1 is a I from Label11 to Label12
Label11:
	iconst_3
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label12:
	goto Label6
Label4:
	iconst_0
	ifle Label5
.var 1 is a I from Label13 to Label14
Label13:
	iconst_4
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label14:
	goto Label6
Label5:
.var 1 is a I from Label15 to Label16
Label15:
	iconst_5
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label16:
Label6:
	return
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public <clinit>()V
	return
.limit stack 0
.limit locals 0
.end method
