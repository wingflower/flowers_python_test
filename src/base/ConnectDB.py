#-*- coding : utf-8 -*-
"""
    Author : Flower
    Time attack
        2017.11.13 ~
    Start log
        2017.11.13  [start]
        2017.11.13  [A] kind of dbms
                    1 : Postgres (default)
                    2 : Oracle
                    3 : MySQL
                    4 : SQLite
"""
import psycopg


class ConnectDB():
    def __init__(self):
        self.conn = None

    def get_cur(self, info, dbms=1):
        try:
            if dbms == 1:
                conn_str = "dbname='%s' user='%s' host='%s' password='%s' port='%s'" % tuple(info)
                self.conn = psycopg2.connect(conn_str)
            elif dbms == 2:
                pass
            elif dbms == 3:
                pass
            elif dbms == 4:
                pass
            return conn.cursor()
        except Exception as e:
            return e

    def close_cur(self, cursor):
        self.conn.close()
        cursor.close()

    def run():
        pass


if __name__ == '__main__':
    CD = ConnectDB()
    CD.run()
