from datetime import datetime as dt
from logging import exception
import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
import os
import sys

from imageBot.imageCog import ImageCog
# from pokeBot.pokeCog import PokeCog
from spyBot.spyCog import SpyCog
from voiceBot.voiceCog import VoiceCog
from ballBot.ballCog import BallCog
from wikiuBot.wikiuCog import WikiuCog
from dayBot.dayCog import DayCog

bot = commands.Bot(command_prefix = '.')

if(len(sys.argv) > 1 and sys.argv[1] == "debug"):
    from dotenv import load_dotenv
    load_dotenv()

@bot.event
async def on_ready():
    print("Bot is ready")
    bot.remove_command('help')
    activity = discord.Activity(name='Digimon', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.command()
async def clear(ctx):
    commands = ['.spy','.start','.vote', '.local', '.stop','.clear','.helpspy','.waifu','.poke','.furry','.person','.meeting','.ovo','.remix']
    commands += ['.see','.set','.reset','.remove']
    deletar = []
    async for msg in ctx.channel.history(limit=100):
        if msg.author == bot.user or msg.content.startswith(tuple(commands)):
            diasPassados = dt.now().date() - msg.created_at.date()
            if diasPassados.days  < 14:
                deletar.append(msg)
    await ctx.message.channel.delete_messages(deletar)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

bot.add_cog(ImageCog(bot))
# bot.add_cog(PokeCog(bot))
bot.add_cog(SpyCog(bot))
bot.add_cog(VoiceCog(bot))
bot.add_cog(BallCog(bot))
bot.add_cog(WikiuCog(bot))
bot.add_cog(DayCog(bot))


token = os.environ.get('TOKEN')
bot.run(token)
