import select
import psycopg2
import psycopg2.extensions
from time import sleep

import pgpubsub


pubsub = pgpubsub.connect(user='postgres', database='testdb', host='10.101.30.117', port=5432,
        password='1111')

while True:
    pubsub.listen('mymessage')
    temp = pubsub.get_event()
    if temp:
        temp = str(temp)
        print(temp.split(',')[-1].strip().split("'")[1])
    sleep(3)


