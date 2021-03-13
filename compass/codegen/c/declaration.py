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

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_declaration(declaration: ast.Declaration) -> str:
    """
    Outputs the C code for the provided declaration.
    """
    # We downcast the Declaration to its real type.
    if isinstance(declaration, ast.InputDeclaration):
        return f"const int *{declaration.signal}"
    elif isinstance(declaration, ast.OutputDeclaration):
        return f"int *{declaration.signal}"
    else:
        raise ValueError(f"Invalid declaration type for {declaration}")


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
