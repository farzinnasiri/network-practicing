from socket import *
# DNS lookup will automatically be performed to get the IP address
serverName = 'localhost'
# random port number
serverPort = 12121
# creating client socket with IPv4 and UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input your sentence in lowercase:')
# encode message to byte
clientSocket.sendto(message.encode(), (serverName, serverPort))
# waiting for the response ( buffer size = 2048)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
