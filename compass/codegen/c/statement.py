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
from compass.codegen.c.expression import (
    codegen_expression,
)  # Used for recursive codegen

################################### CLASSES ####################################


class SSAGenerator:
    """
    Static class used to build a singleton that outputs new unique names.
    """

    # The counter used to build the unique names.
    COUNTER = 0

    @classmethod
    def new_name(cls, base_name: str) -> str:
        """
        Returns a new unique name based on the provided one.
        """
        # We build the new name from the counter.
        new_name_string = f"{base_name}_{SSAGenerator.COUNTER}"
        # We increment the counter for the next call.
        SSAGenerator.COUNTER += 1
        # We return the built string.
        return new_name_string


################################## FUNCTIONS ###################################


def codegen_statement(
    statement: ast.Statement, indent: int
) -> Tuple[str, str, List[str]]:
    """
    Outputs the Compass code corresponding to the provided Statement.

    Arguments
    =========
     - statement: The statement to build the code for.
     - indent: The current indentation level.

    Returns
    =======
    A tuple with three values:
     - The requested code.
     - The immediate state of this statement, used by seq and par.
     - The list of states owned by this statement (and its children).

    Note
    ====
    All the real states are always contained in the owned states. Immediate
    states are boolena values telling whether a statement is done or not and can
    be rvalues. Owned states are used for initialization and resets.
    """
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # Several cases appear, one for each kind of statements.
    if isinstance(statement, ast.Each):
        return codegen_each(statement, indent)
    elif isinstance(statement, ast.Seq):
        return codegen_seq(statement, indent)
    elif isinstance(statement, ast.Par):
        return codegen_par(statement, indent)
    elif isinstance(statement, ast.AwaitStatement):
        return codegen_await(statement, indent)
    elif isinstance(statement, ast.EmitStatement):
        return codegen_emit(statement, indent)
    else:
        raise ValueError(f"Unknown statement {statement}")


def codegen_each(
    statement: ast.Each, indent: int
) -> Tuple[str, str, List[str]]:
    """
    Specialized variant of codegen_statement for for-each statements.
    """
    source_code = ""
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # We build the code for the inner body of the for-each loop.
    inner_body, inner_immediate, inner_states = codegen_statement(
        statement.statement, indent
    )
    # We build the code for the reset expression.
    inner_expression = codegen_expression(statement.expression)
    # for-each statements don't use the inner_immediate states in any particular way.
    owned_states = inner_states
    # The each loops don't have any state, but we have to build a bit of code foe the reset.
    source_code += indent_str + f"if ({inner_expression}) {{\n"
    # We have to reset all the states owned by the body of the loop.
    for state in owned_states:
        source_code += indent_str + "\t" + f"{state} = 0;\n"
    # Closing the reset statement and beginning the statement of the body.
    source_code += indent_str + "}\n"
    # Adding the code for the inner body.
    source_code += inner_body
    # Returning the source code, the immediate states and the owned states. Note
    # that an each loop never ends.
    return source_code, "0", owned_states


def codegen_seq(statement: ast.Seq, indent: int) -> Tuple[str, str, List[str]]:
    """
    Specialized variant of codegen_statement for seq statements.
    """
    source_code = ""
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # We need a state to keep track of the sequential execution.
    seq_state = SSAGenerator.new_name("seq")
    # Used to keep track of all the owned states.
    owned_states: List[str] = [seq_state]
    # We build some code for each of the inner sequential statements.
    for index, inner_statement in enumerate(statement.statements):
        # We build the code for the inner body of the seq statement.
        inner_body, inner_immediate, inner_states = codegen_statement(
            inner_statement, indent + 1
        )
        # We keep track of all the states owned by our seq statement.
        owned_states += inner_states
        # We add the code for the case. Note that we always use ifs (and never
        # else) to fall to the next case whenever possible.
        source_code += indent_str + f"if ({seq_state} == {index}) {{\n"
        # We add the source code for the statement executed sequentially.
        source_code += inner_body
        # EDGE CASE
        # If we have reached the last state of the sequential execution, we don't jump.
        if index + 1 == len(statement.statements):
            source_code += indent_str + "\t" + "/* LAST SEQUENTIAL STATE */\n"
        else:
            # We move to the next state if all the immediate states of the inner
            # statement are true, or if there are no immediate states.
            source_code += (
                indent_str + "\t" + f"{seq_state} += {inner_immediate};\n"
            )
        # Closing the if statement.
        source_code += indent_str + "}\n"
    # We return the expected source code. The single immediate state of a seq
    # statement is whether it reached its last state.
    return (
        source_code,
        f"({seq_state} == {len(statement.statements) - 1}",
        owned_states,
    )


def codegen_par(statement: ast.Par, indent: int) -> Tuple[str, str, List[str]]:
    """
    Specialized variant of codegen_statement for par statements.
    """
    source_code = ""
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # Used to keep track of all the owned states.
    owned_states: List[str] = list()
    # We also keep track of all the immediate states of our sub statements to
    # build our own immediate state at the end.
    immediate_states: List[str] = list()
    # Par statements are mostly invisible in the produced code, they look like
    # normal C execution.
    # We build some code for each of the inner parallel statements.
    for index, inner_statement in enumerate(statement.statements):
        # We build the code for the inner body of the par statement. We don't
        # need to indent the code.
        inner_body, inner_immediate, inner_states = codegen_statement(
            inner_statement, indent
        )
        # We keep track of all the states owned by our seq statement.
        owned_states += inner_states
        # We also keep track of the immediate state.
        immediate_states.append(inner_immediate)
        # We add the source code for the statement executed sequentially.
        source_code += inner_body
    # We return the expected source code. The single immediate state of a par
    # statement is the intersection of all the immediate states of its children
    # (i.e. the parallel execution ends when all the threads end).
    return source_code, "(" + " && ".join(immediate_states) + ")", owned_states


def codegen_await(
    statement: ast.AwaitStatement, indent: int
) -> Tuple[str, str, List[str]]:
    """
    Specialized variant of codegen_statement for await statements.
    """
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # We build the code for the inner expression.
    inner_expression = codegen_expression(statement.expression)
    # We need a new state for the await statement.
    await_state = SSAGenerator.new_name("await")
    # We build the expected source code.
    source_code = indent_str + f"{await_state} |= {inner_expression};\n"
    # We return the expected triple.
    return source_code, await_state, [await_state]


def codegen_emit(
    statement: ast.EmitStatement, indent: int
) -> Tuple[str, str, List[str]]:
    """
    Specialized variant of codegen_statement for emit statements.
    """
    # We quickly compute the indentation string we will need for this statement.
    indent_str = "\t" * indent
    # We get the C code for the inner expression (the rvalue).
    inner_expression = codegen_expression(statement.expression)
    # We build the expected source code.
    source_code = indent_str + f"*{statement.signal} = {inner_expression};\n"
    # We return the expected triple. An emit statement always exits instantly.
    return source_code, "1", list()


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
