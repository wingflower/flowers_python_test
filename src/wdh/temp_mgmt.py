# -*- coding : utf-8 -*-

from socket import *

import sys

HOST = '127.0.0.1'
PORT = 30000
BUFSIZE = 1024

class TempMGMT():
    def __init__(self, ip, port):
        pass

    def mgmt(self):
        soc = get_connection(self.ip, self.port)
        while True:
            try:
                data, addr = serverSock.recvfrom(BUFSIZE)

                print("Sender data : ", data.decode())
                print("Senderaddr : ", addr)

                val = input("Input : ")
                if val.lower() == 'quit':
                    sys.exit()

                serverSock.sendto(val.encode(), addr)
            except KeyboardInterrupt:
                serverSock.close()
    def get_connection(self, ip, port):
        serverSock = socket(AF_INET, SOCK_DGRAM)
        serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSock.bind((ip, port))
        return serverSock

    def run(self):
        self.mgmt()

if __name__ == '__main__':
    TM = TempMGMT(sys.argv[1], sys.argv[2])
    TM.run()
