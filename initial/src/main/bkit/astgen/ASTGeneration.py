from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):


    def visitIds(self,ctx:BKITParser.IdsContext):
        size = len(ctx.ID())
        lst = []
        print("Thist is  test " + str(size))
        for i in range(1, size + 1):
            lst = lst + [Id(ctx.ID(i - 1).getText())]
        return lst
        print(lst)