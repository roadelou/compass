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
# Your imports within this package go here

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################

# Defining once all the tokens used for the compass language.
tokens = {
    "MODULE",  # module keyword.
    "INPUT",  # input keyword.
    "OUTPUT",  # output keyword.
    "NAME",  # string used to identify somathing (probably a signal).
    "EACH",  # each loop keyword.
    "SEQ",  # seq keyword.
    "PAR",  # par keyword.
    "AWAIT",  # await keyword.
    "ASSIGN",  # assignation symbol (<-).
    "EMIT",  # emit keyword.
    "NUMBER",  # literal integer.
    "AND",  # && operator.
    "OR",   # || operator.
    "TESTEQ",   # == operator.
}

# Defining the litteral tokens used in the compass language.
literals = {"(", ")", "{", "}", ";", ",", "+", "-", "/", "%", "*", "!"}

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
