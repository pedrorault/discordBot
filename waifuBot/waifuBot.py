from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

def getWaifuFromScrapping():
    url = "https://www.thiswaifudoesnotexist.net/"
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(chrome_options=chrome_options) 
    #chromedriver already installed by Heroku, otherwise set path to chromedriver
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')    
    imgTag = soup.find_all('img')[1] 
    imgLink = 'http:' + imgTag['src']
    r = requests.get(imgLink,allow_redirects=True)
    open('img.jpg','wb').write(r.content)
    driver.close()