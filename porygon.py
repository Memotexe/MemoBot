from aiohttp import JsonPayload
import nextcord
from nextcord.ext import commands, tasks
from nextcord import member
from nextcord import Interaction
from nextcord import FFmpegPCMAudio
from contextlib import suppress
import json
import random
from datetime import date
import math, decimal, datetime
from stackapi import StackAPI
import pandas as pd

dec = decimal.Decimal

SERVERID= 869397848125485186

with open('discordToken.json','r') as discordFile:
    data=discordFile.read()

jsonObj = json.loads(data)
DISCORD_TOKEN = str(jsonObj['DiscordToken'])
client = commands.Bot(command_prefix="")


@client.event
async def on_ready():
    print("Porygon is up and running!")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name='Type /Help for Commands'))


# """
# .########..########....###.....######..########.####..#######..##....##....########...#######..##.......########
# .##.....##.##.........##.##...##....##....##.....##..##.....##.###...##....##.....##.##.....##.##.......##......
# .##.....##.##........##...##..##..........##.....##..##.....##.####..##....##.....##.##.....##.##.......##......
# .########..######...##.....##.##..........##.....##..##.....##.##.##.##....########..##.....##.##.......######..
# .##...##...##.......#########.##..........##.....##..##.....##.##..####....##...##...##.....##.##.......##......
# .##....##..##.......##.....##.##....##....##.....##..##.....##.##...###....##....##..##.....##.##.......##......
# .##.....##.########.##.....##..######.....##....####..#######..##....##....##.....##..#######..########.########
# """

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 870847081210843167:
        guild_id = payload.guild_id
        guild = nextcord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'licker':
            role = nextcord.utils.get(guild.roles, name='NSFW')
        elif payload.emoji.name == 'chieflookup':
            role = nextcord.utils.get(guild.roles, name='Halo')
        elif payload.emoji.name == 'bob':
            role = nextcord.utils.get(guild.roles, name='Runescape')
        elif payload.emoji.name == 'minecraft_bounce':
            role = nextcord.utils.get(guild.roles, name='Minecraft')
        elif payload.emoji.name == 'aSDVstardrop':
            role = nextcord.utils.get(guild.roles, name='Stardew Valley')
        elif payload.emoji.name == 'switch':
            role = nextcord.utils.get(guild.roles, name='Nintendo')
        elif payload.emoji.name == '❤️':
            role = nextcord.utils.get(guild.roles, name='Red')
        elif payload.emoji.name == '💙':
            role = nextcord.utils.get(guild.roles, name='Blue')
        elif payload.emoji.name == '🤎':
            role = nextcord.utils.get(guild.roles, name='Brown')
        elif payload.emoji.name == '💛':
            role = nextcord.utils.get(guild.roles, name='Yellow')
        elif payload.emoji.name == '💚':
            role = nextcord.utils.get(guild.roles, name='Green')
        elif payload.emoji.name == '🤍':
            role = nextcord.utils.get(guild.roles, name='White')
        elif payload.emoji.name == '💜':
            role = nextcord.utils.get(guild.roles, name='Purple')
        elif payload.emoji.name == '🧡':
            role = nextcord.utils.get(guild.roles, name='Orange')
        elif payload.emoji.name == '🖤':
            role = nextcord.utils.get(guild.roles, name='Black')
        elif payload.emoji.name == 'pink_heart':
            role = nextcord.utils.get(guild.roles, name='Pink')
        else:
            role = nextcord.utils.get(guild.roles, name = payload.emoji.name)
       
        if role is not None:
            member = payload.member
         
            if member is not None:
                await member.add_roles(role)
                print("Done")
            else:
                print("Member Not Found.")
        else:
            print("Role Not Found.")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 870847081210843167:
        guild_id = payload.guild_id
        guild = nextcord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'licker':
            role = nextcord.utils.get(guild.roles, name='NSFW')
        elif payload.emoji.name == 'chieflookup':
            role = nextcord.utils.get(guild.roles, name='Halo')
        elif payload.emoji.name == 'bob':
            role = nextcord.utils.get(guild.roles, name='Runescape')
        elif payload.emoji.name == 'minecraft_bounce':
            role = nextcord.utils.get(guild.roles, name='Minecraft')
        elif payload.emoji.name == 'aSDVstardrop':
            role = nextcord.utils.get(guild.roles, name='Stardew Valley')
        elif payload.emoji.name == 'switch':
            role = nextcord.utils.get(guild.roles, name='Nintendo')
        elif payload.emoji.name == '❤️':
            role = nextcord.utils.get(guild.roles, name='Red')
        elif payload.emoji.name == '💙':
            role = nextcord.utils.get(guild.roles, name='Blue')
        elif payload.emoji.name == '🤎':
            role = nextcord.utils.get(guild.roles, name='Brown')
        elif payload.emoji.name == '💛':
            role = nextcord.utils.get(guild.roles, name='Yellow')
        elif payload.emoji.name == '💚':
            role = nextcord.utils.get(guild.roles, name='Green')
        elif payload.emoji.name == '🤍':
            role = nextcord.utils.get(guild.roles, name='White')
        elif payload.emoji.name == '💜':
            role = nextcord.utils.get(guild.roles, name='Purple')
        elif payload.emoji.name == '🧡':
            role = nextcord.utils.get(guild.roles, name='Orange')
        elif payload.emoji.name == '🖤':
            role = nextcord.utils.get(guild.roles, name='Black')
        elif payload.emoji.name == 'pink_heart':
            role = nextcord.utils.get(guild.roles, name='Pink')
        else:
            role = nextcord.utils.get(guild.roles, name = payload.emoji.name)

        print("Role Removed:")
        print(role)
        
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            print("Member Removed:")
            print(member)
            
            if member is not None:
                await member.remove_roles(role)
                print("Done")
            else:
                print("Member Not Found.")
        else:
            print("Role Not Found.")

# """
# .########.....###....##....##.########...#######..##.....##.......##.##.....##.########.##.....##.########..######.
# .##.....##...##.##...###...##.##.....##.##.....##.###...###......##..###...###.##.......###...###.##.......##....##
# .##.....##..##...##..####..##.##.....##.##.....##.####.####.....##...####.####.##.......####.####.##.......##......
# .########..##.....##.##.##.##.##.....##.##.....##.##.###.##....##....##.###.##.######...##.###.##.######....######.
# .##...##...#########.##..####.##.....##.##.....##.##.....##...##.....##.....##.##.......##.....##.##.............##
# .##....##..##.....##.##...###.##.....##.##.....##.##.....##..##......##.....##.##.......##.....##.##.......##....##
# .##.....##.##.....##.##....##.########...#######..##.....##.##.......##.....##.########.##.....##.########..######.
# """

@client.slash_command(guild_ids=[SERVERID], description="Rolls a Digital Dice for you! Choose between 3,6 ,8 ,10 ,12 , and 20")
async def dice(interaction:Interaction, arg):
    
    if(arg == "20"):
        randomNum = random.randint(1,20)
        if randomNum == 1:
            await interaction.response.send_message(str(randomNum) + ": Critical Fail! <a:F_:925511019655200841>")
        elif randomNum <= 10 and randomNum > 1:
            await interaction.response.send_message(str(randomNum) + ": Thats not a good roll <:tanjiroD:925511021261631528>")
        elif randomNum >=11 and randomNum < 20:
            await interaction.response.send_message(str(randomNum) + ": Thats a good roll <a:gachi:926278637341245471>")
        elif randomNum == 20:
            await interaction.response.send_message(str(randomNum) + ": CRITICAL ROLL! <a:gachihyperclap:890777869360431104>")
    elif(arg == "3"):
        randomNum = random.randint(1,3)
        if randomNum == 1:
            await interaction.response.send_message(str(randomNum) + ": OOF! Thats a 1 <a:F_:925511019655200841>")
        elif randomNum == 2:
            await interaction.response.send_message(str(randomNum) + ": I mean 2 is greater than 1 <a:gachi:926278637341245471>")
        elif randomNum == 3:
            await interaction.response.send_message(str(randomNum) + ": WOOOO BABY! THATS WHAT IM TALKING ABOUT! <a:gachihyperclap:890777869360431104>")
    elif(arg == "6"):
        randomNum = random.randint(1,6)
        if randomNum == 1:
            await interaction.response.send_message(str(randomNum) + ": A 1 on a 6 sided dice? yikes... <a:F_:925511019655200841>")
        elif randomNum >=2 and randomNum <= 5:
            await interaction.response.send_message(str(randomNum) + ": Your roll was... average I guess <:tanjiroD:925511021261631528>")
        elif randomNum == 6:
            await interaction.response.send_message(str(randomNum) + ": HIGHEST ROLL! <a:gachihyperclap:890777869360431104>")
    elif(arg == "8"):
        randomNum = random.randint(1,8)
        if randomNum == 1:
            await interaction.response.send_message(str(randomNum) + ": How do i explain this... Your roll sucked <a:F_:925511019655200841>")
        elif randomNum >=2 and randomNum <= 7:
            await interaction.response.send_message(str(randomNum) + ": cool, not perfect but not awful! <:tanjiroD:925511021261631528>")
        elif randomNum == 8:
            await interaction.response.send_message(str(randomNum) + ": if thats for damage, Good roll! <a:gachihyperclap:890777869360431104>")
    elif(arg == "10"):
        randomNum = random.randint(0,9)
        if randomNum == 0:
            await interaction.response.send_message(str(randomNum) + ": You got a 0, like, if there was negative numbers. You would have probably gotten that. <a:F_:925511019655200841>")
        elif randomNum >=1 and randomNum <= 8:
            await interaction.response.send_message(str(randomNum) + ": good! You didnt fail, but... whats this dice even for? <:tanjiroD:925511021261631528>")
        elif randomNum == 9:
            await interaction.response.send_message(str(randomNum) + ": Aye, thats a 9! That will do something good... right? <a:gachihyperclap:890777869360431104>")
    elif(arg == "12"):
        randomNum = random.randint(1,12)
        if randomNum == 1:
            await interaction.response.send_message(str(randomNum) + ": The return of 1! You might as well put the dice in jail right <a:F_:925511019655200841>")
        elif randomNum >=2 and randomNum <= 11:
            await interaction.response.send_message(str(randomNum) + ": hopefully this is in your favor! <:tanjiroD:925511021261631528>")
        elif randomNum == 12:
            await interaction.response.send_message(str(randomNum) + ": You got a 12, do you want praise? go somewhere else <a:gachihyperclap:890777869360431104>")
    else:
        await interaction.response.send_message("Please choose from the options here for dice to roll: 3,6,8,10,12,20")

@client.slash_command(guild_ids=[SERVERID], description="Only a Friday Thing")
async def friday(interaction: Interaction, member: nextcord.Member):
    with suppress(Exception):
        if date.today().isoweekday() == 5:
            try:
                channel = member.voice.channel
                if channel:
                    voice = await channel.connect()
                    source = FFmpegPCMAudio('friday.mp3')
                    voice.play(source)
                    await interaction.response.send_message("ITS FRIDAY BABY! WOOOOO!")
            finally:
                await interaction.response.send_message("You're not in a VC")
        else:
            await interaction.response.send_message("It's Not Friday!")

@client.slash_command(guild_ids=[SERVERID], description="I'll never give you up!")
async def riro(interaction: Interaction, member: nextcord.Member):
            now = datetime.datetime.now()
            diff = now - datetime.datetime(2001, 1, 1)
            days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
            lunations = dec("0.20439731") + (days * dec("0.03386319269"))
            pos = lunations % dec(1)
            index = (pos * dec(8)) + dec("0.5")
            index = math.floor(index)
            if index == 4:
                try:
                    channel = member.voice.channel
                    if channel:
                        voice = await channel.connect()
                        source = FFmpegPCMAudio('never.mp3')
                        voice.play(source)
                        await interaction.response.send_message(f"{member} just got memed <a:gachihyperclap:890777869360431104>")
                finally:
                    await interaction.response.send_message("You're not in a VC")
       
            await interaction.response.send_message("Now is not the time. Try again later, maybe when the stars allign?")

@client.event
async def on_message(message):
    partyChance =random.randint(0,100)
    if "party" in message.content and partyChance == 69:
        await message.channel.send("Did someone say party!?",file=nextcord.File('party.mp4'))


# """
# .##.....##.##.....##..######..####..######.
# .###...###.##.....##.##....##..##..##....##
# .####.####.##.....##.##........##..##......
# .##.###.##.##.....##..######...##..##......
# .##.....##.##.....##.......##..##..##......
# .##.....##.##.....##.##....##..##..##....##
# .##.....##..#######...######..####..######.
# """

@client.slash_command(guild_ids=[SERVERID], description="Plays Lofi! Options: Pokemon, Japan, Morning, Coding")
async def lofi(interaction:Interaction , arg):
    with suppress(Exception):
        channel = client.get_channel(939788377732050945)
        if(arg.lower() == "japan"):
            voice = await channel.connect()
            source = FFmpegPCMAudio('japanLofi.mp3')
            voice.play(source)
            await interaction.response.send_message("Now playing Japan Lofi")
        elif(arg.lower() == "morning"):
            voice = await channel.connect()
            source = FFmpegPCMAudio('morningLofi.mp3')
            voice.play(source)
            await interaction.response.send_message("Now playing Morning Lofi")
        elif(arg.lower() == "pokemon"):
            voice = await channel.connect()
            source = FFmpegPCMAudio('pokemonLofi.mp3')
            voice.play(source)
            await interaction.response.send_message("Now playing Pokemon Lofi")
        elif(arg.lower() == "coding"):
            voice = await channel.connect()
            source = FFmpegPCMAudio('codingLofi.mp3')
            voice.play(source)
            await interaction.response.send_message("Now playing Coding Lofi")
        else:
            await interaction.response.send_message("Please choose a valid option") 


@client.slash_command(guild_ids=[SERVERID], description="Tells the Bot to Leave the Lofi VC")
async def leave(interaction: Interaction):
    with suppress(Exception):
        try:
            if(interaction.guild.voice_client):
                await interaction.guild.voice_client.disconnect()
                await interaction.response.send_message("goodbye")
        finally:
            await interaction.response.send_message("I'm not in a VC")

@client.slash_command(guild_ids=[SERVERID], description="Tells the Bot to Pause the Lofi")
async def pause(interaction: Interaction):
    voice = nextcord.utils.get(client.voice_clients,guild=interaction.guild)
    with suppress(Exception):
        try:
            if voice.is_playing():
                voice.pause()
                await interaction.response.send_message("paused")
        finally:
            await interaction.response.send_message("Sorry, but no music is playing.")

@client.slash_command(guild_ids=[SERVERID], description="Tells the Bot to Resume the Lofi")
async def resume(interaction: Interaction):
    voice = nextcord.utils.get(client.voice_clients,guild=interaction.guild)
    with suppress(Exception):
        try:
            if voice.is_paused():
                voice.resume()
                await interaction.response.send_message("resumed")
        finally:
            await interaction.response.send_message("Sorry, but there is no paused music.") 
 

# """
# .##.....##..#######..########..########.########.....###....########.####..#######..##....##
# .###...###.##.....##.##.....##.##.......##.....##...##.##......##.....##..##.....##.###...##
# .####.####.##.....##.##.....##.##.......##.....##..##...##.....##.....##..##.....##.####..##
# .##.###.##.##.....##.##.....##.######...########..##.....##....##.....##..##.....##.##.##.##
# .##.....##.##.....##.##.....##.##.......##...##...#########....##.....##..##.....##.##..####
# .##.....##.##.....##.##.....##.##.......##....##..##.....##....##.....##..##.....##.##...###
# .##.....##..#######..########..########.##.....##.##.....##....##....####..#######..##....##
# """

@client.slash_command(guild_ids=[SERVERID], description="Clears Messages based on amount given")
@commands.has_permissions(manage_messages=True)
async def purge(interaction: Interaction, amount: int):
    await interaction.channel.purge(limit = amount)
    await interaction.response.send_message(f"Trash was taken out. {amount} messages deleted")

#CHECK FOR UNWELCOME PROFANITY
#ENHANCE BAN OR KICK

@client.slash_command(guild_ids=[SERVERID], description="Provides you with the information available about commands with Porygon-B")
async def help(interaction:Interaction):
    embed = nextcord.Embed(title="Porygon",url="https://github.com/Memotexe/Porygon-D", description="Programmed in Python using Nextcord", color=0x83b7f7)
    embed.set_author(name="Memotexe", url="https://github.com/Memotexe")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1530033914/137porygon_200x200.png")
    embed.add_field(name="/Lofi", value="Arg: (Pokemon, Morning, Coding, Japan) :: Porygon-B will then join the Lofi VC in the Server with the Genre you selected",inline=False)
    embed.add_field(name="/Pause", value="Pauses the Lofi Music",inline=True)
    embed.add_field(name="/Resume", value="Resumes the Lofi Music",inline=True)
    embed.add_field(name="/Leave", value="Leaves the Lofi VC when called",inline=True)
    embed.add_field(name="/Friday", value="Arg: @(Member) :: Its a Friday Thing",inline=False)
    embed.add_field(name="/Dice", value="Arg: (3,6,8,10,12,20) :: Porygon will roll a virtual dice based on the dice you chose.",inline=False)
    embed.add_field(name="/Purge", value="Arg: Amount :: Only Works if you are a Mod, but will clear messages given the amount provided",inline=False)
    embed.set_footer(text="If you have any command suggestions let me know! - Memotexe")
    await interaction.response.send_message(embed=embed)

# """
# .########.########..########...#######..########.....##.....##....###....##....##.########..##.......########.########...######.
# .##.......##.....##.##.....##.##.....##.##.....##....##.....##...##.##...###...##.##.....##.##.......##.......##.....##.##....##
# .##.......##.....##.##.....##.##.....##.##.....##....##.....##..##...##..####..##.##.....##.##.......##.......##.....##.##......
# .######...########..########..##.....##.########.....#########.##.....##.##.##.##.##.....##.##.......######...########...######.
# .##.......##...##...##...##...##.....##.##...##......##.....##.#########.##..####.##.....##.##.......##.......##...##.........##
# .##.......##....##..##....##..##.....##.##....##.....##.....##.##.....##.##...###.##.....##.##.......##.......##....##..##....##
# .########.##.....##.##.....##..#######..##.....##....##.....##.##.....##.##....##.########..########.########.##.....##..######.
# """

@client.event
async def on_command_error(interaction:Interaction,error):
    if isinstance(error,commands.MissingPermissions):
        await interaction.response.send_message("You are not allowed to use that command")


# """
# .########...#######..##....##.########.########..########.##.....##
# .##.....##.##.....##.##...##..##.......##.....##.##........##...##.
# .##.....##.##.....##.##..##...##.......##.....##.##.........##.##..
# .########..##.....##.#####....######...##.....##.######......###...
# .##........##.....##.##..##...##.......##.....##.##.........##.##..
# .##........##.....##.##...##..##.......##.....##.##........##...##.
# .##.........#######..##....##.########.########..########.##.....##
# """






# """
# ..######..########....###.....######..##....##..#######..##.....##.########.########..########.##........#######..##......##
# .##....##....##......##.##...##....##.##...##..##.....##.##.....##.##.......##.....##.##.......##.......##.....##.##..##..##
# .##..........##.....##...##..##.......##..##...##.....##.##.....##.##.......##.....##.##.......##.......##.....##.##..##..##
# ..######.....##....##.....##.##.......#####....##.....##.##.....##.######...########..######...##.......##.....##.##..##..##
# .......##....##....#########.##.......##..##...##.....##..##...##..##.......##...##...##.......##.......##.....##.##..##..##
# .##....##....##....##.....##.##....##.##...##..##.....##...##.##...##.......##....##..##.......##.......##.....##.##..##..##
# ..######.....##....##.....##..######..##....##..#######.....###....########.##.....##.##.......########..#######...###..###.
# """

@client.slash_command(guild_ids=[SERVERID], description="Searches StackOverFlow for Keywords Provided!")
async def stack(interaction:Interaction, arg):
    stackTitles = []
    stackLinks=[]
    SITE = StackAPI("stackoverflow")
    SITE.max_pages = 1
    SITE.page_size=5
    title_search = arg
    response = SITE.fetch('search/advanced', title = title_search, sort='votes')
    data = json.dumps(response, indent=4)
    jsonData = json.loads(data)

    for i in jsonData['items']:
        stackTitles.append(i['title'])
        stackLinks.append(i['link'])
    
    embed = nextcord.Embed(title="Results!", description="Your Search: "+ arg, color=0x343190)
    embed.set_author(name="StackOverFlow")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1530033914/137porygon_200x200.png")
    embed.set_footer(text="These results are formed by StackAPI")
    
    j=0
    for i in stackTitles:
            embed.add_field(name=i, value=stackLinks[j] ,inline=False)
            j=j+1

    await interaction.response.send_message(embed=embed)


client.run(DISCORD_TOKEN)
