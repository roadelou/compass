#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-12
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from setuptools import setup  # Used to build the python package.


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################

# Your classes go here

################################## FUNCTIONS ###################################


def main():
    """
    Calls the setup function to define the python package.
    """
    setup(
        name="compass",
        version="0.0.1",
        author="roadelou",
        author_email="",
        packages=[
            "compass",
            "compass/ast",
            "compass/codegen",
            "compass/codegen/compass",
            "compass/codegen/c",
            "compass/frontend",
            "compass/grammar",
        ],
        license="GPL3",
        install_requires=["sly"],
        python_requires=">=3.6",
        entry_points="""
        [console_scripts]
        compass=compass.frontend:command_line
        """,
    )


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    main()

##################################### EOF ######################################