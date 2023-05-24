# Developers notes
This project was tested using Python 3.10 using a Python virtual environment ('venv'). It makes use of a Python API wrapper for Discord, [Discord.py](https://discordpy.readthedocs.io/en/stable/index.html).

## Getting started

### Token storage
For the bot to come online, create a `.env` file with property `DISCORD_TOKEN={your_bot_token}`, do not push this, the file will (should) be gitignored. Double check before pushing to a public repository at your own risk.

If you have have not created a bot token, read more about creating your bot and token [here](https://discordpy.readthedocs.io/en/stable/discord.html).

### venv
It is highly recommended to develop in a venv to contain the projects required dependencies.

A bash script has been made to setup the virtual environment on linux, simply run `source _setup_venv.sh`

A windows script has been made to setup the virtual environment, simply run `_setup_windows_venv.bat`

### Starting the bot
A Dockerfile is provided for local development or running your bot locally (requires [Docker Desktop](https://www.docker.com/products/docker-desktop/))

To build docker image, run command
```
docker build -t discord_bot .
```

To run docker image (named discord_bot), run command
```
docker run -d discord_bot
```

Not recommended, but alternatively, run the bot locally from the home directory with the command:
```
python -m discord_bot
```

## Structure
This bot makes use of discord.py's "cog" feature to group related commands.

Each cog has a related "commands" file that provides the logic behind each implemented command, allowing for unit testing of each command.

`__main__.py` contains the logic to add all cogs to the bot and bring the bot online when run.

## Testing
Each command file has it's own testing file, and each command should be tested (expected result and expected exceptions)

Run the tests through `python -m pytest tests/` or vscode's testing functionality

## Deployment
### Github actions
Currently github actions only runs (and fails/passes according to) our unit tests.

