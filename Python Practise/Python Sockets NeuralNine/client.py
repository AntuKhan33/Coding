import socket

from Server import Port
Host='192.168.31.140'
Port=4444
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

socket.send("hello wolrd".encode('utf-8'))
print(socket.recv(1024))