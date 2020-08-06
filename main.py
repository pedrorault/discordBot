import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os

from waifuBot.waifuCog import WaifuCog
from pokeBot.pokeCog import PokeCog
from spyBot.spyCog import SpyCog

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("Bot is ready")
    bot.remove_command('help')
    activity = discord.Activity(name='Digimon', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.command()
async def teste(ctx):
    name = "Graveler"
    number = "075"
    serebii = "https://www.serebii.net/pokedex-sm/075.shtml"
    icon = "https://www.serebii.net/pokedex-sm/icon/075.png"

    embedVar = discord.Embed(color=0x00ffff,type="rich") 
    embedVar.set_author(name=name, url=serebii, icon_url=icon)   
    embedVar.set_image(
        url="https://assets.pokemon.com/assets/cms2/img/pokedex/detail/075.png"
    )
    embedVar.add_field(name="Número", value=f'#{number}', inline=True)
    embedVar.add_field(name="Tipo", value="Rock \t Ground", inline=False)
    embedVar.add_field(name="Evolui de", value="Geodude",inline=True)
    embedVar.add_field(name="Evolui para", value="Golem",inline=True)

    await ctx.send(embed=embedVar)

@bot.command()
async def clear(ctx):
    commands = ['.spy','.start','.vote', '.local', '.stop','.clear','.helpspy','.waifu','.poke','.furry','.person' ]
    commands.append('.teste')
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
