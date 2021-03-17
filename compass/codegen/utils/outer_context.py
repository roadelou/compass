#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-17
# Language: Python3

################################### IMPORTS ####################################

# Standard library
# Your imports from the standard library go here


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################


class OuterContext:
    """
    Class used to provide several interesting values during the recursive
    compilation of compass statements. The variable will often be called "oc" in
    the python code.
    """

    def __init__(self, indent: int = 0):
        """
        Constructor of the OuterContext class.

        Arguments
        =========
         - indent: The current level of indentation.
        """
        # Storing the arguments.
        self.indent = indent
        # Creating the indentation string.
        self.indent_str = indent * "\t"


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
