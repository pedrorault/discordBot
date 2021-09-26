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
        
    @commands.command(name='vino')
    async def _vino(self,ctx):
        msg = f'O QUEEE???!?!?!! VOCÊ PEGOU ESSE PERSONAGEM?!!?!?! NAO ACREDITO'
        for i in range(5):
            await ctx.send(msg)
        await ctx.send(f"🤯🤯🤯🤯🤯🤯🤯🤯🤯")
        
    @commands.command(name='vino')
    async def _oniv(self,ctx):
        msg = f'Ainda bem que você pegou esse personagem!!! 😊😊😊'
        for i in range(3):
            await ctx.send(msg)

