from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
    print("http error" + e.code)

try:
    bsObj = BeautifulSoup(html, "html.parser")
    nameList = bsObj.findAll("span", {"class":"green"})
    for name in nameList:
        print(name.get_text())
except AttributeError as e:
    print("attribute error")