.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I

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
	bipush 10
	putstatic MCClass.x I
	getstatic MCClass.x I
	invokestatic MCClass/fact(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static fact(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
Label6:
	iconst_1
	ireturn
Label7:
	goto Label3
Label2:
	iload_0
	iconst_0
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
Label10:
Label11:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fact(I)I
	imul
	ireturn
	goto Label3
Label3:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fact(I)I
	imul
	ireturn
Label1:
.limit stack 7
.limit locals 1
.end method

.method public <clinit>()V
	iconst_0
	putstatic MCClass.x I
	return
.limit stack 1
.limit locals 0
.end method
