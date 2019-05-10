# PiBot Test V0.3
# A simple script designed to test PiBot V0.2.1
# This script is under the CC-by 4.0 license

# Full credit to Alexander Lacy
#  Byrith International


# Include libraries

import RPi.GPIO as GPIO  # starts the GPIO library
import time  # allows for timing and pausing of script

# set up GPIO libraries

GPIO.setmode(GPIO.BCM)  # Gives the GPIO pins names
GPIO.setwarnings(False)  # prints errors and warnings

# set GPIO outputs
GPIO.setup(5, GPIO.OUT)  # right Motor clockwise
GPIO.setup(6, GPIO.OUT)  # right Motor anticlockwise
GPIO.setup(13, GPIO.OUT)  # Left Motor anticlockwise
GPIO.setup(19, GPIO.OUT)  # Left Motor clockwise

# the "main" code
print "driving forwards"
GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
time.sleep(2)

print "stopping"
GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
time.sleep(1)

print "driving backwards"
GPIO.output(5, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
time.sleep(2)

print "stopping"
GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
time.sleep(1)

print "paning left"
GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
time.sleep(2)

print "stopping"
GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
time.sleep(1)

print "paning right"
GPIO.output(5, GPIO.HIGH)
GPIO.output(19, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
time.sleep(2)

print "end of script"
GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
time.sleep(1)

# end of python script
