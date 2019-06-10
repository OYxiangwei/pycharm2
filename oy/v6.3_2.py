from urllib import request,error
if __name__ =="__main__":
    baseurl = "https://www.baidu.com"
    proxy = {'http':'120.194.18.90:81'}
    proxy_hander = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_hander)
    request.install_opener(opener)
    try:
        #headers = {}
        #headers["user-agent"]="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        #req = request.Request(baseurl,headers=headers)
        req = request.Request(baseurl)
        req.add_header("user-agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e.reason)
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)