#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-12
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from typing import List  # Used for type hints


# External imports
# Your imports from other packages go here


# Internal imports
from compass.ast.statement import (
    Statement,
)  # Used for type hints and inheritance

################################### CLASSES ####################################


class Seq(Statement):
    """
    Class used to represent the sequential execution of several Statements in
    the AST.
    """

    def __init__(self, list_statement: List[Statement]):
        """
        Constructor of the Seq class.

        Arguments
        =========
         - list_statement: The list of Statements to build this Seq from.
        """
        # Store our arguments.
        self.statements = list_statement


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
