#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-30
# Language: Python3

################################### IMPORTS ####################################

# Standard library
import json  # Used for json files manipulations
import argparse  # Used for CLI of compass-builder


# External imports
# Your imports from other packages go here


# Internal imports
from compass.frontend.builder_configuration import (
    BuilderConfiguration,
)  # Used for Makefile generation

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def build(json_path: str, makefile_path: str):
    """
    Builds the Makefile to compile the code for the project based on the
    provided JSON specification.

    Arguments
    =========
     - json_path: The path to the JSON containing the description of the
        project.
     - makefile_path: The file to which the Makefile should be written.
    """
    # We first read the JSON file.
    with open(json_path, "r") as json_file:
        json_content = json.load(json_file)
    # We deserialize the content of the JSON file.
    builder_configuration = BuilderConfiguration.from_json(json_content)
    # We build the code for the Makefile.
    makefile_source = builder_configuration.to_makefile()
    # We write the content of the Makefile to the provided path.
    with open(makefile_path, "w") as makefile_file:
        makefile_file.write(makefile_source)


def command_line():
    """
    Entry point for the CLI of compass-builder.
    """
    # We build the argparse parser in this method because it is quite short.
    # We add an epilog about examples of the JSON files.
    cli_parser = argparse.ArgumentParser(
        prog="compass-builder",
        epilog="See the documentation for JSON examples.",
    )
    # Adding the arguments compass-builder.
    cli_parser.add_argument(
        "JSON", type=str, help="The JSON description of the project."
    )
    cli_parser.add_argument(
        "MAKEFILE",
        type=str,
        help="The path to which the Makefile should be written.",
    )
    # We parse the provided arguments.
    arguments = cli_parser.parse_args()
    # We call the build function with the right arguments.
    build(arguments.JSON, arguments.MAKEFILE)


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
