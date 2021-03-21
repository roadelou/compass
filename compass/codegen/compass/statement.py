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
        # We build the code for the reset expression.
        inner_expression = codegen_expression(statement.expression)
        # We return the code for the whole for-each loop.
        return f"{indent_str}each {inner_expression}\n{inner_body}"
    elif isinstance(statement, ast.Seq):
        # We build the code for each inner statement.
        inner_statement_bodies = [
            codegen_statement(inner_statement, indent + 1)
            for inner_statement in statement.statements
        ]
        # We join the different lines.
        inner_body = ";\n".join(inner_statement_bodies) + ";\n"
        # We return the code for the Seq statement.
        return indent_str + f"seq {{\n{inner_body}" + indent_str + "}"
    elif isinstance(statement, ast.Par):
        # We build the code for each inner statement.
        inner_statement_bodies = [
            codegen_statement(inner_statement, indent + 1)
            for inner_statement in statement.statements
        ]
        # We join the different lines.
        inner_body = ";\n".join(inner_statement_bodies) + ";\n"
        # We return the code for the Par statement.
        return indent_str + f"par {{\n{inner_body}" + indent_str + "}"
    elif isinstance(statement, ast.IfStatement):
        # The condition to branch on.
        inner_expression = codegen_expression(statement.expression)
        # The inner if branch.
        inner_if = codegen_statement(statement.statement, indent + 1)
        # Two cases appear, depending whether an else statement was also used.
        if statement.else_statement is None:
            return (
                f"{indent_str}if ({inner_expression})\n{inner_if}\n"
                f"{indent_str}endif"
            )
        else:
            # The code for the else branch.
            inner_else = codegen_statement(statement.else_statement, indent + 1)
            return (
                f"{indent_str}if ({inner_expression})\n{inner_if}\n"
                f"{indent_str}else\n{inner_else}\n"
                f"{indent_str}endif"
            )
    elif isinstance(statement, ast.Submodule):
        # We create code for the list of arguments.
        code_arguments = ", ".join(
            [str(signal) for signal in statement.arguments]
        )
        # We return the code that calls the submodule with the right arguments.
        return f"{indent_str}submodule {statement.name}({code_arguments})"
    elif isinstance(statement, ast.AwaitStatement):
        # Getting the expression that we have to await.
        inner_expression = codegen_expression(statement.expression)
        # We return the code for the await statement.
        return indent_str + f"await {inner_expression}"
    elif isinstance(statement, ast.EmitStatement):
        # We build the code for the inner expression.
        inner_expression = codegen_expression(statement.expression)
        # We return the code for the emit statement.
        return indent_str + f"emit {statement.signal} <- {inner_expression}"
    elif isinstance(statement, ast.LocalStatement):
        # We return the code for the local variable declaration.
        return indent_str + f"local {statement.name}"
    else:
        raise ValueError(f"Unknown statement {statement}")


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
