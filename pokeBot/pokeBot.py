import requests
import random  

<<<<<<< HEAD
def choosePoke(x,y):
    if type(x) is int and x in range(1,152):
        if type(y) is int and y in range(1,152):
            return getPoke(x,y)
        else:
            return randomPoke()

=======
>>>>>>> parent of 7f01e55... add option to specify 2 random pokemon
def randomPoke():
    x = random.randrange(1,152)
    y = random.randrange(1,152)
    url = 'https://images.alexonsager.net/pokemon/fused/{0}/{0}.{1}.png'.format(x,y)
    r = requests.get(url,allow_redirects=True)
    name = 'poke.png'
    open(name,'wb').write(r.content)
    return name
