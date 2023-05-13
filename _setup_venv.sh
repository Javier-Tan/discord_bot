#!/bin/bash

# Create python 3.10 virtual environment
python3.10 -m venv .venv

# Activate virtual environment.
. .venv/bin/activate

# Pip install required files
pip install -r requirements.txt