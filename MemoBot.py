import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import os
import time
import asyncio
import time
from itertools import cycle
from dotenv import load_dotenv
from discord.ext.commands import Bot
from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
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

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!", help_command=None)
status = ["Hello! I'm MemoBot!", "Type !Help For Commands!"]

@bot.event
async def on_ready():
    print("This lil Bob-omb is ready to assist!")
    bot.loop.create_task(change_status())


async def change_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Hello! Im Memobot!'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Type !Help For Commands'))
        await asyncio.sleep(10)


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `!Help` command for details!')


@bot.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=bot.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))

@bot.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()



@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 870847081210843167:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'mSwitch':
            role = discord.utils.get(guild.roles, name='Switch')
        elif payload.emoji.name == 'mPlayStation':
            role = discord.utils.get(guild.roles, name='PlayStation')
        elif payload.emoji.name == 'mPC':
            role = discord.utils.get(guild.roles, name='PC')
        elif payload.emoji.name == 'mXbox':
            role = discord.utils.get(guild.roles, name='Xbox')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Done")
            else:
                print("Member Not Found.")
        else:
            print("Role Not Found.")

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 870847081210843167:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'mSwitch':
            role = discord.utils.get(guild.roles, name='Switch')
        elif payload.emoji.name == 'mPlayStation':
            role = discord.utils.get(guild.roles, name='PlayStation')
        elif payload.emoji.name == 'mPC':
            role = discord.utils.get(guild.roles, name='PC')
        elif payload.emoji.name == 'mXbox':
            role = discord.utils.get(guild.roles, name='Xbox')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.remove_roles(role)
                print("Done")
            else:
                print("Member Not Found.")
        else:
            print("Role Not Found.")

@bot.command(name='clear')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Deleting %s Messages" %(amount))

    



bot.run(DISCORD_TOKEN)
