# -*- coding : utf-8 -*-

from socket import *

import sys

HOST = '127.0.0.1'
SPORT = 30000
CPORT = 30001
BUFSIZE = 1024

clientSock = socket(AF_INET, SOCK_DGRAM)

clientSock.bind((HOST, CPORT))

while True:
    try:
        val = input("Input : ")
        if val.lower() == "quit":
            sys.exit()

        clientSock.sendto(val.encode(), (HOST, SPORT))

        data, addr = clientSock.recvfrom(BUFSIZE)

        print("data : ", data.decode())
        print("addr : ", addr)
    except KeyboardInterrupt:
        clientSock.close()
