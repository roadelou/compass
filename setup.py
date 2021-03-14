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
    # Reading the long description from the README file.
    with open("README.md", "r") as readme_file:
        readme_content = readme_file.read()

    setup(
        name="roadelou-compass",
        version="0.0.2",
        author="roadelou",
        author_email="",
        packages=[
            "compass",
            "compass/ast",
            "compass/ast/unary",
            "compass/ast/binary",
            "compass/codegen",
            "compass/codegen/compass",
            "compass/codegen/c",
            "compass/codegen/header",
            "compass/codegen/debug",
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
        description="Simple synchronous programming language",
        long_description=readme_content,
        long_description_content_type="text/markdown",
        url="https://github.com/roadelou/compass",
        classifiers=[
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux",
            "Topic :: Software Development :: Compilers",
            "Topic :: Software Development :: Code Generators",
            "Topic :: System :: Hardware",
        ]
    )


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    main()

##################################### EOF ######################################
