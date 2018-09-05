# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:23:05 2018

@author: Farai Murinye
"""
#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM

led = 17
but1 = 18
but2 = 27
but3 = 22

# setup our output pins
GPIO.setup(led,GPIO.OUT)
# setup our input pins
GPIO.setup(but1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(but2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(but3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Set the frequency of the led
PWM = GPIO.PWM(led, 100)
PWM.start(0)
#PWM.stop()

#set Variables
#dim = 100
#bri = 0
o_f = False
lit = 0

try:
    while True:
        if (GPIO.input(but1) == False):  #dimming
            sleep(0.5)
            print ("Button1 has been pressed")
            if (lit<=0):
                lit = 100
                PWM.ChangeDutyCycle(lit)
            else:
                PWM.ChangeDutyCycle(lit)
                lit = lit-(100/7)
            

             
        if ( (GPIO.input(but2)) == False): #brightening
            sleep(0.5)
            print ("Button2 has been pressed")
            if (lit>=100):
                lit = 0
                PWM.ChangeDutyCycle(lit)
            else:
                lit=lit+10
                PWM.ChangeDutyCycle(lit)
                

            
        if ((GPIO.input(but3)) == False ): #on-off
            sleep(0.5)
            print ("Button3 has been pressed")
            
            o_f = not o_f
            GPIO.output(led, o_f)

finally:
    
    PWM.stop()
    GPIO.cleanup()
