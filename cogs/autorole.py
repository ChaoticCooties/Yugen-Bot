import discord
from discord.ext import commands
import asyncio
import re

class autoRoleCog(commands.Cog):

    def __init__(self, bot): 
        self.bot = bot

    #add a role into json list
    @commands.command(name='addrole')
    @commands.has_any_role("admin","moderator")
    async def addrole(self, ctx):
        await ctx.send("What should the role be called?") 
        #To make sure the one entering the variables are the same person
        def check(message):
            return message.author == ctx.author
        
        #Listen for user input
        #This is a Q&A set which acquires four variables: title, desc, color, and ID.
        try:
            roleTitle = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Command Timeout.")
            return
        else:
            await ctx.send("What is " + roleTitle.content + "\'s description?")
            try: 
                roleDesc = await self.bot.wait_for('message', check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Command Timeout.")
                return
            else:
                await ctx.send("What color should the embed message be?")
                try:
                    roleColor = await self.bot.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send("Command Timeout.")
                    return
                else:
                    await ctx.send("What is the role id? ")
                    try:
                        roleID = await self.bot.wait_for('message', check=check, timeout=30)
                    except asyncio.TimeoutError:
                        await ctx.send("Command Timeout.")
                        return
                    else:
                        await ctx.send("Successfully added " + roleTitle.content + " with roleID of " + roleID.content)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case SimpleCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(autoRoleCog(bot))