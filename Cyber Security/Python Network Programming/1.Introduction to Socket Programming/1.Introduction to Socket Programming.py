import socket
import sys
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket is created")
except socket.error as err:
    print(f'socket creating failed with error{err}')
    
    
port=808
try:
    host_ip=socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('erro resolving the host')
    sys.exit()
server_socket.connect((host_ip,port))
print(f'socket has successfully connected to github on port {host_ip}')