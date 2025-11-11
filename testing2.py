
import time
import sys
import json

with open('settings.json') as settings_file:
    settings = json.load(settings_file)
    right_axis = settings["Right_Axis"]
    left_axis = settings["Left_Axis"]
    front_forward = settings["Front_Forward"]
    front_reverse = settings["Front_Reverse"]
    mid_forward = settings["Mid_Forward"]
    mid_reverse = settings["Mid_Reverse"]
    dump_toggle = settings["Dump_Toggle"]
    

Dumped = False
Front_Driving = False
Mid_Driving = False


import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


main_dir = os.path.dirname(os.path.realpath(__file__))

packages_path = os.path.join(main_dir, "Packages")
sphero_path = os.path.join(packages_path, "sphero-sdk-raspberrypi-python")

import pygame

sys.path.append(packages_path)
sys.path.append(sphero_path)

from PCA9685 import PCA9685
from sphero_sdk import SpheroRvrObserver
from sphero_sdk.common.enums.drive_enums import RawMotorModesEnum as RawMotorModes
rvr = SpheroRvrObserver()
rvr.wake()
rvr.drive_control.reset_heading()
map_val = 250
pygame.init()
pygame.display.init()
pygame.display.set_mode((1,1))
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
debug = True
print(sys.version)

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

joys = pygame.joystick.Joystick(0)

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize the appended joystick (-1 means last array item)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    if debug: print ("Detected joystick "),joysticks[-1].get_name(),"'"
left_tread = 0
right_tread = 0


  
def State():
   rvr.raw_motors(
        RawMotorModes.off, 0,
        RawMotorModes.off, 0
) 


    #cases: 1 - backwards BB, 2 - counter back tread CCBT, 3 - counter back point CCBP, 4 - clock back tread CBT, 5 - state S,
    #6 - counter front tread CCFT, 7 - clock front point CFP, 8 - clock front tread CFT, 9 - forwards FF

def driver(left_t, right_t):

    drive_mode = []
    if left_t == 0 and right_t == 0:
        State()
        
    else:
        
        if left_t > 0:
            left_mode = (RawMotorModes.forward, left_t)
        elif left_t < 0:
            left_mode = (RawMotorModes.reverse, abs(left_t))
        else:
            left_mode = (RawMotorModes.off, 0)
        for i in range(2):
            drive_mode.append(left_mode[i])
        if right_t > 0:
            right_mode = (RawMotorModes.forward, right_t)
        elif right_t < 0:
            right_mode = (RawMotorModes.reverse, abs(right_t))
        else:
            right_mode = (RawMotorModes.off, 0)
        for i in range(2):
            drive_mode.append(right_mode[i])
        rvr.raw_motors(drive_mode[0], drive_mode[1], drive_mode[2], drive_mode[3])

def drive_servo(channel, direction):
    if direction == "Forward":
        pwm.setServoPulse(channel,600)
    elif direction == "Reverse":
        pwm.setServoPulse(channel,2500)
    else:
        pwm.setServoPulse(channel, 500)

def angle_servo(channel, angle):
    pulse = 500+(2000*(angle/360))
    pwm.setServoPulse(channel, pulse)
   
   
   
while keepPlaying:
    clock.tick(60)
    for event in pygame.event.get():

        # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
        try:
            if event.axis == left_axis:
                    #left Tread
                if event.value > 0.1:
                    left_tread = int(event.value * map_val) * -1
                elif event.value < -0.1:
                    left_tread = int(event.value * map_val) * -1
                else:
                    left_tread = 0
                if debug: print(left_tread)
                 #print(f"Left: {left_tread}")     
            elif event.axis == right_axis: #Vert Movement
                if event.value > 0.1:
                    right_tread = int(event.value * map_val) * -1
                elif event.value < -0.1:
                    right_tread = int(event.value * map_val) * -1
                else:
                    right_tread = 0
                if debug: print(right_tread)
                #print(f"Right: {right_tread}")
            elif event.axis == front_forward: #front servos
                if event.value > -0.9:
                    drive_servo(0, "Reverse")
                else:
                    drive_servo(0, "None")
            elif event.axis == mid_forward:
                if event.value > -0.9:
                    drive_servo(1, "Reverse")
                else:
                    drive_servo(1, "None")

        except:
            print("No Axis")
            if event.type == pygame.JOYBUTTONDOWN:
                if joys.get_button(front_reverse):
                    if Front_Driving:
                        drive_servo(0, "None")
                        Front_Driving = False
                    else:
                        drive_servo(0, "Forward")
                        Front_Driving = True
                if joys.get_button(mid_reverse):
                    if Mid_Driving:
                        drive_servo(1, "None")
                        Mid_Driving = False
                    else:
                        drive_servo(1, "Forward")
                        Mid_Driving = True
                if joys.get_button(dump_toggle):
                    if Dumped:
                        angle_servo(2, 180)
                        Dumped = False

                    else:
                        angle_servo(2, 0)
                        Dumped = True
            else:
                print("Event Not JOYBUTTON")


        try:
            right_tread = right_tread
            left_tread = left_tread
        except:
            print("tread Net")
            right_tread = 0
            left_tread = 0
        if debug: print(left_tread, right_tread)
        driver(left_tread, right_tread)

                
                 
                    
        
