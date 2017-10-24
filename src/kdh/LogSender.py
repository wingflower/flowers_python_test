#!/usr/bin/env python
#-*- cofing : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.10.14 ~
    Start Log
        2017.10.14  [start]
        2017.10.22  [A] asyncio
"""

import os
import sys
import psutil
import asyncio
import platform
import configparser as cp

from socket import *
from time import sleep
from random import randint


file_name = 'log_config'
file_path = os.path.dirname(os.path.abspath(__file__))

BUFSIZE = 1024


class LogSender():
    def __init__(self, m_ip, m_port):
        info = cp.ConfigParser()
        info.read(os.path.join(file_path, file_name))
        self.local_ip   = info.get('localhost', 'local_ip')
        self.local_port = info.get('localhost', 'local_port')
        self.log_path   = info.get('log_info', 'log_path')
        self.mgmt_ip    = m_ip
        self.mgmt_port  = m_port
        self.mgmt_key   = True
        self.col_ip     = None
        self.col_port   = None
        self.col_name   = None
        self.col_key    = True
        self.connected  = False
        self.sock       = None

    async def main(self):
        while True:
            while self.mgmt_key:
                self.set_conn(self.local_ip, self.local_port)
                self.send_data('#'.join(self.get_resource()).encode(), self.mgmt_ip, self.mgmt_port)
                temp_col = self.recv_data()
                if not temp_col:
                    self.close_conn()
                    continue
                else:
                    self.mgmt_key = False
                    self.col_ip   = temp_col[0]
                    self.col_port = temp_col[1]
                    self.col_name = temp_col[2]
                    self.close_conn()
            self.set_conn(self.local_ip, self.local_port)
            log_cnt = 0
            while True:
                if self.col_key:
                    log_cnt += 1
                    log_init = 'SENDER01,127.0.0.1:30003,name|work'
                    self.send_data(('[%s]'%log_init).encode(), self.col_ip, self.col_port)
                    self.col_key = False
                else:
                    for i in range(randint(4, 10)):
                        log_cnt += 1
                        log_msg = await get_log()
                        self.send_data(('%s'%log_msg).encode(), self.col_ip, self.col_port)
                    sleep(1) # test

#WatchDog
    async def get_log(self):
        return log_msg

    def set_conn(self, h, p):
        try:
            self.sock = socket(AF_INET, SOCK_DGRAM)
            #self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.sock.bind((h, int(p)))
            self.connected = True
        #except ConnectionError as ce:
        except Exception as e:
            pass

    def close_conn(self):
        self.connected = False
        self.sock.close()

    def get_resource(self):
        res_info = []
        res_info.append(str(platform.processor()))
        res_info.append(str(psutil.cpu_count()))
        res_info.append(str(psutil.cpu_times_percent()))
        mem = psutil.virtual_memory()
        res_info.append(str(mem.total/1024))
        res_info.append(str(mem.used/1024))
        res_info.append(str(mem.free/1024))
        res_info.append(str(mem.percent))
        swap = psutil.swap_memory()
        res_info.append(str(swap.total/1024))
        res_info.append(str(swap.used/1024))
        res_info.append(str(swap.free/1024))
        res_info.append(str(swap.percent))
        disk = psutil.disk_partitions()
        disk_info = psutil.disk_usage(disk[0].mountpoint)
        res_info.append(str(disk_info.total/1024))
        res_info.append(str(disk_info.used/1024))
        res_info.append(str(disk_info.free/1024))
        res_info.append(str(disk_info.percent))
        return res_info

    def recv_data(self):
        try:
            data, addr = self.sock.recvfrom(BUFSIZE)
            data = data.decode()
        except:
            pass
        else:
            return data.split(',')

    def send_data(self, log, h, p):
        try:
            self.sock.sendto(log, (h, int(p)))
        except:
            pass
        else:
            pass

    def run(self):
        self.main()


if __name__ == "__main__":
    LS = LogSender(sys.argv[1], int(sys.argv[2]))
    LS.run()
