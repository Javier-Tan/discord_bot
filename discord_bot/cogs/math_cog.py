import logging
import discord
from discord.ext import commands
from discord_bot.commands.math_commands import math_commands

class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rng(self, ctx):
        ''' Returns a random integer between 1 and 100 inclusive '''

        logging.info('Random number generator command executed.')
        try:
            response = await math_commands.rng()
            await ctx.send(response)
        except Exception as e:
            await ctx.send("error")

async def setup(bot):
    await bot.add_cog(math(bot))