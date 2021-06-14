import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
 

class javaToPythonListener(ParseTreeListener):
    code = ""
    indents = 0
    convertedString = ""

    def getTabs(self, level):
        tabs = ""
        for i in range(level):
            tabs += "    "
        return tabs

    def convertIfStatement(self, ctx, level):
        condition = ctx.statement_if().condition().getText()
        self.convertedString += self.getTabs(level) + "if (" + condition + "):\n"
        return level + 1

    def convertIfElseStatement(self, ctx, level):
        condition = ctx.statement_elseif().condition().getText()
        self.convertedString += self.getTabs(level) + "elif (" + condition + "):\n"
        return level + 1

    def convertElseStatement(self, ctx, level):
        self.convertedString += self.getTabs(level) + "else:\n"
        return level + 1

    def convertConditionStatement(self, ctx, level):
        childCtx = ctx.getChild(0)
        childCtxRuleName = str(javaToPythonParser.ruleNames[childCtx.getRuleIndex()])
        if(childCtxRuleName == "statement_if"):
            level = self.convertIfStatement(ctx, level)
        elif(childCtxRuleName == "statement_elseif"):
            level = self.convertIfElseStatement(ctx, level)
        elif(childCtxRuleName == "statement_else"):
            level = self.convertElseStatement(ctx, level)
        return level


    def convertMethodDeclaration(self, ctx, level):
        # Extracting method type
        methodType = ctx.methodType().getText()
        # Extracting method name
        methodName = ctx.ID().getText()

        # Extracting parameters
        params = ""
        if (len(ctx.params().ID())):
            params = ctx.params().ID()[0].getText()
            for i in range (1, len(ctx.params().ID())):
                params += ", " + ctx.params().ID()[i].getText()

        # Create "type methodName("
        self.convertedString += "def " + methodName + "(" + params + "):\n"

        # IncreASE level of indendation
        return level + 1


    def convertForStatement(self, ctx, level):
        print(ctx.getText())
        letter = ctx.assignment().ID().getText()
        startNumber = ctx.assignment().identifierInitializer().getText()
        compare = ctx.expression_for().compare().getText()
        boundaryNumber = ctx.expression_for().expression()[1].getText()
        rangeNumbers = ""

        if (compare == "<"):
            if (startNumber == "0"):
                rangeNumbers = boundaryNumber
            else:
                rangeNumbers = str(startNumber) + ", " + str(boundaryNumber)

        elif (compare == "<="):
            if (startNumber == "0"):
                rangeNumbers = int(boundaryNumber) + 1
            else:
                rangeNumbers = str(startNumber) + ", " + str(int(boundaryNumber) + 1)

        forConditionString = letter + " in range (" + str(rangeNumbers) + ")"
        self.convertedString += self.getTabs(level) + "for " + forConditionString + ":\n"

        # IncreASE level of indendation
        return level + 1

    def convertWhileStatement(self, ctx, level):
        self.convertedString += self.getTabs(level) + "while " + "(" + ctx.condition().getText() + "):\n"
        return level + 1


    def convertIdentifierDec(self, ctx, level):
        letter = ctx.ID().getText()
        assignValue = ""
        if (ctx.identifierInitializer()):
            assignValue = " = " + ctx.identifierInitializer().getText()
        self.convertedString += self.getTabs(level) + letter + assignValue + "\n"
        return level

    def convertIncrementOperation(self, ctx, level):
        letter = ctx.ID().getText()
        self.convertedString += self.getTabs(level) + letter + " += 1\n"
        return level

    def convertDecrementOperation(self, ctx, level):
        letter = ctx.ID().getText()
        self.convertedString += self.getTabs(level) + letter + " -= 1\n"
        return level



    # methodCall: 	ID L_PAREN expression (COMMA expression)* R_PAREN;
    def convertMethodCall(self, ctx, level):
        args = ctx.expression()[0].getText()
        for i in range (1, len(ctx.expression())):
            args += ", " + ctx.expression()[i].getText()
        self.convertedString += self.getTabs(level) + ctx.ID().getText() + "(" + args + ")\n"
        return level

    def explore(self, ctx, level, indents):
        ruleName = str(javaToPythonParser.ruleNames[ctx.getRuleIndex()])

        # for i in range(indents):
        #     print("    ", end = '')

        # print(ruleName + ": " + ctx.getText())

        if (ruleName == "statement_condition"):
            level = self.convertConditionStatement(ctx, level)

        if (ruleName == "statement_for"):
            level = self.convertForStatement(ctx, level)

        if (ruleName == "statement_while"):
            level = self.convertWhileStatement(ctx, level)

        if (ruleName == "methodDec"):
            level = self.convertMethodDeclaration(ctx, level)

        if (ruleName == "methodCall"):
            level = self.convertMethodCall(ctx, level)

        print(ruleName)
        if (ruleName == "identifierDec"):
            level = self.convertIdentifierDec(ctx, level)
        if (ruleName == "incrementOperation"):
            level = self.convertIncrementOperation(ctx, level)


        
        # if (ruleName == "statement"):
        #     self.convertedString += "statement\n"
        # if (ruleName == "assignment"):
        #     self.convertedString += "assignment\n"

        for i in range(ctx.getChildCount()):
            element = ctx.getChild(i)
            if (isinstance(element, RuleContext)):
                self.explore(element, level, indents + 1)


    def enterStart(self, ctx):
        self.explore(ctx, 0,0)
        print("\n\n-----------------------------------\nConversion result:")
        print(self.convertedString)

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
