import socket
import sys

if len(sys.argv) == 0:
    print("Error: usage: client <port>")
    exit()

port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '127.0.0.1'

server_socket.bind((IP, port))
server_socket.listen(5)
client_socket, client_ip = server_socket.accept()

print(client_ip[0] + ":" + str(client_ip[1]) +  " connected")

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    message = data.decode()
    print(message)

    result = eval(message)

    client_socket.sendall((str(result)+"\n").encode("utf-8"))
