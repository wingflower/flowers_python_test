#-*- coding : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.11.25 ~
    Start log
        2017.11.25  [start]
"""

#base import
import GetSock as gs

#python import
import configparser as cp

from time import sleep
from random import randint

file_name = 'collector_config'
file_path = os.path.dirname(os.path.abspath(__file__))

BUFSIZE = 1024

class Collector():
    def __init__(self):
        info = cp.ConfigParser()
        info.read(os.path.join(file_path, file_name))
        self.col_ip   = info.get('col_server', 'col_ip')
        self.col_port = info.get('col_server', 'col_port')
        self.ma_ip    = info.get('mgmt_agent', 'ma_ip')
        self.ma_port  = info.get('mgmt_agent', 'ma_port')

    def main(self):
        col_sock = gs.get_conn(self.col_ip, self.col_port)
        ma_sock = gs.get_conn(self.ma_ip, self.ma_port)

    def run(self):


if __name__ == '__main__':
    C = Collector()
    C.run()
