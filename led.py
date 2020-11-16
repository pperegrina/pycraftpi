import RPi.GPIO as GPIO
from time import sleep
pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]
print("Init %d general purpose pins"%len(pins))
GPIO.setmode(GPIO.BOARD)
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)    
for pin in pins:
    print("PIN %d"  % pin)
#    input("Press the <ENTER> key to continue...")    
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
    sleep(3)
    GPIO.output(pin,GPIO.LOW)
    sleep(1)
