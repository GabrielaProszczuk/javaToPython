from antlr4 import *
import sys
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from antlr4.error.ErrorListener import ErrorListener

class ErrorListener( ErrorListener ):

    def __init__(self):
        super(ErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("You gave a file with mistake, try again!"
        "        Info: " + str(msg) + "  Line: " + str(line) + " Column: " + str(column))
        #raise Exception("Oh no!!")

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     raise Exception("Oh no!!")

    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     raise Exception("Oh no!!")

    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     raise Exception("Oh no!!")