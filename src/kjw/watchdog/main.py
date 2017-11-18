import logging
import psycopg2
from psycopg2.extras import LoggingConnection
import sys

logging.basicConfig(filename='./logDir/test3.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

con = None
class CreateFilter(logging.Filter):
    def filter(self, record):
            print record.getMessage().startswith('CREATE')
            return record.getMessage().startswith('CREATE')

class Test():
    def __init__(self, ip, port, userid, userpw):
        self.ip = ip
        self.port = port
        self.userid = userid
        self.userpw = userpw

    def main(self):
        cur = self.get_connection()
        self.create(cur)
        self.select(cur.cursor())
        self.createTable(cur)

    def select(self,cur):
        cur.execute('SELECT * from teacher')
        ver = cur.fetchall()

    def create(self,con):
        cursor = con.cursor()
        cursor.execute("INSERT INTO teacher(name,jumin) VALUES('AUDI','1111')")
        con.commit()

    def createTable(self, con):
        cursor = con.cursor()
        cursor.execute("CREATE TABLE DEPT22(ID integer,DEP CHAR(50),EMP CHAR(50))")
        con.commit()

    def get_connection(self):
        con = psycopg2.connect(connection_factory=LoggingConnection, database='douzone', user=self.userid, password=self.userpw)
        logger.addFilter(CreateFilter())
        con.initialize(logger)
        return con

    def run(self):
        self.main()

if __name__ == "__main__":
    T = Test(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    T.run()
