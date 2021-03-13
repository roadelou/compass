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
from compass.ast.signal import Signal  # Used for type hints

################################### CLASSES ####################################


class AwaitStatement(Statement):
    """
    Class used to represent an awiat statement in the AST.
    """

    def __init__(self, signal: Signal):
        """
        Constructor of the Await class.

        Arguments
        =========
         - signal: The Signal to wait for.
        """
        # Storing the arguments.
        self.signal = signal


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
