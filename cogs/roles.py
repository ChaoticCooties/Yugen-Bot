import discord
from discord.ext import commands
import asyncio
import re


class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    roles = {
        # role, messageid
        'fitness': 721144001029472367,
        'food': 721144114015633519,
        'granblue': 721144509076996096,
        'raidping': 721144822005760041,
        'fgo': 721145457807589456,
        'chat': 721145780815134762,
        'nsfw': 721145979675475968
    }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

        # add role auto role
        if(payload.channel_id == 454239659254480896):
            for role_name, role_id in self.roles.items():
                if(payload.message_id == role_id):
                    role = discord.utils.get(guild.roles, name=role_name)
                    await user.add_roles(role, reason="Reaction roles")

        # starboard
        for i in message.reactions:
            if('⭐' == i.emoji):
                if(user.top_role.name == "admin" or user.top_role.name == "moderator" or i.count == 3):
                    embed = discord.Embed(description=(
                        message.content + "\n\n" + "[Jump to](" + message.jump_url + ")"))
                    embed.set_footer(text=("Author: " + message.author.name+"#"+message.author.discriminator),
                                     icon_url=message.author.avatar_url)
                    try:
                        embed.set_image(url=message.attachments[0].url)
                    except:
                        # ignore if no attachments
                        pass
                    # starboard channel
                    star_channel = message.guild.get_channel(
                        721493535572099142)
                    await star_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # remove role auto role
        if(payload.channel_id == 454239659254480896):
            for role_name, role_id in self.roles.items():
                if(payload.message_id == role_id):
                    guild = self.bot.get_guild(payload.guild_id)
                    user = guild.get_member(payload.user_id)
                    role = discord.utils.get(guild.roles, name=role_name)
                    await user.remove_roles(role, reason="Reaction roles")


def setup(bot):
    bot.add_cog(Roles(bot))
