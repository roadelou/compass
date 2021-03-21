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
from compass.codegen.utils import (
    InnerContext,
    OuterContext,
)  # Used for type hints

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
    statement: ast.Statement, oc: OuterContext
) -> InnerContext:
    """
    Outputs the Compass code corresponding to the provided Statement.

    Arguments
    =========
     - statement: The statement to build the code for.
     - oc: The OuterContext we have to take into account when building this statement.

    Returns
    =======
    The InnerContext produced by this code (which includes the generated code).

    Note
    ====
    All the real states are always contained in the owned states. Immediate
    states are boolena values telling whether a statement is done or not and can
    be rvalues. Owned states are used for initialization and resets.
    """
    # Several cases appear, one for each kind of statements.
    if isinstance(statement, ast.Each):
        return codegen_each(statement, oc)
    elif isinstance(statement, ast.Seq):
        return codegen_seq(statement, oc)
    elif isinstance(statement, ast.Par):
        return codegen_par(statement, oc)
    elif isinstance(statement, ast.AwaitStatement):
        return codegen_await(statement, oc)
    elif isinstance(statement, ast.EmitStatement):
        return codegen_emit(statement, oc)
    elif isinstance(statement, ast.LocalStatement):
        return codegen_local(statement, oc)
    elif isinstance(statement, ast.IfStatement):
        return codegen_if(statement, oc)
    elif isinstance(statement, ast.Submodule):
        return codegen_submodule(statement, oc)
    else:
        raise ValueError(f"Unknown statement {statement}")


def codegen_each(statement: ast.Each, oc: OuterContext) -> InnerContext:
    """
    Specialized variant of codegen_statement for for-each statements.
    """
    # The Inner Context we will return. Note that an each loop never ends.
    ic = InnerContext(immediate_state="0")
    # We build the code for the inner body of the for-each loop.
    inner_ic = codegen_statement(statement.statement, oc)
    # We build the code for the reset expression.
    inner_expression = codegen_expression(statement.expression)
    # for-each statements don't use the inner_immediate states in any particular
    # way.
    ic.inherit(inner_ic)
    # The each loops don't have any state, but we have to build a bit of code
    # for the reset.
    ic.source_code += oc.indent_str + f"if ({inner_expression}) {{\n"
    # We have to reset all the states owned by the body of the loop.
    for state in ic.owned_states:
        ic.source_code += oc.indent_str + "\t" + f"{state} = 0;\n"
    # Closing the reset statement and beginning the statement of the body.
    ic.source_code += oc.indent_str + "}\n"
    # Adding the code for the inner body.
    ic.source_code += inner_ic.source_code
    # Returning the source code, the immediate states and the owned states.
    return ic


def codegen_seq(statement: ast.Seq, oc: OuterContext) -> InnerContext:
    """
    Specialized variant of codegen_statement for seq statements.
    """
    # The Inner Context we will return.
    ic = InnerContext()
    # We need a state to keep track of the sequential execution.
    seq_state = SSAGenerator.new_name("seq")
    # We add our new state to the list of states we need to keep track of.
    ic.owned_states.append(seq_state)
    # We build some code for each of the inner sequential statements. We first
    # have to create the context for those future statement.
    inner_oc = OuterContext(indent=oc.indent + 1)
    for index, inner_statement in enumerate(statement.statements):
        # We build the code for the inner body of the seq statement.
        inner_ic = codegen_statement(inner_statement, inner_oc)
        # We inherit the recursive values from the InnerContext.
        ic.inherit(inner_ic)
        # We add the code for the case. Note that we always use ifs (and never
        # else) to fall to the next case whenever possible.
        ic.source_code += oc.indent_str + f"if ({seq_state} == {index}) {{\n"
        # We add the source code for the statement executed sequentially.
        ic.source_code += inner_ic.source_code
        # EDGE CASE
        # If we have reached the last state of the sequential execution, we
        # don't jump.
        if index + 1 == len(statement.statements):
            ic.source_code += (
                oc.indent_str + "\t" + "/* LAST SEQUENTIAL STATE */\n"
            )
        else:
            # We move to the next state if all the immediate states of the inner
            # statement are true, or if there are no immediate states.
            ic.source_code += (
                oc.indent_str
                + "\t"
                + f"{seq_state} += {inner_ic.immediate_state};\n"
            )
        # Closing the if statement.
        ic.source_code += oc.indent_str + "}\n"
    # We return the expected source code. The single immediate state of a seq
    # statement is whether it reached its last state.
    ic.immediate_state = (f"({seq_state} == {len(statement.statements) - 1}",)
    return ic


def codegen_par(statement: ast.Par, oc: OuterContext) -> InnerContext:
    """
    Specialized variant of codegen_statement for par statements.
    """
    # The Inner Context we will return.
    ic = InnerContext()
    # We also keep track of all the immediate states of our sub statements to
    # build our own immediate state at the end.
    immediate_states: List[str] = list()
    # Par statements are mostly invisible in the produced code, they look like
    # normal C execution.
    # We build some code for each of the inner parallel statements.
    for index, inner_statement in enumerate(statement.statements):
        # We build the code for the inner body of the par statement. We don't
        # need to indent the code.
        inner_ic = codegen_statement(inner_statement, oc)
        # We inherit the recursive values from the InnerContext.
        ic.inherit(inner_ic)
        # We also keep track of the immediate state.
        immediate_states.append(inner_ic.immediate_state)
        # We add the source code for the statement executed sequentially.
        ic.source_code += inner_ic.source_code
    # We return the expected source code. The single immediate state of a par
    # statement is the intersection of all the immediate states of its children
    # (i.e. the parallel execution ends when all the threads end).
    ic.immediate_state = "(" + " && ".join(immediate_states) + ")"
    return ic


def codegen_await(
    statement: ast.AwaitStatement, oc: OuterContext
) -> InnerContext:
    """
    Specialized variant of codegen_statement for await statements.
    """
    # The Inner Context we will return.
    ic = InnerContext()
    # We build the code for the inner expression.
    inner_expression = codegen_expression(statement.expression)
    # We need a new state for the await statement.
    await_state = SSAGenerator.new_name("await")
    # We build the expected source code.
    ic.source_code = oc.indent_str + f"{await_state} |= {inner_expression};\n"
    # Our immediate state is given by the "await_state".
    ic.immediate_state = await_state
    # We own the new single state associated with the await statement.
    ic.owned_states.append(await_state)
    return ic


def codegen_emit(
    statement: ast.EmitStatement, oc: OuterContext
) -> InnerContext:
    """
    Specialized variant of codegen_statement for emit statements.
    """
    # The Inner Context we will return.
    ic = InnerContext()
    # We get the C code for the inner expression (the rvalue).
    inner_expression = codegen_expression(statement.expression)
    # We build the expected source code.
    ic.source_code = (
        oc.indent_str + f"*{statement.signal} = {inner_expression};\n"
    )
    # We return the expected triple. An emit statement always exits instantly.
    ic.immediate_state = "1"
    return ic


def codegen_local(
    statement: ast.EmitStatement, oc: OuterContext
) -> InnerContext:
    """
    Specialized variant of codegen_statement for local statements.
    """
    # The Inner Context we will return.
    ic = InnerContext()
    # We add a new local to our InnerContext based on the name provided in the
    # source code.
    ic.owned_locals.append(statement.name)
    # There is no code associated with a local statement.
    # We return the expected triple. A local statement always exits instantly.
    ic.immediate_state = "1"
    return ic


def codegen_if(statement: ast.IfStatement, oc: OuterContext) -> InnerContext:
    """
    Specialized variant of codegen_statement for if-else statements.
    """
    # The Inner Context we will return.
    ic = InnerContext()
    # We start by building the code for our conditional expression.
    inner_expression = codegen_expression(statement.expression)
    # We also build the code for our indented if statement.
    inner_ic = codegen_statement(
        statement.statement, OuterContext(oc.indent + 1)
    )
    # Inheriting the owned and local of our inner expression.
    ic.inherit(inner_ic)
    # We start by filling the code for the if branch before checking if there is
    # an else.
    ic.source_code += f"{oc.indent_str}if ({inner_expression}) {{\n"
    ic.source_code += inner_ic.source_code
    ic.source_code += f"{oc.indent_str}}}\n"
    if statement.else_statement is None:
        # No else statement, this is the easy case. The immediate state of the
        # if statement is that of its if branch if it is taken, otherwise it
        # exits immediately.
        ic.immediate_state = (
            f"(!{inner_expression} || {inner_ic.immediate_state} * "
            f"{inner_expression})"
        )
        # We simply return the InnerContext we have built so far.
        return ic
    else:
        # We must add the code for the else statement.
        else_ic = codegen_statement(
            statement.else_statement, OuterContext(oc.indent + 1)
        )
        # We also inherit the InnerContext from the else branch.
        ic.inherit(else_ic)
        # We add the code for the else branch.
        ic.source_code += (
            f"{oc.indent_str}else {{\n"
            f"{else_ic.source_code}"
            f"{oc.indent_str}}}\n"
        )
        # We return the Inner Context we have built.
        return ic


def codegen_submodule(
    statement: ast.Submodule, oc: OuterContext
) -> InnerContext:
    """
    Specialized variant of codegen_statement for submodule statements.
    """
    # The inner context we will return.
    ic = InnerContext()
    # All the argument signals are already pointers, which is what the callee
    # expects, hence we may directly build the code for the arguments.
    code_arguments = ", ".join([str(signal) for signal in statement.arguments])
    # We then simply call the the C function associated with the module by name.
    ic.source_code += f"{oc.indent_str}{statement.name}({code_arguments});\n"
    # A submodule call is always instantaneous, like an emit.
    ic.immediate_state = "1"
    # We add the new submodule to the owned submodules.
    ic.owned_submodules.append(statement.name)
    # We return the newly built context.
    return ic


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
