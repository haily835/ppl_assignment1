.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

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
	iconst_0
	putstatic MCClass.i I
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass.i I
Label4:
	getstatic MCClass.i I
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	getstatic MCClass.i I
	invokestatic MCClass/createArr(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	iconst_1
	getstatic MCClass.i I
	iadd
	putstatic MCClass.i I
	goto Label4
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static createArr(I)Ljava/lang/String;
.var 0 is i I from Label0 to Label1
.var 1 is a [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Happy "
	aastore
	dup
	iconst_1
	ldc "new "
	aastore
	dup
	iconst_2
	ldc "year"
	aastore
	astore_1
	aload_1
	iload_0
	aaload
	areturn
Label1:
.limit stack 4
.limit locals 2
.end method
