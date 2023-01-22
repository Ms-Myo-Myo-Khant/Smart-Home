# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

 
def SetAngle(angle):
    pwm=GPIO.PWM(11,20)
    pwm.start(0)
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)
    
    
def open_door():
    SetAngle(80) 
    return

def close_door():
    SetAngle(0) 
    return

open_door()
sleep(2)
close_door()

 
GPIO.cleanup()