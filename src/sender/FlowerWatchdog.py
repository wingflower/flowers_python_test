#-*- coding : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.10.30 ~
    Start log
        2017.10.30  [start]
"""

import sys
import time


class FlowerWatchdog():
    def __init__(self,):
        self.log_cnt = 0
        self.log_data = None

    def get_line_changed(self,):
        f = open(self.path, 'r')
        temp_cnt = len(f.readlines())
        f.close()
        if self.log_cnt == temp_cnt
            return True
        else:
            self.log_cnt = temp_cnt
            return False

    def get_data_changed(self,):
        f = open(self.path, 'r')
        temp_data = f.readlines()
        f.close()
        if self.log_data == temp_data
            return True
        else:
            self.log_data = temp_data
            return False

    def get_line_log(self,):
        f = open(self.path, 'r')
        temp_data = f.readline()
        temp_cnt = self.log_cnt
        self.log_cnt = len(temp_data)
        return temp_data[temp_cnt-1:-1]

    def get_data_log(self,):
        f = open(self.path, 'r')
        temp_data = f.readline()
        rs = [val for val in temp_data if val not in self.log_data]
        self.log_data = temp_data
        return rs

    def run(self,):
        pass


if __name__ == '__main__':
    FW = FlowerWatchdog()
    FW.run()
