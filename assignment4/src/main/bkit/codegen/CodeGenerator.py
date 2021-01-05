'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from functools import reduce
from AST import *
from abc import ABC, abstractmethod

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    # change type only if the current type is Unknown
    def inferFunc(self, expect):
        for i in range(0, len(expect)):
            if isinstance(self.mtype.partype[i], Unknown):
                self.mtype.partype[i] = expect[i]

    def inferFuncOut(self, expect):
        if isinstance(self.mtype, MType):
            if isinstance(self.mtype.rettype, Unknown):
                self.mtype.rettype = expect
        # else:
        #     raise Undeclared(Function(), self.name)

    def inferVar(self, expect):
        if isinstance(self.mtype, Unknown):
            self.mtype = expect

class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self,et,s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  
class Unknown(Type):
    pass
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isDup=False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame  = frame
        self.sym    = sym
        self.isLeft = isLeft
        self.isDup  = isDup
class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        # list of function with full detail of types
        env = StaticChecker(ast).check()
        print(env[0][-2].name)
        print(env[0][-2].mtype.partype)
        print(env[0][-2].mtype.rettype.eleType)
        print(env[0][-1].name)
        print(env[0][-1].mtype.partype[0].eleType)
        
        gc = CodeGenVisitor(ast, env[0], dir_)
        gc.visit(ast, None)

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        # visit global variables = static field in java
        globalVarDecls = list(filter(lambda ele: isinstance(ele,VarDecl), ast.decl))

        # generate directives for static fields
        for var in globalVarDecls:
            for sym in self.env:
                if sym.name == var.variable.name:
                    if var.varDimen == []:
                        self.emit.printout(self.emit.emitATTRIBUTE(sym.name, sym.mtype, False, ""))
                    else:
                        typ = sym.mtype.eleType
                        for dimen in var.varDimen:
                            typ = ArrayType(typ, var.varDimen)
                        self.emit.printout(self.emit.emitATTRIBUTE(sym.name, typ, False, ""))
                            
            

        # generate default constructor
        self.genInit()

        # generate class init to initialize global vars
        self.genClassInit(globalVarDecls)

        # visit function declarations
        globalFuncs = list(filter(lambda ele: isinstance(ele,FuncDecl), ast.decl))
        [x.accept(self, MethodEnv(None, self.env)) for x in globalFuncs]
        self.emit.emitEPILOG()
        return c

    def genClassInit(self, globalVarDecls):
        methodname, methodtype = "<clinit>", MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)

        # generate code to initialize the variable
        for vardecl in globalVarDecls:
            initCode, initType = vardecl.varInit.accept(self,SubBody(frame, self.env))
            self.emit.printout(initCode)     
            self.emit.printout(self.emit.emitPUTSTATIC('MCClass' + '.' + vardecl.variable.name, initType, frame))
        
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))

        frame.exitScope()
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
    # The following code is just for initial, students should remove it and write your visitor from here
    def genMain(self,o):
        methodname,methodtype = "main",MType([ArrayType(StringType(),[])],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitPUSHICONST(120, frame))
        sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
        sym = next(filter(lambda x: x.name == "print",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    def visitVarDecl(self,ctx, o):
        idx = o.frame.getNewIndex()

        initCode, initType = ctx.varInit.accept(self, Access(o.frame, o.sym, False))
        # write variable
        # if len(ctx.varDimen) > 0:
        #     initCode = self.emit.emitPUSHICONST(ctx.varDimen[0], o.frame) + initCode

        initCode += self.emit.emitWRITEVAR(ctx.variable.name, initType, idx, o.frame)

        # directive
        dir = self.emit.emitVAR(idx, ctx.variable.name, initType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        self.emit.printout(dir)

        if ctx.varDimen != []:
            if 'I' in dir:
                initType = ArrayType(IntType(), ctx.varDimen)
            elif 'F' in dir:
                initType = ArrayType(FloatType(), ctx.varDimen)
            elif 'Z' in dir:
                initType = ArrayType(BoolType(), ctx.varDimen)
            elif 'String' in dir:
                initType = ArrayType(StringType(), ctx.varDimen)

        return Symbol(ctx.variable.name, initType, Index(idx)), initCode

    def visitFuncDecl(self,ctx,o):
        hasReturn = False
        funcSym = None
        for func in o.sym:
            if func.name == ctx.name.name:
                funcSym = func
    
        if funcSym.name == "main":
            funcSym.mtype = MType([ArrayType(StringType(),[])],VoidType())
        
        frame = Frame(funcSym.name, funcSym.mtype.rettype)

        self.emit.printout(self.emit.emitMETHOD(funcSym.name,funcSym.mtype,True,frame))
        frame.enterScope(True)
        
        # directive for parameters
        if funcSym.name == "main":
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), 'args', funcSym.mtype.partype[0], frame.getStartLabel(), frame.getEndLabel() ,frame ))
        else:
            dir = ""
            param = zip(ctx.param, funcSym.mtype.partype)
            for para in param:
                idx = frame.getNewIndex()
                dir += self.emit.emitVAR(idx, para[0].variable.name, para[1], frame.getStartLabel(), frame.getEndLabel(), frame)
                o.sym += [Symbol(para[0].variable.name, para[1], Index(idx))]
            self.emit.printout(dir)

        # directive for local variables
        varInitCode = ""
        for vardecl in ctx.body[0]:
            sym, initCode = vardecl.accept(self, SubBody(frame, o.sym[::-1]))
            o.sym += [sym]    
            varInitCode += initCode
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(varInitCode)

        for stmt in ctx.body[1]:
            stmt.accept(self, SubBody(frame, o.sym[::-1]))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if funcSym.name == "main":
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitId(self, ctx, o):
        if o.isLeft:
            for id in o.sym:
                if id.name == ctx.name:
                    if isinstance(id.value, Index):
                        return self.emit.emitWRITEVAR(id.name, id.mtype, id.value.value, o.frame), id.mtype
                    else:
                        return self.emit.emitPUTSTATIC(id.value.value + '.' + id.name, id.mtype, o.frame), id.mtype
        else:
            for id in o.sym:
                if id.name == ctx.name:
                    if isinstance(id.value, Index):
                        return self.emit.emitREADVAR(id.name, id.mtype, id.value.value, o.frame), id.mtype
                    else:
                        if type(id.mtype) is ArrayType:
                            typ = id.mtype.eleType
                            for dimen in id.mtype.dimen:
                                typ = ArrayType(typ, id.mtype.dimen)
                            return self.emit.emitGETSTATIC(id.value.value + '.' + id.name, typ, o.frame), id.mtype
                        return self.emit.emitGETSTATIC(id.value.value + '.' + id.name, id.mtype, o.frame), id.mtype
    
    
    def visitAssign(self, ctx, o):
        codeR, typeR = ctx.rhs.accept(self, Access(o.frame, o.sym, False))
        codeL, typeL = ctx.lhs.accept(self, Access(o.frame, o.sym, True))
        
        if type(ctx.lhs) is ArrayCell:
            lines = codeL.split('\n')
            lines.insert(-2, codeR[:-1])
            for line in lines:
                self.emit.printout(line + '\n')
        else:
            self.emit.printout(codeR + codeL)


    def visitBinaryOp(self,ctx,o):
        left, typeL = ctx.left.accept(self,o)
        right, typeR = ctx.right.accept(self,o)
        code = left + right
        if ctx.op in ('+', '-', '*', '\\', '+.', '-.', '*.', '\\.', '%'):
            code += (self.emit.emitADDOP(ctx.op[0],typeL,o.frame) if ctx.op in ('+', '-', '+.', '-.') else self.emit.emitMULOP(ctx.op[0],typeL,o.frame))
            return code, typeL

        if ctx.op in ('<', '<=', '>', '>=', '!=', '==', '<.', '<=.', '>.', '>=.', '=/='):
            code += self.emit.emitREOP(ctx.op, typeL, o.frame)
            return code, BoolType()

        if ctx.op == '&&':
            code += self.emit.emitANDOP(o.frame)
            return code, BoolType()
        
        if ctx.op == '||':
            code += self.emit.emitOROP(o.frame)
            return code, BoolType()

    def visitUnaryOp(self,ctx,o):
        code, type = ctx.body.accept(self, o)
        if ctx.op == '!':
            code += self.emit.emitNOT(type, o.frame)
            return code, type
        if ctx.op in ('-', '-.'):
            code += self.emit.emitNEGOP(type, o.frame)
            return code, type


    def visitCallExpr(self, ctx, o):
        retCode = ''
        # code to put param on frame
        for x in ctx.param:
            code, typ = x.accept(self, o)
            retCode += code
        
        # find the function
        funcSym = None
        for x in o.sym:
            if x.name == ctx.method.name:
                funcSym = x
        
        retCode += self.emit.emitINVOKESTATIC(funcSym.value.value+"/" + funcSym.name,funcSym.mtype,o.frame)

        return retCode, funcSym.mtype.rettype

    def visitCallStmt(self, ctx, o):
        # code to put param on frame
        for x in ctx.param:
            code, typ = x.accept(self, Access(o.frame, o.sym, False))
            self.emit.printout(code)
        
        # find the function
        funcSym = None
        for x in o.sym:
            if x.name == ctx.method.name:
                funcSym = x
        
        self.emit.printout(self.emit.emitINVOKESTATIC(funcSym.value.value+"/" + funcSym.name,funcSym.mtype,o.frame))
        # self.emit.printout(self.emit.emitPOP(o.frame))

    def visitReturn(self, ctx, o):
        if ctx.expr:
            code, typ = ctx.expr.accept(self, Access(o.frame, o.sym, False))
            self.emit.printout(code)
            self.emit.printout(self.emit.emitRETURN(typ, o.frame))
            
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))

    def visitIf(self, ctx, o):
        isLast = False
        lastReturn = None
        # generate next label for each else if
        labelNexts = [o.frame.getNewLabel() for x in range(0, len(ctx.ifthenStmt) - 1)]

        # generate next label for else
        if ctx.elseStmt[0] != [] or ctx.elseStmt[1] != []:
            labelNexts += [o.frame.getNewLabel()]
        
        # generate out label
        labelOut = o.frame.getNewLabel()
        
        for i in range(0, len(ctx.ifthenStmt)):
            exprCode, exprType = ctx.ifthenStmt[i][0].accept(self, Access(o.frame, o.sym, False))

            # emit the label for the current elseif part
            if (i != 0):
                self.emit.printout(self.emit.emitLABEL(labelNexts[i-1], o.frame))
            self.emit.printout(exprCode)

            # go to next elseif if false
            # at the last elseif part there may be the next else part or not
            if (i + 1) == len(ctx.ifthenStmt): 
                if i < len(labelNexts):
                    self.emit.printout(self.emit.emitIFFALSE(labelNexts[i], o.frame))
                else:
                    self.emit.printout(self.emit.emitIFFALSE(labelOut, o.frame))
            else:
                self.emit.printout(self.emit.emitIFFALSE(labelNexts[i], o.frame))

            # visit inside scope
            o.frame.enterScope(False)
            varInitCode = ''
            localSym = o.sym
            for x in ctx.ifthenStmt[i][1]:
                sym, initCode = x.accept(self, SubBody(o.frame,localSym))
                localSym = [sym] + localSym
                varInitCode += initCode

            self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
            self.emit.printout(varInitCode)

            for x in ctx.ifthenStmt[i][2]:
                x.accept(self, SubBody(o.frame,localSym))

            self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
            o.frame.exitScope()

            self.emit.printout(self.emit.emitGOTO(labelOut, o.frame))
            i += 1

        if ctx.elseStmt[0] != [] or ctx.elseStmt[1] != []:
            isLast = True
            self.emit.printout(self.emit.emitLABEL(labelNexts[-1], o.frame))
            o.frame.enterScope(False)
            varInitCode = ''
            localSym = o.sym
            for x in ctx.elseStmt[0]:
                sym, initCode = x.accept(self, SubBody(o.frame,localSym))
                localSym = [sym] + localSym
                varInitCode += initCode
            self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
            self.emit.printout(varInitCode)
            for x in ctx.elseStmt[1]:
                if isinstance(x, Return):
                    lastReturn = x
                    continue
                x.accept(self, SubBody(o.frame,localSym))
            self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
            o.frame.exitScope()

        self.emit.printout(self.emit.emitLABEL(labelOut, o.frame))
        if lastReturn:
            lastReturn.accept(self, SubBody(o.frame, localSym))

    def visitFor(self, ctx, o):
        o.frame.enterLoop()
        labelBegin = o.frame.getNewLabel()
        
        # code to initialize the variable
        codeInit, typeInit = ctx.expr1.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(codeInit)
        codeId, typeId = ctx.idx1.accept(self, Access(o.frame, o.sym, True))
        self.emit.printout(codeId)

        # emit label begin
        self.emit.printout(self.emit.emitLABEL(labelBegin, o.frame))

        # code to evaluate the condition
        codeCon, typeCon = ctx.expr2.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(codeCon)

        # code to go to Label Out if false
        self.emit.printout(self.emit.emitIFFALSE(o.frame.getBreakLabel(), o.frame))

        # code to execute the statement inside
        o.frame.enterScope(False)
        localSyms = o.sym
        varInitCodes = ''
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
        for var in ctx.loop[0]:
            sym, varInitCode = var.accept(self, SubBody(o.frame, localSyms))
            localSyms = [sym] + localSyms
            varInitCodes += varInitCode

        self.emit.printout(varInitCodes)

        [x.accept(self, SubBody(o.frame, localSyms)) for x in ctx.loop[1]]
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()

        # continue label = go to the update state and start a new iteration
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))

        # code to update the variable
        codeExpr, typeExpr = ctx.expr3.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(codeExpr)
        loadIdCode, typeId = ctx.idx1.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(loadIdCode)

        
        # adding 
        self.emit.printout(self.emit.emitADDOP('+', IntType(), o.frame))
        updateIdCode, typeUpdate = ctx.idx1.accept(self, Access(o.frame, o.sym, True))
        self.emit.printout(updateIdCode)

        # go to LabelBegin
        self.emit.printout(self.emit.emitGOTO(labelBegin, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))

        o.frame.exitLoop()

    def visitWhile(self, ctx, o):
        o.frame.enterLoop()
        labelBegin = o.frame.getNewLabel()

        # emit the label begin
        self.emit.printout(self.emit.emitLABEL(labelBegin, o.frame))

        # evalue the expression
        exprCode, exprType = ctx.exp.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(exprCode)

        # code if false go to break label
        self.emit.printout(self.emit.emitIFFALSE(o.frame.getBreakLabel(), o.frame))

        # code for inside scope
        o.frame.enterScope(False)
        localSyms = o.sym
        varInitCodes = ''

        # start label of inside scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))

        # directive for inside var
        for var in ctx.sl[0]:
            sym, initCode = var.accept(self, SubBody(o.frame, localSyms))
            localSyms = [sym] + localSyms
            varInitCodes += initCode

        # init code var
        self.emit.printout(varInitCodes)

        # code for statements inside
        [x.accept(self, SubBody(o.frame, localSyms)) for x in ctx.sl[1]]

        # print end label of scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()

        # emit Continue label
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))

        # emit go to the begin label
        self.emit.printout(self.emit.emitGOTO(labelBegin, o.frame))

        # emit break label
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))

        # exitLoop
        o.frame.exitLoop()

    def visitDowhile(self, ctx, o): 
        o.frame.enterLoop()
        labelBegin = o.frame.getNewLabel()
        # emit the label begin
        self.emit.printout(self.emit.emitLABEL(labelBegin, o.frame))

        # code for inside scope
        o.frame.enterScope(False)
        localSyms = o.sym
        varInitCodes = ''

        # start label of inside scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))

        # directive for inside var
        for var in ctx.sl[0]:
            sym, initCode = var.accept(self, SubBody(o.frame, localSyms))
            localSyms = [sym] + localSyms
            varInitCodes += initCode

        # init code var
        self.emit.printout(varInitCodes)

        # code for statements inside
        [x.accept(self, SubBody(o.frame, localSyms)) for x in ctx.sl[1]]

        # print end label of scope
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()

        # emit Continue label
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))

        # evalue the expression
        exprCode, exprType = ctx.exp.accept(self, Access(o.frame, o.sym, False))
        self.emit.printout(exprCode)

        # code if false go to break label
        self.emit.printout(self.emit.emitIFFALSE(o.frame.getBreakLabel(), o.frame))


        # emit go to the begin label
        self.emit.printout(self.emit.emitGOTO(labelBegin, o.frame))

        # emit break label
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))

        # exitLoop
        o.frame.exitLoop()

    def visitBreak(self, ctx, o): 
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        
    def visitContinue(self, ctx, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
    
    def visitArrayCell(self, ctx, o):
        retCode = ''
        codeId, typeId = ctx.arr.accept(self, Access(o.frame, o.sym, False))
        retCode += codeId

        for idx in ctx.idx[:-1]:
            codeExp, typeExp = idx.accept(self, Access(o.frame, o.sym, False))
            retCode += codeExp
            retCode += self.emit.emitALOAD(ArrayType(ArrayType(None, None), []), o.frame)
        
        codeExp, typeExp = ctx.idx[-1].accept(self, Access(o.frame, o.sym, False))
        retCode += codeExp
        if o.isLeft:
            retCode += self.emit.emitASTORE(typeId.eleType, o.frame)
        else:
            retCode += self.emit.emitREADVAR2("" ,typeId.eleType, o.frame)
        return retCode, typeId.eleType

    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()

    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(str(ctx.value), o.frame), FloatType()

    def visitStringLiteral(self, ctx, o):
        return self.emit.emitPUSHCONST('"' + ctx.value + '"', StringType(), o.frame), StringType()

    def visitBooleanLiteral(self,ctx,o):
        return (self.emit.emitPUSHICONST(str(ctx.value), o.frame), BoolType())

    def visitArrayLiteral(self, ctx, o):

        retCode = ""
        eleCode = ""
        eleType = None
        retType = None
        initType = None
        idx = 0

        # put the size on stack
        retCode += self.emit.emitPUSHICONST(len(ctx.value), o.frame)

        # code to push elements on the stack
        for ele in ctx.value:
            eleCode += self.emit.emitDUP(o.frame)
            eleCode += self.emit.emitPUSHICONST(idx,o.frame)
            code, typ = ele.accept(self,o)
            eleType = typ
            eleCode += code
            eleCode += self.emit.emitASTORE(typ, o.frame)
            idx += 1

        if type(eleType) is ArrayType:
            retType = ArrayType(eleType, [len(ctx.value)] + eleType.dimen)
        else:
            retType = ArrayType(eleType, [len(ctx.value)])


        # put the pointer
        retCode += self.emit.emitPUSHARRAY(retType, o.frame)
        # put the code to intialize ele
        retCode += eleCode
        return retCode, retType
            
class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.libName = "io"
        self.global_envi = [
                    Symbol("read", MType([], StringType()), CName(self.libName)),
                    Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                    Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName)),
                    Symbol("string_of_float", MType([FloatType()], StringType()), CName(self.libName)),
                    Symbol("string_of_bool", MType([BoolType()], StringType()), CName(self.libName)),
                    Symbol("int_of_float", MType([FloatType()], IntType()), CName(self.libName)),
                    Symbol("float_to_int", MType([IntType()], FloatType()), CName(self.libName)),
                    Symbol("int_of_string", MType([StringType()], IntType()), CName(self.libName)),
                    Symbol("float_of_string", MType([StringType()], FloatType()), CName(self.libName)),
                    Symbol("bool_of_string", MType([StringType()], BoolType()), CName(self.libName)),
                    ]

    def check(self):
        return self.visit(self.ast,self.global_envi)
        

    # get Symbol object by name
    def getSym(self, c, name):
        for scope in c:
            if isinstance(scope, List):
                for x in scope:
                    if x.name == name:
                        return x

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
            return sym.mtype.rettype

    def visitProgram(self, ast, c):
        varDecls = list(filter(lambda x: isinstance(x, VarDecl), ast.decl))
        varList = reduce(lambda acc, ele: acc + [ele.accept(self,acc)], varDecls, c)
        c = varList

        funcDecls = list(filter(lambda x: isinstance(x, FuncDecl), ast.decl))
        for i in range(0, len(funcDecls)):
            c.append(Symbol(name=(funcDecls[i].name.name), mtype=(MType([Unknown() for x in range(0, len(funcDecls[i].param))], Unknown())), value=CName('MCClass')))
        
        c = [c]
        # foundMain = 0
        for x in funcDecls:
            if x.name.name == 'main':
                foundMain = 1
            x.accept(self, c)
        # if foundMain == 0:
        #     raise NoEntryPoint()
        return c


    def visitVarDecl(self, ast, c):
        # for x in c:
        #     if x.name == ast.variable.name:
        #         raise Redeclared(Variable(), ast.variable.name)
        var = None
        if ast.varDimen:
            eletype = (ast.varInit.accept(self, c) if ast.varInit else Unknown())
            mytype = ArrayType(eletype, ast.varDimen)
            var = Symbol(ast.variable.name, mytype, CName('MCClass'))
        else:
            var = Symbol(ast.variable.name, (ast.varInit.accept(self, c) if ast.varInit else Unknown()), CName('MCClass'))
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
            if not isinstance(funcSym.mtype.partype[i], Unknown):
                if isinstance(c[0][i].mtype, Unknown):
                    c[0][i].mtype = funcSym.mtype.partype[i]
        
        # visit statements 
        for x in ast.body[1]:
            env = [c, ast.name.name]
            x.accept(self, env)
            # continuously update the function input type
            for i in range(0, sizePara):
                if not isinstance(funcSym.mtype.partype[i], Unknown):
                    if isinstance(c[0][i].mtype, Unknown):
                        c[0][i].mtype = funcSym.mtype.partype[i]
                funcSym.mtype.partype[i] = c[0][i].mtype

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
        # raise TypeMismatchInExpression(ast)

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
        # raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        argsType = [x.accept(self, c) for x in ast.param]
        sym = self.getFuncSym(c, ast.method.name)

        # modify here
        sym.inferFunc(argsType)
        return sym.mtype.rettype

        # for typ in argsType:
        #     if isinstance(typ, Unknown):
        #         raise TypeCannotBeInferred(c[-1])
        # if sym:
        #     # check whether args are compatible with paras
        #     if len(argsType) == len(sym.mtype.intype):
        #         # try to infer the function parameters by args
        #         sym.inferFunc(argsType)
        #         # check if there are some parameters cannot infer type
        #         for typ in sym.mtype.intype:
        #             if isinstance(typ, Unknown):
        #                 raise TypeMismatchInExpression(ast)
                
                
        #         pair = zip(sym.mtype.intype, argsType)
        #         for x in pair:
        #             if type(x[0]) != type(x[1]):
        #                 raise TypeMismatchInExpression(ast)
        #         return sym.mtype.restype
        #     else:
        #         raise TypeMismatchInExpression(ast)
        # else:
        #     raise Undeclared(Function(), ast.method.name)

    def visitId(self, ast, c):
        # if the last element is the outer statement contains the epxression than c[:-1]
        sym = (self.getSym(c, ast.name) if isinstance(c[-1], List) else self.getSym(c[:-1], ast.name))
        if sym:
            return sym.mtype
        # else:
        #     raise Undeclared(Identifier(), ast.name)

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
            self.infer(c, ast.arr, ArrayType(Unknown(),[-1 for x in range(0, dimen)]))

        # if isinstance(ast.arr.accept(self, c), ArrayType):
        #     if not (len(ast.arr.accept(self,c).dimen) == dimen):
        #         raise TypeMismatchInExpression(ast)

        #     there still some dimension has no size.
        #     if (-1) in ast.arr.accept(self,c).dimen:
        #         raise TypeCannotBeInferred(c[-1])
        # else:
        #     raise TypeMismatchInExpression(ast)
        
        return ast.arr.accept(self,c).eleType
    
    def visitAssign(self, ast, c):
        env = c[0]
        typeLeft = ast.lhs.accept(self, env + [ast])
        typeRight = ast.rhs.accept(self, env + [ast])
        if isinstance(typeLeft, Unknown) and not isinstance(typeRight, Unknown):
            self.infer(env, ast.lhs, typeRight)
            typeLeft = ast.lhs.accept(self, env)
        if isinstance(typeRight, Unknown)and not isinstance(typeLeft, Unknown):
            self.infer(env, ast.rhs, typeLeft)
            typeRight = ast.rhs.accept(self, env)
        # if not isinstance(typeLeft, Unknown) and not isinstance(typeRight, Unknown):
        #     if isinstance(typeLeft, ArrayType) and isinstance(typeRight, ArrayType):
        #         if not(typeLeft == typeRight):
        #             raise TypeMismatchInStatement(ast)
        #     if type(typeLeft) != type(typeRight):
        #         raise TypeMismatchInStatement(ast)
        # if isinstance(typeLeft, Unknown) and isinstance(typeRight, Unknown):
        #     raise TypeCannotBeInferred(ast)

    def visitIf(self, ast, c):
        scope = c[0]
        for ifthenStmt in ast.ifthenStmt:
            if isinstance(ifthenStmt[0].accept(self, scope + [ast]),Unknown):
                self.infer(scope, ifthenStmt[0], BoolType())

            # if not isinstance(ifthenStmt[0].accept(self, scope),BoolType):
            #     raise TypeMismatchInStatement(ast)

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

        # if not (isinstance(sym, IntType) and  isinstance(expr1, IntType) and isinstance(expr2, BoolType) and isinstance(expr3, IntType)):
        #     raise TypeMismatchInStatement(ast)
        
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
        # modify here
        if isinstance(sym.mtype.rettype, Unknown):
            if ast.expr:
                sym.mtype.rettype = ast.expr.accept(self, c[0] + [ast])
            else:
                sym.mtype.rettype = VoidType()
        # else:
        #     if (not isinstance(sym.mtype.restype, VoidType)) and (ast.expr == None):
        #         raise TypeMismatchInStatement(ast)
        #     if type(sym.mtype.restype) is not type(ast.expr.accept(self, c[0])):
        #         raise TypeMismatchInStatement(ast)


    def visitDowhile(self, ast, c):
        scope = c[0]
        if ast.sl != ([],[]):
            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.sl[0], [])
            for x in ast.sl[1]:
                x.accept(self, ([localvar] + scope, c[1]))

        exp = self.infer(scope, ast.exp, BoolType()) if isinstance(ast.exp.accept(self,scope + [ast]), Unknown) else ast.exp.accept(self,scope + [ast])
        
        # if not isinstance(exp, BoolType):
        #     raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        scope = c[0]
        exp = self.infer(scope, ast.exp, BoolType()) if isinstance(ast.exp.accept(self,scope + [ast]), Unknown) else ast.exp.accept(self,scope + [ast])
        
        # if not isinstance(exp, BoolType):
        #     raise TypeMismatchInStatement(ast)

        if ast.sl != ([],[]):
            localvar = reduce(lambda acc, ele: acc + [ele.accept(self, acc)], ast.sl[0], [])
            for x in ast.sl[1]:
                x.accept(self, ([localvar] + scope, c[1]))

    def visitCallStmt(self, ast, c):
        c = c[0]
        argsType = [x.accept(self, c + [ast]) for x in ast.param]
        sym = self.getFuncSym(c,ast.method.name)
        sym.inferFuncOut(VoidType())
        sym.inferFunc(argsType)
        
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