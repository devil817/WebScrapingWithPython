from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

try:
    html = urlopen("http://en.wikipedia.org/wiki/kevin_Bacon")
except HTTPError as e:
    print(e)

try:
    bsObj = BeautifulSoup(html, "html.parser")
    links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^/wiki/((?!:).)*$"))
    for link in links:
        if 'href' in link.attrs:
            print(link.attrs['href'])
except AttributeError as e:
    print(e)


