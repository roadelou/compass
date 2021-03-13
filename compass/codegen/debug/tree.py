#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-13
# Language: Python3

################################### IMPORTS ####################################

# Standard library
import logging  # Used to log some information for the user.


# External imports
# Your imports from other packages go here


# Internal imports
import compass.ast as ast  # Used for downcasts

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################

# Source code for a C function that reads the next word from stdin, used in
# codegen_tree.
next_word_C_code = """
int next_word(char *buffer, size_t buffer_size) {
    size_t cursor = 0;
    int next_char;
    int working = 1;
    while (working && ((next_char = getchar()) != EOF)) {
        switch (next_char) {
            case '\\n':
            case ' ':
                buffer[cursor] = '\\0';
                working = 0;
                break;
            default:
                if (cursor < buffer_size) {
                    buffer[cursor] = next_char;
                    cursor++;
                }
                else {
                    buffer[buffer_size-1] = '\\0';
                    working = 0;
                }
                break;
        }
    }
    return (next_char != EOF);
}
"""


def codegen_tree(tree: ast.Tree) -> str:
    """
    Outputs the C source code for debugging the provided AST through the command
    line.
    """
    source_code = ""
    # Adding common inclusions for the code.
    source_code += (
        "#include <stdio.h>\n" "#include <stdlib.h>\n" "#include <string.h>\n"
    )
    # Adding an include for the Compass module, assuming the default header name
    # has been used.
    assumed_header = f"{tree.module.name}_compass.h"
    logging.info(f"Assuming header used is {assumed_header}")
    source_code += f'#include "{assumed_header}"\n'

    # Newline for the style.
    source_code += "\n"

    # Forward declaration of the next_word function, used to read the input word
    # by word.
    source_code += "int next_word(char *buffer, size_t buffer_size);\n"

    # Newline for the style.
    source_code += "\n"

    # Starting the main function.
    source_code += "int main(int argc, const char **argv) {\n"
    # We grab the signals from the module.
    module_signals = [
        declaration.signal.name for declaration in tree.module.declarations
    ]
    # We also make separate lists for the input and output signals.
    module_inputs = [
        declaration.signal.name
        for declaration in tree.module.declarations
        if isinstance(declaration, ast.InputDeclaration)
    ]
    module_outputs = [
        declaration.signal.name
        for declaration in tree.module.declarations
        if isinstance(declaration, ast.OutputDeclaration)
    ]
    # Allocating the signals on the stack.
    source_code += "\tint " + ", ".join(module_signals) + ";\n"
    # To decide what buffer size to use, we pick the longest signal name + 1.
    buffer_size = max(len(signal) for signal in module_signals) + 1
    # We allocate some memory on the stack for the names (which are assumed to
    # be rather short).
    source_code += f"\tchar word[{buffer_size}];\n"
    # Newline for the style.
    source_code += "\n"
    # We enter the event loop, which starts by resetting all the signals.
    source_code += "\twhile(1) {\n"
    for signal in module_signals:
        source_code += f"\t\t{signal} = 0;\n"

    # We read the next word from the user.
    source_code += (
        "\n"  # For the style
        f"\t\tif (!next_word(word, {buffer_size})) {{\n"
        f"\t\t\tword[{buffer_size - 1}] = '\\0';\n"
        '\t\t\tfprintf(stderr, "Encountered EOF after %s\\n", word);\n'
        "\t\t\treturn -1;\n"
        "\t\t}\n"
        "\n"  # For the style
    )

    # Setting the right signal depending on the user input.
    for index, signal in enumerate(module_inputs):
        # Using if only for the first test.
        if index == 0:
            keyword = "if"
        else:
            keyword = "else if"
        # Adding the source code.
        source_code += (
            f'\t\t{keyword} (strncmp(word, "{signal}", {len(signal)+1}) == '
            "0) {\n"
            f"\t\t\t{signal} = 1;\n"
            "\t\t}\n"
        )
    # Adding the else case.
    source_code += (
        "\t\telse {\n"
        '\t\t\tfprintf(stderr, "Unknown Signal %s\\n", word);\n'
        "\t\t}\n"
        "\n"  # For the style
    )

    # Calling the module.
    source_code += (
        f"\t\t{tree.module.name}("
        + ", ".join([f"&{signal}" for signal in module_signals])
        + ");\n"
        "\n"  # For the style
    )

    # Reporting the values of all the signals.
    source_code += '\t\tputs("Signal Report\\n=============");\n'
    for signal in module_signals:
        source_code += f'\t\tprintf("Signal {signal}: %d\\n", {signal});\n'

    # Ending the interaction loop and the main function.
    source_code += (
        "\t}\n" "\treturn EXIT_SUCCESS;\n" "}\n" "\n"  # Newline for the style
    )

    # Adding the source code for next_word.
    source_code += next_word_C_code

    # Returning the built source code.
    return source_code


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
