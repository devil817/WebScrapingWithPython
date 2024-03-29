from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

try:
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
except HTTPError as e:
    print(e)

try:
    bsObj = BeautifulSoup(html, "html.parser")
    images = bsObj.findAll("img",{"src":re.compile("\.\./img/gifts/img.*\.jpg")})
    for image in images:
        print(image.attrs["src"])

    tagLen2 = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
    for item in tagLen2:
        if item is not None:
            print(item)

except AttributeError as e:
    print(e)

