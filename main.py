import discord 
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os

from waifuBot.waifuCog import WaifuCog
from pokeBot.pokeCog import PokeCog
from spyBot.spyCog import SpyCog

bot = commands.Bot(command_prefix = '.',description=".help para os comandos")

def firstTimeScripts():
    exec(open("./pokeBot/scripts/downloadPokemonImages.py").read())
    print("Done")

@bot.event
async def on_ready():
    print("Bot is ready")
    firstTimeScripts()

@bot.command()
async def clear(ctx):
    commands = ['.spy','.start','.vote', '.local', '.stop','.clear','.helpspy','.waifu','.poke','.furry','.person' ]
    async for msg in ctx.channel.history(limit=20):
        if msg.author == bot.user or msg.content.startswith(tuple(commands)):
            await discord.Message.delete(msg)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

bot.add_cog(WaifuCog(bot))
bot.add_cog(PokeCog(bot))
bot.add_cog(SpyCog(bot))

token = os.environ.get('TOKEN')
bot.run(token)