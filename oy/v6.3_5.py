from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.12306.cn/mormhweb/"

rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)