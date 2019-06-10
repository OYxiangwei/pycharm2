import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
def getmsg():
    email = "992543768@qq.com"
    pwd = "inbrlvqdrxwnbbcj"
    pop3_srv ="pop.qq.com"
    srv = poplib.POP3_SSL(pop3_srv)
    srv.user(email)
    srv.pass_(pwd)
    msgs,counts = srv.stat()
    print("Message:{0},size:{1}".format(msgs,counts))
    rsp , mails,octets = srv.list()
    print(mails)
    index = len(mails)
    rsp,lines,octets =srv.retr(index)
    print(rsp,lines,octets)
if __name__ == "__main__":
    getmsg()