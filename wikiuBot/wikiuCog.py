import discord
import aiohttp

from discord.ext import commands

class WikiuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self,ctx,arg=None):
        #Apenas a primeira palavra eh um arg, precisa colocar entre aspas pra vir mais
        if arg == None:
            return await ctx.send("Digite algo depois do .wiki. Use aspas se quer usar mais que uma palavra.")
        nome = arg
        url = f'http://wikiu.app/generate?name={nome}'
        response = await aiohttp.ClientSession().get(url)
        data = await response.json()        
        text = data["result"]
        await ctx.send(text)
    