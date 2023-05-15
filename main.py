# Dependencies
import asyncio
import discord
import os
import sys
from dotenv import load_dotenv
from discord.ext import commands

COMMAND_PREFIX = '!'
# Loads environmental variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = COMMAND_PREFIX, intents = intents, help_command = commands.DefaultHelpCommand())

# Load all cogs
async def load():
    for filename in os.listdir('discord_bot/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'discord_bot.cogs.{filename[:-3]}')

# Start the bot
async def main():
    await load()
    await bot.start(TOKEN)

if __name__ == "__main__":
    # Setup logging
    import logging

    file_handler = logging.FileHandler(filename='tmp.log')
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    handlers = [file_handler, stdout_handler]

    logging.basicConfig(
        level=logging.INFO, 
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        handlers=handlers
    )

    # Execute main
    asyncio.run(main())