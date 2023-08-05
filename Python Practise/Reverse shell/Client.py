import socket
s=socket.socket()
host=socket.gethostname()
port=15200 

s.connect((host,port))
message=input('=>')
while message!='Q':
    s.send(message.encode())
    message=input("=>")
s.close()