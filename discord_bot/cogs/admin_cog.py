import logging
import discord
from discord.ext import commands
from discord_bot.commands.admin_commands import admin_commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        ''' Logs when the bot is online '''
        logging.debug("Bot is online.")

    @commands.command()
    async def ping(self, ctx):
        ''' Responds with pong, used to check if bot is functional '''
        logging.info('Ping command executed.')
        response = await admin_commands.ping()
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(admin(bot))