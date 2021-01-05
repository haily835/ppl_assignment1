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
	iconst_0
	ifle Label2
Label4:
	ldc "1"
	invokestatic io/print(Ljava/lang/String;)V
Label5:
	goto Label3
Label2:
	iconst_1
	ifle Label3
Label6:
	ldc "2"
	invokestatic io/print(Ljava/lang/String;)V
Label7:
	goto Label3
Label3:
	return
Label1:
	return
.limit stack 3
.limit locals 1
.end method
