import asyncio
import os
from datetime import datetime
import pytz

import discord
from discord.ext import commands, tasks

async def awaitRealTime(seconds):
    counter = 0
    duration = seconds
    while not counter >= duration:
        await asyncio.sleep(1)
        counter = counter + 1

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
        mus = os.environ.get("HORARIO")
        som = discord.FFmpegPCMAudio(f"./voiceBot/mp3/{mus}.mp3")
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
    async def ovo(self,ctx):
        idCanal = ctx.message.author.voice.channel
        if not discord.opus.is_loaded():
            discord.opus.load_opus('libopus.so')
        som = discord.FFmpegPCMAudio("./voiceBot/mp3/carrodoovo.mp3")
        voice = await idCanal.connect()
        voice.play(som)
        await awaitRealTime(15)
        await voice.disconnect()

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

    @commands.command()
    async def meeting(self,ctx):
        idCanal = ctx.message.author.voice.channel
        if not discord.opus.is_loaded():
            discord.opus.load_opus('libopus.so')
        som = discord.FFmpegPCMAudio("./voiceBot/mp3/meet.mp3")
        voice = await idCanal.connect()
        voice.play(som)
        text = "Envie o @ do usuário que quer votar para ejetar, tens 20 segundos!\nSó o último voto de cada um é válido."
        await ctx.send(text)
        await awaitRealTime(3)
        await voice.disconnect()

        await awaitRealTime(20)
        messages = await ctx.history(limit=50).flatten()
        votes = dict()
        hasVoted = []
        for m in messages:
            if m.author == self.bot.user:
                break
            if m.mentions == [] or m.author in hasVoted:
                continue
            mention = m.mentions[0]
            hasVoted.append(m.author)
            if mention in votes.keys():
                votes[mention] += 1
            else:
                votes[mention] = 1

        if hasVoted != []:
            ordenado = sorted(votes.items(), key=lambda x: x[1], reverse=True)
            if len(ordenado) == 1 or ordenado[0][1] != ordenado[1][1]:
                conectados = idCanal.voice_states.keys()
                kicked = False
                for user in conectados:
                    membro = await ctx.message.guild.fetch_member(member_id=user)
                    if ordenado[0][0] == membro:
                        await membro.move_to(channel=None,reason="Votado pra fora")
                        await ctx.send(f'O usuário {membro.display_name} foi votado pra fora UwU')
                        kicked = True
                        break
                if not kicked:
                	await ctx.send(f'Ē̵̛̫͗̎̔̿̌̾̕r̴̀̉̃̋̀́͑̏̑͆͊̚͝͝ͅr̷͓̗̿͗̇ǫ̶͚̓̓̈́͋̽͊̄̈́͆͝ŗ̷̧̗̦̣̞̥̼͖͚̯̗̥̀͑̂͜ ̷̢̧̼͈͙̹͉͈̾̿͊́̾͜ͅ4̵͙͖̼̞͌̏̆0̴̜̖͕̯̝͖̗̓4̸̛̦̮̠̥̱̏: Usuário não encontrado no c̵̳͕͎͎̲̦̩̝̮̖͓̦̊̆̈̈́̓́̓̊͋̓͐͋̈͋̏ͅȁ̷̢̡̨̢̙̲̩͍̤̻͎͐̇̓͛͛̆͜ͅn̶̪͚̤̪͎͚͕̹̫͕̹̿͑͊͂͑̓̎̈́͐̅̚͘͝ǎ̷̮̞̮͔͐͋͆̋̈̿̃͗̒̓̆͘͠ĺ̸̨͔̈́ ̶̢̗̦̘̰͚̦̗̥̳̼͈̼̥̗͊͆̃̓d̸̢̖̭̹͔͑̆̾̇̍̌̂͛̍̎̏͛̂͝ȩ̸̛̤͙̩̱͓̲͍͇̜͐͊͌͋͋̚ ̵̧̨̛̬̳̖̲̖͍̯̲̠̝̿̑̍͒̇͋̔͆̓͝ͅv̶̟̟͖̼̬̻̜̝̜̳̞̈͒ǫ̴̢̯͎̥͚͕͍̘̱̆̐̀̽̀́̈́͌͛̂̒̚ͅz̷̺̞̦̅͒͌̀̿́̐̄̅͋͌̅̈́̈́ ')
                	await ctx.send(f'Ē̵̛̫͗̎̔̿̌̾̕r̴̀̉̃̋̀́͑̏̑͆͊̚͝͝ͅr̷͓̗̿͗̇ǫ̶͚̓̓̈́͋̽͊̄̈́͆͝ŗ̷̧̗̦̣̞̥̼͖͚̯̗̥̀͑̂͜ ̷̢̧̼͈͙̹͉͈̾̿͊́̾͜ͅ4̵͙͖̼̞͌̏̆0̴̜̖͕̯̝͖̗̓4̸̛̦̮̠̥̱̏: Usuário não encontrado no c̵̳͕͎͎̲̦̩̝̮̖͓̦̊̆̈̈́̓́̓̊͋̓͐͋̈͋̏ͅȁ̷̢̡̨̢̙̲̩͍̤̻͎͐̇̓͛͛̆͜ͅn̶̪͚̤̪͎͚͕̹̫͕̹̿͑͊͂͑̓̎̈́͐̅̚͘͝ǎ̷̮̞̮͔͐͋͆̋̈̿̃͗̒̓̆͘͠ĺ̸̨͔̈́ ̶̢̗̦̘̰͚̦̗̥̳̼͈̼̥̗͊͆̃̓d̸̢̖̭̹͔͑̆̾̇̍̌̂͛̍̎̏͛̂͝ȩ̸̛̤͙̩̱͓̲͍͇̜͐͊͌͋͋̚ ̵̧̨̛̬̳̖̲̖͍̯̲̠̝̿̑̍͒̇͋̔͆̓͝ͅv̶̟̟͖̼̬̻̜̝̜̳̞̈͒ǫ̴̢̯͎̥͚͕͍̘̱̆̐̀̽̀́̈́͌͛̂̒̚ͅz̷̺̞̦̅͒͌̀̿́̐̄̅͋͌̅̈́̈́ ')
                	await ctx.send(f'Ē̵̛̫͗̎̔̿̌̾̕r̴̀̉̃̋̀́͑̏̑͆͊̚͝͝ͅr̷͓̗̿͗̇ǫ̶͚̓̓̈́͋̽͊̄̈́͆͝ŗ̷̧̗̦̣̞̥̼͖͚̯̗̥̀͑̂͜ ̷̢̧̼͈͙̹͉͈̾̿͊́̾͜ͅ4̵͙͖̼̞͌̏̆0̴̜̖͕̯̝͖̗̓4̸̛̦̮̠̥̱̏: Usuário não encontrado no c̵̳͕͎͎̲̦̩̝̮̖͓̦̊̆̈̈́̓́̓̊͋̓͐͋̈͋̏ͅȁ̷̢̡̨̢̙̲̩͍̤̻͎͐̇̓͛͛̆͜ͅn̶̪͚̤̪͎͚͕̹̫͕̹̿͑͊͂͑̓̎̈́͐̅̚͘͝ǎ̷̮̞̮͔͐͋͆̋̈̿̃͗̒̓̆͘͠ĺ̸̨͔̈́ ̶̢̗̦̘̰͚̦̗̥̳̼͈̼̥̗͊͆̃̓d̸̢̖̭̹͔͑̆̾̇̍̌̂͛̍̎̏͛̂͝ȩ̸̛̤͙̩̱͓̲͍͇̜͐͊͌͋͋̚ ̵̧̨̛̬̳̖̲̖͍̯̲̠̝̿̑̍͒̇͋̔͆̓͝ͅv̶̟̟͖̼̬̻̜̝̜̳̞̈͒ǫ̴̢̯͎̥͚͕͍̘̱̆̐̀̽̀́̈́͌͛̂̒̚ͅz̷̺̞̦̅͒͌̀̿́̐̄̅͋͌̅̈́̈́ ')
                	await ctx.send(f'Ē̵̛̫͗̎̔̿̌̾̕r̴̀̉̃̋̀́͑̏̑͆͊̚͝͝ͅr̷͓̗̿͗̇ǫ̶͚̓̓̈́͋̽͊̄̈́͆͝ŗ̷̧̗̦̣̞̥̼͖͚̯̗̥̀͑̂͜ ̷̢̧̼͈͙̹͉͈̾̿͊́̾͜ͅ4̵͙͖̼̞͌̏̆0̴̜̖͕̯̝͖̗̓4̸̛̦̮̠̥̱̏: Usuário não encontrado no c̵̳͕͎͎̲̦̩̝̮̖͓̦̊̆̈̈́̓́̓̊͋̓͐͋̈͋̏ͅȁ̷̢̡̨̢̙̲̩͍̤̻͎͐̇̓͛͛̆͜ͅn̶̪͚̤̪͎͚͕̹̫͕̹̿͑͊͂͑̓̎̈́͐̅̚͘͝ǎ̷̮̞̮͔͐͋͆̋̈̿̃͗̒̓̆͘͠ĺ̸̨͔̈́ ̶̢̗̦̘̰͚̦̗̥̳̼͈̼̥̗͊͆̃̓d̸̢̖̭̹͔͑̆̾̇̍̌̂͛̍̎̏͛̂͝ȩ̸̛̤͙̩̱͓̲͍͇̜͐͊͌͋͋̚ ̵̧̨̛̬̳̖̲̖͍̯̲̠̝̿̑̍͒̇͋̔͆̓͝ͅv̶̟̟͖̼̬̻̜̝̜̳̞̈͒ǫ̴̢̯͎̥͚͕͍̘̱̆̐̀̽̀́̈́͌͛̂̒̚ͅz̷̺̞̦̅͒͌̀̿́̐̄̅͋͌̅̈́̈́ ')
            else:
                await ctx.send("Houve empate e ninguém foi ejetado")
