# Generated from javaToPython.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .javaToPythonParser import javaToPythonParser
else:
    from javaToPythonParser import javaToPythonParser

# This class defines a complete listener for a parse tree produced by javaToPythonParser.
class javaToPythonListener(ParseTreeListener):

    # Enter a parse tree produced by javaToPythonParser#start.
    def enterStart(self, ctx:javaToPythonParser.StartContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#start.
    def exitStart(self, ctx:javaToPythonParser.StartContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement.
    def enterStatement(self, ctx:javaToPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement.
    def exitStatement(self, ctx:javaToPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_print.
    def enterStatement_print(self, ctx:javaToPythonParser.Statement_printContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_print.
    def exitStatement_print(self, ctx:javaToPythonParser.Statement_printContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_println.
    def enterStatement_println(self, ctx:javaToPythonParser.Statement_printlnContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_println.
    def exitStatement_println(self, ctx:javaToPythonParser.Statement_printlnContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#inPrint.
    def enterInPrint(self, ctx:javaToPythonParser.InPrintContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#inPrint.
    def exitInPrint(self, ctx:javaToPythonParser.InPrintContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#operacjeMatematyczne.
    def enterOperacjeMatematyczne(self, ctx:javaToPythonParser.OperacjeMatematyczneContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#operacjeMatematyczne.
    def exitOperacjeMatematyczne(self, ctx:javaToPythonParser.OperacjeMatematyczneContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#identifierDec.
    def enterIdentifierDec(self, ctx:javaToPythonParser.IdentifierDecContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#identifierDec.
    def exitIdentifierDec(self, ctx:javaToPythonParser.IdentifierDecContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#identifierInitializer.
    def enterIdentifierInitializer(self, ctx:javaToPythonParser.IdentifierInitializerContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#identifierInitializer.
    def exitIdentifierInitializer(self, ctx:javaToPythonParser.IdentifierInitializerContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_condition.
    def enterStatement_condition(self, ctx:javaToPythonParser.Statement_conditionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_condition.
    def exitStatement_condition(self, ctx:javaToPythonParser.Statement_conditionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_if.
    def enterStatement_if(self, ctx:javaToPythonParser.Statement_ifContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_if.
    def exitStatement_if(self, ctx:javaToPythonParser.Statement_ifContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_elseif.
    def enterStatement_elseif(self, ctx:javaToPythonParser.Statement_elseifContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_elseif.
    def exitStatement_elseif(self, ctx:javaToPythonParser.Statement_elseifContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_else.
    def enterStatement_else(self, ctx:javaToPythonParser.Statement_elseContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_else.
    def exitStatement_else(self, ctx:javaToPythonParser.Statement_elseContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#block.
    def enterBlock(self, ctx:javaToPythonParser.BlockContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#block.
    def exitBlock(self, ctx:javaToPythonParser.BlockContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#block_function.
    def enterBlock_function(self, ctx:javaToPythonParser.Block_functionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#block_function.
    def exitBlock_function(self, ctx:javaToPythonParser.Block_functionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#compare.
    def enterCompare(self, ctx:javaToPythonParser.CompareContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#compare.
    def exitCompare(self, ctx:javaToPythonParser.CompareContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#conditions.
    def enterConditions(self, ctx:javaToPythonParser.ConditionsContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#conditions.
    def exitConditions(self, ctx:javaToPythonParser.ConditionsContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#condition.
    def enterCondition(self, ctx:javaToPythonParser.ConditionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#condition.
    def exitCondition(self, ctx:javaToPythonParser.ConditionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#condOp.
    def enterCondOp(self, ctx:javaToPythonParser.CondOpContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#condOp.
    def exitCondOp(self, ctx:javaToPythonParser.CondOpContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#toNot.
    def enterToNot(self, ctx:javaToPythonParser.ToNotContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#toNot.
    def exitToNot(self, ctx:javaToPythonParser.ToNotContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#orOperation.
    def enterOrOperation(self, ctx:javaToPythonParser.OrOperationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#orOperation.
    def exitOrOperation(self, ctx:javaToPythonParser.OrOperationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#andOperation.
    def enterAndOperation(self, ctx:javaToPythonParser.AndOperationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#andOperation.
    def exitAndOperation(self, ctx:javaToPythonParser.AndOperationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_for.
    def enterStatement_for(self, ctx:javaToPythonParser.Statement_forContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_for.
    def exitStatement_for(self, ctx:javaToPythonParser.Statement_forContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#expression_for.
    def enterExpression_for(self, ctx:javaToPythonParser.Expression_forContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#expression_for.
    def exitExpression_for(self, ctx:javaToPythonParser.Expression_forContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_while.
    def enterStatement_while(self, ctx:javaToPythonParser.Statement_whileContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_while.
    def exitStatement_while(self, ctx:javaToPythonParser.Statement_whileContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement_return.
    def enterStatement_return(self, ctx:javaToPythonParser.Statement_returnContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement_return.
    def exitStatement_return(self, ctx:javaToPythonParser.Statement_returnContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#assignment.
    def enterAssignment(self, ctx:javaToPythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#assignment.
    def exitAssignment(self, ctx:javaToPythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#methodDec.
    def enterMethodDec(self, ctx:javaToPythonParser.MethodDecContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#methodDec.
    def exitMethodDec(self, ctx:javaToPythonParser.MethodDecContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#params.
    def enterParams(self, ctx:javaToPythonParser.ParamsContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#params.
    def exitParams(self, ctx:javaToPythonParser.ParamsContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#methodCall.
    def enterMethodCall(self, ctx:javaToPythonParser.MethodCallContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#methodCall.
    def exitMethodCall(self, ctx:javaToPythonParser.MethodCallContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#minusOperator.
    def enterMinusOperator(self, ctx:javaToPythonParser.MinusOperatorContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#minusOperator.
    def exitMinusOperator(self, ctx:javaToPythonParser.MinusOperatorContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#oneArgumentExpressionFor.
    def enterOneArgumentExpressionFor(self, ctx:javaToPythonParser.OneArgumentExpressionForContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#oneArgumentExpressionFor.
    def exitOneArgumentExpressionFor(self, ctx:javaToPythonParser.OneArgumentExpressionForContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#incrementOperationFor.
    def enterIncrementOperationFor(self, ctx:javaToPythonParser.IncrementOperationForContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#incrementOperationFor.
    def exitIncrementOperationFor(self, ctx:javaToPythonParser.IncrementOperationForContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#decrementOperationFor.
    def enterDecrementOperationFor(self, ctx:javaToPythonParser.DecrementOperationForContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#decrementOperationFor.
    def exitDecrementOperationFor(self, ctx:javaToPythonParser.DecrementOperationForContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#oneArgumentExpression.
    def enterOneArgumentExpression(self, ctx:javaToPythonParser.OneArgumentExpressionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#oneArgumentExpression.
    def exitOneArgumentExpression(self, ctx:javaToPythonParser.OneArgumentExpressionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#twoArgumentExpression.
    def enterTwoArgumentExpression(self, ctx:javaToPythonParser.TwoArgumentExpressionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#twoArgumentExpression.
    def exitTwoArgumentExpression(self, ctx:javaToPythonParser.TwoArgumentExpressionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#incrementOperation.
    def enterIncrementOperation(self, ctx:javaToPythonParser.IncrementOperationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#incrementOperation.
    def exitIncrementOperation(self, ctx:javaToPythonParser.IncrementOperationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#decrementOperation.
    def enterDecrementOperation(self, ctx:javaToPythonParser.DecrementOperationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#decrementOperation.
    def exitDecrementOperation(self, ctx:javaToPythonParser.DecrementOperationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#notOperation.
    def enterNotOperation(self, ctx:javaToPythonParser.NotOperationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#notOperation.
    def exitNotOperation(self, ctx:javaToPythonParser.NotOperationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#expression.
    def enterExpression(self, ctx:javaToPythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#expression.
    def exitExpression(self, ctx:javaToPythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#value.
    def enterValue(self, ctx:javaToPythonParser.ValueContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#value.
    def exitValue(self, ctx:javaToPythonParser.ValueContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#identifierType.
    def enterIdentifierType(self, ctx:javaToPythonParser.IdentifierTypeContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#identifierType.
    def exitIdentifierType(self, ctx:javaToPythonParser.IdentifierTypeContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#methodType.
    def enterMethodType(self, ctx:javaToPythonParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#methodType.
    def exitMethodType(self, ctx:javaToPythonParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#boolean_val.
    def enterBoolean_val(self, ctx:javaToPythonParser.Boolean_valContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#boolean_val.
    def exitBoolean_val(self, ctx:javaToPythonParser.Boolean_valContext):
        pass



del javaToPythonParser