import asyncio
import discord
import logging
import os
from dotenv import load_dotenv
from discord.ext import commands

# Loads environmental variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = '!'

handler = logging.FileHandler(filename = 'bot.log', encoding = 'utf-8', mode = 'w')

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = COMMAND_PREFIX, intents = intents, help_command = commands.MinimalHelpCommand())

# Load all cogs
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

# Start the bot
async def main():
    await load()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())