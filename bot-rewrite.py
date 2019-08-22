# Dependencies
import discord
from discord.ext import commands
import data.jsonparse as jsonparse
import asyncio

bot = commands.Bot(command_prefix="!",
                   description="Republic's Custom Bot", pm_help=False)

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

    # Autorole Setup
    roles = jsonparse.readJSON("data/roles.json")
    roleChannel = bot.get_channel(454239659254480896)
    await roleChannel.purge(limit=10)

    # loop through json and output as embeds
    for role_id, role_info in roles.items():
        embed = discord.Embed(
            title=role_info['game'], color=discord.Color.blurple())
        embed.description = role_info['desc']
        avatar = bot.user.avatar_url or bot.user.default_avatar_url
        embed.set_author(name="Yugen", icon_url=avatar)
        embed.set_footer(text="github.com/ChaoticCooties")
        msg = await roleChannel.send("", embed=embed)
        # Set up reactions
        await msg.add_reaction(bot.get_emoji(454239994219986944))  # Add
        await msg.add_reaction(bot.get_emoji(454239995969011713))  # Remove
        await asyncio.sleep(0.1)
        # Wait for response and react accordingly
        while True:
            res, user = await bot.wait_for('reaction_add')
            role = discord.utils.get(
                user.guild.roles, id=int(role_info['roleid']))
            if res.emoji == bot.get_emoji(454239994219986944):
                await msg.remove_reaction(bot.get_emoji(454239994219986944), user)
                await user.add_roles(role, reason="Autorole")
            if res.emoji == bot.get_emoji(454239995969011713):
                await msg.remove_reaction(bot.get_emoji(454239995969011713), user)
                await user.remove_roles(role, reason="Autorole")


initial_extensions = ['cogs.admin', 'cogs.autorole']

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# Bot Token (DO NOT REVEAL)
bot.run("NDU0MTY1MTk1MTY2NTgwNzQ2.XVvarw.R0nkOhWwuTZDMoCp0HtlhQqW8Ts",
        reconnect="True")
