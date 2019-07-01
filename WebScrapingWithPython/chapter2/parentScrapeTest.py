from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
except HTTPError as e:
    print("http error : " + e.code)

try:
    bsObj = BeautifulSoup(html, "html.parser")
    print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous__siblings.get_text())
except AttributeError as e:
    print("attribute error:"+e.code)




