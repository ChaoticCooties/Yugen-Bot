import discord
from discord.ext import commands


class Granblue(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Granblue(bot))
