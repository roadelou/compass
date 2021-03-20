#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-12
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from typing import Optional  # Used for type hints


# External imports
# Your imports from other packages go here


# Internal imports
from compass.grammar import CompassLexer, CompassParser  # Used to build the AST
from compass.ast import Tree  # Used for type hints

# The codegen functions for the different targets.
from compass.codegen.compass import codegen_tree as codegen_compass
from compass.codegen.c import codegen_tree as codegen_c
from compass.codegen.header import codegen_tree as codegen_header
from compass.codegen.debug import codegen_tree as codegen_debug

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def compass_compile(
    source_code: str, target: str, rename: Optional[str]
) -> str:
    """
    Runs the compilation process for the provided source code.

    Arguments
    =========
     - source_code: The source code to compile.
     - target: The target to compile to. Valid targets are detailed in the
        documentation.
     - rename: The new name to use for the module in the compiled code. This is
        usefull to create several modules from the same source code.

    Returns
    =======
    The compiled source code.
    """
    # We first build the tokens from the source code.
    tokens = CompassLexer().tokenize(source_code)
    # We then build the AST from the tokens.
    ast = CompassParser().parse(tokens)

    # If the parsing step failed because of syntax errors, the AST will be None
    # here.
    if ast is None:
        raise ValueError("Source code could not be parsed")

    # We rename the compiled module if we were asked to.
    if rename is not None:
        ast.rename(rename)

    # The we turn the AST into source code using the right codegen based on the
    # provided target.
    if target == "compass":
        return codegen_compass(ast)
    elif target in ["C", "c"]:
        return codegen_c(ast)
    elif target in ["H", "h", "header"]:
        return codegen_header(ast)
    elif target == "debug":
        return codegen_debug(ast)
    else:
        raise ValueError(f"Unknown target {target}")


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
