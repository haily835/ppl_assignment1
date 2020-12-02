
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
    def __init__(self, dimen, eletype):
        self.dimen = dimen
        self.eletype = eletype

    def __str__(self):
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
    def __init__(self, intype: List[Type], restype: Type):
        self.intype = intype 
        self.restype = restype
    def __str__(self):
        return printlist(self.intype) + ":" + str(self.restype)
    def __repr__(self):
        return str(self)

@dataclass
class Symbol:
    def __init__(self, **decl):
        if 'variable' in decl:
            self.name = decl['variable'].variable.name
            self.mtype = decl['mtype']
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

    def inferFuncOut(self, expect):
        if isinstance(self.mtype.restype, Unknown):
            self.mtype.restype = expect

    def inferVar(self, expect):
        if isinstance(self.mtype, Unknown):
            self.mtype = expect

    def __str__(self):
        if(isinstance(self.mtype, MType)):
            return self.name + '' + str(self.mtype)
        return self.name + ': ' + str(self.mtype)

    def __repr__(self):
        return str(self)


class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = []
#         self.global_envi = [
# Symbol(name='int_of_float', mtype=(MType([FloatType()], IntType()))),
# Symbol(name='float_of_int', mtype=(MType([IntType()], FloatType()))),
# Symbol(name='int_of_string', mtype=(MType([StringType()], IntType()))),
# Symbol(name='string_of_int', mtype=(MType([IntType()], StringType()))),
# Symbol(name='float_of_string', mtype=(MType([StringType()], FloatType()))),
# Symbol(name='string_of_float', mtype=(MType([FloatType()], StringType()))),
# Symbol(name='bool_of_string', mtype=(MType([StringType()], BoolType()))),
# Symbol(name='string_of_bool', mtype=(MType([BoolType()], StringType()))),
# Symbol(name='read', mtype=(MType([], StringType()))),
# Symbol(name='printLn', mtype=(MType([], VoidType()))),
# Symbol(name='printStr', mtype=(MType([StringType()], VoidType()))),
# Symbol(name='printStrLn', mtype=(MType([StringType()], VoidType())))]
                        
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def getSym(self, c, name):
        for scope in c:
            for x in scope:
                if x.name == name:
                    return x
        return None

    def infer(self, c, expr, expect):
        if isinstance(expr, Id):
            sym = self.getSym(c, expr.name)
            sym.inferVar(expect)
        else:
            sym = self.getSym(c,expr.method)
            sym.inferFuncOut(expect)
    

    def visitProgram(self, ast, c):
        varDecls = list(filter(lambda x: isinstance(x, VarDecl), ast.decl))
        varList = reduce(lambda acc, ele: acc + [ele.accept(self,c)], varDecls, c)
        c = c + varList

        funcDecls = list(filter(lambda x: isinstance(x, FuncDecl), ast.decl))
        for i in range(0, len(funcDecls)):
            # check redeclaration of function name with global var decls
            for x in c:
                if x.name == funcDecls[i].name.name:
                    raise Redeclared(Function(), funcDecls[i].name.name)
            
            # check redeclare parameters of a function declare
            for k in range(0, len(funcDecls[i].param)):
                for h in range(k + 1, len(funcDecls[i].param)):
                    if funcDecls[i].param[k].variable.name == funcDecls[i].param[h].variable.name:
                        raise Redeclared(Parameter(), funcDecls[i].param[h].variable.name)
            
            # add the function into the global scope
            c.append(Symbol(name=(funcDecls[i].name.name), mtype=(MType([Unknown() for x in range(0, len(funcDecls[i].param))], Unknown()))))
        
        c = [c]
        foundMain = 0
        for x in funcDecls:
            if x.name == 'main':
                foundMain = 1
            x.accept(self, c)
        # if foundMain == 0:
        #     raise NoEntryPoint()

    def visitVarDecl(self, ast, c):
        var = None
        if ast.varDimen:
            eletype = ast.varInit.accept(self, c)
            mytype = ArrayType(ast.varDimen, eletype)
            var = Symbol(variable=ast, mtype = mytype)
        else:
            var = Symbol(variable=ast, mtype=(ast.varInit.accept(self, c) if ast.varInit else Unknown()))
        for x in c:
            if x.name == var.name:
                raise Redeclared(var.kind, var.name)
        else:
            return var

    def visitFuncDecl(self, ast, c):
        # create a list of symbol for parameters
        paraList = [Symbol(para=x) for x in ast.param]

        # visit local declarations
        localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.body[0], paraList)

        # combine them together to make local scope to visit the statements in body
        c = [localvar] + c
        print(ast.name.name)
        print(c)

        # visit statements 
        for x in ast.body[1]:
            if isinstance(x, Return):
                c = (c, ast.name.name)
                x.accept(self, c)
            x.accept(self, c)

    def visitBinaryOp(self, ast, c):
        if ast.op in ('+', '-', '*', '\\', '%'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left, IntType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right, IntType())
            if isinstance(ast.left.accept(self, c), IntType):
                if isinstance(ast.right.accept(self, c), IntType):
                    return IntType()
        if ast.op in ('+.', '-.', '*.', '\\.'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left, FloatType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right, FloatType())
            if isinstance(ast.left.accept(self, c), FloatType):
                if isinstance(ast.right.accept(self, c), FloatType):
                    return FloatType()
        if ast.op == '&&' or (ast.op == '||'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left, BoolType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right, BoolType())
            if isinstance(ast.left.accept(self, c), BoolType):
                if isinstance(ast.right.accept(self, c), BoolType):
                    return BoolType()
        if ast.op in ('<', '>', '<=', '>=', '=='):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left, IntType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right, IntType())
            if isinstance(ast.left.accept(self, c), IntType):
                if isinstance(ast.right.accept(self, c), IntType):
                    return BoolType()
        if ast.op in ('<.', '>.', '<=.', '>=.', '=/='):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c, ast.left, FloatType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c, ast.right, FloatType())
            if isinstance(ast.left.accept(self, c), FloatType):
                if isinstance(ast.right.accept(self, c), FloatType):
                    return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        if ast.op == '-':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c, ast.body, IntType())
            if isinstance(ast.body.accept(self, c), IntType):
                return IntType()
        if ast.op == '-.':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c, ast.body, FloatType())
            if isinstance(ast.body.accept(self, c), FloatType):
                return FloatType()
        if ast.op == '!':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c, ast.body, BoolType())
            if isinstance(ast.body.accept(self, c), BoolType):
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        argsType = [x.accept(self, c) for x in ast.param]
        sym = self.getSym(c, ast.method.name)
        if sym:
            sym.inferFuncOut(VoidType())
            # check if function output is voidtype
            if not isinstance(sym.mtype.restype, VoidType):
                raise TypeCannotBeInferred(ast)
            
            # check whether args are compatible with paras
            if len(argsType) == len(sym.mtype.intype):
                # try to infer the function parameters by args
                sym.inferFunc(argsType)

                # check if there are some parameters cannot infer type
                for typ in sym.mtype.intype:
                    if isinstance(typ, Unknown):
                        raise TypeCannotBeInferred(ast)
                
                # check if args and paras are not matched
                if sym.mtype.intype != argsType:
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        else:
            raise Undeclared(Function(), ast.method.name)


    
    def visitId(self, ast, c):
        sym = self.getSym(c, ast.name)
        if sym:
            return sym.mtype
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, c):
        dimen = 0
        
        # count dimension and check type of indexes
        for x in ast.idx:
            if not isinstance(x.accept(self, c), IntType):
                raise TypeMismatchInExpression(ast)
            dimen += 1
        
        if not isinstance(ast.arr.accept(self), ArrayType):
            raise TypeMismatchInExpression(ast)

        if ast.arr.accept(self).dimen != dimen:
            raise TypeMismatchInExpression(ast)
    
    def visitAssign(self, ast, c):
        print(c)
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
        # for ifthenStmt in ast.ifthenStmt:
        #     if isinstance(ifthenStmt[0].accept(self, c),Unknown):
        #         self.self.infer(c, ifthenStmt[0], BoolType())

        #     if not isinstance(ifthenStmt[0].accept(self, c),Booltype):
        #         raise TypeMismatchInStatement(ast)

        #     localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ifthenStmt[1], paraList)
        #     # combine them together to make local scope to visit the statements in body
        #     c = [localvar] + c
        #     # visit statements 
        #     for x in ifthenStmt[2]:
        #         x.accept(self, c)


    def visitFor(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        sym = self.getSym(c[0], c[1])
        if isinstance(sym.mtype.restype, VoidType):
            if not ast.expr:
                raise TypeMismatchInStatement(ast)
        elif isinstance(sym.mtype.restype, Unknown):
            sym.mtype.restype = ast.expr.accept(self, c[0])
        else:
            if type(sym.mtype.restype) != type(ast.expr.accept(self, c[0])):
                raise TypeMismatchInStatement(ast)


    def visitDowhile(self, ast, c):
        pass

    def visitWhile(self, ast, c):
        pass

    def visitCallStmt(self, ast, c):
        argsType = [x.accept(self, c) for x in ast.param]
        sym = self.getSym(c,ast.method.name)
        if sym:
            sym.inferFuncOut(VoidType())
            # check if function output is voidtype
            if not isinstance(sym.mtype.restype, VoidType):
                raise TypeCannotBeInferred(ast)
            
            # check whether args are compatible with paras
            if len(argsType) == len(sym.mtype.intype):
                # try to infer the function parameters by args
                sym.inferFunc(argsType)

                # check if there are some parameters cannot infer type
                for typ in sym.mtype.intype:
                    if isinstance(typ, Unknown):
                        raise TypeCannotBeInferred(ast)
                
                # check if args and paras are not matched
                if sym.mtype.intype != argsType:
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        else:
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