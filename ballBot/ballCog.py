import discord
from discord.ext import commands
from ballBot.ball import randomResponse
import random

class BallCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def _8ball(self,ctx):
        msg = randomResponse()
        await ctx.send(msg)
    
    @commands.command(name='random')
    async def _random(self,ctx):
        alternativas = ['A','B','C','D','E']
        msg = f'Escolha {random.choice(alternativas)}'
        await ctx.send(msg)