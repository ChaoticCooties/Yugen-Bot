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

    def embed(self, desc, color):
        color = discord.Color(int(color, 16))
        embed = discord.Embed(color=color)
        embed.description = desc
        return embed

    @commands.command(name='invite')
    async def invite(self, ctx):
        await ctx.send(config['DEFAULT']['invite_link'])

    @commands.command(name='clear')
    async def clear(self, ctx):
        # Let mee6 handle this
        pass

    @commands.command(name='pin', pass_context=True)
    @commands.has_any_role("admin", "moderator")
    async def pin(self, ctx, message, link, userid):
        embedMsg = self.embed(
            "{} \n\n [Link]({})".format(message, link), "45b6fe")
        # Get user data and set as footer
        author = self.bot.get_user(int(userid))
        embedMsg.set_footer(text="Contributor: {}".format(
            author.name), icon_url=author.avatar_url)
        await ctx.send("", embed=embedMsg)

    @commands.command(name='gwtoggle')
    @commands.has_any_role("admin", "moderator")
    async def gwtoggle(self, ctx):
        activated = not config['DEFAULT'].getboolean('gwtoggle')
        config['DEFAULT']['gwtoggle'] = str(activated)
        embedMsg = self.embed(
            "GW Alerts are now toggled " + str(activated), "FFFFFF")
        await ctx.send("", embed=embedMsg)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


def setup(bot):
    bot.add_cog(Chat(bot))
