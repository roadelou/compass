# Compass

> Disclaimer: This is a personal side-project

__Compass__ :compass: is a small programming language with strong inpiration from [Esterel](https://en.wikipedia.org/wiki/Esterel). It is a _synchronous programming language_ meant to build finite state machines easily for your C code.

Unlike Esterel, Compass is very bare bones and uses a rather trivial compilation process, which can lead to very different behaviours for code that looks similar.

The __ABRO__ code example adapted for Compass looks like:

```
module abro(input A, input B, input R, output O)
    each R seq {
        par {
            await A;
            await B;
        };
        emit O;
    }
endmodule
```

# Installation

The Compass compiler is distributed as a Python source package. To install it, one can run:

```bash
# Fetch the source code
git clone https://github.com/roadelou/compass.git
# Go into the repository
cd compass
# Install the python package
pip3 install .
``` 

A [PyPi package](https://pypi.org/project/roadelou-compass/) is also available for the compiler, and it can be installed with `pip3 install roadelou-compass` :tada:

# Usage

Once the compiler is installed, it can be used from the terminal through the `compass` command. Basic usage is:

```bash
# This will output a C file called abro_compass.c
compass abro.cmps
# To compile the header file to use the C code
compass --lang header abro.cmps
# To compile a CLI interface to test the module
compass --lang debug abro.cmps
```

# Examples

Some examples of the language can be found in the [examples](https://github.com/roadelou/compass/tree/master/examples) folder.

# Compass Builder

__Compass Builder__ is a small tool provided by the package to automate the compilation of projects with submodules. It takes a _JSON_ file describing the project as input and outputs a _Makefile_ to automate the compilation of the project.

:bulb: For an example JSON description of a project, see [cascade_abro.json](https://github.com/roadelou/compass/tree/master/examples/cascade_abro.json).

Basic usage of compass-builder is:

```bash
# Creates a Makefile from the description given in project.json
compass-builder project.json Makefile
```

# Features

The version of compass in the repository supports:

 - `input` and `output` signals
 - `local` variables
 - `each`, `par`, `seq`, `await` and `emit` statements
 - Conditional tests with `if`, `elif`, `else` and `endif`
 - The ability to use submodules within a module with the `extern` and `submodule` keywords
 - Many C-inspired operators for expressions

:warning: Be careful about the syntax for end-of lines. The `;` operator should only be used to separate several statements in a list of statements, i.e. only in `seq` and `par` blocks. The last `;` is optional by the way.

### METADATA

Field | Value
--- | ---
:pencil: Contributors | roadelou
:email: Contacts | 
:date: Creation Date | 2021-03-12
:bulb: Language | Markdown Document

### EOF
