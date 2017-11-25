#-*- cofing : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.11.25 ~
    Start log
        2017.11.25  [start]
"""

from socket import *

def __init__(self):
    pass

def get_conn(self, ip, port):
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((ip, port))
    except:
        pass
    else:
        return sock

def close_conn(self, sock):
    sock.close()

def send_msg(self, sock, addr, port, msg):
    try:
        sock.sendto(msg, addr, port)
    except:
        pass
    else:
        pass

def get_msg(self, sock, bs):
    try:
        data, addr = sock.recvfrom(bs)
    except:
        pass
    else:
        return data, addr

    def run(self):
        pass

