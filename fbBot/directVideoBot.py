from bs4 import BeautifulSoup as bs
import requests
import re
from urllib import parse

FB_VIDEO_PREFIX="www.facebook.com/watch?v="

def convert_url(url: str = ""):
    if url is None or url.strip() == "":
        return "Error: Url é vazia"
    if FB_VIDEO_PREFIX not in url:
        return f"Error: URL tem que estar no formato {FB_VIDEO_PREFIX}"
    return url.replace("www","mbasic")

async def scrap_for_video(url: str = ""):
    converted_url = convert_url(url)
    respose = requests.get(converted_url)
    body = respose.text
    soup = bs(body, "html.parser")
    anchor_video = soup.find("a", attrs={"target":"_blank", "href":re.compile("\/video_redirect")})
    href_video = anchor_video.attrs['href']
    link = href_video.split("/video_redirect/?src=")[1]
    unquoted_link = parse.unquote(link)
    return unquoted_link
