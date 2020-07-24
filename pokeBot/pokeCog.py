import discord
from discord.ext import commands
from pokeBot.pokeBot import *

class PokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pokemon(self,ctx):   
        file = pokemonLogo()
        await ctx.send(file=discord.File(file))
        
    @commands.command()
    async def poke(self,ctx):
        msg = (ctx.message.content.replace(".poke ","")).split(" ")
        if len(msg) == 2:
            try:
                x = int(msg[0])
                y = int(msg[1])
                file = choosePoke(x,y)
            except:
                file = randomPoke()
        elif len(msg) == 1:
            if msg[0] == ".poke":
                file = randomPoke()
            else:
                cnt, file = whichPoke(msg[0])
                if cnt != "" and file !="":
                    return await ctx.send(content=cnt, file=discord.File(file))
                elif cnt != "":
                    return await ctx.send(content=cnt)
                else:
                    return 
        else:
            file = randomPoke()
        await ctx.send(file=discord.File(file))