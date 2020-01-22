import discord
from discord.ext import commands
import asyncio
import data.jsonparse as jsonparse
import re


class AutoRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Autorole Startup
    def embed(self, title, desc, color):
        color = discord.Color(int(color, 16))
        embed = discord.Embed(title=title, color=color)
        embed.description = desc
        embed.set_footer(text="github.com/ChaoticCooties/Yugen-Bot")
        return embed

    # Add role to JSON store
    @commands.command(name='addrole')
    @commands.has_any_role("admin", "moderator")
    async def addrole(self, ctx):
        await ctx.send("", embed=discord.Embed(title="Role Title",
                                               description="What should the role be called?"))

        # To Ensure It's The Same User Who Evoked The Command
        def check(message):
            return message.author == ctx.author

        # Listen for user input
        # This is a Q&A set which acquires four variables: title, desc, color, and ID.
        try:
            roleTitle = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("", embed=discord.Embed(title="Command Timeout"))
            return
        else:
            await ctx.send("", embed=discord.Embed(title=roleTitle.content,
                                                   description="What should be the description?"))
            try:
                roleDesc = await self.bot.wait_for('message', check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("", embed=discord.Embed(title="Command Timeout"))
                return
            else:
                await ctx.send("", embed=discord.Embed(title=roleTitle.content,
                                                       description="What color should the embed message be?"))
                try:
                    roleColor = await self.bot.wait_for('message', check=check, timeout=30)
                    if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', roleColor.content):
                        raise ValueError(
                            'Invalid color, use hexadecimal values!')
                except asyncio.TimeoutError:
                    await ctx.send("", embed=discord.Embed(title="Command Timeout"))
                    return
                except ValueError as err:
                    await ctx.send(err)
                else:
                    await ctx.send("", embed=discord.Embed(title=roleTitle.content,
                                                           description="What is the role id?"))
                    try:
                        roleID = await self.bot.wait_for('message', check=check, timeout=30)
                    except asyncio.TimeoutError:
                        await ctx.send("", embed=discord.Embed(title="Command Timeout"))
                        return
                    else:
                        await ctx.send("Successfully added " + roleTitle.content + " with roleID of " + roleID.content)
                        jsonparse.appendJSON({"game": roleTitle.content, "desc": roleDesc.content,
                                              "color": roleColor.content, "roleid": roleID.content}, "data/roles.json")

    @commands.command(name='delrole')
    @commands.has_any_role("admin", "moderator")
    async def delrole(self, ctx):
        print(ctx.content)

        # The setup fucntion below is necessary. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
        # When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(AutoRole(bot))
