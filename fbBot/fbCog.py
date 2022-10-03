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
        new_url = await scrap_for_video(url = arg)
        await ctx.send(new_url)
