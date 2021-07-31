import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import os
import time
import asyncio
import time
from itertools import cycle
import youtube_dl

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="?", help_command=None)
status = ["Hello! I'm MemoBot!", "Type ?Help For Commands!"]

@bot.event
async def on_ready():
    print("This lil Bob-omb is ready to assist!")
    bot.loop.create_task(change_status())


async def change_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Hello! Im Memobot!'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Type ?Help For Commands'))
        await asyncio.sleep(10)

@bot.command(name='Help')
async def help_command(ctx):
    await ctx.channel.send("Help")



@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'Stop' Command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Bot')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not pause.")

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@bot.event()
async def on_raw_reaction_add(payload):
    

bot.run(DISCORD_TOKEN)
