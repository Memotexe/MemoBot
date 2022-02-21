# Porygon-D
Discord bot named **Porygon-D** created using [Nextcord](https://github.com/nextcord/nextcord), a discord.py wrapper, using [Python v3.10.0](https://www.python.org/downloads/release/python-3100/).

![Porygon-D](https://pbs.twimg.com/profile_images/1530033914/137porygon_200x200.png)

***Install commands for Libraries:***

*Linux/macOS:*
```
pip3 install -U nextcord
 
pip3 install -U "nextcord[voice]"

pip3 install stackapi
```
*Windows:*
```
pip install -U nextcord :: pip3 install -U nextcord :: py -3 -m pip install -U nextcord

pip install -U nextcord[voice] :: pip 3 install -U nextcord[voice] :: py -3 -m pip install -U nextcord[voice]

pip install stackapi
```
**NOTE:** Its important to mention the work I've done was on Python `v3.10.0`, I cannot gaurantee that any other version of Python will work

## Client Listeners:
* Reaction Roles:
  - When a user adds or removes a specific reaction on a defined message in the server it will manage the user's roles by adding or removing them from it. The server uses role reactions to limit what people wish to see on the server by topics/games that interest them.
* Keywords said in chat might provide a meme! Who knows what the words are ¯\\__(ツ)_/¯

## Current Commands:
* Lofi ; arg (Genre):
  - This command will take an argument based on a genre of Lofi and with that join the Lofi and Vibe channel in the discord and play music.
  - Commands for Lofi:
   - Pause: Pauses the music.
   - Resume: Resumes the music.
   - Leave: Tells the bot to leave the VC (Voice Channel).
* Dice ; arg (Sides):
  - Its as it seems, give this bot the argument of the sided dice you wish to roll and it will give you a result!
* Friday ; arg (Member):
  - A command to only be called on Friday >.>
* Purge ; arg (Amount):
  - Given the amount, it will delete messages in the channel it was called in.
* Help:
  - Responds with a embedded message giving all the commands that Porygon has with a description about them.
* Riro ; arg (Member):
  - Only if the stars align will this work.
* Stack ; arg (tags/topics) :
  - This call utilizes the StackAPI import to search StackOverFlow and return Titles and Links related to what you put in your argument.

## To-Do's:
* Large Features:
  - Creation of Pokedex Command that will listen for the pokemon and return an embed of some light information along with links to Serebii's Page.
* Moderation Features:
  - Enhanced Ban and Kick.
