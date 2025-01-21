# Generated from GosuParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GosuParser import GosuParser
else:
    from GosuParser import GosuParser

# This class defines a complete listener for a parse tree produced by GosuParser.
class GosuParserListener(ParseTreeListener):

    # Enter a parse tree produced by GosuParser#start.
    def enterStart(self, ctx:GosuParser.StartContext):
        pass

    # Exit a parse tree produced by GosuParser#start.
    def exitStart(self, ctx:GosuParser.StartContext):
        pass


    # Enter a parse tree produced by GosuParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:GosuParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:GosuParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#usesStatementList.
    def enterUsesStatementList(self, ctx:GosuParser.UsesStatementListContext):
        pass

    # Exit a parse tree produced by GosuParser#usesStatementList.
    def exitUsesStatementList(self, ctx:GosuParser.UsesStatementListContext):
        pass


    # Enter a parse tree produced by GosuParser#usesStatement.
    def enterUsesStatement(self, ctx:GosuParser.UsesStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#usesStatement.
    def exitUsesStatement(self, ctx:GosuParser.UsesStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#usesFeatureLiteral.
    def enterUsesFeatureLiteral(self, ctx:GosuParser.UsesFeatureLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#usesFeatureLiteral.
    def exitUsesFeatureLiteral(self, ctx:GosuParser.UsesFeatureLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:GosuParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:GosuParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#annotation.
    def enterAnnotation(self, ctx:GosuParser.AnnotationContext):
        pass

    # Exit a parse tree produced by GosuParser#annotation.
    def exitAnnotation(self, ctx:GosuParser.AnnotationContext):
        pass


    # Enter a parse tree produced by GosuParser#classDeclaration.
    def enterClassDeclaration(self, ctx:GosuParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#classDeclaration.
    def exitClassDeclaration(self, ctx:GosuParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#classSignature.
    def enterClassSignature(self, ctx:GosuParser.ClassSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#classSignature.
    def exitClassSignature(self, ctx:GosuParser.ClassSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#enhancementDeclaration.
    def enterEnhancementDeclaration(self, ctx:GosuParser.EnhancementDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#enhancementDeclaration.
    def exitEnhancementDeclaration(self, ctx:GosuParser.EnhancementDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#enhancementSignature.
    def enterEnhancementSignature(self, ctx:GosuParser.EnhancementSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#enhancementSignature.
    def exitEnhancementSignature(self, ctx:GosuParser.EnhancementSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:GosuParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:GosuParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#interfaceSignature.
    def enterInterfaceSignature(self, ctx:GosuParser.InterfaceSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#interfaceSignature.
    def exitInterfaceSignature(self, ctx:GosuParser.InterfaceSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#structureDeclaration.
    def enterStructureDeclaration(self, ctx:GosuParser.StructureDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#structureDeclaration.
    def exitStructureDeclaration(self, ctx:GosuParser.StructureDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#structureSignature.
    def enterStructureSignature(self, ctx:GosuParser.StructureSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#structureSignature.
    def exitStructureSignature(self, ctx:GosuParser.StructureSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:GosuParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:GosuParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#enumSignature.
    def enterEnumSignature(self, ctx:GosuParser.EnumSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#enumSignature.
    def exitEnumSignature(self, ctx:GosuParser.EnumSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#annotationDeclaration.
    def enterAnnotationDeclaration(self, ctx:GosuParser.AnnotationDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#annotationDeclaration.
    def exitAnnotationDeclaration(self, ctx:GosuParser.AnnotationDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#annotationSignature.
    def enterAnnotationSignature(self, ctx:GosuParser.AnnotationSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#annotationSignature.
    def exitAnnotationSignature(self, ctx:GosuParser.AnnotationSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#classBody.
    def enterClassBody(self, ctx:GosuParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#classBody.
    def exitClassBody(self, ctx:GosuParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#enhancementBody.
    def enterEnhancementBody(self, ctx:GosuParser.EnhancementBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#enhancementBody.
    def exitEnhancementBody(self, ctx:GosuParser.EnhancementBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#interfaceBody.
    def enterInterfaceBody(self, ctx:GosuParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#interfaceBody.
    def exitInterfaceBody(self, ctx:GosuParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#structureBody.
    def enterStructureBody(self, ctx:GosuParser.StructureBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#structureBody.
    def exitStructureBody(self, ctx:GosuParser.StructureBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#enumBody.
    def enterEnumBody(self, ctx:GosuParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#enumBody.
    def exitEnumBody(self, ctx:GosuParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#annotationBody.
    def enterAnnotationBody(self, ctx:GosuParser.AnnotationBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#annotationBody.
    def exitAnnotationBody(self, ctx:GosuParser.AnnotationBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#enumConstants.
    def enterEnumConstants(self, ctx:GosuParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by GosuParser#enumConstants.
    def exitEnumConstants(self, ctx:GosuParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by GosuParser#enumConstant.
    def enterEnumConstant(self, ctx:GosuParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by GosuParser#enumConstant.
    def exitEnumConstant(self, ctx:GosuParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by GosuParser#classMembers.
    def enterClassMembers(self, ctx:GosuParser.ClassMembersContext):
        pass

    # Exit a parse tree produced by GosuParser#classMembers.
    def exitClassMembers(self, ctx:GosuParser.ClassMembersContext):
        pass


    # Enter a parse tree produced by GosuParser#enhancementMembers.
    def enterEnhancementMembers(self, ctx:GosuParser.EnhancementMembersContext):
        pass

    # Exit a parse tree produced by GosuParser#enhancementMembers.
    def exitEnhancementMembers(self, ctx:GosuParser.EnhancementMembersContext):
        pass


    # Enter a parse tree produced by GosuParser#interfaceMembers.
    def enterInterfaceMembers(self, ctx:GosuParser.InterfaceMembersContext):
        pass

    # Exit a parse tree produced by GosuParser#interfaceMembers.
    def exitInterfaceMembers(self, ctx:GosuParser.InterfaceMembersContext):
        pass


    # Enter a parse tree produced by GosuParser#structureMembers.
    def enterStructureMembers(self, ctx:GosuParser.StructureMembersContext):
        pass

    # Exit a parse tree produced by GosuParser#structureMembers.
    def exitStructureMembers(self, ctx:GosuParser.StructureMembersContext):
        pass


    # Enter a parse tree produced by GosuParser#annotationMembers.
    def enterAnnotationMembers(self, ctx:GosuParser.AnnotationMembersContext):
        pass

    # Exit a parse tree produced by GosuParser#annotationMembers.
    def exitAnnotationMembers(self, ctx:GosuParser.AnnotationMembersContext):
        pass


    # Enter a parse tree produced by GosuParser#function.
    def enterFunction(self, ctx:GosuParser.FunctionContext):
        pass

    # Exit a parse tree produced by GosuParser#function.
    def exitFunction(self, ctx:GosuParser.FunctionContext):
        pass


    # Enter a parse tree produced by GosuParser#constructor.
    def enterConstructor(self, ctx:GosuParser.ConstructorContext):
        pass

    # Exit a parse tree produced by GosuParser#constructor.
    def exitConstructor(self, ctx:GosuParser.ConstructorContext):
        pass


    # Enter a parse tree produced by GosuParser#property.
    def enterProperty(self, ctx:GosuParser.PropertyContext):
        pass

    # Exit a parse tree produced by GosuParser#property.
    def exitProperty(self, ctx:GosuParser.PropertyContext):
        pass


    # Enter a parse tree produced by GosuParser#defaultValueFunction.
    def enterDefaultValueFunction(self, ctx:GosuParser.DefaultValueFunctionContext):
        pass

    # Exit a parse tree produced by GosuParser#defaultValueFunction.
    def exitDefaultValueFunction(self, ctx:GosuParser.DefaultValueFunctionContext):
        pass


    # Enter a parse tree produced by GosuParser#functionSignature.
    def enterFunctionSignature(self, ctx:GosuParser.FunctionSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#functionSignature.
    def exitFunctionSignature(self, ctx:GosuParser.FunctionSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#constructorSignature.
    def enterConstructorSignature(self, ctx:GosuParser.ConstructorSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#constructorSignature.
    def exitConstructorSignature(self, ctx:GosuParser.ConstructorSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#functionBody.
    def enterFunctionBody(self, ctx:GosuParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#functionBody.
    def exitFunctionBody(self, ctx:GosuParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#statementBlock.
    def enterStatementBlock(self, ctx:GosuParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by GosuParser#statementBlock.
    def exitStatementBlock(self, ctx:GosuParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by GosuParser#statement.
    def enterStatement(self, ctx:GosuParser.StatementContext):
        pass

    # Exit a parse tree produced by GosuParser#statement.
    def exitStatement(self, ctx:GosuParser.StatementContext):
        pass


    # Enter a parse tree produced by GosuParser#ifStatement.
    def enterIfStatement(self, ctx:GosuParser.IfStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#ifStatement.
    def exitIfStatement(self, ctx:GosuParser.IfStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#elseStatement.
    def enterElseStatement(self, ctx:GosuParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#elseStatement.
    def exitElseStatement(self, ctx:GosuParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#tryCatchFinallyStatement.
    def enterTryCatchFinallyStatement(self, ctx:GosuParser.TryCatchFinallyStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#tryCatchFinallyStatement.
    def exitTryCatchFinallyStatement(self, ctx:GosuParser.TryCatchFinallyStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#catchClause.
    def enterCatchClause(self, ctx:GosuParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by GosuParser#catchClause.
    def exitCatchClause(self, ctx:GosuParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by GosuParser#throwStatement.
    def enterThrowStatement(self, ctx:GosuParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#throwStatement.
    def exitThrowStatement(self, ctx:GosuParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#returnStatement.
    def enterReturnStatement(self, ctx:GosuParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#returnStatement.
    def exitReturnStatement(self, ctx:GosuParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#whileStatement.
    def enterWhileStatement(self, ctx:GosuParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#whileStatement.
    def exitWhileStatement(self, ctx:GosuParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:GosuParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:GosuParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#switchStatement.
    def enterSwitchStatement(self, ctx:GosuParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#switchStatement.
    def exitSwitchStatement(self, ctx:GosuParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#switchBlockStatement.
    def enterSwitchBlockStatement(self, ctx:GosuParser.SwitchBlockStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#switchBlockStatement.
    def exitSwitchBlockStatement(self, ctx:GosuParser.SwitchBlockStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#caseOrDefaultStatement.
    def enterCaseOrDefaultStatement(self, ctx:GosuParser.CaseOrDefaultStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#caseOrDefaultStatement.
    def exitCaseOrDefaultStatement(self, ctx:GosuParser.CaseOrDefaultStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#usingStatement.
    def enterUsingStatement(self, ctx:GosuParser.UsingStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#usingStatement.
    def exitUsingStatement(self, ctx:GosuParser.UsingStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#assertStatement.
    def enterAssertStatement(self, ctx:GosuParser.AssertStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#assertStatement.
    def exitAssertStatement(self, ctx:GosuParser.AssertStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#localVarStatement.
    def enterLocalVarStatement(self, ctx:GosuParser.LocalVarStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#localVarStatement.
    def exitLocalVarStatement(self, ctx:GosuParser.LocalVarStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#breakStatement.
    def enterBreakStatement(self, ctx:GosuParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#breakStatement.
    def exitBreakStatement(self, ctx:GosuParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#continueStatement.
    def enterContinueStatement(self, ctx:GosuParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#continueStatement.
    def exitContinueStatement(self, ctx:GosuParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#assignStatement.
    def enterAssignStatement(self, ctx:GosuParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#assignStatement.
    def exitAssignStatement(self, ctx:GosuParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#forEachStatement.
    def enterForEachStatement(self, ctx:GosuParser.ForEachStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#forEachStatement.
    def exitForEachStatement(self, ctx:GosuParser.ForEachStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#finallyStatement.
    def enterFinallyStatement(self, ctx:GosuParser.FinallyStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#finallyStatement.
    def exitFinallyStatement(self, ctx:GosuParser.FinallyStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#indexRest.
    def enterIndexRest(self, ctx:GosuParser.IndexRestContext):
        pass

    # Exit a parse tree produced by GosuParser#indexRest.
    def exitIndexRest(self, ctx:GosuParser.IndexRestContext):
        pass


    # Enter a parse tree produced by GosuParser#indexVar.
    def enterIndexVar(self, ctx:GosuParser.IndexVarContext):
        pass

    # Exit a parse tree produced by GosuParser#indexVar.
    def exitIndexVar(self, ctx:GosuParser.IndexVarContext):
        pass


    # Enter a parse tree produced by GosuParser#iteratorVar.
    def enterIteratorVar(self, ctx:GosuParser.IteratorVarContext):
        pass

    # Exit a parse tree produced by GosuParser#iteratorVar.
    def exitIteratorVar(self, ctx:GosuParser.IteratorVarContext):
        pass


    # Enter a parse tree produced by GosuParser#propertySignature.
    def enterPropertySignature(self, ctx:GosuParser.PropertySignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#propertySignature.
    def exitPropertySignature(self, ctx:GosuParser.PropertySignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#field.
    def enterField(self, ctx:GosuParser.FieldContext):
        pass

    # Exit a parse tree produced by GosuParser#field.
    def exitField(self, ctx:GosuParser.FieldContext):
        pass


    # Enter a parse tree produced by GosuParser#delegate.
    def enterDelegate(self, ctx:GosuParser.DelegateContext):
        pass

    # Exit a parse tree produced by GosuParser#delegate.
    def exitDelegate(self, ctx:GosuParser.DelegateContext):
        pass


    # Enter a parse tree produced by GosuParser#delegateStatement.
    def enterDelegateStatement(self, ctx:GosuParser.DelegateStatementContext):
        pass

    # Exit a parse tree produced by GosuParser#delegateStatement.
    def exitDelegateStatement(self, ctx:GosuParser.DelegateStatementContext):
        pass


    # Enter a parse tree produced by GosuParser#modifiers.
    def enterModifiers(self, ctx:GosuParser.ModifiersContext):
        pass

    # Exit a parse tree produced by GosuParser#modifiers.
    def exitModifiers(self, ctx:GosuParser.ModifiersContext):
        pass


    # Enter a parse tree produced by GosuParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:GosuParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by GosuParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:GosuParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by GosuParser#parameterDeclarationList.
    def enterParameterDeclarationList(self, ctx:GosuParser.ParameterDeclarationListContext):
        pass

    # Exit a parse tree produced by GosuParser#parameterDeclarationList.
    def exitParameterDeclarationList(self, ctx:GosuParser.ParameterDeclarationListContext):
        pass


    # Enter a parse tree produced by GosuParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:GosuParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by GosuParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:GosuParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by GosuParser#blockType.
    def enterBlockType(self, ctx:GosuParser.BlockTypeContext):
        pass

    # Exit a parse tree produced by GosuParser#blockType.
    def exitBlockType(self, ctx:GosuParser.BlockTypeContext):
        pass


    # Enter a parse tree produced by GosuParser#typeParameters.
    def enterTypeParameters(self, ctx:GosuParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by GosuParser#typeParameters.
    def exitTypeParameters(self, ctx:GosuParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by GosuParser#typeParameter.
    def enterTypeParameter(self, ctx:GosuParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by GosuParser#typeParameter.
    def exitTypeParameter(self, ctx:GosuParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by GosuParser#typeArguments.
    def enterTypeArguments(self, ctx:GosuParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by GosuParser#typeArguments.
    def exitTypeArguments(self, ctx:GosuParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by GosuParser#typeArgument.
    def enterTypeArgument(self, ctx:GosuParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by GosuParser#typeArgument.
    def exitTypeArgument(self, ctx:GosuParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by GosuParser#optionalType.
    def enterOptionalType(self, ctx:GosuParser.OptionalTypeContext):
        pass

    # Exit a parse tree produced by GosuParser#optionalType.
    def exitOptionalType(self, ctx:GosuParser.OptionalTypeContext):
        pass


    # Enter a parse tree produced by GosuParser#typeLiteral.
    def enterTypeLiteral(self, ctx:GosuParser.TypeLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#typeLiteral.
    def exitTypeLiteral(self, ctx:GosuParser.TypeLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#type.
    def enterType(self, ctx:GosuParser.TypeContext):
        pass

    # Exit a parse tree produced by GosuParser#type.
    def exitType(self, ctx:GosuParser.TypeContext):
        pass


    # Enter a parse tree produced by GosuParser#blockLiteral.
    def enterBlockLiteral(self, ctx:GosuParser.BlockLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#blockLiteral.
    def exitBlockLiteral(self, ctx:GosuParser.BlockLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#blockLiteralArg.
    def enterBlockLiteralArg(self, ctx:GosuParser.BlockLiteralArgContext):
        pass

    # Exit a parse tree produced by GosuParser#blockLiteralArg.
    def exitBlockLiteralArg(self, ctx:GosuParser.BlockLiteralArgContext):
        pass


    # Enter a parse tree produced by GosuParser#arguments.
    def enterArguments(self, ctx:GosuParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GosuParser#arguments.
    def exitArguments(self, ctx:GosuParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by GosuParser#argExpression.
    def enterArgExpression(self, ctx:GosuParser.ArgExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#argExpression.
    def exitArgExpression(self, ctx:GosuParser.ArgExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#namedArgumentExpression.
    def enterNamedArgumentExpression(self, ctx:GosuParser.NamedArgumentExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#namedArgumentExpression.
    def exitNamedArgumentExpression(self, ctx:GosuParser.NamedArgumentExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:GosuParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:GosuParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#intervalExpression.
    def enterIntervalExpression(self, ctx:GosuParser.IntervalExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#intervalExpression.
    def exitIntervalExpression(self, ctx:GosuParser.IntervalExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#memberAccess.
    def enterMemberAccess(self, ctx:GosuParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by GosuParser#memberAccess.
    def exitMemberAccess(self, ctx:GosuParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by GosuParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:GosuParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:GosuParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#typeCastExpression.
    def enterTypeCastExpression(self, ctx:GosuParser.TypeCastExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#typeCastExpression.
    def exitTypeCastExpression(self, ctx:GosuParser.TypeCastExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#relationalExpression.
    def enterRelationalExpression(self, ctx:GosuParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#relationalExpression.
    def exitRelationalExpression(self, ctx:GosuParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#newExpression.
    def enterNewExpression(self, ctx:GosuParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#newExpression.
    def exitNewExpression(self, ctx:GosuParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#evalExpression.
    def enterEvalExpression(self, ctx:GosuParser.EvalExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#evalExpression.
    def exitEvalExpression(self, ctx:GosuParser.EvalExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:GosuParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:GosuParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#safeTernaryExpression.
    def enterSafeTernaryExpression(self, ctx:GosuParser.SafeTernaryExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#safeTernaryExpression.
    def exitSafeTernaryExpression(self, ctx:GosuParser.SafeTernaryExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#thisSuperExpression.
    def enterThisSuperExpression(self, ctx:GosuParser.ThisSuperExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#thisSuperExpression.
    def exitThisSuperExpression(self, ctx:GosuParser.ThisSuperExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#unaryExpressionNot.
    def enterUnaryExpressionNot(self, ctx:GosuParser.UnaryExpressionNotContext):
        pass

    # Exit a parse tree produced by GosuParser#unaryExpressionNot.
    def exitUnaryExpressionNot(self, ctx:GosuParser.UnaryExpressionNotContext):
        pass


    # Enter a parse tree produced by GosuParser#bitwiseExpressison.
    def enterBitwiseExpressison(self, ctx:GosuParser.BitwiseExpressisonContext):
        pass

    # Exit a parse tree produced by GosuParser#bitwiseExpressison.
    def exitBitwiseExpressison(self, ctx:GosuParser.BitwiseExpressisonContext):
        pass


    # Enter a parse tree produced by GosuParser#logicalExpression.
    def enterLogicalExpression(self, ctx:GosuParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#logicalExpression.
    def exitLogicalExpression(self, ctx:GosuParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#typeisExpression.
    def enterTypeisExpression(self, ctx:GosuParser.TypeisExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#typeisExpression.
    def exitTypeisExpression(self, ctx:GosuParser.TypeisExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#typeofExpression.
    def enterTypeofExpression(self, ctx:GosuParser.TypeofExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#typeofExpression.
    def exitTypeofExpression(self, ctx:GosuParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#elementAccessExpression.
    def enterElementAccessExpression(self, ctx:GosuParser.ElementAccessExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#elementAccessExpression.
    def exitElementAccessExpression(self, ctx:GosuParser.ElementAccessExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GosuParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GosuParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#preIncrementExpression.
    def enterPreIncrementExpression(self, ctx:GosuParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#preIncrementExpression.
    def exitPreIncrementExpression(self, ctx:GosuParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#ternaryExpression.
    def enterTernaryExpression(self, ctx:GosuParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#ternaryExpression.
    def exitTernaryExpression(self, ctx:GosuParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#methodCall.
    def enterMethodCall(self, ctx:GosuParser.MethodCallContext):
        pass

    # Exit a parse tree produced by GosuParser#methodCall.
    def exitMethodCall(self, ctx:GosuParser.MethodCallContext):
        pass


    # Enter a parse tree produced by GosuParser#anonymousInnerClass.
    def enterAnonymousInnerClass(self, ctx:GosuParser.AnonymousInnerClassContext):
        pass

    # Exit a parse tree produced by GosuParser#anonymousInnerClass.
    def exitAnonymousInnerClass(self, ctx:GosuParser.AnonymousInnerClassContext):
        pass


    # Enter a parse tree produced by GosuParser#lambdaSignature.
    def enterLambdaSignature(self, ctx:GosuParser.LambdaSignatureContext):
        pass

    # Exit a parse tree produced by GosuParser#lambdaSignature.
    def exitLambdaSignature(self, ctx:GosuParser.LambdaSignatureContext):
        pass


    # Enter a parse tree produced by GosuParser#lambdaBody.
    def enterLambdaBody(self, ctx:GosuParser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by GosuParser#lambdaBody.
    def exitLambdaBody(self, ctx:GosuParser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by GosuParser#arrayCreator.
    def enterArrayCreator(self, ctx:GosuParser.ArrayCreatorContext):
        pass

    # Exit a parse tree produced by GosuParser#arrayCreator.
    def exitArrayCreator(self, ctx:GosuParser.ArrayCreatorContext):
        pass


    # Enter a parse tree produced by GosuParser#initializer.
    def enterInitializer(self, ctx:GosuParser.InitializerContext):
        pass

    # Exit a parse tree produced by GosuParser#initializer.
    def exitInitializer(self, ctx:GosuParser.InitializerContext):
        pass


    # Enter a parse tree produced by GosuParser#initializerExpression.
    def enterInitializerExpression(self, ctx:GosuParser.InitializerExpressionContext):
        pass

    # Exit a parse tree produced by GosuParser#initializerExpression.
    def exitInitializerExpression(self, ctx:GosuParser.InitializerExpressionContext):
        pass


    # Enter a parse tree produced by GosuParser#arrayValueList.
    def enterArrayValueList(self, ctx:GosuParser.ArrayValueListContext):
        pass

    # Exit a parse tree produced by GosuParser#arrayValueList.
    def exitArrayValueList(self, ctx:GosuParser.ArrayValueListContext):
        pass


    # Enter a parse tree produced by GosuParser#mapInitializerList.
    def enterMapInitializerList(self, ctx:GosuParser.MapInitializerListContext):
        pass

    # Exit a parse tree produced by GosuParser#mapInitializerList.
    def exitMapInitializerList(self, ctx:GosuParser.MapInitializerListContext):
        pass


    # Enter a parse tree produced by GosuParser#objectInitializer.
    def enterObjectInitializer(self, ctx:GosuParser.ObjectInitializerContext):
        pass

    # Exit a parse tree produced by GosuParser#objectInitializer.
    def exitObjectInitializer(self, ctx:GosuParser.ObjectInitializerContext):
        pass


    # Enter a parse tree produced by GosuParser#initializerAssignment.
    def enterInitializerAssignment(self, ctx:GosuParser.InitializerAssignmentContext):
        pass

    # Exit a parse tree produced by GosuParser#initializerAssignment.
    def exitInitializerAssignment(self, ctx:GosuParser.InitializerAssignmentContext):
        pass


    # Enter a parse tree produced by GosuParser#primary.
    def enterPrimary(self, ctx:GosuParser.PrimaryContext):
        pass

    # Exit a parse tree produced by GosuParser#primary.
    def exitPrimary(self, ctx:GosuParser.PrimaryContext):
        pass


    # Enter a parse tree produced by GosuParser#namespace.
    def enterNamespace(self, ctx:GosuParser.NamespaceContext):
        pass

    # Exit a parse tree produced by GosuParser#namespace.
    def exitNamespace(self, ctx:GosuParser.NamespaceContext):
        pass


    # Enter a parse tree produced by GosuParser#identifier.
    def enterIdentifier(self, ctx:GosuParser.IdentifierContext):
        pass

    # Exit a parse tree produced by GosuParser#identifier.
    def exitIdentifier(self, ctx:GosuParser.IdentifierContext):
        pass


    # Enter a parse tree produced by GosuParser#semicolon.
    def enterSemicolon(self, ctx:GosuParser.SemicolonContext):
        pass

    # Exit a parse tree produced by GosuParser#semicolon.
    def exitSemicolon(self, ctx:GosuParser.SemicolonContext):
        pass


    # Enter a parse tree produced by GosuParser#literal.
    def enterLiteral(self, ctx:GosuParser.LiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#literal.
    def exitLiteral(self, ctx:GosuParser.LiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#stringLiteral.
    def enterStringLiteral(self, ctx:GosuParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#stringLiteral.
    def exitStringLiteral(self, ctx:GosuParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#stringPart.
    def enterStringPart(self, ctx:GosuParser.StringPartContext):
        pass

    # Exit a parse tree produced by GosuParser#stringPart.
    def exitStringPart(self, ctx:GosuParser.StringPartContext):
        pass


    # Enter a parse tree produced by GosuParser#interpolation.
    def enterInterpolation(self, ctx:GosuParser.InterpolationContext):
        pass

    # Exit a parse tree produced by GosuParser#interpolation.
    def exitInterpolation(self, ctx:GosuParser.InterpolationContext):
        pass


    # Enter a parse tree produced by GosuParser#numberLiteral.
    def enterNumberLiteral(self, ctx:GosuParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#numberLiteral.
    def exitNumberLiteral(self, ctx:GosuParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:GosuParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:GosuParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#featureLiteral.
    def enterFeatureLiteral(self, ctx:GosuParser.FeatureLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#featureLiteral.
    def exitFeatureLiteral(self, ctx:GosuParser.FeatureLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:GosuParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:GosuParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#mapLiteral.
    def enterMapLiteral(self, ctx:GosuParser.MapLiteralContext):
        pass

    # Exit a parse tree produced by GosuParser#mapLiteral.
    def exitMapLiteral(self, ctx:GosuParser.MapLiteralContext):
        pass


    # Enter a parse tree produced by GosuParser#greaterEqual.
    def enterGreaterEqual(self, ctx:GosuParser.GreaterEqualContext):
        pass

    # Exit a parse tree produced by GosuParser#greaterEqual.
    def exitGreaterEqual(self, ctx:GosuParser.GreaterEqualContext):
        pass



del GosuParser