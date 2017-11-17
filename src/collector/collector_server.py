#-*- coding : utf-8 -*-
"""
    Author : Flower
    Time attack
        2017.10.10 ~
    Start log
        2017.10.10  [start]
"""

from socket import *
import psycopg2
import sys
import os
import udp_query
from psycopg2.extras import RealDictCursor


HOST = '127.0.0.1'
#HOST = '192.168.1.10'
PORT = 30003
BUFSIZE = 1024
SLEEP_TIME = '99'


class udp_server():
    def __init__(self):
        self.socket = None
        self.host = HOST
        self.port = PORT
        self.bufsize = BUFSIZE
        self.serverSock = socket(AF_INET, SOCK_DGRAM)
        self.serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSock.bind( (HOST, PORT) )
        self.c_addr = None
        self.c_data = None
        self.clients = {} # manage clients
        self.cursor = None
        self.conn = None


    def run(self):
        while True:
            try:
                self.get_data()
                parse_data = self.parsing_data()
                print('parse_data:',str(parse_data))
                #self.cursor = self.set_connection()

                self.set_connection() # set conn, cursor
                self.cursor.execute(parse_data['final_query'])
                self.conn.commit()
                res = self.cursor.fetchall()
                print('executed_query: ',res)

                print(parse_data['client_id'])
                self.send_data(parse_data['client_id'])

                if str(self.c_addr[1]) not in self.clients.keys():
                    print(str(self.clients))
                    self.set_client()
                    print(str(self.clients))
                    print('entered new user')

                #self.serverSock.close()
            except Exception as e :
                print ('error accured: ',str(e))
                pass

    def set_client(self):
        self.clients[str(self.c_addr[1])] = self.c_addr[0]


    def get_data(self):
        self.c_data, self.c_addr = self.serverSock.recvfrom(BUFSIZE)
        print('data : ', self.c_data.decode())
        print('addr : ', self.c_addr)

    def send_data(self,client_id):
        self.serverSock.sendto(client_id.encode(), self.c_addr)


    def set_connection(self):
        conn_string = "host='127.0.0.1' dbname='postgres' user='postgres' password='1111' port='5430' "
        print("connecting to DB")

        self.conn = psycopg2.connect(conn_string)
        self.cursor = conn.cursor(cursor_factory=RealDictCursor)
        print("connected!")


    def parsing_data(self):
        '''
            explain : confirm new user or not
                      if new user then create new table
                      else insert data

                     if first get data to start  "client_id"

        '''
        parsed_data = self.c_data.decode().split(',')
        print('parsed_data:',parsed_data)
        print('addr : ',self.c_addr)
        # add reg expression

        parse_dic = {}
        if parsed_data[0] == 'log': # list.pop() ???  end of list ??
            # insert log data
            # insert client_id table
            # must get table_name (client_id)
            client_id = parsed_data[1]
            insert_data = parsed_data[2].split('|')       # must fix to insert columns's data

            insert_query = ""
            if len(insert_data) > 0:
                for insert_col in insert_data:
                    insert_query += " " + insert_col + " ,"
                insert_query = insert_query[:-1]

                final_query = """
                    insert into {0} (data_log, client_id, logged_time, insert_time)
                    values ({1})
                """.format(client_id, insert_query)
        else :
            # create table
            client_id = parsed_data[0] + ',' + SLEEP_TIME
            columns = parsed_data[2].split('|')
            columns_query = ' id bigserial primary key,  '

            if len(columns) > 0:
                for col in columns:
                    columns_query += " " + col  + " text, "

                final_query = """
                    create table {0} (
                        {1}
                    );

                    select 'success' as res ;
                """.format(client_id[:-3],columns_query) # client_id[:-3] :  fix sleep time is less then 100
                print('final_query : ',final_query)

        parse_dic['client_id'] = client_id
        parse_dic['final_query'] = final_query
        return parse_dic

    def close_conn():
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    kdy_server = udp_server()
    kdy_server.run()

