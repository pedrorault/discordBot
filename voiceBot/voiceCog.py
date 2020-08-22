import asyncio
import os
from datetime import datetime
import pytz

import discord
from discord.ext import commands, tasks


class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.horario.start()
        
    def cog_unload(self):
        self.horario.cancel()

    @tasks.loop(hours=24.0)
    async def horario(self):
        idCanal = int(os.environ.get('idInvade'))

        som = discord.FFmpegPCMAudio("./voiceBot/mp3/Horario2.mp3")
        canal = self.bot.get_channel(idCanal)
        voice = await canal.connect()
        voice.play(som)

        counter = 0
        duration = 8
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()
   
    @horario.before_loop
    async def before_horario(self):
        await self.bot.wait_until_ready()
        tz = pytz.timezone('America/Sao_Paulo')
        dt = datetime.now(tz)    
        secondsLeft = ((24 - dt.hour - 1) * 60 * 60) + ((60 - dt.minute - 1) * 60) + (60 - dt.second)
        counter = 0  
        while not counter >= secondsLeft:
            await asyncio.sleep(1)
            counter +=1

    @commands.command()
    async def remix(self,ctx):
        idCanal = int(os.environ.get('idSoloQ'))
        if not discord.opus.is_loaded():
            discord.opus.load_opus('libopus.so')
        som = discord.FFmpegPCMAudio("./voiceBot/mp3/Horario2.mp3")
        canal = self.bot.get_channel(idCanal)
        voice = await canal.connect()
        voice.play(som)

        counter = 0
        duration = 8
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()