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
from compass.ast.node import Node  # Used for inheritance
from compass.ast.declaration import Declaration  # Used for type hints
from compass.ast.statement import Statement  # Used for type hints

################################### CLASSES ####################################


class Module(Node):
    """
    Class used to represent a Module in the AST.
    """

    def __init__(
        self,
        name: str,
        list_declaration: List[Declaration],
        statement: Statement,
    ):
        """
        Constructor of the Module class.

        Arguments
        =========
         - name: The name to use for this Module.
         - list_declaration: The inputs and outputs declared for this Module.
         - statement: The Statement in the body of this Module.
        """
        # Storing the arguments.
        self.name = name
        self.declarations = list_declaration
        self.statement = statement


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
