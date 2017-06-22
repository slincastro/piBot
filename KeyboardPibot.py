import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import sys



GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

while 1:
    option = raw_input('Enter the direction of PiBot \n')
    if(option == "f"):
        GPIO.output(17, False)
        GPIO.output(27,True)
        GPIO.output(22, False)
        GPIO.output(18,True)
        print ("Voy adelante")
    elif(option == "b"):
        GPIO.output(17, True)
        GPIO.output(27,False)
        GPIO.output(22, True)
        GPIO.output(18,False)
        print("Voy de vuelta")
    else :
        GPIO.output(17, False)
        GPIO.output(27,False)
        GPIO.output(22, False)
        GPIO.output(18,False)

        print("bye ... \n")
        sys.exit()
        break
