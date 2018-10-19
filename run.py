# Dependencies
#Import these modules into Python
import discord
import asyncio
import sys
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import os

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(command_prefix="!", description="Bot", pm_help=False)

#BasicBot startup
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Developed by Cooties#1066')
	return await client.change_presence(game=discord.Game(name='www.repsports.org'))

#Variables
add = '454239994219986944'
remove = '454239995969011713'

roledict =  {
  "granblue": "307856397515882500",
  "rainbow": "453220899089547274",
  "fgo": "383614957369032704",
  "league": "307872181352792065",
  "nsfw": "307858033525129219"
}
# a dictionary where a 'TITLE' is assigned to an Discord role ID

#Role Functions 
async def role1(message):
    em = discord.Embed(title='Granblue Fantasy', description='Granblue Fantasy community of dank memes and Dankchou leeching.', colour=0x33cccc)
    msg = await client.send_message(message.channel, embed=em)
    await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id=add))
    await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id=remove))
    await asyncio.sleep(0.1)
    while True:
        res = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id=add), discord.utils.get(client.get_all_emojis(), id=remove)], message=msg)
        if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=add):
            await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id=add), res.user)
            await client.add_roles(res.user, discord.utils.get(msg.server.roles, id=roledict["granblue"]))
        if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=remove):
            await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id=remove), res.user)
            await client.remove_roles(res.user, discord.utils.get(msg.server.roles, id=roledict["granblue"]))   

async def role2(message):
    em2 = discord.Embed(title='Rainbow Six Siege', description='Rainbow Six Siege channel and church of Tachanka', colour=0x009933)
    msg2 = await client.send_message(message.channel, embed=em2)
    await client.add_reaction(msg2, discord.utils.get(client.get_all_emojis(), id=add))
    await client.add_reaction(msg2, discord.utils.get(client.get_all_emojis(), id=remove))
    await asyncio.sleep(0.1)
    while True:
        res2 = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id=add), discord.utils.get(client.get_all_emojis(), id=remove)], message=msg2)
        if res2.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=add):
            await client.remove_reaction(msg2, discord.utils.get(client.get_all_emojis(), id=add), res2.user)
            await client.add_roles(res2.user, discord.utils.get(msg2.server.roles, id=roledict["rainbow"]))
        if res2.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=remove):
            await client.remove_reaction(msg2, discord.utils.get(client.get_all_emojis(), id=remove), res2.user)
            await client.remove_roles(res2.user, discord.utils.get(msg2.server.roles, id=roledict["rainbow"]))

async def role3(message):
    em3 = discord.Embed(title='Fate Grand Order', description='FGO channel, Yorokobe Shounen', colour=0x0066cc)
    msg3 = await client.send_message(message.channel, embed=em3)
    await client.add_reaction(msg3, discord.utils.get(client.get_all_emojis(), id=add))
    await client.add_reaction(msg3, discord.utils.get(client.get_all_emojis(), id=remove))
    await asyncio.sleep(0.1)
    while True:
        res3 = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id=add), discord.utils.get(client.get_all_emojis(), id=remove)], message=msg3)
        if res3.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=add):
            await client.remove_reaction(msg3, discord.utils.get(client.get_all_emojis(), id=add), res3.user)
            await client.add_roles(res3.user, discord.utils.get(msg3.server.roles, id=roledict["fgo"]))
        if res3.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=remove):
            await client.remove_reaction(msg3, discord.utils.get(client.get_all_emojis(), id=remove), res3.user)
            await client.remove_roles(res3.user, discord.utils.get(msg3.server.roles, id=roledict["fgo"]))

async def role4(message):
    em4 = discord.Embed(title='League Of Legends', description='League of Legends memes and discussion.', colour=0xFD6A02)
    msg4 = await client.send_message(message.channel, embed=em4)
    await client.add_reaction(msg4, discord.utils.get(client.get_all_emojis(), id=add))
    await client.add_reaction(msg4, discord.utils.get(client.get_all_emojis(), id=remove))
    await asyncio.sleep(0.1)
    while True:
        res4 = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id=add), discord.utils.get(client.get_all_emojis(), id=remove)], message=msg4)
        if res4.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=add):
            await client.remove_reaction(msg4, discord.utils.get(client.get_all_emojis(), id=add), res4.user)
            await client.add_roles(res4.user, discord.utils.get(msg4.server.roles, id=roledict["league"]))
        if res4.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=remove):
            await client.remove_reaction(msg4, discord.utils.get(client.get_all_emojis(), id=remove), res4.user)
            await client.remove_roles(res4.user, discord.utils.get(msg4.server.roles, id=roledict["league"]))

async def role5(message):
    em5 = discord.Embed(title='Not Safe For Work', description='NSFW channel, for all your 18+ needs.', colour=0xcc3300)
    msg5 = await client.send_message(message.channel, embed=em5)
    await client.add_reaction(msg5, discord.utils.get(client.get_all_emojis(), id=add))
    await client.add_reaction(msg5, discord.utils.get(client.get_all_emojis(), id=remove))
    await asyncio.sleep(0.1)
    while True:
        res5 = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id=add), discord.utils.get(client.get_all_emojis(), id=remove)], message=msg5)
        if res5.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=add):
            await client.remove_reaction(msg5, discord.utils.get(client.get_all_emojis(), id=add), res5.user)
            await client.add_roles(res5.user, discord.utils.get(msg5.server.roles, id=roledict["nsfw"]))
        if res5.reaction.emoji == discord.utils.get(client.get_all_emojis(), id=remove):
            await client.remove_reaction(msg5, discord.utils.get(client.get_all_emojis(), id=remove), res5.user)
            await client.remove_roles(res5.user, discord.utils.get(msg5.server.roles, id=roledict["nsfw"]))

# Reaction auto roles
@client.event
async def on_message(message):
    if message.content.startswith('.autorole1'):
        await client.delete_message(message)
        await asyncio.gather(
        role1(message),
        role2(message),
        role3(message),
        role4(message),
        role5(message)
        )
    await client.process_commands(message)

#Provides !emo [arg] to post png memes
@client.command(pass_context=True)
async def emo(ctx, arg):
    suffix = "png" ##Not case sensitive
    path = os.path.join("images/" + "{0}" + "." + suffix).format(arg) #Directory images/*.png
    try:
        await client.send_file(ctx.message.channel, path) # Sends the fukin image
    except: 
        await client.say('Image Not Found!')
    return

#Auto Choose
@client.command()
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))

# Bot Token Below	
client.run(BOT_TOKEN)
