import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17, false)
