import logging
import discord
from discord.ext import commands
from discord_bot.commands.music_commands import *
from discord_bot.exceptions.music_exceptions import BotNotInChannelException, UserNotInChannelException, NotPlayingAudioException, InvalidNumberException

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.isLooping = "none"
        self.playlist = []

    @commands.command()
    async def play(self, ctx, *, search):
        ''' Queue song'''
        logging.info("play command invoked")

        # connect bot into channel of user
        isconnected = await is_connected(ctx)
        if not isconnected:
            try:
                if (ctx.message.author.voice == None):
                    raise UserNotInChannelException()
                
                vc = ctx.message.author.voice.channel
                await join(vc, ctx)
            except UserNotInChannelException as e:
                await ctx.send("I can't play to an empty crowd. Go join a channel first")
                logging.info(e.message)
                return

        # obtain audio url
        file = await YTDLSource.from_url(search, loop=self.bot.loop)
        
        vc = ctx.voice_client

        # queue song
        self.queue.append(file)
        logging.info("Queued " + file[1])
        await ctx.send("Queued " + file[1])

        # immediately play song if bot is not currently playing audio
        if not vc.is_playing():
            logging.info("Playing: " + file[1])
            vc.play(discord.FFmpegPCMAudio(source=file[0], before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",options="-vn"), after=lambda x=None: self.play_next(ctx = ctx))
            

    def play_next(self, ctx):
        ''' play music until queue is empty '''
        logging.info("play_next command invoked")
        if len(self.queue) > 1:
            if self.isLooping == "none":
                self.queue.pop(0)
            elif self.isLooping == "playlist":
                playlistsong = self.queue.pop(0)
                self.playlist.append(playlistsong)
            song = self.queue[0]
            vc = ctx.guild.voice_client
            logging.info("Playing: " + song[1])
            vc.play(discord.FFmpegPCMAudio(source=song[0], before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",options="-vn"), after = lambda x=None: self.play_next(ctx = ctx))
        else:
            if self.isLooping == "none":
                self.queue.pop(0)
            else:
                if self.isLooping == "playlist":
                    logging.info("Playlist looped")
                    playlistsong = self.queue.pop(0)
                    self.playlist.append(playlistsong)
                    for track in self.playlist:
                        self.queue.append(track)
                song = self.queue[0]
                vc = ctx.guild.voice_client
                logging.info("Playing: " + song[1])
                vc.play(discord.FFmpegPCMAudio(source=song[0], before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",options="-vn"), after = lambda x=None: self.play_next(ctx = ctx))

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
            await ctx.send("Skip what?? There's nothing to skip")
            logging.info(e.message)
    
    @commands.command()
    async def disconnect(self, ctx):
        ''' Disconnect bot '''
        isconnected = await is_connected(ctx)
        try:
            if(not isconnected): 
                raise BotNotInChannelException()
            await ctx.send("Have fun sitting in silence")
            voice_channel = ctx.message.guild.voice_client
            await voice_channel.disconnect()
            self.queue = []
        except BotNotInChannelException as e:
            await ctx.send("I can't leave if I wasn't here in the first place")
            logging.info(e.message)         

    @commands.command()
    async def queue(self, ctx):
        ''' Display queue of songs '''
        if len(self.queue) == 0:
            await ctx.send("**Currently playing: Absolute Silence**")
            return
        output = ""
        for i in range(len(self.queue)):
            if i == 0:
                output += "**Currently playing: " + self.queue[i][1] + "**\n"
            else:
                output += str(i) + ". " + self.queue[i][1] + "\n"
        await ctx.send(output)

    @commands.command()
    async def remove(self, ctx, numstring):
        ''' Remove song from queue '''
        if(numstring == "all"):
            await ctx.send("Wiped entire queue")
            self.queue = [self.queue[0]]
            return

        num = int(numstring)
        try:
            if num <= 0 or num >= len(self.queue):
                raise InvalidNumberException()
            await ctx.send("Removed **" + numstring + ". " + self.queue[num][1] + "** from the queue")
            self.queue.pop(num)
        except InvalidNumberException as e:
            await ctx.send("There's no song queued up at that number...")
            logging.info(e.message)

    @commands.command()
    async def loop(self, ctx):
        if self.isLooping == "none":
            self.isLooping = "playlist"
            await ctx.send("Looping queue")
        elif self.isLooping == "playlist":
            self.isLooping = "song"
            self.playlist = []
            await ctx.send("Looping song")
        else:
            self.isLooping = "none"
            await ctx.send("No longer looping")
        logging.info("Loop toggle swapped")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("TESTING")

async def setup(bot):
    await bot.add_cog(music(bot))