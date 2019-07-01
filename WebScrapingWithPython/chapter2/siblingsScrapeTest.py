from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
except HTTPError as e:
    print("error code:"+e.code)

try:
    bsObj = BeautifulSoup(html, "html.parser")
    for item in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
        print(item)
except AttributeError as e:
    print("attribute error:"+e.__doc__)


