import nextcord
from nextcord.ext import commands, tasks
from nextcord import member
from nextcord import Interaction, SlashOption
from nextcord import FFmpegPCMAudio
import json
import random

SERVERID= 869397848125485186

with open('discordToken.json','r') as discordFile:
    data=discordFile.read()

jsonObj = json.loads(data)
DISCORD_TOKEN = str(jsonObj['DiscordToken'])
client = commands.Bot(command_prefix="",)


@client.event
async def on_ready():
    print("This lil Bob-omb is ready to assist!")
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
# .########.....###....##....##.########...#######..##.....##
# .##.....##...##.##...###...##.##.....##.##.....##.###...###
# .##.....##..##...##..####..##.##.....##.##.....##.####.####
# .########..##.....##.##.##.##.##.....##.##.....##.##.###.##
# .##...##...#########.##..####.##.....##.##.....##.##.....##
# .##....##..##.....##.##...###.##.....##.##.....##.##.....##
# .##.....##.##.....##.##....##.########...#######..##.....##
# """

@client.slash_command(guild_ids=[SERVERID], description="Rolls a Digital D20 for you!")
async def d20(interaction:Interaction):
    randomNum = random.randint(1,20)
    if randomNum == 1:
        await interaction.response.send_message(str(randomNum) + " Critical Fail! <a:F_:925511019655200841>")
    elif randomNum <= 10 and randomNum > 1:
        await interaction.response.send_message(str(randomNum) + " Yikes! Thats not a good role <:tanjiroD:925511021261631528>")
    elif randomNum >=11 and randomNum < 20:
        await interaction.response.send_message(str(randomNum) + " Ok! Thats a good role <a:gachi:926278637341245471>")
    elif randomNum == 20:
        await interaction.response.send_message(str(randomNum) + " LETS GOO! CRITICAL ROLE! <a:gachihyperclap:890777869360431104>")

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
    elif(arg.lower() == "coding"):
        voice = await channel.connect()
        source = FFmpegPCMAudio('codingLofi.mp3')
        voice.play(source)
        await interaction.response.send_message("Now playing Coding Lofi")
    else:
       await interaction.response.send_message("Please choose a valid option") 


@client.slash_command(guild_ids=[SERVERID], description="Tells the Bot to Leave the Lofi VC")
async def leave(interaction: Interaction):
    if(interaction.guild.voice_client):
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("goodbye")
    else:
        await interaction.response.send_message("I'm not in a VC")

@client.slash_command(guild_ids=[SERVERID], description="Tells the Bot to Pause the Lofi")
async def pause(interaction: Interaction):
    voice = nextcord.utils.get(client.voice_clients,guild=interaction.guild)
    if voice.is_playing():
        voice.pause()
        await interaction.response.send_message("paused")
    else:
        await interaction.response.send_message("Sorry, but no music is playing.")

@client.slash_command(guild_ids=[SERVERID], description="Tells the Bot to Resume the Lofi")
async def resume(interaction: Interaction):
    voice = nextcord.utils.get(client.voice_clients,guild=interaction.guild)
    if voice.is_paused():
        voice.resume()
        await interaction.response.send_message("resumed")
    else:
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
