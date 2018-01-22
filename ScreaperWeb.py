from urllib.request import urlopen
from bs4 import BeautifulSoup
content = urlopen("https://www.ebay.com")
#print(content.read())
sou = BeautifulSoup(content.read(),"lxml")
print(sou.h1)


