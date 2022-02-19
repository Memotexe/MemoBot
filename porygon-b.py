import nextcord
from nextcord.ext import commands, tasks
from nextcord import member
from nextcord import Interaction
from nextcord import FFmpegPCMAudio
from contextlib import suppress
import json
import random
from datetime import date

SERVERID= 869397848125485186

with open('discordToken.json','r') as discordFile:
    data=discordFile.read()

jsonObj = json.loads(data)
DISCORD_TOKEN = str(jsonObj['DiscordToken'])
client = commands.Bot(command_prefix="")


@client.event
async def on_ready():
    print("Porygon is up and running!")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name='Type /Help for Commands'))


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

@client.slash_command(guild_ids=[SERVERID], description="Rolls a Digital D20 for you!")
async def d20(interaction:Interaction):
    randomNum = random.randint(1,20)
    if randomNum == 1:
        await interaction.response.send_message(str(randomNum) + " Critical Fail! <a:F_:925511019655200841>")
    elif randomNum <= 10 and randomNum > 1:
        await interaction.response.send_message(str(randomNum) + " Thats not a good roll <:tanjiroD:925511021261631528>")
    elif randomNum >=11 and randomNum < 20:
        await interaction.response.send_message(str(randomNum) + " Thats a good roll <a:gachi:926278637341245471>")
    elif randomNum == 20:
        await interaction.response.send_message(str(randomNum) + " CRITICAL ROLL! <a:gachihyperclap:890777869360431104>")

@client.slash_command(guild_ids=[SERVERID], description="Only a Friday Thing")
async def friday(interaction: Interaction, member: nextcord.Member):
    with suppress(Exception):
        if date.today().isoweekday() == 5:
            try:
                channel = member.voice.channel
                if channel:#value or Null
                    voice = await channel.connect()
                    source = FFmpegPCMAudio('friday.mp3')
                    voice.play(source)
                    await interaction.response.send_message("ITS FRIDAY BABY! WOOOOO!")
            finally:
                await interaction.response.send_message("You're not in a VC")
        else:
            await interaction.response.send_message("It's Not Friday!")

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

# @client.command(pass_context=True)
# async def clear(ctx, amount=100):
#     channel = ctx.message.channel
#     messages = []
#     async for message in client.logs_from(channel, limit=int(amount) + 1):
#         messages.append(message)
#     await client.delete_messages(messages)
#     await client.say("I took out the trash for you!")

#LIST OF MODERATION COMMANDS
#CLEAR
#CHECK FOR UNWELCOME PROFANITY
#ENHANCE BAN OR KICK
#HELP COMMAND


# @client.command(pass_context=True)
# async def help(ctx):
#     author = ctx.message.author

#     embed = discord.Embed(
#         color=discord.Colour.orange()
#     )

#     embed.set_author(name="Help")
#     embed.add_field(name="!clear (Enter number from 1-100)", value='Clears as many messages asked up til 14 days.',
#                     inline=False)
#     embed.add_field(name="!help", value='Direct Messages you the command list.',
#                     inline=False)
#     embed.add_field(name="!stop",
#                     value='Amadeus will stop the music completely and leave the voice channel you are in.',
#                     inline=False)
#     embed.add_field(name="!play", value='Amadeus will play a youtube link url.',
#                     inline=False)
#     embed.add_field(name="!queue", value='Amadeus will add the song/video to the player queue.',
#                     inline=False)
#     embed.add_field(name="!skip", value='Amadeus will skip the song.',
#                     inline=False)
#     embed.add_field(name="!pause", value='Amadeus will pause the music for you.',
#                     inline=False)
#     embed.add_field(name="!resume", value='Amadeus will resume the music for you.',
#                     inline=False)
#     embed.add_field(name="!leave", value='Amadeus will leave the voice channel you are in.',
#                     inline=False)
#     embed.add_field(name="!baka", value='Amadeus will help you call your friend an idiot!.',
#                     inline=False)

#     await author.channel.send(embed)

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
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You are not allowed to use that command")


# """
# .########.##.....##.########..########.########.....########.########.##.....##.########..##..........###....########.########
# .##.......###...###.##.....##.##.......##.....##.......##....##.......###...###.##.....##.##.........##.##......##....##......
# .##.......####.####.##.....##.##.......##.....##.......##....##.......####.####.##.....##.##........##...##.....##....##......
# .######...##.###.##.########..######...##.....##.......##....######...##.###.##.########..##.......##.....##....##....######..
# .##.......##.....##.##.....##.##.......##.....##.......##....##.......##.....##.##........##.......#########....##....##......
# .##.......##.....##.##.....##.##.......##.....##.......##....##.......##.....##.##........##.......##.....##....##....##......
# .########.##.....##.########..########.########........##....########.##.....##.##........########.##.....##....##....########
# """
@client.command()
async def embed(ctx):
    embed = nextcord.Embed(title="Title",url="https://google.com", description="Description", color=0x343190)
    embed.set_author(name=ctx.author.display_name, url="https://twitter.com", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://instagram.com")
    embed.add_field(name="Field 1", value="Value 1", inline=True)
    embed.add_field(name="Field 2", value="Value 2", inline=True)
    embed.set_footer(text="Footer")
    await ctx.send(embed=embed)


client.run(DISCORD_TOKEN)
