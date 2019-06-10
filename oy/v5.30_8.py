import socket
def serverfunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr = ("127.0.0.1",7852)
    sock.bind(addr)
    data,addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    text = data.decode()
    print(type(text))
    print(text)
    rsp = "i recev"
    data = rsp.encode()
    sock.sendto(data,addr)

def clientfunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = "i love hack"
    data = text.encode()
    sock.sendto(data,("127.0.0.1",7852))
    data,addr = sock.recvfrom(200)
    text = data.decode()
    print(text)
if __name__=="__main__":
    import time
    while 1:
        try:
            serverfunc()
        except Exception as e:
            print(e)
        time.sleep(3)
            #clientfunc()