#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM

led = 17

#setup our output pins
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
print ("Led On")

GPIO.output(led, GPIO.HIGH)
sleep(10)
print ("now off")
GPIO.output(led, GPIO.LOW)