import requests
import random  

def choosePoke(x,y):
    if type(x) is int and type(y) is int:
        if x in (1,152) and y in (1,152):
            return getPoke(x,y)
        else:
            return randomPoke()

def randomPoke():
    x = random.randrange(1,152)
    y = random.randrange(1,152)
    return getPoke(x,y)

def getPoke(x,y):
    url = 'https://images.alexonsager.net/pokemon/fused/{0}/{0}.{1}.png'.format(x,y)
    r = requests.get(url,allow_redirects=True)
    name = 'poke.png'
    open(name,'wb').write(r.content)
    return name
