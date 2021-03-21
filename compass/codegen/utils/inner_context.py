#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-17
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from __future__ import annotations  # Used for self reference
from typing import List, Optional  # Used for type hints


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################


class InnerContext:
    """
    Class used to return several interesting values during the recursive
    compilation of compass statements. The variable will often be called "ic" in
    the python code.
    """

    # For some mysterious reasons, the default arguments in the constructor seem
    # to be static, which means shared between the instances of the InnerContext
    # class. That is not at all what I want, hence why I have to dance around
    # with the None here...
    def __init__(
        self,
        source_code: Optional[str] = None,
        immediate_state: Optional[str] = None,
        owned_states: Optional[List[str]] = None,
        owned_locals: Optional[List[str]] = None,
        owned_submodules: Optional[List[str]] = None,
    ):
        """
        Constructor of the InnerContext class.

        Arguments
        =========
         - source_code: The code produced for the inner statement.
         - immediate_state: The immediate state of the Statement returning this
            InnerContext.
         - owned_state: The list of all the states owned by the producer
            statement and all its children.
         - owned_locals: The list of all the local variables owned by this
            statement and its children.
         - owned_locals: The list of all the submodules used by this statement
            and its children.
        """
        # Storing the arguments
        if source_code is None:
            self.source_code = ""
        else:
            self.source_code = source_code

        if immediate_state is None:
            self.immediate_state = ""
        else:
            self.immediate_state = immediate_state

        if owned_states is None:
            self.owned_states = list()
        else:
            self.owned_states = owned_states

        if owned_locals is None:
            self.owned_locals = list()
        else:
            self.owned_locals = owned_locals

        if owned_submodules is None:
            self.owned_submodules = list()
        else:
            self.owned_submodules = owned_submodules

    def inherit(self, ic: InnerContext):
        """
        Inherits all the recursive variables from the provided InnerContext.
        """
        self.owned_states.extend(ic.owned_states)
        self.owned_locals.extend(ic.owned_locals)
        self.owned_submodules.extend(ic.owned_submodules)

################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
