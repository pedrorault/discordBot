import requests
import random
import waifuBot.sendImageFromWeb

def getWaifu():
    i = random.randrange(1000,100000)
    url = "https://www.thiswaifudoesnotexist.net/example-{}.jpg".format(i)    
    r = requests.get(url,allow_redirects=True)
    open('img.jpg','wb').write(r.content)

def getFurry():
    i = random.randrange(0,100000)
    url = f'https://thisfursonadoesnotexist.com/v2/jpgs/seed{i:05}.jpg'
    r = requests.get(url,allow_redirects=True)
    open('fur.jpg','wb').write(r.content)

def getPerson():
    url = f'https://thispersondoesnotexist.com/image'
    r = requests.get(url,allow_redirects=True)
    open('person.jpg','wb').write(r.content)
    
