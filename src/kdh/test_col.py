#-*- coding : utf-8 -*-

import sys

from socket import *


HOST = '10.101.30.176'
PORT = 30003
BUFSIZE = 1024


srv_sock = socket(AF_INET, SOCK_DGRAM)

srv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

srv_sock.bind((HOST, PORT))

while True:
    try:
        data, addr = srv_sock.recvfrom(BUFSIZE)

        if 'sender01' in data.decode().lower():
            srv_sock.sendto('Connected'.encode(), addr)
        else:
            print(data.decode())

    except KeyboardInterrupt:
        srv_sock.close()
        sys.exit()

