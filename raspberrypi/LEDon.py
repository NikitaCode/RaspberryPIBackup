import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i = 1
while i < 100:
	print(i)
	GPIO.setup(18,GPIO.OUT)
	print('LED On')
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)
	print('LED Off')
	GPIO.output(18,GPIO.LOW)
	time.sleep(1)
	i += 1
