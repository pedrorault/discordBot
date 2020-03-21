import requests
import random  

def randomPoke():
    x = random.randrange(1,152)
    y = random.randrange(1,152)
    url = 'https://images.alexonsager.net/pokemon/fused/{0}/{0}.{1}.png'.format(x,y)
    r = requests.get(url,allow_redirects=True)
    name = 'poke.png'
    open(name,'wb').write(r.content)
    return name
