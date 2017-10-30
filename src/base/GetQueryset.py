#-*- coding : utf-8 -*-

class GetQueryset():
    def __init__(self):
        pass

    def get_log_queryset01(self, qs_key, args):
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

    def get_re_queryset01(self, qs_key, args):
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
