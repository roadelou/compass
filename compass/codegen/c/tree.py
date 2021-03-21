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
from compass.codegen.c.module import (
    codegen_module,
)  # Used for recursive codegen
from compass.codegen.c.declaration import (
    codegen_declaration,
)  # Used for recursive codegen

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_tree(tree: ast.Tree) -> str:
    """
    Outputs the C source code for the provided AST.
    """
    source_code = ""
    # For now an AST only contains one module.
    source_module, owned_states, owned_locals = codegen_module(tree.module)

    # We add some code to statically allocate the states used in the modules.
    # The states have value 0 by default.
    for state in owned_states:
        source_code += f"static int {state} = 0;\n"
    # If there are no states, we add a small comment instead.
    if len(owned_states) == 0:
        source_code += "/* No states for this code. */\n"

    # Creating the clock signal, which always evaluates to True.
    source_code += "\n"
    source_code += f"const int clock_constant = 1;\n"
    source_code += f"const int *clk = &clock_constant;\n"
    # Creating the never signal, which always evaluates to False.
    source_code += f"const int never_constant = 0;\n"
    source_code += f"const int *never = &never_constant;\n"
    source_code += "\n"

    # Creating all the locals as global signals for the code.
    for local in owned_locals:
        source_code += f"static int {local}_value = 0;\n"
        source_code += f"static int *{local} = &{local}_value;\n"
    # If there are no locals, we add a small comment instead.
    if len(owned_locals) == 0:
        source_code += "/* No locals for this code. */\n"

    # Newline for the style.
    source_code += "\n"

    # We also have to declare all the extern submodules used here.
    for extern in tree.externs:
        # We build the source code for the arguments of the extern C function.
        code_arguments = ", ".join([codegen_declaration(declaration) for declaration in extern.declarations])
        # We add the source code for the extern C function declaration.
        source_code += f"extern void {extern.name}({code_arguments});\n"
    # If no extern submodules are used, we add a small comment instead.
    if len(tree.externs) == 0:
        source_code += "/* No extern subodules for this code. */\n"

    # Newline for the style.
    source_code += "\n"

    # Adding the code for the inner module.
    source_code += source_module
    # Returning the expected source code.
    return source_code


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
