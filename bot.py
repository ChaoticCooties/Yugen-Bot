# Dependencies
import discord
from discord.ext import commands
import data.jsonparse as jsonparse
import asyncio
import configparser

bot = commands.Bot(command_prefix="!", description="Republic's Custom Bot")
config = configparser.ConfigParser()
config.read('config.ini')

# Extensions to load on startup
startup_extensions = ["cogs.main", "cogs.roles",
                      "cogs.chat", "cogs.admin", "cogs.gbf"]


# Embedded Message
def embed(title, desc, color):
    color = discord.Color(int(color, 16))
    embed = discord.Embed(title=title, color=color)
    embed.description = desc
    embed.set_footer(text="github.com/ChaoticCooties/Yugen-Bot")
    return embed


@bot.event
async def on_message(message):
    if message.content.startswith('ping!'):
        await message.channel.send('pong!')
    await bot.process_commands(message)

# admins and moderator
@bot.command(name='embed', pass_context=True)
async def embedmsg(ctx, title: str, message: str, color: str):
    await ctx.message.delete()
    embed_message = embed(title, message, color)
    await ctx.message.channel.send("", embed=embed_message)

# Loads all extensions stated in startup_extensions
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    # Bot Token
    bot.run(config['config']['bot_token'], reconnect="True")
