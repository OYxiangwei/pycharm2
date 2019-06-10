import smtplib
from email.mime.text import MIMEText
msg = MIMEText("i ma a hacker","plain","utf-8")
from_addr = "992543768@qq.com"
from_pwd = "inbrlvqdrxwnbbcj"
to_addr = "992543768@qq.com"
smtp_srv = "smtp.qq.com"
try:
    srv=smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,to_addr,msg.as_string())
    srv.quit()
except Exception as e:
    print(e)