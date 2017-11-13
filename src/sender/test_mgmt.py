#-*- coding : utf-8 -*-

import sys

from socket import *


HOST = '10.101.30.176'
PORT = 30000
BUFSIZE = 1024


srv_sock = socket(AF_INET, SOCK_DGRAM)

srv_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

srv_sock.bind((HOST, PORT))

while True:
    try:
        data, addr = srv_sock.recvfrom(BUFSIZE)

        if 'meta' in data.decode().lower():
            print(data.decode())
            srv_sock.sendto('COLECTOR01,SENDER01,10.101.30.176:30003'.encode(), addr)
        else:
            srv_sock.sendto('Your msg is not META data!'.encode(), addr)

    except KeyboardInterrupt:
        srv_sock.close()
        sys.exit()

