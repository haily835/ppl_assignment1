# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#relational_op.
    def visitRelational_op(self, ctx:BKITParser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_op.
    def visitLogical_op(self, ctx:BKITParser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding_op.
    def visitAdding_op(self, ctx:BKITParser.Adding_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying_op.
    def visitMultiplying_op(self, ctx:BKITParser.Multiplying_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_op.
    def visitSign_op(self, ctx:BKITParser.Sign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argList.
    def visitArgList(self, ctx:BKITParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#tailArg.
    def visitTailArg(self, ctx:BKITParser.TailArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_op.
    def visitIndex_op(self, ctx:BKITParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term.
    def visitTerm(self, ctx:BKITParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#globalVar.
    def visitGlobalVar(self, ctx:BKITParser.GlobalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDeclPart.
    def visitFuncDeclPart(self, ctx:BKITParser.FuncDeclPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDecl.
    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varList.
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varInit.
    def visitVarInit(self, ctx:BKITParser.VarInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDecl.
    def visitFuncDecl(self, ctx:BKITParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paraDecl.
    def visitParaDecl(self, ctx:BKITParser.ParaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paraList.
    def visitParaList(self, ctx:BKITParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mainFunc.
    def visitMainFunc(self, ctx:BKITParser.MainFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#otherStmt.
    def visitOtherStmt(self, ctx:BKITParser.OtherStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignStmt.
    def visitAssignStmt(self, ctx:BKITParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStmt.
    def visitIfStmt(self, ctx:BKITParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStmt.
    def visitForStmt(self, ctx:BKITParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStmt.
    def visitWhileStmt(self, ctx:BKITParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhileStmt.
    def visitDowhileStmt(self, ctx:BKITParser.DowhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStmt.
    def visitBreakStmt(self, ctx:BKITParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStmt.
    def visitContinueStmt(self, ctx:BKITParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStmt.
    def visitCallStmt(self, ctx:BKITParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStmt.
    def visitReturnStmt(self, ctx:BKITParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmtList.
    def visitStmtList(self, ctx:BKITParser.StmtListContext):
        return self.visitChildren(ctx)



del BKITParser