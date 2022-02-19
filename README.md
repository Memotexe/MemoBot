# MemoBot
Discord bot named Porygon-B created using [Nextcord](https://github.com/nextcord/nextcord), a discord.py wrapper for [Python v3.10.0](https://www.python.org/downloads/release/python-3100/).

![Porygon-B](https://pbs.twimg.com/profile_images/1530033914/137porygon_200x200.png)

Install commands for Libraries:
Linux/macOS:
> python3 -m pip install -U nextcord
> 
> python3 -m pip install -U "nextcord[voice]"

Windows:
> pip install -U nextcord :: pip3 install -U nextcord :: py -3 -m pip install -U nextcord
> 
> pip install -U nextcord[voice] :: pip 3 install -U nextcord[voice] :: py -3 -m pip install -U nextcord[voice]


# Client Listeners:
* Reaction Roles:
  - When a user adds or removes a specific reaction on a defined message in the server it will manage the user's roles by adding or removing them from it. The server uses role reactions to limit what people wish to see on the server by topics/games that interest them.

# Current Commands:
* Lofi ; arg (Genre):
  - This command will take an argument based on a genre of Lofi and with that join the Lofi and Vibe channel in the discord and play music
  - Commands for Lofi:
   - Pause: Pauses the music
   - Resume: Resumes the music
   - Leave: Tells the bot to leave the VC (Voice Channel)
* D20:
  - Its as it seems, this command will randomly roll a D20 for you and produce your results!
* Friday:
  - A command to only be called on Friday >.>


# To-Do's:
* Large Features:
  - Creation of Pokedex command that will listen for the pokemon and return an embed of some light information along with links to Serebii's Page
* Moderation Features:
  - Enhanced Ban and Kick
  - Clear Messages Command
  - Message Watcher(Protection against harsh/profanity-based word usage)
* Etc Features:
  - Help Command
  - Turn D20 command into any DnD Dice based on arg
  - R&R Command Hint:Never Gonna Give You Up
