# Starting from python3.9
FROM python:3.9

# Using the recommended installation path
WORKDIR /usr/src/app
# Copying the source code to the docker container
COPY . .
# Installing compass as a package
RUN pip3 install .
# Going back to the HOME for any manipulations the user could desire...
WORKDIR /root
