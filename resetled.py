import RPi.GPIO as GPIO
from time import sleep
pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]
print("Init %d general purpose pins"%len(pins))
GPIO.setmode(GPIO.BOARD)
cpt = 1
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)   
