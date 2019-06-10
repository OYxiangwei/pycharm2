import requests
url = "https://www.baidu.com/s?"
data = {'kw':'王八蛋'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
rsp = requests.get(url,params=data ,headers = headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.status_code)
print(rsp.encoding)
#rsp2 = requests.request("get",url)
#print(rsp2.text)