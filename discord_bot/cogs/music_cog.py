import logging
import discord
from discord.ext import commands
from discord_bot.commands.music_commands import *
import yt_dlp
import nacl
import ffmpeg
import asyncio
from discord_bot.exceptions.music_exceptions import BotNotInChannelException, UserNotInChannelException, NotPlayingAudioException

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
            try:
                if (ctx.message.author.voice == None):
                    raise UserNotInChannelException()
                
                vc = ctx.message.author.voice.channel
                await join(vc, ctx)
            except UserNotInChannelException as e:
                await ctx.send("Go join a channel first")
                logging.info(e.message)
                return

        file = await YTDLSource.from_url(search, loop=self.bot.loop)
        
        vc = ctx.voice_client

        if not vc.is_playing():
            logging.info("Playing: " + file[1])
            vc.play(discord.FFmpegPCMAudio(source=file[0]), after=lambda x=None: self.play_next(ctx = ctx))
        else:
            self.queue.append(file)
            await ctx.send("Queued " + file[1])

    def play_next(self, ctx):
        ''' play music until queue is empty '''
        logging.info("play_next command invoked")
        if len(self.queue) > 0:
            song = self.queue.pop(0)
            vc = ctx.guild.voice_client
            logging.info("Playing: " + song[1])
            vc.play(discord.FFmpegPCMAudio(source=song[0]), after = lambda x=None: self.play_next(ctx = ctx))
            
    @commands.command()
    async def skip(self, ctx):
        ''' skip current song '''
        logging.info("skip command invoked")
        vc = ctx.voice_client
        try:
            if not vc.is_playing():
                raise NotPlayingAudioException()
            vc.stop()
        except NotPlayingAudioException as e:
            await ctx.send("Not playing any music right now")
            logging.info(e.message)
            return

    
    @commands.command()
    async def disconnect(self, ctx):
        ''' Disconnect bot '''
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