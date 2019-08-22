import discord
from discord.ext import commands
import asyncio


class startupCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(startupCog(bot))
