import requests
import json
url = "https://fanyi.baidu.com/sug"
data = {'kw':'girl'}
headers = {'Content-Length':str(len(data))}
rsp = requests.post(url,data = data ,headers=headers)
print(rsp.text)
print(rsp.json())