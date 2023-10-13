import socket

servSock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         proto=0)
print("Сокет создан")
servSock.bind(('localhost', 53210))
servSock.listen(1)
print("Прослушивание портов...")

while True:
    clientSock, clientAddr = servSock.accept()
    print("Соединение соединено с ", clientAddr)
    while True:
        data = clientSock.recv(1024)
        if not data:
            break
        print(data.decode())
        print('получили')
        clientSock.sendall(((data.decode()).upper()).encode())
    clientSock.close()