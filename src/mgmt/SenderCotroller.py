#-*- coding : utf-8 -*-

"""
    Author : Flower
    Time attack
        2017.10.24 ~
    Start log
        2017.10.24  [start]
        2017.11.11  [A] Controll meta data
"""

import redis


class SenderController():
    def __init__(self, h='localhost', p=6379):
        self.rd_conn = redis.StrictRedis(host=h, port=p, db=0)

    def get_sender_key(self):
        pass

    def set_sender_key(self):
        pass

    def get_meta(self, sender_key=None, meta=None):
        if meta:
            return meta.split('|')
        if sender_key:
            return self.rd_conn.get(meta)

    def set_meta(self, sender_key=None, meta=None):
        self.rd_conn.set(sender_key, meta)

    def run(self):
        pass


if __name__ == '__main__':
    SC = SenderController()
    SC.run()
