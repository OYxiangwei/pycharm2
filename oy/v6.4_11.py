from urllib import request,parse
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
print(soup.prettify())
print("*"*111)
titles = soup.select('title')
print(titles[0])
print("*"*22)
print(soup.select("meta[content='always']"))
