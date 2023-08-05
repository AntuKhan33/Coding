import socket
s=socket.socket()
port=5678
s.connect(('127.0.0.1',port))
print(s.recv(1024))
s.close()