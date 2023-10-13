import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('localhost', 53210))
clientSock.send(input().encode())
data = clientSock.recv(1024)
clientSock.close()
print(data.decode())