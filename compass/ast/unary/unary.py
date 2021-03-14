#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-14
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here

# External imports
# Your imports from other packages go here

# Internal imports
from compass.ast.expression import (
    Expression,
)  # Used for inheritance and type hints.

################################### CLASSES ####################################


class Unary(Expression):
    """
    Base class used to represent unary operators in the AST.
    """

    def __init__(self, expression: Expression):
        """
        Constructor of the base Unary class.

        Arguments
        =========
         - expression: The expression to apply the unary operator to.
        """
        # Storing the arguments.
        self.expression = expression


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
