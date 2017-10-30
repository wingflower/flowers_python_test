from socket import *

# HOST = '127.0.0.1'
HOST = '192.168.1.5'
PORT = 30001
BUFSIZE = 1024

serverSock = socket(AF_INET, SOCK_DGRAM)

serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSock.bind((HOST, PORT))

cnt = 0

while True:
    cnt += 1
    data, addr = serverSock.recvfrom(BUFSIZE)
    print("[%d] data : " % cnt, data.decode())

serverSock.close()
