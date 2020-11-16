from threading import Thread
from time import sleep
import signal
import sys

threads = []

def start_thread(t):
    global threads
    threads.append(t)
    t.start()
    return t

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for t in threads:
        t.stop()
        t.join()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class displayNameThread(Thread):
    lastname = 'N/A'
    name = 'N/A'
    stopped = False

    def stop(self):
        self.stopped = True

    def start(self):
        self.stopped = False
        Thread.start(self)

    def setName(self,name):
        self.name = name

    def run(self):
        while not self.stopped:
            if self.name != self.lastname:
                print('CHANGED TO %s'%self.name)
                self.lastname = self.name
            sleep(0.1)
        print('thread exit')


t = start_thread(displayNameThread())
while True:
    name = input('Enter new name: ')
    t.setName(name)
    