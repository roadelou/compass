#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-16
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here


# External imports
# Your imports from other packages go here


# Internal imports
from compass.ast.statement import Statement  # Used for inheritance

################################### CLASSES ####################################


class LocalStatement(Statement):
    """
    The "local" statement used to create local variables in the code.
    """

    def __init__(self, name: str):
        """
        Constructor of the LocalStatement class.

        Arguments
        =========
         - name: The name to use for the local variable.
        """
        # Storing the arguments
        self.name = name


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
