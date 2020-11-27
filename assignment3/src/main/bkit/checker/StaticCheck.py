
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
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

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

    def visitProgram(self,ast, c):
        # visit all function once
        # get the basic types in the parameters, if some parameters dont initialize just let them Type()
        # don't go to the statements inside because it can contain a call to another function that have not been declared

        func_list = list(map(lambda x: Symbol(x.name.name, MType([var.accept(self,c) for var in x.c]))))
        c.append(func_list)
        [self.visit(x,c) for x in ast.decl]

    def visitVarDecl(self, ast, c):
        return None
    
    def visitFuncDecl(self, ast, c):
        return None
    
    def visitBinaryOp(self, ast, c):
        return None
    
    def visitUnaryOp(self, ast, c):
        return None
    
    def visitCallExpr(self, ast, c):
        return None
    
    def visitId(self, ast, c):
        return None
    
    def visitArrayCell(self, ast, c):
        return None
    
    def visitAssign(self, ast, c):
        return None
    
    def visitIf(self, ast, c):
        return None
    
    def visitFor(self, ast, c):
        return None
    
    def visitContinue(self, ast, c):
        return None
    
    def visitBreak(self, ast, c):
        return None
    
    def visitReturn(self, ast, c):
        return None
    
    def visitDowhile(self, ast, c):
        return None

    def visitWhile(self, ast, c):
        return None

    def visitCallStmt(self, ast, c):
        return None
    
    def visitIntLiteral(self, ast, c):
        return None
    
    def visitFloatLiteral(self, ast, c):
        return None
    
    def visitBooleanLiteral(self, ast, c):
        return None
    
    def visitStringLiteral(self, ast, c):
        return None

    def visitArrayLiteral(self, ast, c):
        return None



        
