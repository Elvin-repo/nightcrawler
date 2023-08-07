#!/bin/bash

# Specify the desired name for the virtual environment folder
venv_name="venv"

# Check if the virtual environment already exists
if [ ! -d "$venv_name" ]; then
    # Create a new virtual environment
    python -m venv "$venv_name"
    echo "Virtual environment created at: $venv_name"
else
    echo "Virtual environment already exists at: $venv_name"
fi

# Activate the virtual environment based on the OS
if [ "$OSTYPE" == "msys" ]; then  # Windows using Git Bash or MinGW
    source "$venv_name/Scripts/activate"
elif [ "$OSTYPE" == "cygwin" ]; then  # Windows using Cygwin
    source "$venv_name/Scripts/activate"
else  # macOS and Linux
    source "$venv_name/bin/activate"
fi

# Install requirements.txt
pip install -r requirements.txt

# Install requirements-dev.txt
pip install -r requirements-dev.txt
