import requests
import random  

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
    url = 'https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg'
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
