#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts: 
# Creation Date: 2021-03-13
# Language: Python3

################################### IMPORTS ####################################

# Standard library 
# Your imports from the standard library go here 


# External imports 
from compass.frontend import compass_compile    # The function we wnat ot test.


# Internal imports 
# Your imports within this package go here 

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def test_compass_compiler():
    """
    Simple test for the compass_compile function, with compass backend.
    """
    # Reading the source code.
    with open("test/files/abro.cmps", "r") as abro_file:
        abro_source = abro_file.read()
    # Runs the compilation to compass target.
    abro_compiled = compass_compile(abro_source, "compass")
    # Writes the output to a file.
    with open("test/files/abro_compiled.cmps", "w") as abro_compiled_file:
        abro_compiled_file.write(abro_compiled)

def test_c_compiler():
    """
    Simple test for the compass_compile function, with C backend.
    """
    # Reading the source code.
    with open("test/files/abro.cmps", "r") as abro_file:
        abro_source = abro_file.read()
    # Runs the compilation to compass target.
    abro_compiled = compass_compile(abro_source, "C")
    # Writes the output to a file.
    with open("test/files/abro_compiled.c", "w") as abro_compiled_file:
        abro_compiled_file.write(abro_compiled)

def test_header_compiler():
    """
    Simple test for the compass_compile function, with header backend.
    """
    # Reading the source code.
    with open("test/files/abro.cmps", "r") as abro_file:
        abro_source = abro_file.read()
    # Runs the compilation to compass target.
    abro_compiled = compass_compile(abro_source, "H")
    # Writes the output to a file.
    with open("test/files/abro_compiled.h", "w") as abro_compiled_file:
        abro_compiled_file.write(abro_compiled)

def test_debug_compiler():
    """
    Simple test for the compass_compile function, with debug backend.
    """
    # Reading the source code.
    with open("test/files/abro.cmps", "r") as abro_file:
        abro_source = abro_file.read()
    # Runs the compilation to compass target.
    abro_compiled = compass_compile(abro_source, "debug")
    # Writes the output to a file.
    with open("test/files/abro_compiled.debug.c", "w") as abro_compiled_file:
        abro_compiled_file.write(abro_compiled)


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
