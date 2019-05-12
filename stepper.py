# First, we import libraries that will be
# needed in the program: time and support for raspberry GPIO pins
import time
import RPi.GPIO as GPIO
# We determine how we will call our pins,
# in this version we do it via GPIO numbers
GPIO.setmode(GPIO.BCM)

# Here we define further output pins for IN1, IN2, IN3, IN4 controller inputs
pins =[18,23,24,25]

# We note that pins are output and give them a starting position of false or 0
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
# We define next electromagnet activation sequences for half-step control
sequence = [ [1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1] ]

# Here we define the number of steps to be performed.
# Our engine has a gear ratio of 1:64, therefore, to perform a full rotation in half-steps
# we have to pass each step 8x64 times or 512
step_count = 512
# The loop that performs the steps looks like this:
for i in range(step_count):
    for half_step in range(8):
        for pin in range(4):
            GPIO.output(pins[pin], sequence[half_step][pin])
        time.sleep(0.0007)
        # we set the time for the next repeat, if it's too low
        # the frequency will be too high and the engine will not move
        # with this time it's the highest speed I have managed to achieve.
        # If you want to see how the sequence looks like
        # on the LEDs, set the time to 0.1 seconds
		

# At the end, we clean all the pins        
GPIO.cleanup()
