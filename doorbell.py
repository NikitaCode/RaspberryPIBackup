import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
	GPIO.output(buzzer,GPIO.HIGH)
        time.sleep(0.5)
	GPIO.output(buzzer,GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(buzzer,GPIO.LOW)
