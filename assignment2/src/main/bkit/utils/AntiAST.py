from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor

def printlist(lst,f=str,start="[",sepa=",",ending="]"):
	return start + sepa.join(f(i) for i in lst) + ending


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)
class Expr(AST):
    __metaclass__ = ABCMeta
    pass
    
class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl):
    # variable : Id
    # varDimen : List[int] # empty list for scalar variable
    # varInit  : Literal   # null if no initial
    def __init__(self, variable, varDimen, varInit):
        self.variable = variable
        self.varDimen = varDimen
        self.varInit = varInit

    def __str__(self):
        initial = ("," + str(self.varInit)) if self.varInit else ",None"
        dimen = (","+printlist(self.varDimen)) if self.varDimen else ",[]"
        return "VarDecl(" + str(self.variable) + dimen + initial + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)

class FuncDecl(Decl):
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def __init__(self, name, param, body):
        self.name = name
        self.param = param
        self.body = body
	# FuncDecl(Id("a"), [Vardecl()], (
    def __str__(self):
        return "FuncDecl(" + str(self.name) + "," + printlist(self.param)+ ",(" + printlist(self.body[0]) + "," + printlist(self.body[1]) + "))"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Assign(Stmt):
    #lhs:LHS
    #exp:Expr
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return "Assign(" + str(self.lhs) + "," +  str(self.rhs) + ")"

    def accept(self, v, param):
        return v.visitAssign(self, param)

def printListStmt(stmt):
	return printlist(stmt[0]) + "," + printlist(stmt[1])


def printIfThenStmt(stmt):
	return "(" + str(stmt[0])+","+printListStmt((stmt[1],stmt[2])) + ")"



class If(Stmt):
    """Expr is the condition, 
        List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
        List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    """
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
    # def printlist(lst,f=str,start="[",sepa=",",ending="]"):
    def __init__(self, ifthenStmt, elseStmt):
        self.ifthenStmt = ifthenStmt
        self.elseStmt = elseStmt
    def __str__(self):
        ifstmt = printlist(self.ifthenStmt,printIfThenStmt,"[",",","]")
        elsestmt = ("("+printListStmt(self.elseStmt)+")" ) if self.elseStmt else "([],[])"
        return "If(" + ifstmt + "," + elsestmt + ")"

    def accept(self, v, param):
        return v.visitIf(self, param)


class For(Stmt):
    # idx1: Id
    # expr1:Expr
    # expr2:Expr
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]
    
    def __init__(self, idx1, expr1, expr2, expr3, loop):
        self.idx1 = idx1
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.loop = loop

    def __str__(self):
        return "For(" + \
        	str(self.idx1)+","+ \
        	str(self.expr1) + ","+ \
        	str(self.expr2) + "," + \
        	str(self.expr3) + "," + \
        	"(" + printListStmt(self.loop) + ")" + ")"

    def accept(self, v, param):
        return v.visitFor(self, param)

class Break(Stmt):
    def __str__(self):
        return "Break()"

    def accept(self, v, param):
        return v.visitBreak(self, param)
    
class Continue(Stmt):
    def __str__(self):
        return "Continue()"

    def accept(self, v, param):
        return v.visitContinue(self, param)


class Return(Stmt):
    # expr:Expr # None if no expression
    def __init__(self, expr):
        self.expr = expr
    def __str__(self):
        return "Return(" + ("None" if (self.expr is None) else str(self.expr)) + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)


class Dowhile(Stmt):
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def __init__(self, sl, exp):
        self.sl = sl
        self.exp = exp
    def __str__(self):
        return "Dowhile((" + printListStmt(self.sl) + ")," + str(self.exp) + ")"

    def accept(self, v, param):
        return v.visitDowhile(self, param)


class While(Stmt):
    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    
    def __init__(self, exp, sl):
        self.exp = exp
        self.sl = sl

    def __str__(self):
        return "While(" + str(self.exp) + ",(" + printListStmt(self.sl)+ "))"

    def accept(self, v, param):
        return v.visitWhile(self, param)


class CallStmt(Stmt):
    # method:Id
    # param:List[Expr]
    
    def __init__(self, method, param):
        self.method = method
        self.param = param

    def __str__(self):
        return "CallStmt(" + str(self.method) + "," + printlist(self.param) + ")"

    def accept(self, v, param):
        return v.visitCallStmt(self, param)

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


class BinaryOp(Expr):
    #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
    #left:Expr
    #right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        oper = ""
        if (self.op == "\\"):
            oper = "\\\\"
        else:
            oper = self.op
        return "BinaryOp(\"" + oper + "\"," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

class UnaryOp(Expr):
    #op:string
    #body:Expr
    def __init__(self, op, body):
        self.op = op
        self.body = body

    def __str__(self):
        return "UnaryOp(\"" + self.op + "\"," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)

class CallExpr(Expr):
    #method:Id
    #param:list(Expr)
    def __init__(self, method, param):
        self.method = method
        self.param = param

    def __str__(self):
        return "CallExpr(" + str(self.method) + "," +  printlist(self.param) + ")"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)

class Id(LHS):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(\"" + self.name + "\")"

    def accept(self, v, param):
        return v.visitId(self, param)

class ArrayCell(LHS):
	# arr:Expr
    # idx:List[Expr]
    def __init__(self, arr, idx):
	    self.arr = arr
	    self.idx = idx
    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + printlist(self.idx) + ")"

    def accept(self, v, param):
        return v.visitArrayCell(self, param)



class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

class IntLiteral(Literal):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class FloatLiteral(Literal):
    #value:float
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)

class StringLiteral(Literal):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "StringLiteral(\"" + self.value + "\")"

    def accept(self, v, param):
        return v.visitStringLiteral(self, param)

class BooleanLiteral(Literal):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)
        
class ArrayLiteral(Literal):
    # value:List[Literal]
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return printlist(self.value,start="ArrayLiteral([",ending="])")

    def accept(self, v, param):
        return v.visitArrayLiteral(self, param)
