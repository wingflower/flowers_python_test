from socket import *
import redis

# HOST = '127.0.0.1'
HOST = '192.168.1.9'
PORT = 30000
BUFSIZE = 1024

serverSock = socket(AF_INET, SOCK_DGRAM)

serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSock.bind((HOST, PORT))

while True:

    data, addr = serverSock.recvfrom(BUFSIZE)

    cnt = 0
    for p_data in data.decode().split('#'):
        cnt += 1
        print("data %d : " % cnt, p_data)

    print("data : ", data.decode())
    print("addr : ", addr)

    s_data = (addr)
    # serverSock.sendto('192.168.1.5,30001,col_01'.encode(), addr)
    serverSock.sendto(','.join(s_data()).encode(), addr)
    #serverSock.sendto('192.168.1.6,30001,col_01'.encode(), addr)
    # print('#'.join(addr).encode(), 'col_01')

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('data', data.decode())
    print("redis : ", r.get('data').decode())

serverSock.close()

def s_date(self):

    cnt = 1
    data.append(str((HOST)))
    data.append(str((PORT)))
    data.append(str(cnt))
    return data
