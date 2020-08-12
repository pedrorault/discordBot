from spyBot.locaisEpapeis import *
from spyBot.partidaSpy import *
from discord.ext import commands
import asyncio

dictPartidas = dict()
class SpyCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spy(self,ctx):
        channelId = ctx.message.channel.id
        if channelId not in dictPartidas.keys():
            msg = await ctx.send("Clique na reação para entrar na partida.\nQuando todos estiverem prontos, digite .start\nMínimo: 3 jogadores\t Máx: 8 jogadores")
            emoji = '\U0001F44C'
            await msg.add_reaction(emoji)
            await asyncio.sleep(3)
            msg2 = await ctx.fetch_message(msg.id) #permanent on server
            dictPartidas[channelId] = Partida(channelId,msg2)
        else:
            await ctx.send("Partida registrada como ativa, para reiniciar digite .stop")

    @commands.command()
    async def start(self,ctx):
        channelId = ctx.message.channel.id
        if channelId in dictPartidas.keys():
            msgid = dictPartidas[channelId].idJoin.id
            msgObj = await ctx.fetch_message(msgid) #Recriar objeto Message pra ter as novas reações
            async for user in msgObj.reactions[0].users():
                if user != self.bot.user:
                    dictPartidas[channelId].incluirJogador(user)
            if dictPartidas[channelId].prontoJogadoresInicio():
                await ctx.send("Enviando roles por mensagem privada.")
                lista = dictPartidas[channelId].distribuirRoles()
                for i in lista:
                    directm =  await i[0].create_dm()
                    await directm.send(i[1])
            else:
                pass
                await ctx.send("Número de jogadores inválido")
        else:
            await ctx.send("Partida não ativa, para iniciar digite .spy")

    @commands.command()
    async def helpspy(self,ctx):
        msg = (".spy - Começa uma partida\n"
        ".stop - Para a partida\n"
        ".start - Começa/Recomeça o round com os jogadores que já deram join.\n"
        ".vote - Começa a votação e envia a lista de locais para o espião.\n"
        ".local - Espião vota no local, ex:  \".local Avião\"")
        await ctx.send(msg)

    @commands.command()
    async def stop(self,ctx):
        channelId = ctx.message.channel.id
        if channelId in dictPartidas.keys():
            obj = dictPartidas.pop(channelId)
            del obj
            await ctx.send("Partida anterior do canal encerrada.")
        else:
            await ctx.send("Não há partida ativa no canal.")

    @commands.command()
    async def vote(self,ctx):
        channelId = ctx.message.channel.id
        if channelId in dictPartidas.keys():
            await ctx.send("Votem falando que é mais fácil. (Enviando DM pro espião)")
            directm = await dictPartidas[channelId].spyPlayer.create_dm()
            lista = getPrintableLocationList()
            await directm.send("Responda com um dos seguintes lugares:\n{}".format(lista))
        else:
            await ctx.send("Não há partida ativa no canal.")


    @commands.command()
    async def local(self,ctx):
        channelId = ctx.message.channel.id
        if channelId in dictPartidas.keys():
            if ctx.message.author == dictPartidas[channelId].spyPlayer:
                resp = ctx.message.content.split(".local ")
                if resp[1] in getLocationList():
                    if resp[1] != '' and resp[1] == dictPartidas[channelId].locationRound:
                        await ctx.send("O espião acertou o local.")
                        #await stop(self,ctx)
                    else:
                        await ctx.send("O espião errou o local.")
                        #await stop(self,ctx)
                else:
                    await ctx.send("Local inválido")
        else:
            await ctx.send("Não há partida ativa no canal.")
