from urllib import request ,parse
def youdao(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {

        'i': 'girl',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    data = parse.urlencode(data).encode()
    headers = {
                    'Accept': 'application / json, text / javascript, * / *; q = 0.01',
                    'Accept - Encoding': 'gzip, deflate',
                    'Accept - Language': 'zh - CN, zh;',
                    'Connection': 'keep - alive',
                    'Content - Length': '234',
                    'Content - Type': 'application / x - www - form - urlencoded;',
                    'charset ': 'UTF - 8',
                    'Cookie': 'OUTFOX_SEARCH_USER_ID = -2117044059 @ 10.169.0.83;',
                    'Host': 'fanyi.youdao.com',
                    'Origin' : 'http: // fanyi.youdao.com',
                    'Referer': 'http: // fanyi.youdao.com /',
                    'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36',
                    'X - Requested - With': 'XMLHttpRequest'
    }
    res = request.Request(url,data=data,headers=headers)
    rsp = request.urlopen(res)
    html = rsp.read().decode()
    print(html)

def getsalt():
    import random,time
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt
def getmd5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v,encoding='uft-8')
    sign = md5.hexdigest()
    return sign
def getsign(key):
    sign = 'fanyideskweb'+key+str(getsalt())+"ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getmd5(sign)
    return sign

if __name__ == "__main__":
    youdao("girl")