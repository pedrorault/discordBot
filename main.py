import discord 
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import asyncio
import os
from waifuBot.waifuBot import getWaifuFromScrapping, getFurry, getPerson
from pokeBot.pokeBot import randomPoke, choosePoke, pokemonLogo,whichPoke
from spyBot.partidaSpy import Partida
from spyBot.locaisEpapeis import getLocation,getNroles, getPrintableLocationList, getLocationList


client = commands.Bot(command_prefix = '.',description=".help para os comandos")
dictPartidas = dict()

def firstTimeScripts():
    exec(open("./pokeBot/scripts/downloadPokemonImages.py").read())

@client.event
async def on_ready():
    print("Bot is ready")
    firstTimeScripts()

@client.command()
async def pokemon(ctx):   
    file = pokemonLogo()
    await ctx.send(file=discord.File(file))
    
@client.command()
async def poke(ctx):
    msg = (ctx.message.content.replace(".poke ","")).split(" ")
    if len(msg) == 2:
        try:
            x = int(msg[0])
            y = int(msg[1])
            file = choosePoke(x,y)
        except:
            file = randomPoke()
    elif len(msg) == 1:
        if msg[0] == ".poke":
            file = randomPoke()
        else:
            cnt, file = whichPoke(msg[0])
            if cnt != "" and file !="":
                return await ctx.send(content=cnt, file=discord.File(file))
            elif cnt != "":
                return await ctx.send(content=cnt)
            else:
                return 
    else:
        file = randomPoke()
    await ctx.send(file=discord.File(file))

@client.command()
async def waifu(ctx):       
    getWaifuFromScrapping()
    await ctx.send(file=discord.File('img.jpg'))

@client.command()
async def furry(ctx):       
    getFurry()
    await ctx.send(file=discord.File('fur.jpg'))

@client.command()
async def person(ctx):       
    getPerson()
    await ctx.send(file=discord.File('person.jpg'))

@client.command()
async def spy(ctx):   
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

@client.command()
async def start(ctx):
    channelId = ctx.message.channel.id
    if channelId in dictPartidas.keys():
        msgid = dictPartidas[channelId].idJoin.id
        msgObj = await ctx.fetch_message(msgid) #Recriar objeto Message pra ter as novas reações
        async for user in msgObj.reactions[0].users():
            if user != client.user:
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

@client.command()
async def helpspy(ctx):
    msg = """.spy - Começa uma partida
.stop - Para a partida  
.start - Começa/Recomeça o round com os jogadores que já deram join.
.vote - Começa a votação e envia a lista de locais para o espião.
.local - Espião vota no local, ex:  ".local Avião"
    """
    await ctx.send(msg)

@client.command()
async def stop(ctx):
    channelId = ctx.message.channel.id
    if channelId in dictPartidas.keys():
        obj = dictPartidas.pop(channelId)
        del obj
        await ctx.send("Partida anterior do canal encerrada.")
    else:
        await ctx.send("Não há partida ativa no canal.")  

@client.command()
async def vote(ctx):
    channelId = ctx.message.channel.id
    if channelId in dictPartidas.keys():
        await ctx.send("Votem falando que é mais fácil. (Enviando DM pro espião)")
        directm = await dictPartidas[channelId].spyPlayer.create_dm()
        lista = getPrintableLocationList()
        await directm.send("Responda com um dos seguintes lugares:\n{}".format(lista))
    else:
        await ctx.send("Não há partida ativa no canal.")


@client.command()
async def local(ctx):
    channelId = ctx.message.channel.id
    if channelId in dictPartidas.keys():    
        if ctx.message.author == dictPartidas[channelId].spyPlayer:
            resp = ctx.message.content.split(".local ")            
            if resp[1] in getLocationList():
                if resp[1] != '' and resp[1] == dictPartidas[channelId].locationRound:
                    await ctx.send("O espião acertou o local.")
                    #await stop(ctx)
                else:
                    await ctx.send("O espião errou o local.")
                    #await stop(ctx)
            else:
                await ctx.send("Local inválido")
    else:
        await ctx.send("Não há partida ativa no canal.")

@client.command()
async def clear(ctx):
    commands = ['.spy','.start','.vote', '.local', '.stop','.clear','.helpspy','.waifu','.poke','.furry','.person' ]
    async for msg in ctx.channel.history(limit=50):
        if msg.author == client.user or msg.content.startswith(tuple(commands)):
            await discord.Message.delete(msg)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

token = os.environ.get('TOKEN')
client.run(token)