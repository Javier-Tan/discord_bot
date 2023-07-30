import logging
import discord
from discord.ext import commands
from discord_bot.commands.volleyball_commands import *
from discord_bot.exceptions.volleyball_exceptions import ImageNotFoundException, DateNotFoundException

class volleyball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vb_fixtures(self, ctx):
        ''' Scrapes volleyball league website for fixture details '''
        logging.info('Volleyball fixture command requested.')
        try:
            imgid = "image31"
            dateid = "text17"
            response = await vb_fixtures(imgid, dateid)
            await ctx.send(response)
        except (ImageNotFoundException, DateNotFoundException) as e:
            await ctx.send(e.message)
            raise e

    @commands.command()
    async def vb_ranking(self, ctx):
        ''' Scrapes volleyball league website for ranking details '''
        logging.info('Volleyball ranking command requested.')
        try:
            imgid = "image37"
            dateid = "text12"
            response = await vb_ranking(imgid, dateid)
            await ctx.send(response)
        except (ImageNotFoundException, DateNotFoundException) as e:
            await ctx.send(e.message)
            raise e
        
async def setup(bot):
    await bot.add_cog(volleyball(bot))