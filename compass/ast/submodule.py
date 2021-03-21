#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-21
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
from typing import List # Used for type hints


# External imports 
# Your imports from other packages go here 


# Internal imports 
from compass.ast.statement import Statement  # Used for inheritance
from compass.ast.signal import Signal  # Used for type hints

################################### CLASSES ####################################

class Submodule(Statement):
    """
    Class used to represent a submodule call in the AST.
    """

    def __init__(self, name: str, arguments: List[Signal]):
        """
        Constructor of the Submodule class.

        Arguments
        =========
         - name: The name of the submodule that should be called.
         - arguments: The list of Signals to pass to the submodule.
        """
        # Storing the arguments.
        self.name = name
        self.arguments = arguments

################################## FUNCTIONS ###################################

# Your functions go here 

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
