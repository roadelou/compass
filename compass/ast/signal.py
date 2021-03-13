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

################################### CLASSES ####################################


class Signal(Expression):
    """
    Class used to represent a Signal in the AST. A signal is like a
    non-persistent variable that our program will emit or react to.
    """

    def __init__(self, name: str):
        """
        Constructor of the Signal class.

        Arguments
        =========
         - name: The name used to identify this Signal.
        """
        # Storing our arguments.
        self.name = name

    # To simplify the codegen slightly, we gove a string representation to Signals.
    def __repr__(self) -> str:
        """
        String representation of the Signal.
        """
        return self.name


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
