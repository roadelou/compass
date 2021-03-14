#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-14
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
# Your imports from the standard library go here 


# External imports 
# Your imports from other packages go here 


# Internal imports 
from compass.ast.expression import Expression   # Used for inheritance
from compass.ast.signal import Signal   # Used for type hints

################################### CLASSES ####################################

class SignalExpression(Expression):
    """
    Class used to represent an expression made from a single signal, component
    of complex expressions where signals are used.
    """

    def __init__(self, signal: Signal):
        """
        Constructor for the SignalExpression class.

        Arguments
        =========
         - signal: The Signal to evaluate for this expression.
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
