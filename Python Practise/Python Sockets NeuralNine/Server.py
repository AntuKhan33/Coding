import socket

Host='192.168.31.140'
Port=4444

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((Host,Port))
server.listen(5)


while True:
        communication,address =server.accept()
        print(f"connected to {address}")
        message=communication.recv(1024).decode('utf-8')
        print(f"message from{message}")
        communication.send(f'got your message'.encode('utf-8'))
        communication.close()
        print(f'connectiong with {address} ended')

