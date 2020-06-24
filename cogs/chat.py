import discord
from discord.ext import commands
import re
import configparser
import schedule

config = configparser.ConfigParser()
config.read('config.ini')


class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='invite')
    async def invite(self, ctx):
        await ctx.send(config['DEFAULT']['invite_link'])

    @commands.command(name='clear')
    async def clear(self, ctx):
        # Let mee6 handle this
        pass


def setup(bot):
    bot.add_cog(Chat(bot))
