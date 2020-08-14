import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
import os
import asyncio
import pytz

from waifuBot.waifuCog import WaifuCog
from pokeBot.pokeCog import PokeCog
from spyBot.spyCog import SpyCog
from voiceBot.voiceCog import VoiceCog

bot = commands.Bot(command_prefix = '.')
@bot.event
async def on_ready():
    print("Bot is ready")
    bot.remove_command('help')
    activity = discord.Activity(name='Digimon', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)




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
bot.add_cog(VoiceCog(bot))


token = os.environ.get('TOKEN')
bot.run(token)
