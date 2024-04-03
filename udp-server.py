import socket
import sys

if len(sys.argv) == 0:
    print("Error: usage: client <port>")
    exit()

port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = '127.0.0.1'

server_socket.bind((IP, port))

while True:
    data, address = server_socket.recvfrom(1024)
    if not data:
        break
    
    print("command from " + address[0] + ":" + str(address[1]))

    message = data.decode()
    print(message)

    result = eval(message)

    server_socket.sendto((str(result)+"\n").encode("utf-8"), address)
