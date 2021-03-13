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
from compass.ast.declaration import Declaration  # Used for inheritance.
from compass.ast.signal import Signal  # Used for type hints.

################################### CLASSES ####################################


class InputDeclaration(Declaration):
    """
    Class used to represent the declaration of an input Signal in the AST.
    """

    def __init__(self, signal: Signal):
        """
        Constructor of the InputDeclaration class.

        Arguments
        =========
         - signal: The Signal which will be treated as an input to the module.
        """
        # Storing our argument.
        self.signal = signal


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
