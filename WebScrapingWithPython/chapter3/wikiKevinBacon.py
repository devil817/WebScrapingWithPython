from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())

def getLinks(url):
    try:
        html = urlopen("http://en.wikipedia.org"+url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^/wiki/((?!:).)*$"))
        return links
    except AttributeError as e:
        print(e)
        return None

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0 :
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
