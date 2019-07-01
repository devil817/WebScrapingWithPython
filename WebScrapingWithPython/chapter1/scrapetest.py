from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.title
    except AttributeError as e:
        return None

    return title

title = getTitle("http://www.pythonscraping.com/pages/warandpeace.html")
if title == None:
    print("Title could not be found")
else:
    print(title)