.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [[[I
.field static i I
.field static j I
.field static k I

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
	iconst_2
	anewarray [[I
	dup
	iconst_0
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
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 6
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	aastore
	aastore
	putstatic MCClass.a [[[I
	iconst_0
	putstatic MCClass.i I
	iconst_0
	putstatic MCClass.j I
	iconst_0
	putstatic MCClass.k I
	return
.limit stack 14
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass.i I
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
	iconst_0
	putstatic MCClass.j I
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
	iconst_0
	putstatic MCClass.k I
Label18:
	getstatic MCClass.k I
	iconst_2
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label17
Label21:
	getstatic MCClass.a [[[I
	getstatic MCClass.i I
	aaload
	getstatic MCClass.j I
	aaload
	getstatic MCClass.k I
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label22:
Label16:
	iconst_1
	getstatic MCClass.k I
	iadd
	putstatic MCClass.k I
	goto Label18
Label17:
Label15:
Label9:
	iconst_1
	getstatic MCClass.j I
	iadd
	putstatic MCClass.j I
	goto Label11
Label10:
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
.limit stack 10
.limit locals 1
.end method
