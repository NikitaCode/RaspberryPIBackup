import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_Down)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, 0)

try:
        while True:
            if (GPIO.input(11) == 1):
                    GPIO.output(7,1)
                else:
                        GPIO.output(7,0)
except KeyboardInterrupt:
    GPIO.cleanup()
