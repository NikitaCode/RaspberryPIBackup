import RPi.GPIO as GPIO
import time

pinArray = [5, 6, 13, 19, 26]
currentLED = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for x in pinArray:
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,0)

GPIO.output(pinArray[currentLED],1)

while True:
    moveAction=raw_input("Move Left or Rigth (L / R)")
    if moveAction=='l':
	GPIO.output(pinArray[currentLED],GPIO.LOW)
        currentLED += 1
        GPIO.output(pinArray[currentLED],GPIO.HIGH)

    if moveAction=='r':
	GPIO.output(pinArray[currentLED],GPIO.LOW)
        currentLED -= 1
        GPIO.output(pinArray[currentLED],GPIO.HIGH)

    if currentLED == -1:
        currentLED = 4

    if currentLED == 5:
        currentLED = 0



    # nameTwo = input('Turn LED Off? Y/N')
    # if nameTwo=='y':
    #     GPIO.output(18,GPIO.LOW)
    #     counter-=1
    # if not nameTwo=='y':
    #     GPIO.output(18,GPIO.HIGH)
