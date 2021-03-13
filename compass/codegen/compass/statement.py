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
from compass.codegen.compass.expression import (
    codegen_expression,
)  # Used for recursive codegen

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def codegen_statement(statement: ast.Statement, indent: int) -> str:
    """
    Outputs the Compass code corresponding to the provided Statement.
    """
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # Several cases appear, one for each kind of statements.
    if isinstance(statement, ast.Each):
        # We build the code for the inner body of the for-each loop.
        inner_body = codegen_statement(statement.statement, indent + 1)
        # We return the code for the whole for-each loop.
        return (
            indent_str
            + f"each {statement.signal} {{\n"
            + inner_body
            + indent_str
            + "};\n"
        )
    elif isinstance(statement, ast.Seq):
        # We build the code for each inner statement.
        inner_statement_bodies = [
            codegen_statement(inner_statement, indent + 1)
            for inner_statement in statement.statements
        ]
        # We join the different lines.
        inner_body = "".join(inner_statement_bodies)
        # We return the code for the Seq statement.
        return indent_str + "seq {\n" + inner_body + indent_str + "};\n"
    elif isinstance(statement, ast.Par):
        # We build the code for each inner statement.
        inner_statement_bodies = [
            codegen_statement(inner_statement, indent + 1)
            for inner_statement in statement.statements
        ]
        # We join the different lines.
        inner_body = "".join(inner_statement_bodies)
        # We return the code for the Par statement.
        return indent_str + "par {\n" + inner_body + indent_str + "};\n"
    elif isinstance(statement, ast.AwaitStatement):
        # We return the code for the await statement.
        return indent_str + f"await {statement.signal};\n"
    elif isinstance(statement, ast.EmitStatement):
        # We build the code for the inner expression.
        inner_expression = codegen_expression(statement.expression)
        # We return the code for the await statement.
        return indent_str + f"emit {inner_expression};\n"
    else:
        raise ValueError(f"Unknown statement {statement}")


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
