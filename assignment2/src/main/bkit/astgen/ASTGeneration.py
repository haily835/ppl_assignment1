from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AntiAST import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    # program: globalVar funcDeclPart mainFunc EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(ctx.globalVar().accept(self) + ctx.funcDeclPart().accept(self) + ctx.mainFunc().accept(self))

    # globalVar: (varDecl)*;
    def visitGlobalVar(self, ctx:BKITParser.GlobalVarContext):
        if (ctx.varDecl()):
            varList = [x.accept(self) for x in ctx.varDecl()]
            return reduce(lambda acc,ele: acc + ele, varList, [])
        else:
            return []

    # funcDeclPart: (funcDecl)*;
    def visitFuncDeclPart(self, ctx:BKITParser.FuncDeclPartContext):
        return [x.accept(self) for x in ctx.funcDecl()]

    # varDecl: VAR COLON varList SEMI;
    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        return ctx.varList().accept(self)
    
    # varList: varInit (COMMA varInit)*;
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return [x.accept(self) for x in ctx.varInit()]
    
    # varInit: variable ('=' literal)?;
    """
    class VarDecl(Decl):
    variable : Id
    varDimen : List[int] # empty list for scalar variable
    varInit  : Literal   # null if no initial """
    def visitVarInit(self, ctx:BKITParser.VarInitContext):
        var = ctx.variable().accept(self)
        if ctx.literal():
            return VarDecl(var[0], var[1], ctx.literal().accept(self))
        else:
            return VarDecl(var[0], var[1], None) 

    # variable: ID | ID dimens;
    def visitVariable(self, ctx:BKITParser.VariableContext):
        if ctx.dimens():
            return (Id(ctx.ID().getText()), ctx.dimens().accept(self))
        else:
            return (Id(ctx.ID().getText()), [])

    # dimens: (LS INT_LIT RS)+;
    def visitDimens(self, ctx:BKITParser.DimensContext):
        return [int(x.getText()) for x in ctx.INT_LIT()]
    
    # literal: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | array_lit;
    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if (ctx.INT_LIT()):
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif (ctx.FLOAT_LIT()):
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif (ctx.BOOL_LIT()):
            return BooleanLiteral(True) if ctx.BOOL_LIT().getText() == "True" else BooleanLiteral(False)
        elif (ctx.STRING_LIT()):
            return StringLiteral(ctx.STRING_LIT().getText())
        else:
            return ctx.array_lit().accept(self)
    
    # array_lit: LB (literal (COMMA literal)* | ) RB;
    # class ArrayLiteral(Literal): value:List[Literal]
    def visitArray_lit(self, ctx: BKITParser.Array_litContext):
        if (ctx.literal()):
            return ArrayLiteral([x.accept(self) for x in ctx.literal()])
        else:
            return ArrayLiteral([])

    def visitMainFunc(self, ctx:BKITParser.MainFuncContext):
        if ctx.paraDecl():
            return [FuncDecl(Id("main"), ctx.paraDecl().accept(self), ctx.body().accept(self))]
        else:
            return [FuncDecl(Id("main"), [], ctx.body().accept(self))]
    # funcDecl: FUNCTION COLON ID (paraDecl)? body;
    """
        class FuncDecl(Decl):
            name: Id
            param: List[VarDecl]
            body: Tuple[List[VarDecl],List[Stmt]]
    """
    def visitFuncDecl(self, ctx:BKITParser.FuncDeclContext):
        if ctx.paraDecl():
            return FuncDecl(Id(ctx.ID().getText()), ctx.paraDecl().accept(self), ctx.body().accept(self))
        else:
            return FuncDecl(Id(ctx.ID().getText()), [], ctx.body().accept(self))
    
    # paraDecl: PARAMETER COLON variable (COMMA variable)*;
    def visitParaDecl(self, ctx:BKITParser.ParaDeclContext):
        lst = [x.accept(self) for x in ctx.variable()]
        return list(map(lambda x: VarDecl(x[0], x[1], None),lst))

    # body: BODY COLON stmtList ENDBODY DOT;
    # return Tuple[List[VarDecl],List[Stmt]]
    def visitBody(self, ctx:BKITParser.BodyContext):
        return ctx.stmtList().accept(self)
    
    # stmtList: varDecl* otherStmt*;
    def visitStmtList(self,ctx:BKITParser.StmtListContext):
        varList = [x.accept(self) for x in ctx.varDecl()]
        varList = reduce(lambda acc,ele: acc+ele, varList, [])
        stmtList = [x.accept(self) for x in ctx.otherStmt()]
        return (varList, stmtList)

    # otherStmt: assignStmt | ifStmt | forStmt | whileStmt | dowhileStmt | breakStmt | continueStmt | callStmt | returnStmt;
    def visitOtherStmt(self, ctx:BKITParser.OtherStmtContext):
        if (ctx.assignStmt()):
            return ctx.assignStmt().accept(self)
        elif (ctx.ifStmt()):
            return ctx.ifStmt().accept(self)
        elif (ctx.forStmt()):
            return ctx.forStmt().accept(self)
        elif (ctx.whileStmt()):
            return ctx.whileStmt().accept(self)
        elif (ctx.dowhileStmt()):
            return ctx.dowhileStmt().accept(self)
        elif (ctx.breakStmt()):
            return ctx.breakStmt().accept(self)
        elif (ctx.continueStmt()):
            return ctx.continueStmt().accept(self)
        elif (ctx.callStmt()):
            return ctx.callStmt().accept(self)
        elif ctx.returnStmt():
            return ctx.returnStmt().accept(self)
    
    # assignStmt: lhs  '=' expr SEMI;
    """
    class Assign(Stmt):
    lhs: LHS
    rhs: Expr
    """
    def visitAssignStmt(self, ctx:BKITParser.AssignStmtContext):
        return Assign(ctx.lhs().accept(self), ctx.expr().accept(self))
    
    # lhs: ID | expr6;
    def visitLhs(self, ctx:BKITParser.LhsContext):
        if(ctx.ID()):
            return Id(ctx.ID().getText())
        else:
            return ctx.expr6().accept(self)

    # expr: expr1 (EQ | NOT_EQ | LT | GT | LTE | GTE | F_NOT_EQ | F_LT | F_GT | F_LTE | F_GTE) expr1 | expr1;
    def visitExpr(self, ctx:BKITParser.ExprContext):
        if (ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr1(0).accept(self), ctx.expr1(1).accept(self))
        else:
            return ctx.expr1(0).accept(self)

    # expr1: expr1 (AND | OR) expr2 | expr2;
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        if (ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr1().accept(self), ctx.expr2().accept(self))
        else:
            return ctx.expr2().accept(self)
    
    # expr2: expr2 (ADD | F_ADD | SUB | F_SUB) expr3 | expr3;
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        if (ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr2().accept(self), ctx.expr3().accept(self))
        else:
            return ctx.expr3().accept(self)
    
    # expr3: expr3 (MUL | F_MUL | DIV | F_DIV | REMAIN) expr4 | expr4;
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        if (ctx.getChildCount() == 3):
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr3().accept(self), ctx.expr4().accept(self))
        else:
            return ctx.expr4().accept(self)
    
    # expr4: NEG expr4 | expr5;
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        if (ctx.NEG()):
            return UnaryOp(ctx.NEG().getText(), ctx.expr4().accept(self))
        else: 
            return ctx.expr5().accept(self)
    
    # expr5: (SUB | F_SUB) expr5 | expr6;
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        if (ctx.getChildCount() == 2):
            return UnaryOp(ctx.getChild(0).getText(), ctx.expr5().accept(self))
        else:
            return ctx.expr6().accept(self)
    
    # expr6: expr6 (LS expr RS)+ | expr7;
    # class ArrayCell(LHS): arr:Expr idx:List[Expr]
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        if (ctx.expr6()):
            return ArrayCell(ctx.expr6().accept(self), [x.accept(self) for x in ctx.expr()])
        else:
            return ctx.expr7().accept(self)
    

    # expr7: ID LP argList RP | term;
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        if (ctx.getChildCount() == 4):
            return CallExpr(Id(ctx.ID().getText()), ctx.argList().accept(self))
        else:
            return ctx.term().accept(self)
    
    # term: (LP expr RP) | literal | ID
    def visitTerm(self, ctx: BKITParser.TermContext):
        if (ctx.getChildCount() == 3):
            return ctx.expr().accept(self)
        elif (ctx.literal()):
            return ctx.literal().accept(self)
        else:
            return Id(ctx.ID().getText())

    # argList: expr tailArg | ;
    def visitArgList(self, ctx: BKITParser.ArgListContext):
        if (ctx.expr()):
            return [ctx.expr().accept(self)] + ctx.tailArg().accept(self)
        else:
            return []
    
    # tailArg: COMMA expr tailArg | ;
    def visitTailArg(self, ctx: BKITParser.TailArgContext):
        if (ctx.getChildCount() == 3):
            return [ctx.expr().accept(self)] + ctx.tailArg().accept(self)
        else:
            return []
    
    # ifStmt: IF expr THEN stmtList (ELSEIF expr THEN stmtList)* (ELSE stmtList)? ENDIF DOT;
    # each expr stmtList will create a tuple 3 (expr , vardecl, stmt)
    def visitIfStmt(self, ctx: BKITParser.IfStmtContext):
        stmtList = [x.accept(self) for x in ctx.stmtList()]
        exprList = [x.accept(self) for x in ctx.expr()]
        if ctx.ELSE():
            elsePart = stmtList[-1]
            ifthenPart = list(map(lambda expr, stmt: (expr, stmt[0], stmt[1]),exprList, stmtList))
            return If(ifthenPart, elsePart) 
        else:
            ifthenPart = list(map(lambda expr, stmt: (expr, stmt[0], stmt[1]),exprList, stmtList))
            return If(ifthenPart, ([],[])) 
        
    # forStmt: FOR LP ID '=' expr COMMA expr COMMA expr RP DO stmtList ENDFOR DOT;
    def visitForStmt(self, ctx: BKITParser.ForStmtContext):
        return For(Id(ctx.ID().getText()), ctx.expr(0).accept(self), ctx.expr(1).accept(self), ctx.expr(2).accept(self), ctx.stmtList().accept(self))

    # whileStmt: WHILE expr DO stmtList ENDWHILE DOT;
    def visitWhileStmt(self, ctx: BKITParser.WhileStmtContext):
        return While(ctx.expr().accept(self), ctx.stmtList().accept(self))

    # dowhileStmt: DO stmtList WHILE expr ENDDO DOT;
    def visitDowhileStmt(self, ctx: BKITParser.DowhileStmtContext):
        return Dowhile(ctx.stmtList().accept(self), ctx.expr().accept(self))

    # breakStmt: BREAK SEMI;
    def visitBreakStmt(self, ctx: BKITParser.BreakStmtContext):
        return Break()

    # continueStmt: CONTINUE SEMI;
    def visitContinueStmt(self, ctx: BKITParser.ContinueStmtContext):
        return Continue() 
    
    # callStmt: ID LP argList RP SEMI;
    def visitCallStmt(self, ctx: BKITParser.CallStmtContext):
        return CallStmt(Id(ctx.ID().getText()), ctx.argList().accept(self))

    # returnStmt: RETURN (expr)? SEMI;
    def visitReturnStmt(self, ctx: BKITParser.ReturnStmtContext):
        if (ctx.expr()):
            return Return(ctx.expr().accept(self))
        else:
            return Return(None)


    
