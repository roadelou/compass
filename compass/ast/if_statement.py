#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-18
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from __future__ import annotations  # Used for self reference
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

    def __init__(
        self,
        expression: Expression,
        statement: Statement,
        else_statement: Optional[Statement] = None,
    ):
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
        self.else_statement = else_statement

    def with_else(self, statement: Statement) -> IfStatement:
        """
        Adds the provided statement as an else statement to the current one and
        returns the updated statement with the two branches.

        Arguments
        =========
         - statement: The statement to use in the else branch.
        """
        # We return a new IfStatement to avoid side effects.
        return IfStatement(
            self.expression, self.statement, else_statement=statement
        )


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
