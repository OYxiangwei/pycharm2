from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()
soup = BeautifulSoup(content,'lxml')
content = soup.prettify()
#print(content)
print("="*10)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['href'])
soup.link.attrs['type']='hhhahah'
print(soup.link)
print("-"*12)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("=="*12)
print(soup.name)
print(soup.attrs)
print("#"*23)
for node in soup.head.contents:
    if node.name =="meta":
        print(node)
    if node.name =="title":
        print(node.string)
print("&"*33)
import re
tags = soup.find_all(re.compile('^me'),content="always")
for tag in tags:
    print(tag)
