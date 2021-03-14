# Compass

> Disclaimer: This is a personal side-project

__Compass__ :compass: is a small programming language with strong inpiration from [Esterel](https://en.wikipedia.org/wiki/Esterel). It is a _synchronous programming language_ meant to build finite state machines easily for your C code.

Unlike Esterel, Compass is very bare bones and uses a rather trivial compilation process, which can lead to very different behaviours for code that looks similar.

The __ABRO__ code example adapted for Compass looks like :arrow_down_small:

```
module abro(input A, input B, input R, output O) {
    each R {
        seq {
            par {
                await A;
                await B;
            };
            emit O;
        }
    }
}
```

# Installation

The Compass compiler is distributed as a Python source package. To install it, one can run :arrow_down_small:

```bash
# Fetch the source code
git clone https://github.com/roadelou/compass.git
# Go into the repository
cd compass
# Install the python package
pip3 install .
``` 

A [PyPi package](https://pypi.org/project/roadelou-compass/) is also available for the compiler, and it can be installed with `pip3 install roadelou_compass` :tada:

# Usage

Once the compiler is installed, it can be used from the terminal through the `compass` command. Basic usage is :arrow_down_small:

```bash
# This will output a C file called abro_compass.c
compass abro.cmps
# To compile the header file to use the C code
compass --lang header abro.cmps
# To compile a CLI interface to test the module
compass --lang debug abro.cmps
```

# Examples

Some examples of the language can be found in the [examples](https://github.com/roadelou/compass/examples) folder.

# Features

This section details what language features are currently available in __compass__ :compass: and which ones are planned.

## Current features

The version of compass in the repository supports:

 - Input and output signals
 - `each`, `par`, `seq`, `await` and `emit` statements
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
