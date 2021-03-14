#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-12
# Language: Python3

################################### IMPORTS ####################################

# Standard library
import logging  # Used to print error message, but keep parsing the source


# External imports
from sly import Lexer  # Lexer implementation


# Internal imports
from compass.grammar import compass_tokens  # Used for language tokens

################################### CLASSES ####################################


class CompassLexer(Lexer):
    """
    Lexer for the Compass language.
    """

    # The tokens used to build the source code.
    tokens = compass_tokens.tokens
    # Ignoring whitespace and tab.
    ignore = " \t"
    # Some symbols are used literaly.
    literals = compass_tokens.literals

    # Matching the assignation operator.
    ASSIGN = r"<-"
    # Matching non-literal the binary operators.
    TESTEQ = r"=="
    AND = r"&&"
    OR = r"\|\|"

    # Matching a number, only integers are allowed in compass.
    NUMBER = r"\d+"
    # Matching any string, which is first assumed to be a name.
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"

    # Remapping the language keywords when they are found within the string.
    NAME["module"] = MODULE
    NAME["input"] = INPUT
    NAME["output"] = OUTPUT
    NAME["each"] = EACH
    NAME["seq"] = SEQ
    NAME["par"] = PAR
    NAME["await"] = AWAIT
    NAME["emit"] = EMIT

    # We keep track of newlines to count them.
    @_(r"\n+")
    def newline(self, t):
        self.lineno += len(t.value)

    # Used to print error messages when lexer error is encountered.
    def error(self, t):
        # Logging an error message.
        loggin.error(f"Unrecognized string {t.value}")
        self.index += len(t.value)


################################## FUNCTIONS ###################################

# Your functions go here

##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
