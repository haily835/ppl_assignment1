
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

def printlist(lst, f=str, start='(', sepa=',', ending=')'):
    return start + sepa.join((f(i) for i in lst)) + ending

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    def __str__(self):
        return 'Int'

    def __repr__(self):
        return str(self)

class FloatType(Prim):
    def __str__(self):
        return 'Float'

    def __repr__(self):
        return str(self)

class StringType(Prim):
    def __str__(self):
        return 'String'

    def __repr__(self):
        return str(self)

class BoolType(Prim):
    def __str__(self):
        return 'Bool'

    def __repr__(self):
        return str(self)

class VoidType(Type):
    def __str__(self):
        return 'Void'

    def __repr__(self):
        return str(self)

class Unknown(Type):
    def __str__(self):
        return 'Unknown'

    def __repr__(self):
        return str(self)

@dataclass
class ArrayType(Type):
    def __init__(self, dimen: List[int], eletype: Type):
        self.dimen = dimen
        self.eletype = eletype

    def __str__(self):
        print(self.eletype)
        return str(self.eletype) + str(self.dimen)

    def __eq__(self, other):
        if self.dimen == other.dimen:
            if type(self.eletype) == type(other.eletype):
                return True
        return False

    def __repr__(self):
        return str(self)

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    def __init__(self, **decl):
        if 'variable' in decl:
            self.name = decl['variable'].variable.name
            if decl['variable'].varDimen:
                self.mtype = ArrayType(decl['variable'].varDimen, Unknown)
            elif decl['variable'].varInit:
                self.mtype = decl['mtype']
            else:
                self.mtype = Unknown()
            self.kind = Variable()
        elif 'para' in decl:
            self.name = decl['para'].variable.name
            if decl['para'].varDimen:
                self.mtype = ArrayType(decl['para'].varDimen, Unknown)
            self.mtype = Unknown()
            self.kind = Parameter()
        else:
            self.name = decl['name']
            self.mtype = decl['mtype']
            self.kind = Function()

    def inferFunc(self, expect):
        for i in range(0, len(expect)):
            if isinstance(self.mtype.intype[i], Unknown):
                self.mtype.intype[i] = expect[i]

    def inferVar(self, expect):
        if isinstance(self.mtype, Unknown):
            self.mtype = expect

    def __str__(self):
        return self.name + ': ' + str(self.mtype)

    def __repr__(self):
        return str(self)


class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast, c):
        varDecls = list(filter(lambda x: isinstance(x, VarDecl), ast.decl))
        c = c + [x.accept(self, c) for x in varDecls]
        funcDecls = list(filter(lambda x: isinstance(x, FuncDecl), ast.decl))
        for i in range(0, len(funcDecls)):
            for x in c:
                if x.name == funcDecls[i].name.name:
                    raise Redeclared(Function(), funcDecls[j].name.name)

        else:
            for j in range(i + 1, len(funcDecls)):
                if funcDecls[i].name.name == funcDecls[j].name.name:
                    raise Redeclared(Function(), funcDecls[j].name.name)

        for k in range(0, len(funcDecls[i].param)):
            for h in range(k + 1, len(funcDecls[i].param)):
                if funcDecls[i].param[k].variable.name == funcDecls[i].param[h].variable.name:
                    raise Redeclared(Parameter(), funcDecls[i].param[h].variable.name)
            else:
                c.append(Symbol(name=(funcDecls[i].name.name), mtype=(MType([Unknown() for x in range(0, len(funcDecls[i].param))], Unknown()))))

        else:
            [x.accept(self, c) for x in funcDecls]
            print(c)

    def visitVarDecl(self, ast, c):
        var = None
        if ast.varDimen:
            eletype = ast.varInit.accept(self, c)
            var = Symbol(variable=ast, mtype=(ArrayType(ast.varDimen, eletype)))
        else:
            var = Symbol(variable=ast, mtype=(ast.varInit.accept(self, c) if ast.varInit else Unknown()))
        for x in c:
            if x.name == var.name:
                raise Redeclared(var.kind, var.name)
        else:
            return var

    def visitFuncDecl(self, ast, c):
        paraList = [Symbol(para=x) for x in ast.param]
        localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.body[0], paraList)
        c = [localvar] + [c]
        [x.accept(self, c) for x in ast.body[1]]

    def visitBinaryOp(self, ast, c):
        if ast.op in ('+', '-', '*', '\\', '%'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left.name, IntType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right.name, IntType())
            if isinstance(ast.left.accept(self, c), IntType):
                if isinstance(ast.right.accept(self, c), IntType):
                    return IntType()
        if ast.op in ('+.', '-.', '*.', '\\.'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left.name, FloatType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right.name, FloatType())
            if isinstance(ast.left.accept(self, c), FloatType):
                if isinstance(ast.right.accept(self, c), FloatType):
                    return FloatType()
        if ast.op == '&&' or (ast.op == '||'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left.name, BoolType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right.name, BoolType())
            if isinstance(ast.left.accept(self, c), BoolType):
                if isinstance(ast.right.accept(self, c), BoolType):
                    return BoolType()
        if ast.op in ('<', '>', '<=', '>=', '=='):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left.name, IntType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right.name, IntType())
            if isinstance(ast.left.accept(self, c), IntType):
                if isinstance(ast.right.accept(self, c), IntType):
                    return BoolType()
        if ast.op in ('<.', '>.', '<=.', '>=.', '=/='):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left.name, FloatType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right.name, FloatType())
            if isinstance(ast.left.accept(self, c), FloatType):
                if isinstance(ast.right.accept(self, c), FloatType):
                    return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        if ast.op == '-':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c, ast.body.name, IntType())
            if isinstance(ast.body.accept(self, c), IntType):
                return IntType()
        if ast.op == '-.':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c, ast.body.name, FloatType())
            if isinstance(ast.body.accept(self, c), FloatType):
                return FloatType()
        if ast.op == '!':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c, ast.body.name, BoolType())
            if isinstance(ast.body.accept(self, c), BoolType):
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        pass

    def visitId(self, ast, c):
        unfound = 1
        for scope in c:
            for x in scope:
                if ast.name == x.name:
                    unfound = 0
                    return x.mtype

        else:
            if unfound:
                raise Undeclared(ast.name, Identifier())

    def visitArrayCell(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        typeLeft = ast.lhs.accept(self, c)
        typeRight = ast.rhs.accept(self, c)
        if isinstance(typeLeft, Unknown):
            if not isinstance(typeRight, Unknown):
                self.infer(c, ast.lhs.name, typeRight)
                typeLeft = ast.lhs.accept(self, c)
            if isinstance(typeRight, Unknown):
                if not isinstance(typeLeft, Unknown):
                    self.infer(c, ast.rhs.name, typeLeft)
                    typeRight = ast.rhs.accept(self, c)
                if not isinstance(typeLeft, Unknown):
                    if not isinstance(typeRight, Unknown):
                        if type(typeLeft) != type(typeRight):
                            TypeMismatchInStatement(ast)
            if isinstance(typeLeft, Unknown):
                if isinstance(typeRight, Unknown):
                    TypeCannotBeInferred(ast)

    def visitIf(self, ast, c):
        pass

    def visitFor(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        pass

    def visitDowhile(self, ast, c):
        pass

    def visitWhile(self, ast, c):
        pass

    def visitCallStmt(self, ast, c):
        argsType = [x.accept(self, c) for x in ast.param]
        found = 0
        for scope in c:
            for x in scope:
                if ast.method.name == x.name:
                    found = 1
                    if len(argsType) == len(x.mtype.intype):
                        x.inferFunc(argsType)
                        if Unknown() in x.mtype.intype:
                            raise TypeCannotBeInferred(ast)
                        if x.mtype.intype != argsType:
                            raise TypeMismatchInStatement(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                    break
            else:
                if found:
                    break

        else:
            if found == 0:
                raise Undeclared(Function(), ast.method.name)

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        return ast.value[0].accept(self, c)
