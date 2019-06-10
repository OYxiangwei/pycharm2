from urllib import request,parse
from http import cookiejar

#cookie = cookiejar.CookieJar()
#filename = "cookie.txt"
#cookie = cookiejar.MozillaCookieJar(filename)
cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt",ignore_discard=True,ignore_expires=True)
cookie_hand = request.HTTPCookieProcessor(cookie)
http_hand = request.HTTPHandler()
https_hand = request.HTTPSHandler()
openr = request.build_opener(cookie_hand,http_hand,https_hand)
def login():
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"aidream.1314@163.com",
        "password":"woaixiaomeng1314"
    }
    data = parse.urlencode(data)
    req= request.Request(url,data=data.encode())
    rsp = request.urlopen(req)
def gethomepage():
    url = "http://www.renren.com/273441698/profile"
    rsp = openr.open(url)
    #cookie.save(ignore_discard=True,ignore_expires=True)
    html = rsp.read().decode('utf-8')
    with open("v5.html","w")as f:
        f.write(html)

if __name__ == "__main__":
    login()
    gethomepage()