from dayBot.day import *
import discord
from discord.ext import commands
import datetime
import pytz

class DayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#set, see, reset, remove
    @commands.command()
    async def set(self,ctx,*args):
        if len(args) < 2:
            msg = ("Necessário 2 parâmetros depois do .set\n"
                  "(1) Uma tag\n"
                  "(2) A continuação da frase \"Estamos há x dias sem\"\n"
                  "Ex: .set lol reclamar de lol  (-> Estamos há 0 dias sem reclamar de lol)")
            return await ctx.send(msg,delete_after=10)
        tag, *values = args 
        tz = pytz.timezone('America/Sao_Paulo')
        frase = ' '.join(values)
        dateCreated = datetime.datetime.now(tz).date()
        guild = str(ctx.message.guild.id)
        status = createMemo(tag,frase,dateCreated,guild)
        await ctx.send(status, delete_after=4)    

    @commands.command()
    async def see(self, ctx, arg):
        if isEmpty(arg):
            return
        tag = arg
        guild = str(ctx.message.guild.id)
        msg = getMessage(tag,guild)
        await ctx.send(msg)
    
    @commands.command()
    async def reset(self, ctx, arg):
        if isEmpty(arg):
            return
        tag = arg
        guild = str(ctx.message.guild.id)
        msg = resetMemo(tag,guild)
        await ctx.send(msg)
    
    @commands.command()
    async def remove(self, ctx, arg):
        if isEmpty(arg):
            return
        tag = arg
        guild = str(ctx.message.guild.id)
        msg = removeMemo(tag,guild)
        await ctx.send(msg,delete_after=5)
    