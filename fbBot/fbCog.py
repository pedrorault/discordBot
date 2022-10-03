import discord
from discord.ext import commands
from fbBot.directVideoBot import scrap_for_video

class FbCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fb(self,ctx,arg=None):
        if arg is None:
            return
        await ctx.send(scrap_for_video(url = arg))
