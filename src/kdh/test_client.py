#-*- coding : utf-8 -*-

import sys

from socket import *


BUFSIZE = 1024


class TestClient():
    def __init__(self, m_ip, m_port):
        self.local_ip   = '127.0.0.1'
        self.local_port = 30001
        self.mgmt_ip    = m_ip
        self.mgmt_port  = m_port
        self.sock       = None

    def test_client(self):
        self.set_conn()
        self.sock.sendto('hi'.encode(), (self.mgmt_ip, self.mgmt_port))
        data, addr = self.sock.recvfrom(BUFSIZE)

        print("data : " , data.decode())
        print("addr : " , addr)

    def set_conn(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind((self.local_ip, self.local_port))

    def close_conn(self):
        self.sock.close()

    def run(self):
        self.test_client()


if __name__ == '__main__':
    TC = TestClient(sys.argv[1], int(sys.argv[2]))
    TC.run()

