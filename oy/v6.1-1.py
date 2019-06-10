import socket

def tcp_sev():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    add = ("127.0.0.1",8998)
    sock.bind(add)
    sock.listen()
    while True:
        skt,addr = sock.accept()
        msg = skt.recv(500)
        msg = msg.decode()
        rst ="received msg :{0} from{1}".format(msg,addr)
        print(rst)
        skt.send(rst.encode())
        skt.close()

if __name__=="__main__":
    print("start tcp ")
    tcp_sev()
    print("ending tcp")