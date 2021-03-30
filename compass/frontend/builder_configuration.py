#!/usr/bin/env python3

################################### METADATA ###################################

# Contributors: roadelou
# Contacts:
# Creation Date: 2021-03-30
# Language: Python3

################################### IMPORTS ####################################

# Standard library
from __future__ import annotations  # Used for self reference
from typing import List, Dict, Any  # Used for type hints


# External imports
# Your imports from other packages go here


# Internal imports
# Your imports within this package go here

################################### CLASSES ####################################


class BuilderConfiguration:
    """
    Class used to hold the configuration of the builder that was stored in the
    JSON file.
    """

    def __init__(
        self,
        entry_point: str,
        debug: bool,
        modules: Dict[str, List[str]],
        source_directory: str,
        build_directory: str,
    ):
        """
        Constructors of the BuilderConfiguration class.

        Arguments
        =========
         - entry_points: The module that will be used as an entry-point for your
            program.
         - debug: Whether the CLI debugging wrapper should be computed.
         - modules: A dictionary associating each source module with the
            instances it should be compiled to.
         - source_directory: Path to the directory where the compass files can
            be found.
         - build_directory: Path to the directory where the compiled files
            should be placed.
        """
        # Storing the arguments.
        self.entry_point = entry_point
        self.debug = debug
        self.modules = modules
        self.source_directory = source_directory
        self.build_directory = build_directory

    def to_makefile(self) -> str:
        """
        Compiles this BuilderConfiguration into a Makefile template that can be
        used for configuration.
        """
        source_code = ""
        # Adding a small header to the Makefile.
        source_code += "# Makefile compiled automatically by compass-build.\n\n"
        # Declaring generic aliases to make the built Makefile easier to edit.
        source_code += f"SRC_DIR = {self.source_directory}\n"
        source_code += f"BUILD_DIR = {self.build_directory}\n"
        # We need to at least give the "-c" flag to the compiler to produce
        # object files.
        source_code += f"COMPASS_FLAGS = -c $(CFLAGS)\n"
        source_code += build_source_aliases(self.modules)
        # Blank line for the style.
        source_code += "\n"
        source_code += build_destination_aliases(self.modules)
        # Blank line for the style.
        source_code += "\n"
        source_code += build_entry_point_aliases(
            self.modules, self.entry_point, self.debug
        )
        # Blank line for the style.
        source_code += "\n"
        # Line for separation.
        source_code += "#" * 80 + "\n\n"
        # Adding the code in the Makefile for the rules. We start with the PHONY
        # modifier.
        source_code += ".PHONY: all clean\n\n"
        # Adding the rules for the entry point first.
        source_code += build_entry_point_rule(self.entry_point, self.debug)
        # Adding the rules for all the object files of the module instances.
        source_code += build_module_rules(self.modules)
        # Adding a rule to build the build directory if it doesn't exist.
        source_code += "$(BUILD_DIR):\n" "\tmkdir -p $(BUILD_DIR)\n\n"
        # Adding the rules to clean the code.
        source_code += build_clean_rule()
        # Returning the built Makefile.
        return source_code

    @classmethod
    def from_json(cls, json_content: Any) -> BuilderConfiguration:
        """
        Deserializes the BuildConfiguration from the content of the provided
        Makefile. Will raise an AssertionError if deserialization fails.
        """
        # The root of the JSON file should be a dictionary.
        assert isinstance(json_content, dict)
        # The root of the JSON should have 2 or 3 keys.
        number_keys = len(json_content.keys())
        assert number_keys == 4 or number_keys == 5
        # Getting the entry point.
        assert "entry_point" in json_content
        # Getting the value for the entry_point.
        entry_point: Any = json_content["entry_point"]
        # The entry point should be a string.
        assert isinstance(entry_point, str)
        # Getting the module dictionary.
        assert "modules" in json_content
        modules: Any = json_content["modules"]
        # The modules value should be a dictionary.
        assert isinstance(modules, dict)
        # The keys for the modules should all be string.
        assert all(isinstance(key, str) for key in modules.keys())
        # The values for the modules should all be lists.
        assert all(isinstance(value, list) for value in modules.values())
        # The renamed modules in the value lists should all be strings.
        assert all(
            all(isinstance(renamed_module, str) for renamed_module in value)
            for value in modules.values()
        )
        # Getting the source directory.
        assert "source_directory" in json_content
        # Getting the value for the source_directory.
        source_directory: Any = json_content["source_directory"]
        # The source directory should be a string.
        assert isinstance(source_directory, str)
        # Getting the build directory.
        assert "build_directory" in json_content
        # Getting the value for the build_directory.
        build_directory: Any = json_content["build_directory"]
        # The build directory should be a string.
        assert isinstance(build_directory, str)
        # We try to get the debug value if there is one.
        if number_keys == 5:
            assert "debug" in json_content
            debug: Any = json_content["debug"]
            # debug should be either True or False.
            assert isinstance(debug, bool)
        else:
            # No debug by default.
            debug = False
        # We return an instance of the BuilderConfiguration class from the
        # fetched values.
        return cls(
            entry_point, debug, modules, source_directory, build_directory
        )


################################## FUNCTIONS ###################################


def build_source_aliases(modules: Dict[str, List[str]]) -> str:
    """
    Returns the Makefile snippet for the aliases of all the described source
    modules.
    """
    source_code = ""
    # We first fetch all the source modules.
    source_modules = modules.keys()
    for source_module in source_modules:
        # We create an alias for the source module. We assume that the file for
        # the provided module can be derived from the module name.
        source_code += (
            f"SRC_{source_module.upper()} = $(SRC_DIR)/{source_module}.cmps\n"
        )
    # We return the built source code.
    return source_code


def build_destination_aliases(modules: Dict[str, List[str]]) -> str:
    """
    Returns the Makefile snippet for the aliases of all the described module
    instances.
    """
    source_code = ""
    # We first fetch all the destination modules. We assume that no 2 modules
    # have the same name. We concatenate all the module instances in one big
    # list.
    instances = sum(modules.values(), [])
    # We also keep a list of all the instances we will need for the "all" rule.
    all_instances: List[str] = list()
    # We also need to keep track of the intermediary C files for the "clean"
    # rule.
    all_c_instances: List[str] = list()
    for instance in instances:
        # We create an alias for the provided instance and generate a name for
        # its object file. We also add an alias for its C code.
        source_code += (
            f"DEST_{instance.upper()} = $(BUILD_DIR)/{instance}.o\n"
            f"DEST_C_{instance.upper()} = $(BUILD_DIR)/{instance}.c\n"
        )
        # We add the alias for the object to the list of instances.
        all_instances.append(f"$(DEST_{instance.upper()})")
        # Same for the C file.
        all_c_instances.append(f"$(DEST_C_{instance.upper()})")
    # We build an alias to build all the object files at once.
    source_code += "ALL_DEST = " + " ".join(all_instances) + "\n"
    # Same for the intermediary C files.
    source_code += "ALL_DEST_C = " + " ".join(all_c_instances) + "\n"
    # We return the built snippet.
    return source_code


def build_entry_point_aliases(modules: Dict[str, List[str]], entry_point: str, debug: bool) -> str:
    """
    Returns the Makefile snippet to build the aliases used in the compilation of
    the entry point module.
    """
    source_code = ""

    # We start by finding which module the entry point comes from.
    source_module: Optional[str] = None
    for module, instances in modules.items():
        if entry_point in instances:
            # We have found the module from which the entry point originates,
            # we remember it and exit.
            source_module = module
            break
    # We raise an assertion error if the entry_point is never produced.
    assert source_module is not None, f"{entry_point} is never produced"

    # We add an alias to link the source file of the entry point.
    source_code += f"SRC_ENTRY_POINT = $(SRC_{source_module.upper()})\n"
    # We create an alias for the entry point header. Default header name has a
    # "_compass" at the end, this is to play nicely with the debug backend and
    # avoid name collision.
    source_code += f"HEAD_ENTRY_POINT = $(BUILD_DIR)/{entry_point}_compass.h\n"
    # If required, we add an alias for the CLI debuggin wrapper.
    if debug:
        source_code += (
            f"DEBUG_ENTRY_POINT = $(BUILD_DIR)/{entry_point}.debug.o\n"
            f"DEBUG_C_ENTRY_POINT = $(BUILD_DIR)/{entry_point}.debug.c\n"
            f"DEBUG_ELF_ENTRY_POINT = $(BUILD_DIR)/{entry_point}.debug.elf\n"
        )
    # We return the prepared source code.
    return source_code


def build_entry_point_rule(entry_point: str, debug: bool) -> str:
    """
    Returns the rule to build the entry point of the project.
    """
    source_code = ""
    # We start by making the "all" entry rule. We don't add an EOL because of
    # the debug flag. We also build the "build directory" if it doesn't yet
    # exist.
    source_code += "all: $(ALL_DEST) $(HEAD_ENTRY_POINT) $(BUILD_DIR)"
    if debug:
        # We also have to add the debug entry-point to the all rule.
        source_code += " $(DEBUG_ELF_ENTRY_POINT)"
    # Now that the debug has been handled, we may close the "all" rule.
    source_code += "\n\n"

    # We add the rule to build the header of the entry point.
    source_code += (
        "$(HEAD_ENTRY_POINT): $(SRC_ENTRY_POINT)\n"
        f"\tcompass -r {entry_point} -o $(HEAD_ENTRY_POINT) --lang header "
        "$(SRC_ENTRY_POINT)\n\n"
    )

    if debug:
        # If the debug flag is set, we also have to compile the debugging CLI.
        # We need two rules for this. The first one is to built the C source for
        # the CLI.
        source_code += (
            "$(DEBUG_C_ENTRY_POINT): $(SRC_ENTRY_POINT) $(BUILD_DIR)\n"
            f"\tcompass -r {entry_point} -o $(DEBUG_C_ENTRY_POINT) --lang "
            "debug $(SRC_ENTRY_POINT)\n\n"
        )
        # The second rule is to build the object file from the CLI C source. We
        # need to include the build directory since it is where the header file
        # can be found.
        source_code += (
            "$(DEBUG_ENTRY_POINT): $(DEBUG_C_ENTRY_POINT) $(BUILD_DIR)\n"
            "\t$(CC) $(COMPASS_FLAGS) -o $(DEBUG_ENTRY_POINT) -I $(BUILD_DIR) "
            "$(DEBUG_C_ENTRY_POINT)\n\n"
        )
        # Because the debug file contains the main for the code, we may compile
        # the ELF directly. We include a third rule for this purpose.
        source_code += (
            "$(DEBUG_ELF_ENTRY_POINT): $(DEBUG_ENTRY_POINT) $(ALL_DEST)\n"
            "\t$(CC) $(CFLAGS) -o $(DEBUG_ELF_ENTRY_POINT) "
            "$(DEBUG_ENTRY_POINT) $(ALL_DEST)\n\n"
        )

    # We return the prepared source code.
    return source_code


def build_module_rules(modules: Dict[str, List[str]]) -> str:
    """
    Adds a Makefile snippet with the rules to compile all the required modules.
    """
    source_code = ""
    # We add rules for the modules, one by one.
    for source_module, instances in modules.items():
        # Each module might need to be compiled to several instances.
        for instance in instances:
            # Alias to the C IR.
            c_alias = f"DEST_C_{instance.upper()}"
            # Alias to the compiled object file.
            object_alias = f"DEST_{instance.upper()}"
            # Alias to the compass source file.
            compass_alias = f"SRC_{source_module.upper()}"
            # We add a rule to compile the C code for the module from the compass
            # source code.
            source_code += (
                f"$({c_alias}): $({compass_alias}) $(BUILD_DIR)\n"
                f"\tcompass -r {instance} -o $({c_alias}) --lang C "
                f"$({compass_alias})\n\n"
            )
            # We add a second rule to make the object file from the C intermediate
            # representation.
            source_code += (
                f"$({object_alias}): $({c_alias}) $(BUILD_DIR)\n"
                f"\t$(CC) $(COMPASS_FLAGS) -o $({object_alias}) $({c_alias})\n\n"
            )
    # We return the prepared Makefile snippet.
    return source_code


def build_clean_rule() -> str:
    """
    Builds the Makefile snippet for the "clean" rule of the project.
    """
    # We return the simple snippet for the clean rule.
    return (
        "clean:\n"
        "\trm -f $(ALL_DEST) $(ALL_DEST_C) $(HEAD_ENTRY_POINT) "
        "$(DEBUG_ENTRY_POINT) $(DEBUG_C_ENTRY_POINT)\n\n"
    )


##################################### MAIN #####################################

if __name__ == "__main__":
    # The code to run when this file is used as a script goes here
    pass

##################################### EOF ######################################
