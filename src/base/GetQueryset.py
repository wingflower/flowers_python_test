#-*- coding : utf-8 -*-
"""
    Author : Flower
    Time attack
        2017.11.13 ~
    Start log
        2017.11.13  [start]
"""

class GetQueryset():
    def __init__(self):
        pass

    def log_queryset01(self, qs_key, args):
        query_dic = {
            'create' : '',
            'select' : '',
            'insert' : '',
            'update' : '',
            'delete' : '',
            'alter'  : '',
            'drop'   : '',
        }
        return (query_dic[qs_key] % tuple(args))

    def re_queryset01(self, qs_key, args):
        query_dic = {
            'create' : '',
            'select' : '',
            'insert' : '',
            'update' : '',
            'delete' : '',
            'alter'  : '',
            'drop'   : '',
        }
        return (query_dic[qs_key] % tuple(args))

    def col_queryset01(self, qs_key, args):
        query_dic = {
            'create' : '',
            'select' : '',
            'insert' : '',
            'update' : '',
            'delete' : '',
            'alter'  : '',
            'drop'   : '',
        }
        return (query_dic[qs_key] % tuple(args))

    def run(self):
        pass


if __name__ == '__main__':
    GQ = GetQueryset()
    GQ.run()
