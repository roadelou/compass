#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-13
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from typing import List # Used for type hints.
import os  # Used for path related manipulations.


# External imports
from compass.frontend import compass_compile  # The function we want ot test.


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def collect_examples() -> List[str]:
    """
    Returns the list of the paths of all the example files provided in the
    repository.
    """
    # This can be done in one line.
    return [
        f"examples/{example_file}"
        for example_file in os.listdir("examples")
        if example_file.endswith(".cmps")
    ]


def test_compass_compiler():
    """
    Simple test for the compass_compile function, with compass backend.
    """
    # Collecting the source files.
    examples = collect_examples()
    for example in examples:
        # Reading the source code.
        with open(example, "r") as compass_file:
            compass_source = compass_file.read()
        # Runs the compilation to compass target.
        compass_compiled = compass_compile(compass_source, "compass")
        # Creating the path for the compiled file.
        compiled_path = example.replace("examples/", "test/files/").replace(
            ".cmps", "_compiled.cmps"
        )
        # Writes the output to a file.
        with open(compiled_path, "w") as compass_compiled_file:
            compass_compiled_file.write(compass_compiled)


def test_c_compiler():
    """
    Simple test for the compass_compile function, with C backend.
    """
    # Collecting the source files.
    examples = collect_examples()
    for example in examples:
        # Reading the source code.
        with open(example, "r") as compass_file:
            compass_source = compass_file.read()
        # Runs the compilation to compass target.
        compass_compiled = compass_compile(compass_source, "C")
        # Creating the path for the compiled file.
        compiled_path = example.replace("examples/", "test/files/").replace(
            ".cmps", "_compiled.c"
        )
        # Writes the output to a file.
        with open(compiled_path, "w") as compass_compiled_file:
            compass_compiled_file.write(compass_compiled)


def test_header_compiler():
    """
    Simple test for the compass_compile function, with header backend.
    """
    # Collecting the source files.
    examples = collect_examples()
    for example in examples:
        # Reading the source code.
        with open(example, "r") as compass_file:
            compass_source = compass_file.read()
        # Runs the compilation to compass target.
        compass_compiled = compass_compile(compass_source, "header")
        # Creating the path for the compiled file.
        compiled_path = example.replace("examples/", "test/files/").replace(
            ".cmps", "_compiled.h"
        )
        # Writes the output to a file.
        with open(compiled_path, "w") as compass_compiled_file:
            compass_compiled_file.write(compass_compiled)


def test_debug_compiler():
    """
    Simple test for the compass_compile function, with debug backend.
    """
    # Collecting the source files.
    examples = collect_examples()
    for example in examples:
        # Reading the source code.
        with open(example, "r") as compass_file:
            compass_source = compass_file.read()
        # Runs the compilation to compass target.
        compass_compiled = compass_compile(compass_source, "debug")
        # Creating the path for the compiled file.
        compiled_path = example.replace("examples/", "test/files/").replace(
            ".cmps", "_compiled.debug.c"
        )
        # Writes the output to a file.
        with open(compiled_path, "w") as compass_compiled_file:
            compass_compiled_file.write(compass_compiled)


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
