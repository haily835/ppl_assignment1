
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

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass

class FloatType(Prim):
    pass

class StringType(Prim):
    pass

class BoolType(Prim):
    pass

class VoidType(Type):
    pass

class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    def __init__(self, dimen, eletype):
        self.dimen = dimen
        self.eletype = eletype

    def __eq__(self, other):
        if self.dimen == other.dimen:
            if isinstance(self.eletype, Unknown) and not isinstance(other.eletype, Unknown):
                self.eletype = other.eletype
                return True
            if not isinstance(self.eletype, Unknown) and  isinstance(other.eletype, Unknown):
                other.eletype = self.eletype
                return True
            if type(self.eletype) is type(other.eletype):
                return True

        return False

@dataclass
class MType:
    def __init__(self, intype: List[Type], restype: Type):
        self.intype = intype 
        self.restype = restype
    

@dataclass
class Symbol:
    def __init__(self, **decl):
        if 'variable' in decl:
            self.name = decl['variable'].variable.name
            self.mtype = decl['mtype']
            self.kind = Variable()
        elif 'para' in decl:
            self.name = decl['para'].variable.name
            # if decl['para'].varDimen:
            #     self.mtype = ArrayType(decl['para'].varDimen, Unknown)
            self.mtype = Unknown()
            self.kind = Parameter()
        else:
            self.name = decl['name']
            self.mtype = decl['mtype']
            self.kind = Function()

    # change type only if the current type is Unknown
    def inferFunc(self, expect):
        for i in range(0, len(expect)):
            if isinstance(self.mtype.intype[i], Unknown):
                self.mtype.intype[i] = expect[i]

    def inferFuncOut(self, expect):
        if isinstance(self.mtype, MType):
            if isinstance(self.mtype.restype, Unknown):
                self.mtype.restype = expect
        else:
            raise Undeclared(Function(), self.name)

    def inferVar(self, expect):
        if isinstance(self.mtype, Unknown):
            self.mtype = expect



class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast        
        self.global_envi = [
Symbol(name='int_of_float', mtype=(MType([FloatType()], IntType()))),
Symbol(name='float_of_int', mtype=(MType([IntType()], FloatType()))),
Symbol(name='int_of_string', mtype=(MType([StringType()], IntType()))),
Symbol(name='string_of_int', mtype=(MType([IntType()], StringType()))),
Symbol(name='float_of_string', mtype=(MType([StringType()], FloatType()))),
Symbol(name='string_of_float', mtype=(MType([FloatType()], StringType()))),
Symbol(name='bool_of_string', mtype=(MType([StringType()], BoolType()))),
Symbol(name='string_of_bool', mtype=(MType([BoolType()], StringType()))),
Symbol(name='read', mtype=(MType([], StringType()))),
Symbol(name='printLn', mtype=(MType([], VoidType()))),
Symbol(name='printStr', mtype=(MType([StringType()], VoidType()))),
Symbol(name='printStrLn', mtype=(MType([StringType()], VoidType())))]
                        
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    # get Symbol object by name
    def getSym(self, c, name):
        for scope in c:
            if isinstance(scope, List):
                for x in scope:
                    if x.name == name:
                        return x
        return None

    def getFuncSym(self, c, name):
        for scope in c:
            if isinstance(scope, List):
                for x in scope:
                    if x.name == name and isinstance(x.mtype, MType):
                        return x
        return None

    # infer the type of an Id or function (expr) with expect and return the type (either old or new)
    def infer(self, c, expr, expect):
        if isinstance(expr, Id):
            sym = self.getSym(c, expr.name)
            sym.inferVar(expect)
            return sym.mtype
        elif isinstance(expr, ArrayCell):
            if (isinstance(expr.arr, Id)):
                sym = self.getSym(c, expr.arr.name)
                if isinstance(sym.mtype.eletype, Unknown):
                    sym.mtype.eletype = expect
                return sym.mtype.eletype

        else:
            sym = self.getSym(c,expr.method.name)
            sym.inferFuncOut(expect)
            return sym.mtype.restype

    def visitProgram(self, ast, c):
        varDecls = list(filter(lambda x: isinstance(x, VarDecl), ast.decl))
        varList = reduce(lambda acc, ele: acc + [ele.accept(self,acc)], varDecls, c)
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
            if x.name.name == 'main':
                foundMain = 1
            x.accept(self, c)
        if foundMain == 0:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, c):
        for x in c:
            if x.name == ast.variable.name:
                raise Redeclared(Variable(), ast.variable.name)
        var = None
        if ast.varDimen:
            eletype = (ast.varInit.accept(self, c) if ast.varInit else Unknown())
            mytype = ArrayType(ast.varDimen, eletype)
            var = Symbol(variable=ast, mtype = mytype)
        else:
            var = Symbol(variable=ast, mtype=(ast.varInit.accept(self, c) if ast.varInit else Unknown()))
        return var

    def visitFuncDecl(self, ast, c):
        # create a list of symbol for parameters
        paraList = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.param, [])
        sizePara = len(paraList)

        # visit local declarations
        localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.body[0], paraList)

        # combine them together to make local scope to visit the statements in body
        c = [localvar] + c
        # update the function para
        # c[1:] to advoid inside scope we have a variable has the same name as function.
        funcSym = self.getSym(c[1:], ast.name.name)
        for i in range(0, sizePara):
            if not isinstance(funcSym.mtype.intype[i], Unknown):
                if isinstance(c[0][i].mtype, Unknown):
                    c[0][i].mtype = funcSym.mtype.intype[i]
        # visit statements 
        for x in ast.body[1]:
            env = (c, ast.name.name)
            x.accept(self, env)
            # continuously update the function input type
            for i in range(0, sizePara):
                if not isinstance(funcSym.mtype.intype[i], Unknown):
                    if isinstance(c[0][i].mtype, Unknown):
                        c[0][i].mtype = funcSym.mtype.intype[i]
                funcSym.mtype.intype[i] = c[0][i].mtype

    def visitBinaryOp(self, ast, c):
        if ast.op in ('+', '-', '*', '\\', '%'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c[:-1], ast.left, IntType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c[:-1], ast.right, IntType())
            if isinstance(ast.left.accept(self, c), IntType):
                if isinstance(ast.right.accept(self, c), IntType):
                    return IntType()
        if ast.op in ('+.', '-.', '*.', '\\.'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c[:-1], ast.left, FloatType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c[:-1], ast.right, FloatType())
            if isinstance(ast.left.accept(self, c), FloatType):
                if isinstance(ast.right.accept(self, c), FloatType):
                    return FloatType()
        if ast.op == '&&' or (ast.op == '||'):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c[:-1], ast.left, BoolType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c[:-1], ast.right, BoolType())
            if isinstance(ast.left.accept(self, c), BoolType):
                if isinstance(ast.right.accept(self, c), BoolType):
                    return BoolType()
        if ast.op in ('<', '>', '<=', '>=', '==', '!='):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c[:-1], ast.left, IntType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c[:-1], ast.right, IntType())
            if isinstance(ast.left.accept(self, c), IntType):
                if isinstance(ast.right.accept(self, c), IntType):
                    return BoolType()
        if ast.op in ('<.', '>.', '<=.', '>=.', '=/='):
            if isinstance(ast.left.accept(self, c), Unknown):
                self.infer(c[:-1], ast.left, FloatType())
            if isinstance(ast.right.accept(self, c), Unknown):
                self.infer(c[:-1], ast.right, FloatType())
            if isinstance(ast.left.accept(self, c), FloatType):
                if isinstance(ast.right.accept(self, c), FloatType):
                    return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        if ast.op == '-':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c[:-1], ast.body, IntType())
            if isinstance(ast.body.accept(self, c), IntType):
                return IntType()
        if ast.op == '-.':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c[:-1], ast.body, FloatType())
            if isinstance(ast.body.accept(self, c), FloatType):
                return FloatType()
        if ast.op == '!':
            if isinstance(ast.body.accept(self, c), Unknown):
                self.infer(c[:-1], ast.body, BoolType())
            if isinstance(ast.body.accept(self, c), BoolType):
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        argsType = [x.accept(self, c) for x in ast.param]
        sym = self.getFuncSym(c, ast.method.name)
        for typ in argsType:
            if isinstance(typ, Unknown):
                raise TypeCannotBeInferred(c[-1])
        if sym:
            # check whether args are compatible with paras
            if len(argsType) == len(sym.mtype.intype):
                # try to infer the function parameters by args
                sym.inferFunc(argsType)
                # check if there are some parameters cannot infer type
                for typ in sym.mtype.intype:
                    if isinstance(typ, Unknown):
                        raise TypeMismatchInExpression(ast)
                
                
                pair = zip(sym.mtype.intype, argsType)
                for x in pair:
                    if type(x[0]) != type(x[1]):
                        raise TypeMismatchInExpression(ast)
                return sym.mtype.restype
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise Undeclared(Function(), ast.method.name)

    def visitId(self, ast, c):
        # if the last element is the outer statement contains the epxression than c[:-1]
        sym = (self.getSym(c, ast.name) if isinstance(c[-1], List) else self.getSym(c[:-1], ast.name))
        if sym:
            return sym.mtype
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, c):
        dimen = 0
        
        # count dimension and check type of indexes
        for x in ast.idx:
            if isinstance(x.accept(self,c), Unknown):
                self.infer(c, x, IntType())
            if not isinstance(x.accept(self, c), IntType):
                raise TypeMismatchInExpression(ast)
            dimen += 1
        
        # try to infer type
        if isinstance(ast.arr.accept(self, c), Unknown):
            self.infer(c, ast.arr, ArrayType([-1 for x in range(0, dimen)], Unknown()))

        if isinstance(ast.arr.accept(self, c), ArrayType):
            if not (len(ast.arr.accept(self,c).dimen) == dimen):
                raise TypeMismatchInExpression(ast)

            # there still some dimension has no size.
            if (-1) in ast.arr.accept(self,c).dimen:
                raise TypeCannotBeInferred(c[-1])
        else:
            raise TypeMismatchInExpression(ast)
        
        return ast.arr.accept(self,c).eletype
    
    def visitAssign(self, ast, c):
        c = c[0]
        typeLeft = ast.lhs.accept(self, c + [ast])
        typeRight = ast.rhs.accept(self, c + [ast])
        if isinstance(typeLeft, Unknown) and not isinstance(typeRight, Unknown):
            self.infer(c, ast.lhs, typeRight)
            typeLeft = ast.lhs.accept(self, c)
        if isinstance(typeRight, Unknown)and not isinstance(typeLeft, Unknown):
            self.infer(c, ast.rhs, typeLeft)
            typeRight = ast.rhs.accept(self, c)
        if not isinstance(typeLeft, Unknown) and not isinstance(typeRight, Unknown):
            if isinstance(typeLeft, ArrayType) and isinstance(typeRight, ArrayType):
                if not(typeLeft == typeRight):
                    raise TypeMismatchInStatement(ast)
            if type(typeLeft) != type(typeRight):
                raise TypeMismatchInStatement(ast)
        if isinstance(typeLeft, Unknown) and isinstance(typeRight, Unknown):
            raise TypeCannotBeInferred(ast)

    def visitIf(self, ast, c):
        scope = c[0]
        for ifthenStmt in ast.ifthenStmt:
            if isinstance(ifthenStmt[0].accept(self, scope + [ast]),Unknown):
                self.infer(scope, ifthenStmt[0], BoolType())

            if not isinstance(ifthenStmt[0].accept(self, scope),BoolType):
                raise TypeMismatchInStatement(ast)

            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ifthenStmt[1], [])
            
            # visit statements 
            for x in ifthenStmt[2]:
                x.accept(self, ([localvar] + scope, c[1]))
            
            
        
        if ast.elseStmt != ([],[]):
            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.elseStmt[0], [])
            for x in ast.elseStmt[1]:
                x.accept(self, ([localvar] + scope, c[1]))

    def visitFor(self, ast, c):
        # get the id
        # check if it is an intlit
        # try to infer
        scope = c[0]
        sym = self.infer(scope, ast.idx1, IntType())
        
        expr1 = self.infer(scope, ast.expr1, IntType()) if isinstance(ast.expr1.accept(self,scope + [ast]), Unknown) else ast.expr1.accept(self,scope + [ast])

        expr2 = self.infer(scope, ast.expr3, BoolType()) if isinstance(ast.expr2.accept(self,scope + [ast]), Unknown) else ast.expr2.accept(self,scope + [ast])
        
        expr3 = self.infer(scope, ast.expr3, IntType()) if isinstance(ast.expr3.accept(self,scope + [ast]), Unknown) else ast.expr3.accept(self,scope + [ast])

        if not (isinstance(sym, IntType) and  isinstance(expr1, IntType) and isinstance(expr2, BoolType) and isinstance(expr3, IntType)):
            raise TypeMismatchInStatement(ast)
        
        if ast.loop != ([],[]):
            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.loop[0], [])
            for x in ast.loop[1]:
                x.accept(self, ([localvar] + scope, c[1]))

    def visitContinue(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        sym = self.getFuncSym(c[0], c[1])
        if isinstance(sym.mtype.restype, VoidType):
            if ast.expr:
                raise TypeMismatchInStatement(ast)
        elif isinstance(sym.mtype.restype, Unknown):
            if ast.expr:
                if isinstance(ast.expr.accept(self, c[0] + [ast]), Unknown):
                    raise TypeCannotBeInferred(ast)
                else:
                    sym.mtype.restype = ast.expr.accept(self, c[0] + [ast])
            else:
                sym.mtype.restype = VoidType()
        else:
            if (not isinstance(sym.mtype.restype, VoidType)) and (ast.expr == None):
                raise TypeMismatchInStatement(ast)
            if type(sym.mtype.restype) is not type(ast.expr.accept(self, c[0])):
                raise TypeMismatchInStatement(ast)


    def visitDowhile(self, ast, c):
        scope = c[0]
        if ast.sl != ([],[]):
            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.sl[0], [])
            for x in ast.sl[1]:
                x.accept(self, ([localvar] + scope, c[1]))

        exp = self.infer(scope, ast.exp, BoolType()) if isinstance(ast.exp.accept(self,scope + [ast]), Unknown) else ast.exp.accept(self,scope + [ast])
        
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        scope = c[0]
        exp = self.infer(scope, ast.exp, BoolType()) if isinstance(ast.exp.accept(self,scope + [ast]), Unknown) else ast.exp.accept(self,scope + [ast])
        
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)

        if ast.sl != ([],[]):
            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.sl[0], [])
            for x in ast.sl[1]:
                x.accept(self, ([localvar] + scope, c[1]))

    def visitCallStmt(self, ast, c):
        c = c[0]
        argsType = [x.accept(self, c + [ast]) for x in ast.param]
        sym = self.getFuncSym(c,ast.method.name)
        if sym:
            sym.inferFuncOut(VoidType())
            # check if function output is voidtype
            if not isinstance(sym.mtype.restype, VoidType):
                raise TypeMismatchInStatement(ast)
            
            # check whether args are compatible with paras
            if len(argsType) == len(sym.mtype.intype):
                for typ in argsType:
                    if isinstance(typ, Unknown):
                        raise TypeCannotBeInferred(ast)
                # try to infer the function parameters by args
                sym.inferFunc(argsType)

                # check if there are some parameters cannot infer type
                for typ in sym.mtype.intype:
                    if isinstance(typ, Unknown):
                        raise TypeCannotBeInferred(ast)
                
                # check if args and paras are not matched
                pair = zip(sym.mtype.intype, argsType)
                for x in pair:
                    if type(x[0]) is not type(x[1]):
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