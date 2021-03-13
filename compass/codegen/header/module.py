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
from compass.codegen.c.declaration import (
    codegen_declaration,
)  # Used for recursive codegen, shared with C target

################################### CLASSES ####################################

# Your classes go here 

################################## FUNCTIONS ###################################

def codegen_module(module: ast.Module) -> str:
    """
    Outputs the header declaration corresponding to the provided Module.
    """
    source_code = ""
    # Adding the name of the module.
    source_code += f"void {module.name}("
    # Building the code for each declaration.
    code_declarations = [
        codegen_declaration(declaration) for declaration in module.declarations
    ]
    # Joining the codes for the declarations.
    source_code += ", ".join(code_declarations)
    # Opening the brackets for the body of the code.
    source_code += ");\n"
    # Returning the prepared source code.
    return source_code

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
