import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# Here we define further output pins for IN1, IN2, IN3, IN4 contr$
pins =[18,23,24,25]

# We note that pins are output and give them a starting position $
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
# We define next electromagnet activation sequences for half-step$
sequence = [ [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1] ]

# Here we define the number of steps to be performed.
# Our engine has a gear ratio of 1:64, therefore, to perform a fu$
# we have to pass each step 8x64 times or 512
step_count = 512
# The loop that performs the steps looks like this:
for i in range(step_count):
    for half_step in range(8):
        for pin in range(4):
            GPIO.output(pins[pin], sequence[half_step][pin])
        time.sleep(0.0007)

try:
  while True:
#    p.ChangeDutyCycle(5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(7.5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(10)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(10)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(7.5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)
     p.ChangeDutyCycle(2)
     time.sleep(0.5)
     p.ChangeDutyCycle(1)
     time.sleep(0.5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()



