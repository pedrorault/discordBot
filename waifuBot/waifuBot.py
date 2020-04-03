import requests
import random

def getWaifuFromScrapping():
    i = random.randrange(1000,100000)
    url = "https://www.thiswaifudoesnotexist.net/example-{}.jpg".format(i)    
    r = requests.get(url,allow_redirects=True)
    open('img.jpg','wb').write(r.content)