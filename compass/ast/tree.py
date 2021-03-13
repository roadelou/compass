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
from compass.ast.module import Module  # Used for type hints.

################################### CLASSES ####################################


class Tree:
    """
    Class used to hold the AST of the compass language.
    """

    def __init__(self, module: Module):
        """
        Constructor of the Tree clas.

        Arguments
        =========
         - module: The Module declared in the current file.
        """
        # Storing the arguments.
        self.module = module


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
