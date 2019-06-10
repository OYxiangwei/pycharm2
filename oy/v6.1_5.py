import smtplib
from email.mime.text import MIMEText
mail_content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE html
                PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
                "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
        <head>
            <title>student</title>
        </head>
        <body>
            <school>

                <div>
                    <studnt>
                        <name> Anonymous</name>
                        <age> 41</age>
                        <score>math:&gt;70</score>
                    </studnt>
                </div>

            </school>
        </body>
        </html>
                
"""
msg = MIMEText(mail_content,"html","utf-8")
from_addr = "992543768@qq.com"
from_pwd = "inbrlvqdrxwnbbcj"
to_addr = "992543768@qq.com"
smtp_srv = "smtp.qq.com"
try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,to_addr,msg.as_string())
    srv.quit()
except Exception as e:
    print(e)