# Dependencies
import discord
from discord.ext import commands
from discord.ext.tasks import loop
import data.jsonparse as jsonparse
import asyncio
import configparser
import emoji
import re
from datetime import datetime

bot = commands.Bot(command_prefix="!",
                   description="Republic's Custom Bot", pm_help=False)

config = configparser.ConfigParser()
config.read('testconfig.ini')

# Startup
@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""
    print(
        f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('Developed by Cooties#1101')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cooties.io"))
    await main()

# GW Alerts
@loop(seconds=1)
async def gw_alert():
    # Variables
    crew_channel = bot.get_channel(
        config['config'].getint('crew_channel_id'))
    activated = config['DEFAULT'].getboolean('gwtoggle')
    # 24 hours format 19:00
    current_time = datetime.strftime(datetime.now(), '%H:%M')
    if activated:
        if current_time == '19:00':
            await crew_channel.send("21:31")
            await asyncio.sleep(70)
        else:
            await asyncio.sleep(1)


@gw_alert.before_loop
async def gw_alert_before():
    await bot.wait_until_ready()


async def main():
    # variables
    try:
        roles = jsonparse.readJSON(config['config']['role_json'])
    except:
        print("Make sure you've filled the config correctly!")
    roleChannel = bot.get_channel(config['config'].getint('role_channel_id'))
    role_messages = []

    # cleanup channel
    await roleChannel.purge(limit=10)

    # Store list of commands into array and fire them off using asyncio.gather
    for _, role_info in roles.items():
        role_messages.append(message_setup(roleChannel, role_info))
    await asyncio.gather(*role_messages)


def embed(title, desc, color):
    color = discord.Color(int(color, 16))
    embed = discord.Embed(title=title, color=color)
    embed.description = desc
    embed.set_footer(text="github.com/ChaoticCooties/Yugen-Bot")
    return embed

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


async def message_setup(channel, role_info):
    # setup embed
    embed_message = embed(role_info['game'], role_info['desc'],
                          role_info['color'])
    msg = await channel.send("", embed=embed_message)
    #  reactions
    await msg.add_reaction(bot.get_emoji(config['emoji'].getint('add')))
    await asyncio.sleep(0.2)
    await msg.add_reaction(bot.get_emoji(config['emoji'].getint('remove')))
    await asyncio.sleep(0.2)

    # listen to reactions and apply roles
    while True:
        def check(reaction: discord.Reaction, _) -> bool:
            return reaction.message.id == msg.id
        res, user = await bot.wait_for('reaction_add', check=check)
        role = discord.utils.get(
            user.guild.roles, id=int(role_info['roleid']))
        if res.emoji == bot.get_emoji(config['emoji'].getint('add')):
            await msg.remove_reaction(bot.get_emoji(config['emoji'].getint('add')), user)
            await user.add_roles(role, reason="Auto-role")
        if res.emoji == bot.get_emoji(config['emoji'].getint('remove')):
            await msg.remove_reaction(bot.get_emoji(config['emoji'].getint('remove')), user)
            await user.remove_roles(role, reason="Auto-role")

initial_extensions = ['cogs.admin', 'cogs.autorole', 'cogs.chat']
# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

gw_alert.start()

# Bot Token (DO NOT REVEAL)
bot.run(config['config']['bot_token'], reconnect="True")
