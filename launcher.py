#!env python
# -*- coding: utf-8 -*-

from toolbox.gpio_thread import GPIOThread
from toolbox.mc_thread import MCThread
from toolbox.signals import start_thread

if __name__ == "__main__":
    gpio_thread = start_thread(GPIOThread())    
    mc_thread = start_thread(MCThread('play3.evaway.com', 'r4scu4ch0'))    
    print('Ready !')
    while True:
        command = input('>')
        gpio_thread.addCommand(command)    
