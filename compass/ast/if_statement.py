#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-18
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from typing import Optional  # Used for type hints


# External imports
# Your imports from other packages go here


# Internal imports
from compass.ast.statement import Statement  # Used for inheritance
from compass.ast.expression import Expression  # Used for type hints

################################### CLASSES ####################################


class IfStatement(Statement):
    """
    Class used to represent an if-else statement in the AST.
    """

    def __init__(self, expression: Expression, statement: Statement):
        """
        Constructor of the Await class.

        Arguments
        =========
         - expression: The Expression for the condition to execute the
            statement.
         - statement: The statement to execute if the condition is met.
        """
        # Storing the arguments.
        self.expression = expression
        self.statement = statement
        # Optonal else statement.
        self.else_statement: Optional[Statement] = None


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
