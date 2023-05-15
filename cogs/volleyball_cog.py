import logging
import discord
from discord.ext import commands
from commands.volleyball_commands import volleyball_commands
from exceptions.volleyball_exceptions import ImageNotFoundException

class volleyball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vb_fixtures(self, ctx):
        ''' Scrapes volleyball league website for fixture image '''
        logging.info('Volleyball fixture command requested.')
        try:
            response = await volleyball_commands().fixtures()
            await ctx.send(response)
        except ImageNotFoundException as e:
            ctx.send(e.message)

    @commands.command()
    async def vb_ranking(self, ctx):
        ''' Scrapes volleyball league website for ranking image '''
        logging.info('Volleyball ranking command requested.')
        try:
            response = await volleyball_commands().ranking()
            await ctx.send(response)
        except ImageNotFoundException as e:
            ctx.send(e.message)
        
async def setup(bot):
    await bot.add_cog(volleyball(bot))