#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-12
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here


# External imports
from sly import Parser  # Parser implementation


# Internal imports
import compass.ast as ast  # Used to build the AST
from compass.grammar import compass_tokens  # Used for language tokens

################################### CLASSES ####################################


class CompassParser(Parser):
    """
    Parser for the Compass language, used to build the AST from the tokenized
    source code.
    """

    # DEBUG
    # debugfile = "test/files/parser.out"

    # The tokens for the Compass language.
    tokens = compass_tokens.tokens

    # The only precedence rule is that <- should go before emit.
    precedence = (
        ("nonassoc", MODULE, INPUT, OUTPUT, EACH, EMIT, AWAIT, SEQ, PAR),
        ("left", ","),  # , is left associative, to solve conflicts
        ("left", ";"),  # , is left associative, to solve conflicts
        ("nonassoc", ASSIGN),
        # The next operators are used for expressions.
        ("nonassoc", TESTEQ),
        ("left", OR, "+", "-"),
        ("left", AND, "*", "/", "%"),
        ("right", UMINUS),
        ("right", "!"),
    )

    # The final rule, which returns an AST from the Module.
    @_("module")
    def ast(self, p):
        # Returning an AST from the Module.
        return ast.Tree(p.module)

    # Building a Module from Name + Declarations + Body. The most complex rule
    # in the AST.
    @_('MODULE NAME "(" list_declaration ")" "{" statement "}"')
    def module(self, p):
        # Returning the Module from the provided description.
        return ast.Module(p.NAME, p.list_declaration, p.statement)

    # Merging two lists of declarations.
    @_('list_declaration "," list_declaration')
    def list_declaration(self, p):
        # Concatenating the two lists.
        return p.list_declaration0 + p.list_declaration1

    # Creating a list of declarations of one element from an input signal.
    @_("INPUT signal")
    def list_declaration(self, p):
        # Building a list of declarations from a single input.
        return [ast.InputDeclaration(p.signal)]

    # Creating a list of declarations of one element from an output signal.
    @_("OUTPUT signal")
    def list_declaration(self, p):
        # Building a list of declarations from a single output.
        return [ast.OutputDeclaration(p.signal)]

    # Creating a loop each statement from a reset Signal + Statement body.
    @_('EACH expression "{" statement "}"')
    def statement(self, p):
        # Creating an Each statement.
        return ast.Each(p.expression, p.statement)

    # Creating a list of statements from a single isolated statement.
    @_("statement")
    def list_statement(self, p):
        return [p.statement]

    # Merging two adjacent lists of statement.
    @_("list_statement \";\" list_statement")
    def list_statement(self, p):
        return p.list_statement0 + p.list_statement1

    # Rule to resolve the optionnal last semi-colon for the last statement of a
    # list.
    @_("list_statement \";\"")
    def list_statement(self, p):
        return p.list_statement

    # Creating a sequential statement from a scoped list of statements.
    @_('SEQ "{" list_statement "}"')
    def statement(self, p):
        return ast.Seq(p.list_statement)

    # Creating a parallel statement from a scoped list of statement.
    @_('PAR "{" list_statement "}"')
    def statement(self, p):
        return ast.Par(p.list_statement)

    # Creating an await from a signal.
    @_('AWAIT expression')
    def statement(self, p):
        return ast.AwaitStatement(p.expression)

    # Creating an emit from an assignement.
    @_('EMIT signal ASSIGN expression')
    def statement(self, p):
        return ast.EmitStatement(p.signal, p.expression)

    # Creating an emit from a single signal.
    @_("EMIT signal")
    def statement(self, p):
        # We simply assign 1 to the signal.
        return ast.EmitStatement(p.signal, ast.Number("1"))

    # Creating a Signal from an isolated name.
    @_("NAME")
    def signal(self, p):
        return ast.Signal(p.NAME)

    # Creating an expression from an isolated number.
    @_("NUMBER")
    def expression(self, p):
        return ast.Number(p.NUMBER)

    # Creating an expression from an isolated signal (for complex expressions).
    @_("signal")
    def expression(self, p):
        return ast.SignalExpression(p.signal)

    # Creating the rules for complex expressions which use operators.
    @_("expression TESTEQ expression")
    def expression(self, p):
        return ast.TestEqOp(p.expression0, p.expression1)

    @_("expression OR expression")
    def expression(self, p):
        return ast.OrOp(p.expression0, p.expression1)

    @_("expression \"+\" expression")
    def expression(self, p):
        return ast.PlusOp(p.expression0, p.expression1)

    @_("expression \"-\" expression")
    def expression(self, p):
        return ast.MinusOp(p.expression0, p.expression1)

    @_("expression AND expression")
    def expression(self, p):
        return ast.AndOp(p.expression0, p.expression1)

    @_("expression \"*\" expression")
    def expression(self, p):
        return ast.TimesOp(p.expression0, p.expression1)

    @_("expression \"/\" expression")
    def expression(self, p):
        return ast.DivOp(p.expression0, p.expression1)

    @_("expression \"%\" expression")
    def expression(self, p):
        return ast.ModOp(p.expression0, p.expression1)

    # Rules for unary operators.
    @_("\"-\" expression %prec UMINUS")
    def expression(self, p):
        return ast.UminusOp(p.expression)

    @_("\"!\" expression")
    def expression(self, p):
        return ast.NotOp(p.expression)

    # Enabling the use of parenthesis to prioritize some operations.
    @_("\"(\" expression \")\"")
    def expression(self, p):
        return p.expression

################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
