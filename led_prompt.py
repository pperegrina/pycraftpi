import RPi.GPIO as GPIO
from threading import Thread
from time import time, sleep
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

class GPIOThread(Thread):

    pins = {
        'north1': 3,
        'east1': 5,
        'south1': 7,
        'west1': 8,
        'up1': 10,
        'down1': 11,
        'up2':12,
        'down2':13,
        'north2': 15,
        'east2': 16,
        'south2': 18,
        'west2': 19,
        'north3': 21,
        'south3': 22,
        'north4': 23,
        'south4': 24,
        'extra': 26
    } 

    stopped = False
    commands = []
    blink = {}

    def stop(self):
        self.stopped = True

    def start(self):
        GPIO.setmode(GPIO.BOARD)
        for name, pin in self.pins.items():
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,GPIO.LOW)
        self.stopped = False        
        Thread.start(self)

    def addCommand(self,name):
        self.commands.append(command)

    def run(self):
        while not self.stopped:
            while len(self.commands):
                command = self.commands.pop(0)
                elements = command.split(' ')
                action = elements[0]
                name = elements[1]
                if action=='on':
                    if name in self.blink:
                        del self.blink[name]
                    level = GPIO.HIGH
                    pin = self.pins[name]
                    GPIO.output(pin,level)                    
                elif action=='off':
                    if name in self.blink:
                        del self.blink[name]
                    level = GPIO.LOW
                    pin = self.pins[name]
                    GPIO.output(pin,level)
                elif action=='blink':
                    timer = 0.5
                    if len(elements)>2:
                        timer = float(elements[2])
                    self.blink[name] = [ time(), timer, False ]
            for name, params in self.blink.items():
                if time() > params[0] + params[1]:
                    pin = self.pins[name]
                    if params[2]:
                        level = GPIO.LOW
                    else:
                        level = GPIO.HIGH
                    GPIO.output(pin,level)
                    self.blink[name] = [ time(), timer, not params[2] ]
            sleep(0.1)
        for name, pin in self.pins.items():
            GPIO.output(pin,GPIO.LOW)            
        print('thread exit')


t = start_thread(GPIOThread())
while True:
    command = input('Enter new name: ')
    t.addCommand(command)
    
