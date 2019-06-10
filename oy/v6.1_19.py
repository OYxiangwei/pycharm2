from urllib import request
from urllib import parse
if __name__=="__main__":
    url = "http://www.baid.com/s?"
    wd = input("input you word :")
    qs = {"wd":wd}
    qs =parse.urlencode(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    print(type(html))
    html = html.decoed()
    print(html)