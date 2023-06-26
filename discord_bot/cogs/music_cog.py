import logging
import discord
from discord.ext import commands
from discord_bot.commands.music_commands import *
import yt_dlp
import nacl
import ffmpeg
import asyncio

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.is_playing = False

    @commands.command()
    async def play(self, ctx, search):
        ''' Queues songs by URL '''
        logging.info("play command invoked")
        isconnected = await is_connected(ctx)
        if not isconnected:
            if (ctx.message.author.voice == None): # raise a custom exception
                await ctx.send("Go join a channel first")
                logging.info('User was not in voice channel when invoking bot join')
                return
            else:
                vc = ctx.message.author.voice.channel
                await join(vc, ctx)

        [filename, title] = await YTDLSource.from_url(search, loop=self.bot.loop)
        self.queue.append(filename)
        vc = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if not vc.is_playing():
            vc.play(discord.FFmpegPCMAudio(source=self.queue[0]), after=lambda e: self.play_next(self, ctx))
        
        outputstring = filename.split("[")[0]
        await ctx.send("Queued " + title)

    def play_next(self, ctx, song):
        ''' play music until queue is empty'''
        if len(self.queue) >= 1:
            del self.queue[0]
            vc = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            vc.play(discord.FFmpegPCMAudio(source=song), after=lambda e: self.play_next(self, ctx))
            asyncio.run_coroutine_threadsafe(ctx.send("No more songs in queue."), self.bot.loop)
            
    
    @commands.command()
    async def disconnect(self, ctx):
        ''' Disconnect bot'''
        isconnected = await is_connected(ctx)
        if(not isconnected): # raise custom exception
            await ctx.send("I'm not in a channel...")
            logging.info('Bot was already disconnected when disconnect command invoked')
            return
        else:
            await ctx.send("Oyasumi")
            voice_channel = ctx.message.guild.voice_client
            await voice_channel.disconnect()
            self.queue = []

    @commands.command()
    async def test(self, ctx):
        await ctx.send("TESTING")


async def setup(bot):
    await bot.add_cog(music(bot))