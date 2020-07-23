from bs4 import BeautifulSoup
import requests

# Useful to get it up to date, but otherwise just to have it wrote down how I dit it

url = requests.get('https://pokemondb.net/pokedex/national').content
soup = BeautifulSoup(url,'html.parser')
allPokes = soup.find_all("span",class_="infocard-lg-data text-muted")

allPokes = list(map(lambda x : x.text.replace('#','').split(" "), allPokes))
for i in allPokes:
    try:
       i.remove('·')
    except:
        pass

fileA = open("pokemon.txt", "w",encoding="utf-8")
for number,poke, *_ in allPokes:
    txt = f'{number} {poke}\n'
    fileA.write(txt)
fileA.close()