import discord
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""
        print(
            f'\n\nLogged in as: {self.bot.user.name} - {self.bot.user.id}\nVersion: {discord.__version__}\n')
        print(f'Successfully logged in and booted...!')
        print('Use this link to invite {}:'.format(self.bot.user.name))
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(self.bot.user.id))
        print('Developed by Cooties#1101')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Republic"))


def setup(bot):
    bot.add_cog(Main(bot))
