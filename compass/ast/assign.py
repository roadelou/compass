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
from compass.ast.expression import Expression  # Used for inheritance
from compass.ast.signal import Signal  # Used for type hints
from compass.ast.number import Number  # Used for type hints

################################### CLASSES ####################################


class Assign(Expression):
    """
    Class used to represent an assignation in the AST. An assignation is mostly
    used to emit a Signal with a specific numeric value.
    """

    def __init__(self, signal: Signal, number: Number):
        """
        Constructor of the Assign class.

        Arguments
        =========
         - signal: The Signal to assign to.
         - number: The Number to assign to the Signal.
        """
        # Storing the arguments.
        self.signal = signal
        self.number = number


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
