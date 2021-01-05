.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static j I

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
	iconst_0
	putstatic MCClass.j I
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[I from Label0 to Label1
Label0:
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	astore_1
Label4:
	getstatic MCClass.i I
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
Label11:
	getstatic MCClass.j I
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_1
	getstatic MCClass.i I
	aaload
	getstatic MCClass.j I
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.j I
	iconst_1
	iadd
	putstatic MCClass.j I
Label15:
Label9:
	goto Label11
Label10:
	getstatic MCClass.i I
	iconst_1
	if_icmpne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label16
Label19:
	goto Label3
Label20:
	goto Label16
Label16:
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
.limit stack 13
.limit locals 2
.end method
