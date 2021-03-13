#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-13
# Language: Python3

################################### IMPORTS ####################################

# Standard library
import argparse  # Used to build the command line interface
import os.path  # Used for path manipulations


# External imports
# Your imports from other packages go here


# Internal imports
from compass.frontend.driver import compass_compile  # The compiler driver

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def command_line():
    """
    Entry point of the command line interface.
    """
    # We first build the CLI using argparse.
    cli_parser = build_frontend_parser()
    # Parsing the command line arguments.
    arguments = cli_parser.parse_args()

    # We read the input source code.
    with open(arguments.SOURCE, "r") as source_file:
        source_code = source_file.read()

    # We call the compiler driver with the right arguments.
    built_code = compass_compile(source_code, arguments.LANG)

    # We write the compiled code to the provided output file. If no output file
    # was provided, we try to use a default one based on the input path and the
    # language used.
    if arguments.OUTPUT == None:
        output_path = default_output(arguments.SOURCE, arguments.LANG)
    else:
        output_path = arguments.OUTPUT

    with open(output_path, "w") as output_file:
        output_file.write(built_code)


def build_frontend_parser() -> argparse.ArgumentParser:
    """
    Builds the CLI parser with argparse.
    """
    cli_parser = argparse.ArgumentParser(prog="compass")
    # Adding the arguments for the frontend.
    cli_parser.add_argument(
        "SOURCE", type=str, help="The source code to compile"
    )
    cli_parser.add_argument(
        "-o",
        "--output",
        dest="OUTPUT",
        default=None,
        type=str,
        help="The file to write the compiled code to",
    )
    cli_parser.add_argument(
        "-l",
        "--lang",
        dest="LANG",
        default="C",
        choices=["compass", "C", "c", "H", "h", "header", "debug"],
        type=str,
        help="The language to compile for",
    )
    # Returning the built parser.
    return cli_parser


def default_output(source_path: str, language: str) -> str:
    """
    Returns the default path to put the output in based on the source_path and
    the language (for the extension).
    """
    # We first get the path of the file without extension.
    path_prefix, _ = os.path.splitext(source_path)
    # Getting the extension based on the language used.
    if language in ["C", "c"]:
        extension = ".c"
    elif language == "compass":
        extension = ".cmps"
    elif language in ["H", "h", "header"]:
        extension = ".h"
    elif language == "debug":
        extension = ".debug.c"
    else:
        raise ValueError(f"Unknown Language {language}")
    # Returning the expected output path.
    return path_prefix + "_compass" + extension


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
