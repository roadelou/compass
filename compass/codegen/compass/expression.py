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
    # There is only one subtype for Expression.
    if isinstance(expression, ast.Number):
        return str(expression)
    elif isinstance(expression, ast.SignalExpression):
        return str(expression.signal)
    else:
        raise ValueError(f"Unkown Expression {expression}")


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
