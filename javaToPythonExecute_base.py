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

    def convertConditions(self, ctx):
        # conditions = ""
        # print(ctx.condition()[0].getText())
        if (ctx.condition()[0].NOT()):
            conditions = "not " + ctx.condition()[0].toNot().getText()
        else:
            conditions = ctx.condition()[0].getText()

        for i in range(1, len(ctx.condition())):
            if (ctx.cos()[i-1].getText() == "&&"):
                conditions += " and"
            elif (ctx.cos()[i-1].getText() == "||"):
                conditions += " or"
            if (ctx.condition()[i].NOT()):
                conditions += " not" + ctx.condition()[i].toNot().getText()
            else:
                conditions += " " + ctx.condition()[i].getText()
        self.convertedString += conditions
        
    def convertIfStatement(self, ctx, level):
        # condition = ctx.conditions().getText()
        # self.convertedString += self.getTabs(level) + "if (" + condition + "):\n"
        self.convertedString += self.getTabs(level) + "if (" 
        self.convertConditions(ctx.getChild(2))
        self.convertedString += "):\n"

        return level + 1

    def convertIfElseStatement(self, ctx, level):
        # condition = ctx.conditions().getText()
        # self.convertedString += self.getTabs(level) + "elif (" + condition + "):\n"
        # return level + 1
        self.convertedString += self.getTabs(level) + "elif (" 
        self.convertConditions(ctx.getChild(2))
        self.convertedString += "):\n"

        return level + 1

    def convertElseStatement(self, ctx, level):
        self.convertedString += self.getTabs(level) + "else:\n"
        return level + 1

    def convertConditionStatement(self, ctx, level):
        childCtx = ctx.getChild(0)
        childCtxRuleName = str(javaToPythonParser.ruleNames[childCtx.getRuleIndex()])
        if(childCtxRuleName == "statement_if"):
            level = self.convertIfStatement(childCtx, level)
        elif(childCtxRuleName == "statement_elseif"):
            level = self.convertIfElseStatement(childCtx, level)
        elif(childCtxRuleName == "statement_else"):
            level = self.convertElseStatement(childCtx, level)
        return level


    def convertMethodDeclaration(self, ctx, level):
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

        # Increase level of indendation
        return level + 1

    def convertForStatement(self, ctx, level):
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

        # Increase level of indendation
        return level + 1

    def convertWhileStatement(self, ctx, level):
        # self.convertedString += self.getTabs(level) + "while (" + ctx.condition().getText() + "):\n"

        self.convertedString += self.getTabs(level) + "while ("
        self.convertConditions(ctx.getChild(2))
        self.convertedString += "):\n"


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

        if (ruleName == "identifierDec"):
            level = self.convertIdentifierDec(ctx, level)

        if (ruleName == "incrementOperation"):
            level = self.convertIncrementOperation(ctx, level)

        for i in range(ctx.getChildCount()):
            element = ctx.getChild(i)
            if (isinstance(element, RuleContext)):
                self.explore(element, level, indents + 1)


    def enterStart(self, ctx):
        self.explore(ctx, 0,0)
        print("-----------------------------------\nConversion result:")
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
