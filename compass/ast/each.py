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
from compass.ast.statement import Statement  # Used for inheritance
from compass.ast.expression import Expression  # Used for type hints

################################### CLASSES ####################################


class Each(Statement):
    """
    Class used to represent an Each loop in the AST.
    """

    def __init__(self, expression: Expression, statement: Statement):
        """
        Constructor of the Each class.

        Arguments
        =========
         - expression: The Expression to use as a reset for this loop.
         - statement: The Statement which constitutes the body of this loop.
        """
        # Storing the arguments.
        self.expression = expression
        self.statement = statement


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
