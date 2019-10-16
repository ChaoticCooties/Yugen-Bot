import discord
from discord.ext import commands
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class chatCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='invite')
    async def invite(self, ctx):
        await ctx.send(config['DEFAULT']['invite_link'])


def setup(bot):
    bot.add_cog(chatCog(bot))
