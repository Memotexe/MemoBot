import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import os
import time
import asyncio
import time
from itertools import cycle

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="?", help_command=None)
status = ["Hello! I'm MemoBot!", "Type ?Help For Commands!"]

@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Game('Type ?Help For Commands'))
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

bot.run(DISCORD_TOKEN)
