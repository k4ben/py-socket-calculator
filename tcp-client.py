import socket
import sys

if len(sys.argv) < 2:
    print("Error: usage: client <host> <port>")
    exit()

ip = socket.gethostbyname(sys.argv[1])
port = int(sys.argv[2])

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((ip, port))

print("Connected to " + ip + ":" + str(port))

i = input("calc> ")
clientsocket.send(i.encode("utf-8"))

while True:
    data = clientsocket.recv(1024)
    if not data:
        break
    
    message = data.decode()
    print(message)
    i = input("calc> ")
    clientsocket.send(i.encode("utf-8"))
