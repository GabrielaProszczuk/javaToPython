import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
 

class javaToPythonListener(ParseTreeListener):
    code = ""
    indents = 0
    def explore(self, ctx, level, indents):
        ruleName = str(javaToPythonParser.ruleNames[ctx.getRuleIndex()])
        # for i in range(ctx.getChildCount()):
        #     element = ctx.getChild(i)
        #     if (isinstance(element, RuleContext)):
        #         self.explore(element, level, indents + 1)
    def enterStart(self, ctx):
        self.explore(ctx, 0,0)
    def enterStatement(self, ctx):
        print("statement")
    def enterExpression(self, ctx):
        print("expression")
    def enterValue(self, ctx):
        print("value")
    def enterExpOperation(self, ctx):
        print("ExpOperation")
    def enterMethodType(self, ctx):
        print("MethodType")
    def enterIdentifierDec(self, ctx):
        print("IdentifierDec")       
    def enterAssignment(self, ctx):
        print("Assigement")
    def enterMethodDec(self, ctx):
        print("MethodDec")
    def enterParams(self, ctx):
        print("Params")
    def enterCompare(self, ctx):
        print("Compare")
    def enterCondition(self, ctx):
        print("Condition")
    def enterBlock(self, ctx):
        print("Block")
    def enterMethodCall(self, ctx):
        print("MehodCall")
    def enterStatement_for(self, ctx):
        print("For")
    def enterStatement_while(self, ctx):
        print("While")
       #print(list(ctx.getChildren()))
        for child in list(ctx.getChildren()):
            print(child.getText())
    def enterStatement_if(self, ctx):
        print("If")
    def enterStatement_return(self, ctx):
        print("Return")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = javaToPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = javaToPythonParser(stream)
    tree = parser.start()
    printer = javaToPythonListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)



if __name__ == '__main__':
    main(sys.argv)

