import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,0)
counter = 1
i = 1
while i < 9999:
    i += 1
    if counter==1:
        nameOne=raw_input("LED on? Y/N")
        if nameOne=='y':
            GPIO.output(18,GPIO.HIGH)
            counter+=1
        if not nameOne=='y':
            GPIO.output(18,GPIO.LOW)
            
            
    if counter==2:
        nameTwo = raw_input('Turn LED Off? Y/N')
        if nameTwo=='y':
            GPIO.output(18,GPIO.LOW)
            counter-=1
        if not nameTwo=='y':
            GPIO.output(18,GPIO.HIGH)
        

