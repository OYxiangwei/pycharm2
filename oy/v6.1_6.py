from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart
import smtplib
from email.header import Header
mail_mul = MIMEMultipart()
mail_text = MIMEText("i like hacker","plain","utf-8")
head_from = Header("阳祥伟发的","utf-8")
mail_text["From"] = head_from
head_to = Header("去他的",'utf-8')
mail_text["To"] = head_to
head_sub = Header("这是主题，辞职","utf-8")
mail_text["Subject"] = head_sub
mail_mul.attach(mail_text)

with open("student.xhtml","rb")as f:
    s = f.read()
    m = MIMEText(s,"base64","utf-8")
    m["Content-Type"] = "application/octet-stream"
    m["Content-Disposition"] = "attachment:filenname ='student.xhtml'"
    mail_mul.attach(m)

from_addr = "992543768@qq.com"
from_pwd = "inbrlvqdrxwnbbcj"
to_addr = "992543768@qq.com"
smtp_srv = "smtp.qq.com"
try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,to_addr,mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)