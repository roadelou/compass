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
# Your imports from other packages go here


# Internal imports
import compass.ast as ast  # Used for downcasts

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_expression(expression: ast.Expression) -> str:
    """
    Outputs the Compass code corresponding to the provided Expression.
    """
    if isinstance(expression, ast.Number):
        return str(expression)
    elif isinstance(expression, ast.SignalExpression):
        return str(expression.signal)
    elif isinstance(expression, ast.Binary):
        return codegen_binary(expression)
    elif isinstance(expression, ast.Unary):
        return codegen_unary(expression)
    else:
        raise ValueError(f"Unkown Expression {expression}")

def codegen_binary(expression: ast.Binary) -> str:
    """
    Specialized variant of codegen_expression for binary operators.
    """
    # Recursively building the code for the left and right expressions.
    left_code = codegen_expression(expression.left)
    right_code = codegen_expression(expression.right)
    # We downcast to the right operator.
    if isinstance(expression, ast.AndOp):
        return f"({left_code} && {right_code})"
    elif isinstance(expression, ast.ModOp):
        return f"({left_code} % {right_code})"
    elif isinstance(expression, ast.DivOp):
        return f"({left_code} / {right_code})"
    elif isinstance(expression, ast.MinusOp):
        return f"({left_code} - {right_code})"
    elif isinstance(expression, ast.OrOp):
        return f"({left_code} || {right_code})"
    elif isinstance(expression, ast.PlusOp):
        return f"({left_code} + {right_code})"
    elif isinstance(expression, ast.TestEqOp):
        return f"({left_code} == {right_code})"
    elif isinstance(expression, ast.TimesOp):
        return f"({left_code} * {right_code})"
    else:
        raise ValueError(f"Unknown binary operator {expression}")

def codegen_unary(expression: ast.Unary) -> str:
    """
    Specialized variant of codegen_expression for unary operators.
    """
    # Recursively building the code for the inner expression.
    inner_code = codegen_expression(expression.expression)
    # We downcast to the right operator.
    if isinstance(expression, ast.NotOp):
        return f"(!{inner_code})"
    elif isinstance(expression, ast.UminusOp):
        return f"(-{inner_code})"
    else:
        raise ValueError(f"Unknown unary operator {expression}")



##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
