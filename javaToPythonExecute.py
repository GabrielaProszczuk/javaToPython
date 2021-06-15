import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from ErrorListener import ErrorListener

class javaToPythonListener(ParseTreeListener):
    code = ""
    convertedString = ""

    def saveToFile(self, fileName):
        f = open(fileName, "w")
        f.write(self.convertedString)
        f.close()

    def getIntent(self, level):
        tabs = ""
        for i in range(level):
            tabs += "    "
        return tabs

    def convertConditions(self, ctx):
        if (ctx.condition()[0].NOT()):
            conditions = "not " + ctx.condition()[0].toNot().getText()
        else:
            conditions = ctx.condition()[0].getText()

        for i in range(1, len(ctx.condition())):
            if (ctx.condOp()[i-1].getText() == "&&"):
                conditions += " and"
            elif (ctx.condOp()[i-1].getText() == "||"):
                conditions += " or"
            if (ctx.condition()[i].NOT()):
                conditions += " not" + ctx.condition()[i].toNot().getText()
            else:
                conditions += " " + ctx.condition()[i].getText()
        self.convertedString += conditions
        
    def convertIfStatement(self, ctx, level):
        self.convertedString += self.getIntent(level) + "if (" 
        self.convertConditions(ctx.getChild(2))
        self.convertedString += "):\n"
        return level + 1

    def convertIfElseStatement(self, ctx, level):
        self.convertedString += self.getIntent(level) + "elif (" 
        self.convertConditions(ctx.getChild(2))
        self.convertedString += "):\n"
        return level + 1

    def convertElseStatement(self, ctx, level):
        self.convertedString += self.getIntent(level) + "else:\n"
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
        methodName = ctx.ID().getText()

        params = ""
        if (len(ctx.params().ID())):
            params = ctx.params().ID()[0].getText()
            for i in range (1, len(ctx.params().ID())):
                params += ", " + ctx.params().ID()[i].getText()

        self.convertedString += "def " + methodName + "(" + params + "):\n"
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
        self.convertedString += self.getIntent(level) + "for " + forConditionString + ":\n"
        return level + 1

    def convertWhileStatement(self, ctx, level):
        self.convertedString += self.getIntent(level) + "while ("
        self.convertConditions(ctx.getChild(2))
        self.convertedString += "):\n"
        return level + 1

    def convertIdentifierDec(self, ctx, level):
        letter = ctx.ID().getText()
        assignValue = ""
        if (ctx.identifierInitializer()):
            if(ctx.identifierInitializer().getText() == "true"):
                assignValue = " = True" 
            elif(ctx.identifierInitializer().getText() == "false"):
                assignValue = " = False"
            else:
                assignValue = " = " + ctx.identifierInitializer().getText()
            self.convertedString += self.getIntent(level) + letter + assignValue + "\n"
        return level

    def convertIncrementOperation(self, ctx, level):
        letter = ctx.ID().getText()
        self.convertedString += self.getIntent(level) + letter + " += 1\n"
        return level

    def convertDecrementOperation(self, ctx, level):
        letter = ctx.ID().getText()
        self.convertedString += self.getIntent(level) + letter + " -= 1\n"
        return level

    def convertMethodCall(self, ctx, level):
        args = ctx.expression()[0].getText()
        for i in range (1, len(ctx.expression())):
            args += ", " + ctx.expression()[i].getText()
        self.convertedString += self.getIntent(level) + ctx.ID().getText() + "(" + args + ")\n"
        return level

    def explore(self, ctx, level):
        ruleName = str(javaToPythonParser.ruleNames[ctx.getRuleIndex()])

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
        
        if (ruleName == "decrementOperation"):
            level = self.convertDecrementOperation(ctx, level)

        for i in range(ctx.getChildCount()):
            element = ctx.getChild(i)
            if (isinstance(element, RuleContext)):
                self.explore(element, level)
       

    def enterStart(self, ctx):
        self.explore(ctx, 0)

       # print("Result:")
       # print(self.convertedString)

def handleFiles(files):
    for i in range(len(files)):
        inputFile = files[i]
        name = inputFile.split(".")
        outputFile = name[0]+ "_output.py"
        input_stream = FileStream(inputFile)
        lexer = javaToPythonLexer(input_stream)
        lexer.removeErrorListeners()
        lexer._listeners = [ ErrorListener() ]
        stream = CommonTokenStream(lexer)
        parser = javaToPythonParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener( ErrorListener() )
        lexer._listeners = [ ErrorListener() ]
        tree = parser.start()
        printer = javaToPythonListener()
        walker = ParseTreeWalker()
        try:
            walker.walk(printer, tree)
        except:
            print("Can't proccess this file!")
        printer.saveToFile(outputFile)

def main(argv):
    handleFiles(argv[1:])

        

if __name__ == '__main__':
    main(sys.argv)

