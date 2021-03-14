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
import compass.ast as ast  # Used for downcasts
from compass.codegen.compass.declaration import (
    codegen_declaration,
)  # Used for recursive codegen
from compass.codegen.compass.statement import (
    codegen_statement,
)  # Used for recursive codegen

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_module(module: ast.Module) -> str:
    """
    Outputs the Compass code corresponding to the provided Module.
    """
    source_code = ""
    # Adding the name of the module.
    source_code += f"module {module.name}("
    # Building the code for each declaration.
    code_declarations = [
        codegen_declaration(declaration) for declaration in module.declarations
    ]
    # Joining the codes for the declarations.
    source_code += ", ".join(code_declarations)
    # Opening the brackets for the body of the code.
    source_code += ") {\n"
    # Adding the (indented) code for the body of the module.
    source_code += codegen_statement(module.statement, indent=1) + "\n"
    # Closing the brackets.
    source_code += "}\n"
    # Returing the prepared source code.
    return source_code


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
