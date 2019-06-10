import json
from urllib import request, parse

baseurl = 'https://fanyi.baidu.com/sug'
data ={'kw':'girl'}
data = parse.urlencode(data).encode('utf-8')
headers = {'content-length':len(data)}
req = request.Request(url=baseurl,data=data,headers=headers)
print(req)
rsp = request.urlopen(req)
html = rsp.read().decode('utf-8')
print(html)
py = json.loads(html)
print(py)
for item in py['data']:
    print(item['k'],"----",item['v'])