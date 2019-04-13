#Dependencies
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Republic's Custom Bot", pm_help=False)

#Startup
@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('Developed by Cooties#1066')

initial_extensions = ['cogs.admin','cogs.autorole']

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#Bot Token (DO NOT REVEAL)
bot.run("---")
