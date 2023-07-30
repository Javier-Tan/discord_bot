
import discord
import yt_dlp
import asyncio
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth

async def is_connected(ctx):
        voice_client = discord.utils.get(ctx.bot.voice_clients, guild = ctx.guild)
        return voice_client and voice_client.is_connected()

async def join(vc, ctx):
        ''' Returns channel to be joined '''
        await vc.connect()
        await ctx.send(f"I'm chilling in **{vc}** now")

yt_dlp.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, loop=None):
        loop = loop or asyncio.get_event_loop()    
        with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
            if not url.startswith("https://"):
                url = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]['webpage_url']
            info = ydl.extract_info(url, download=False)
            audio_url = info['formats'][8]['url']
            title = info['title']
        return [audio_url, title]

