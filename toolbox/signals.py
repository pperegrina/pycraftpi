#!env python
# -*- coding: utf-8 -*-

import signal

threads = []

def start_thread(t):
    global threads
    threads.append(t)
    t.start()
    return t

def signal_handler(sig, frame):
    print('You pressed Ctrl+C: stopping threads and exiting')
    for t in threads:
        t.stop()
        t.join()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)