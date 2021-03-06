#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-13
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from typing import List, Tuple  # Used for type hints


# External imports
# Your imports from other packages go here


# Internal imports
import compass.ast as ast  # Used for downcasts
from compass.codegen.c.declaration import (
    codegen_declaration,
)  # Used for recursive codegen
from compass.codegen.c.statement import (
    codegen_statement,
)  # Used for recursive codegen
from compass.codegen.utils import (
    InnerContext,
    OuterContext,
)  # Used for type hints.

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_module(module: ast.Module) -> Tuple[str, List[str], List[str]]:
    """
    Outputs the C code corresponding to the provided Module.

    Returns
    =======
    A tuple with two values:
     - The source code for the inner module.
     - The states that have to be statically allocated for the module.
     - The local variables that have to be statically allocated for the module.
    """
    source_code = ""

    # Compiling the code that goes inside of the module.
    ic = codegen_statement(module.statement, OuterContext(indent=1))

    # Adding the name of the module.
    source_code += f"void {module.name}("
    # Building the code for each declaration.
    code_declarations = [
        codegen_declaration(declaration) for declaration in module.declarations
    ]
    # Joining the codes for the declarations.
    source_code += ", ".join(code_declarations)
    # Opening the brackets for the body of the code.
    source_code += ") {\n"

    # Creating the pointers to the clk and never signals.
    source_code += f"\tconst int *clk = &clock_constant;\n"
    source_code += f"\tconst int *never = &never_constant;\n"

    # Blank line for the style.
    source_code += "\n"

    # Allocating the pointers to all of the statically allocated locals on the
    # stack. That way the pointer can be optimized out by the C compiler.
    for local in ic.owned_locals:
        source_code += f"\tint *{local} = &{local}_value;\n"
    # If there are no locals, we add a small comment instead.
    if len(ic.owned_locals) == 0:
        source_code += "\t/* No locals for this code. */\n"
    
    # Blank line for the style.
    source_code += "\n"

    # Adding the (indented) code for the body of the module.
    source_code += ic.source_code
    # Closing the brackets.
    source_code += "}\n"
    # Returing the prepared source code.
    return source_code, ic.owned_states, ic.owned_locals


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
