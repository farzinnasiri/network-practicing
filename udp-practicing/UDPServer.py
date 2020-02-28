from socket import *
serverPort = 12121
serverSocket = socket(AF_INET, SOCK_DGRAM)
# assign port to server socket
serverSocket.bind(('', serverPort))
print("The server is ready to receive!")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(clientAddress)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
