import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import psycopg2

con = None
class Watcher:
    DIRECTORY_WATCH = "./logDir"

    def __init__(self):
       self.observer = Observer()

    def run(self):
       event_handler = Handler()
       self.observer.schedule(event_handler, self.DIRECTORY_WATCH, recursive=True)
       self.observer.start()
       try:
            while True:
                    time.sleep(5)
       except:
            self.observer.stop()
            print "Error"
       self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        print "event %s" %event.event_type
        file_object = open("./logDir/test3.log","r")
        lineList = file_object.readlines()
        lastLine = lineList[len(lineList)-1]
        print lastLine
        wordTemp = lastLine.split('(')
        wordTemp = wordTemp[0].split(" ")
        print wordTemp[2]
        instance = Handler()
        instance.descTable(wordTemp[2])

    def descTable(self,tableName):
        con = psycopg2.connect(database='douzone',user='wook',password='wldnrdld335!')
        cur = con.cursor()
        cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = '%s'" % str(tableName))
        var = cur.fetchone()
        print var

if __name__ == '__main__':
    w = Watcher()
    w.run()
