# Dependencies
import discord
from discord.ext import commands
import data.jsonparse as jsonparse
import asyncio
import configparser
import emoji
import re

bot = commands.Bot(command_prefix="!",
                   description="Republic's Custom Bot", pm_help=False)

config = configparser.ConfigParser()
config.read('config.ini')

# Startup
@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""
    print(
        f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('Developed by Cooties#2917')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cooties.io"))
    await main()

# Manual autorole restart
@bot.event
async def on_message(message):
    if message.content.startswith('!restart'):
        await main()
    elif message.channel.id == config['config'].getint('emoji_channel_blacklist'):
        # <emoji: 12938712> r'<:\w*:\d*>'
        msg = emoji.demojize(message.content)
        if re.search(r':\w*:\d*', msg):
            await message.channel.purge(limit=1)

    await bot.process_commands(message)


def embed(title, desc, color):
    color = discord.Color(int(color, 16))
    embed = discord.Embed(title=title, color=color)
    embed.description = desc
    embed.set_footer(text="github.com/ChaoticCooties/Yugen-Bot")
    return embed


async def message_setup(channel, role_info):
    # setup embed
    embed_message = embed(role_info['game'], role_info['desc'],
                          role_info['color'])
    msg = await channel.send("", embed=embed_message)
    #  reactions
    await msg.add_reaction(bot.get_emoji(config['emoji'].getint('add')))
    await asyncio.sleep(0.1)  # to prevent misfiring bug
    await msg.add_reaction(bot.get_emoji(config['emoji'].getint('remove')))
    await asyncio.sleep(0.1)

    # listen to reactions and apply roles
    while True:
        def check(reaction: discord.Reaction, _) -> bool:
            return reaction.message.id == msg.id
        res, user = await bot.wait_for('reaction_add', check=check)
        role = discord.utils.get(
            user.guild.roles, id=int(role_info['roleid']))
        if res.emoji == bot.get_emoji(config['emoji'].getint('add')):
            await msg.remove_reaction(bot.get_emoji(config['emoji'].getint('add')), user)
            await user.add_roles(role, reason="Autorole")
        if res.emoji == bot.get_emoji(config['emoji'].getint('remove')):
            await msg.remove_reaction(bot.get_emoji(config['emoji'].getint('remove')), user)
            await user.remove_roles(role, reason="Autorole")


async def main():
    # variables
    roles = jsonparse.readJSON(config['config']['role_json'])
    roleChannel = bot.get_channel(
        config['config'].getint('role_channel_id'))
    role_messages = []

    # cleanup channel
    await roleChannel.purge(limit=10)

    for _, role_info in roles.items():
        role_messages.append(message_setup(roleChannel, role_info))
    await asyncio.gather(*role_messages)


initial_extensions = ['cogs.admin', 'cogs.autorole', 'cogs.chat']

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# Bot Token (DO NOT REVEAL)
bot.run(config['config']['bot_token'],
        reconnect="True")
