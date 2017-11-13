import select
import psycopg2
import psycopg2.extensions
from time import sleep

import pgpubsub


pubsub = pgpubsub.connect(user='postgres', database='testdb', host='localhost', port=5432)

while True:
    pubsub.listen('mymessage')
    temp = pubsub.get_event()
    if temp:
        print(type(temp))
        print(temp)
    sleep(3)


"""
conn_string = "host='127.0.0.1' dbname='testdb' user='postgres' password='1111' port='5432' "
# use our connection values to establish a connection
conn = psycopg2.connect(conn_string)
# create a psycopg2 cursor that can execute queries
cursor = conn.cursor()
# create a new table with a single column called "name"
cursor.execute('listen mymessage')
# run a SELECT statement - no data in there, but we can try it
try:
    print("Waiting for notifications on channel 'test'")
    while True:
	if select.select([conn],[],[],5) == ([],[],[]):
	    print("Timeout")
	else:
	    conn.poll()
	    while conn.notifies:
		notify = conn.notifies.pop(0)
		print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)
    #while True:
    #    print(cursor)
    #    rows = cursor.fetchall()
    #    print(rows)
except Exception as e:
    print(e)
"""
