# Developers notes

## Getting started
This project was tested using Python 3.10 using a Python virtual environment ('venv') and run with Visual Studio Code. 

A bash script has been made to setup the virtual environment on linux. 
```
source _setup_venv.sh
```

Run the bot from the home directory with the command
```
python3 main.py
```

## Structure
This bot makes use of discord.py's "cog" feature to group related commands. 

Each cog has a related "commands" file that provides the logic behind each implemented command, allowing for unit testing of each command.

## Testing
Run the tests through `python -m pytest tests/` or vscode's testing functionality