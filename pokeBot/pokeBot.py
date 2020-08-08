import requests
import random
import json
from difflib import get_close_matches
import os

def choosePoke(x,y):
    if x in range(1,152):
        if y in range(1,152):
            return getPoke(x,y)
        else:
            return randomPoke()

def randomPoke():
    x = random.randrange(1,152)
    y = random.randrange(1,152)
    return getPoke(x,y)

def pokemonLogo():
    url = 'https://logodownload.org/wp-content/uploads/2017/08/pokemon-logo.png'
    r = requests.get(url,allow_redirects=True)
    logo = 'logo.png'
    open(logo,'wb').write(r.content)
    return logo

def getPoke(x,y):
    url = 'https://images.alexonsager.net/pokemon/fused/{0}/{0}.{1}.png'.format(x,y)
    r = requests.get(url,allow_redirects=True)
    name = 'poke.png'
    open(name,'wb').write(r.content)
    return name

def getPokeList():
    tmpList = []
    with open("./pokeBot/pokemon.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n","").split(" ")
            pokeObj = {
                "id": line[0],
                "name": line[1]
            }
            tmpList.append(pokeObj)
    return tmpList

def whichPoke(arg):
    pokeList = getPokeList()
    # The list is read already ordered, so to access a certain index it's simply Number-1

    pokeId = None
    foundPoke = True

    if(arg.isdigit()) and int(arg) > 0 and int(arg) < 891:
        poke = pokeList[int(arg)-1]
        pokeId = int(poke["id"])

    else:
        nomes = []
        for item in pokeList:
            nomes.append(item['name'])
            if arg.lower() == item["name"].lower():
                pokeId = int(item["id"])

        if not pokeId:
            result = get_close_matches(arg,nomes)
            if len(result) > 1:
                closestMatches = ', '.join(result)
                pokeName = f'Você quis dizer: {closestMatches}?'
                foundPoke = False
            elif len(result) == 1:
                pokeId = whichPoke(result[0])[0]
    
    return [pokeId,foundPoke] if foundPoke else [pokeName, foundPoke]
