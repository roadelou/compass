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


class Number(Expression):
    """
    Class used to represent a Number in the AST. A number is a literal integer
    in the source code.
    """

    def __init__(self, number: str):
        """
        Constructor of the Number class.

        Arguments
        =========
         - number: The string representation of the Number in the source code.
        """
        # Storing our argument in the right type.
        self.number = int(number)

    # To simplify the codegen slightly, we give a string representation to
    # Numbers.
    def __repr__(self) -> str:
        """
        String representation of the Number.
        """
        return str(self.number)


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
