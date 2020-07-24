import discord
from discord.ext import commands
from waifuBot.waifuBot import getWaifu,getFurry,getPerson

class WaifuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def waifu(self,ctx):       
        getWaifu()
        await ctx.send(file=discord.File('img.jpg'))

    @commands.command()
    async def furry(self,ctx):       
        getFurry()
        await ctx.send(file=discord.File('fur.jpg'))

    @commands.command()
    async def person(self,ctx):       
        getPerson()
        await ctx.send(file=discord.File('person.jpg'))
