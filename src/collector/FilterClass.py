#-*- coding : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.10.24 ~
    Start log
        2017.10.24  [start]
"""

import re
import psycopg2
import configparser


#from GetQueryset import get_log_queryset as log_qs01
#from GetQueryset import get_re_queryset as re_qs01


class FilterClass():
    def __init__(self):
        pass

    def get_config(self, keyword):
        cf = configparser.ConfigParser()
        cf.config('./config.ini')
        if keyword.lower() is 'default':
            pass
        elif keyword.lower() is 'db':
            db_name = cf['db']['db_name']
            user    = cf['db']['user']
            host    = cf['db']['host']
            passwd  = cf['db']['passwd']
            port    = cf['db']['port']
            return db_name, user, host, passwd
        elif keyword.lower() is 'redis':
            host = cf['redis']['host']
            port = cf['redis']['port']
            db   = cf['redis']['db']
            return host, int(port), int(db)
        elif keyword.lower() is 're':
            return cf['re']['chk_str']

    def get_re(self):
        return re.compile(r'%s' % self.get_config('re'))

    def set_re(self):
        pass

    def get_redis(self):
        return redis.Redis(host='%s', port='%d', db='%d' % self.get_config('redis'))

    def get_cur(self):
        conn_str = "db_name='%s' user='%s' host='%s' password='%s'"
        conn_str = conn_str % self.get_config('db')
        self.conn = psycopg2.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close_cur(self, cursor):
        self.cursor.close()
        self.conn_close()

    def run(self):
        pass


if __name__ == '__main__':
    FC = FilterClass()
    FC.run()
