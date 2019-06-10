from urllib import request
if __name__ == "__main__":
    url ="http://sc.renren.com/scores/mycalendar"
    headers = {"Cookie":"anonymid=jvfezlxg83ydcs; depovince=GW; jebecookies=632b8541-7c4f-4bed-8438-687921d5ce59|||||; _r01_=1; ick_login=0bf2b304-6ff6-4263-87b0-4849614d8b2b; _de=F1483E038E280C871F5F70D757545BF75212E40F3D18115C; p=79934319966cfec95996b1064d6301ea8; first_login_flag=1; ln_uact=aidream.1314@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn511/20090512/0325/main_03PL_5164f204236.jpg; t=d5916669617667c83881ce34425c4d878; societyguester=d5916669617667c83881ce34425c4d878; id=273441698; xnsid=e1f75fe7; ver=7.0; loginfrom=null; jebe_key=fe572cd5-16da-4754-b1b2-7a892d35a880%7Cf23f6b90d4771e3df2ee0800d4b90ae7%7C1559577014705%7C1%7C1559577014754; JSESSIONID=abc88P6zFqp1L7mGlcESw; __guid=87517466.899863278795494900.1559577016546.8064; monitor_count=3; wp_fold=0"}
    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode('utf-8')
    with open("v2html.html","w")as f:
        f.write(html)
