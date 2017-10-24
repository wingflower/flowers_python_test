#-*- coding : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.10.14 ~
    Start Log
        2017.10.14  [start]
        2017.10.22  [M] log_cnt
"""

import os
import sys
import psutil
import platform

from time import ctime
from time import sleep
from random import randint


file_name = 'flower_log'
file_path = os.path.dirname(os.path.abspath(__file__))

pattern = [
    '[%s] CISCO9999_L4 [loginfo:%s] cpu: %s memory: %s|%s disk: %s#\n',
    '[%s] [GIT] [log_cnt=%s] cpu=%s memory=%s|%s disk=%s [log_end]\n',
    '[%s] {Postgres DB} <log:%s> [cpu:%s][memory:%s|%s][disk:%s]\n',
    '[%s|%s] %s:%s|%s:%s [syslog for linux]\n',
]
v_ip = '192.168.200.50'


class LogMaker():
    def __init__(self):
        pass

    def log_maker(self):
        log_cnt = 0
        f_set = self.get_file()
        while True:
            try:
                res_rs = self.get_resource()
                for n in range(randint(5,10)):
                    log_cnt += 1
                    for i, f in enumerate(f_set):
                        temp_log_cnt = str(log_cnt).zfill(8)
                        f.write(pattern[i] % (ctime(), temp_log_cnt, res_rs['cpu'], res_rs['memory'], res_rs['swap'], res_rs['disk']))
                sleep(randint(1,3))
            except KeyboardInterrupt:
                for f in f_set:
                    f.close()
                sys.exit()

    def get_file(self):
        f = []
        # Default 4 files
        for i in range(4):
            f.append(open(os.path.join(file_path, file_name + str(i) + '.log'), 'a'))
        return f

    def get_resource(self):
        res_info = {}
        # CPU info
        temp_str = str(platform.processor())
        temp_str += '#' + str(psutil.cpu_count())
        temp_str += '#' + str(psutil.cpu_times_percent())
        res_info['cpu'] = temp_str
        # Memory info
        mem = psutil.virtual_memory()
        temp_str = str(mem.total/1024)
        temp_str += '#' + str(mem.used/1024)
        temp_str += '#' + str(mem.free/1024)
        temp_str += '#' + str(mem.percent)
        res_info['memory'] = temp_str
        # Swap info
        swap = psutil.swap_memory()
        temp_str = str(swap.total/1024)
        temp_str += '#' + str(swap.used/1024)
        temp_str += '#' + str(swap.free/1024)
        temp_str += '#' + str(swap.percent)
        res_info['swap'] = temp_str
        # Disk info
        disk = psutil.disk_partitions()
        disk_info = psutil.disk_usage(disk[0].mountpoint)
        temp_str = str(disk_info.total/1024)
        temp_str += '#' + str(disk_info.used/1024)
        temp_str += '#' + str(disk_info.free/1024)
        temp_str += '#' + str(disk_info.percent)
        res_info['disk'] = temp_str
        return res_info

    def run(self):
        self.log_maker()


if __name__ == '__main__':
    LM = LogMaker()
    LM.run()
