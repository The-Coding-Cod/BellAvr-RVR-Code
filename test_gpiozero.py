# This is a good tester to see if the servos are working
# Pulled from gpiozero docs

from gpiozero import AngularServo, Servo
from time import sleep

PosServo = AngularServo(17, min_angle=-90, max_angle=90)
ContServo = Servo(18)

while True:
    PosServo.angle = -90
    sleep(2)
    PosServo.angle = -45
    sleep(2)
    PosServo.angle = 0
    sleep(2)
    PosServo.angle = 45
    sleep(2)
    PosServo.angle = 90
    sleep(2)
    ContServo.min() # servo.value = -1
    sleep(2)
    ContServo.mid() # servo.value = 0
    sleep(2)
    ContServo.max() # servo.value = 1