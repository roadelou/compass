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
from compass.codegen.compass.module import (
    codegen_module,
)  # Used for recursive codegen
from compass.codegen.compass.declaration import (
    codegen_declaration,
)  # Used for recursive codegen

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_tree(tree: ast.Tree) -> str:
    """
    Outputs the Compass source code for the provided AST.
    """
    source_code = ""

    # We start by building the code for all the extern declarations.
    for extern in tree.externs:
        # We build the source for the arguments of the extern submodule.
        code_arguments = ", ".join(
            [
                codegen_declaration(declaration)
                for declaration in extern.declarations
            ]
        )
        # We add the source code for the entire declaration of the extern
        # submodule.
        source_code += f"extern {extern.name}({code_arguments});\n"
    # If there are no extern modules, we just add a comment.
    if len(tree.externs) == 0:
        source_code += "# No extern submodules."

    # A blank line for the style.
    source_code += "\n"

    # We add the source code for the main module.
    source_code += codegen_module(tree.module)

    # We return the complete source code.
    return source_code


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
