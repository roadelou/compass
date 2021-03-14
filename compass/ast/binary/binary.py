#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021 - 03 - 14
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


class Binary(Expression):
    """
    Base class used to represent binary operators in the AST.
    """

    def __init__(self, left: Expression, right: Expression):
        """
        Constructor of the base Binary class.

        Arguments
        =========
         - left: The first operand of the binary Expression.
         - right: The second operand of the binary Expression.
        """
        # Storing the arguments.
        self.left = left
        self.right = right


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
