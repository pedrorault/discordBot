import sys
sys.path.insert(0,'..')
from spyBot.locaisEpapeis import getLocation, getNroles
from random import choice
import discord 

class Partida:
    players = []
    spyPlayer = None
    locationRound = None
    channelResposta = None
    idJoin = None

    def __init__(self, channel : int, idJoin):
        self.channelResposta = channel
        self.idJoin = idJoin
        
    def incluirJogador(self,member):
        #TODO: tirar return, pq sim
        if len(self.players) <= 8 and member not in self.players:
            self.players.append(member)
            return True
        else:
            return False
    
    def prontoJogadoresInicio(self):
        nPlayers = len(self.players)
        if nPlayers >= 3 and nPlayers <= 8:
            return True
        else:
            return False

    def distribuirRoles(self):
        lista = list()
        self.locationRound = getLocation()
        roles = getNroles(len(self.players),self.locationRound)
        for x in self.players:
            papel = choice(roles) #random.choice(roles)
            roles.remove(papel)
            if papel != "Espião" and papel != "Spy":
                message = "Localização: {}\nPapel: {}".format(self.locationRound,papel)
            else:
                message = "Localização: Desconhecida\nPapel: {}".format(papel)
                self.spyPlayer = x
            lista.append((x,message))
        return lista