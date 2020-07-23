import requests
import os

lastPokemonNum = 890
imgDir = "./pokeBot/pokes"

if not os.path.isdir(imgDir):
    os.mkdir(imgDir)
    for i in range(1,lastPokemonNum+1):
        url = f'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{i:03}.png'
        r = requests.get(url)
        open(f'./pokeBot/pokes/{i:03}.png','wb').write(r.content)
else:
    print("Already downloaded images")