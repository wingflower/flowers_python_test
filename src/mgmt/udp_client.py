from socket import *

HOST = '127.0.0.1'
SPORT = 30000
CPORT = 30001
BUFSIZE = 1024

clientSock = socket(AF_INET, SOCK_DGRAM)

clientSock.bind((HOST, CPORT))

clientSock.sendto('"data01":hello01, "data02":hello02'.encode(), (HOST, SPORT))

data, addr = clientSock.recvfrom(BUFSIZE)

for d in data.decode().split(','):
    print("data : ", d)
print("addr : ", addr)

clientSock.close()

