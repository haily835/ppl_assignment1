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
Label4:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	getstatic MCClass.i I
	iconst_5
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
Label12:
	goto Label3
Label13:
	goto Label9
Label9:
	getstatic MCClass.i I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label8:
Label2:
	goto Label4
Label3:
Label1:
	return
.limit stack 6
.limit locals 1
.end method
