from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda acc,ele: acc + [ele.accept(self,[acc])], ctx.decl,[])
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        # ignore the function name
        if (ctx.name in o[0][1:]):
            raise RedeclaredVariable(ctx.name)
        else:
            return ctx.name
    
    # FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if (ctx.name in o[0]):
            raise RedeclaredFunction(ctx.name)

        # visit local 
        local = reduce(lambda acc,ele: acc + [ele.accept(self, [acc] + o)], ctx.param + ctx.body[0],[ctx.name])
        for x in ctx.body[1]:
            x.accept(self,[local] + o)
        return ctx.name
        
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if (ctx.name in o[0][1:]):
            raise RedeclaredConstant(ctx.name)
        else:
            return ctx.name

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
    
    def visitId(self,ctx:Id,o:object):
        flag = 1
        # print(o)
        for x in o:
            if ctx.name in x:
                flag = 0
        if flag:
            raise UndeclaredIdentifier(ctx.name)


