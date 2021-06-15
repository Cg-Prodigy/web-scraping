from urllib.request import urlopen
from bs4 import BeautifulSoup

theurl=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj=BeautifulSoup(theurl.read(),'html5lib')
print(bsObj)
emel_list=bsObj.find_all('span', {'class','red'})


for each in emel_list:
    print(each.get_text())
