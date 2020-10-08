import discord
from discord.ext import commands
from ballBot.ball import randomResponse

class BallCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.commandd(name='8ball')
    async def _8ball(self,ctx):
        msg = randomResponse()
        await ctx.send(msg)