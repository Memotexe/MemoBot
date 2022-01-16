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
import random

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
    await channel.send('Welcome {member.mention} See `!Help` command for details!')

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 870847081210843167:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == 'licker':
            role = discord.utils.get(guild.roles, name='NSFW')
        elif payload.emoji.name == 'chieflookup':
            role = discord.utils.get(guild.roles, name='Halo')
        elif payload.emoji.name == 'bob':
            role = discord.utils.get(guild.roles, name='Runescape')
        elif payload.emoji.name == 'minecraft_bounce':
            role = discord.utils.get(guild.roles, name='Minecraft')
        elif payload.emoji.name == 'aSDVstardrop':
            role = discord.utils.get(guild.roles, name='Stardew Valley')
        elif payload.emoji.name == 'switch':
            role = discord.utils.get(guild.roles, name='Nintendo')
        elif payload.emoji.name == '❤️':
            role = discord.utils.get(guild.roles, name='Red')
        elif payload.emoji.name == '💙':
            role = discord.utils.get(guild.roles, name='Blue')
        elif payload.emoji.name == '🤎':
            role = discord.utils.get(guild.roles, name='Brown')
        elif payload.emoji.name == '💛':
            role = discord.utils.get(guild.roles, name='Yellow')
        elif payload.emoji.name == '💚':
            role = discord.utils.get(guild.roles, name='Green')
        elif payload.emoji.name == '🤍':
            role = discord.utils.get(guild.roles, name='White')
        elif payload.emoji.name == '💜':
            role = discord.utils.get(guild.roles, name='Purple')
        elif payload.emoji.name == '🧡':
            role = discord.utils.get(guild.roles, name='Orange')
        elif payload.emoji.name == '🖤':
            role = discord.utils.get(guild.roles, name='Black')
        elif payload.emoji.name == 'pink_heart':
            role = discord.utils.get(guild.roles, name='Pink')
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

        if payload.emoji.name == 'licker':
            role = discord.utils.get(guild.roles, name='NSFW')
        elif payload.emoji.name == 'chieflookup':
            role = discord.utils.get(guild.roles, name='Halo')
        elif payload.emoji.name == 'bob':
            role = discord.utils.get(guild.roles, name='Runescape')
        elif payload.emoji.name == 'minecraft_bounce':
            role = discord.utils.get(guild.roles, name='Minecraft')
        elif payload.emoji.name == 'aSDVstardrop':
            role = discord.utils.get(guild.roles, name='Stardew Valley')
        elif payload.emoji.name == 'switch':
            role = discord.utils.get(guild.roles, name='Nintendo')
        elif payload.emoji.name == '❤️':
            role = discord.utils.get(guild.roles, name='Red')
        elif payload.emoji.name == '💙':
            role = discord.utils.get(guild.roles, name='Blue')
        elif payload.emoji.name == '🤎':
            role = discord.utils.get(guild.roles, name='Brown')
        elif payload.emoji.name == '💛':
            role = discord.utils.get(guild.roles, name='Yellow')
        elif payload.emoji.name == '💚':
            role = discord.utils.get(guild.roles, name='Green')
        elif payload.emoji.name == '🤍':
            role = discord.utils.get(guild.roles, name='White')
        elif payload.emoji.name == '💜':
            role = discord.utils.get(guild.roles, name='Purple')
        elif payload.emoji.name == '🧡':
            role = discord.utils.get(guild.roles, name='Orange')
        elif payload.emoji.name == '🖤':
            role = discord.utils.get(guild.roles, name='Black')
        elif payload.emoji.name == 'pink_heart':
            role = discord.utils.get(guild.roles, name='Pink')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        print("Role Removed:")
        print(role)
        
        if role is not None:
            member = await(await bot.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            print("Member Removed:")
            print(member)
            
            if member is not None:
                await member.remove_roles(role)
                print("Done")
            else:
                print("Member Not Found.")
        else:
            print("Role Not Found.")

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    authors = {}
    async for message in ctx.channel.history(limit=amount + 1):
        if message.author not in authors:
            authors[message.author] = 1
        else:
            authors[message.author] += 1
        await message.delete()

    msg = "I took out the trash for you!"
    await ctx.channel.send(msg)   

@bot.command(name="d20")
async def rng(ctx):
    randomNum = random.randint(1,20)
    if randomNum == 1:
        await ctx.channel.send(str(randomNum) + " Critical Fail! <a:F_:925511019655200841>")
    elif randomNum <= 10 and randomNum > 1:
        await ctx.channel.send(str(randomNum) + " Yikes! Thats not a good role <:tanjiroD:925511021261631528>")
    elif randomNum >=11 and randomNum < 20:
        await ctx.channel.send(str(randomNum) + " Ok! Thats a good role <a:gachi:926278637341245471>")
    elif randomNum == 20:
        await ctx.channel.send(str(randomNum) + " LETS GOO! CRITICAL ROLE! <a:gachihyperclap:890777869360431104>")
        
    
@bot.command(name="sus")
async def sus(ctx):
    randomNum = random.randint(1,11)
    await ctx.channel.send(file = discord.File("Sus Folder\sus"+str(randomNum)+".gif"))
    

@bot.command(name="headpat")
async def headpat(ctx):
    randomNum = random.randint(1,11)
    await ctx.channel.send(file = discord.File("Head Pats\hp"+str(randomNum)+".gif"))
    
 
    
bot.run(DISCORD_TOKEN)
