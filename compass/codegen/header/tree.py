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
# Your imports from other packages go here 


# Internal imports 
import compass.ast as ast  # Used for downcasts
from compass.codegen.header.module import (
    codegen_module,
)  # Used for recursive codegen


################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def codegen_tree(tree: ast.Tree) -> str:
    """
    Outputs the C source code for the provided AST.
    """
    source_code = ""
    # We have to add a include header guard. The string used for the header
    # guard is built from the name of the module.
    header_guard = f"{tree.module.name}_COMPASS_INCLUDED".upper()
    # Adding the guard to the header.
    source_code += f"#ifndef {header_guard}\n"
    source_code += f"#define {header_guard}\n"
    # Newline for the style.
    source_code += "\n"
    # For now an AST only contains one module.
    source_code += codegen_module(tree.module)
    # Newline for the style.
    source_code += "\n"
    # Closing the include guard.
    source_code += "#endif\n"
    # Returning the built source code.
    return source_code

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
