#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-21
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
from typing import List  # Used for type hints


# External imports 
# Your imports from other packages go here 


# Internal imports 
from compass.ast.node import Node  # Used for inheritance
from compass.ast.declaration import Declaration  # Used for type hints

################################### CLASSES ####################################

class Extern(Node):
    """
    Class used to represent the declaration of extern submodules in the AST.
    """

    def __init__(
        self,
        name: str,
        list_declaration: List[Declaration],
    ):
        """
        Constructor of the Extern class.

        Arguments
        =========
         - name: The name to use for this subodule.
         - list_declaration: The inputs and outputs declared for this subodule.
        """
        # Storing the arguments.
        self.name = name
        self.declarations = list_declaration

################################## FUNCTIONS ###################################

# Your functions go here 

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
