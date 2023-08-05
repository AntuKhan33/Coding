import socket
s=socket.socket()
host=socket.gethostname()
port=443


s.bind((host,port))
s.listen(5)


c,addr=s.accept()
print('got connection from',addr)


while True:
    data=c.recv(1024).decode()
    if not data:
        break
    
    print(str(data))
    
c.close()