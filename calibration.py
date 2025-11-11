import pygame
import json
import sys

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
debug = True

ready = False

Start_time = 0
Elapsed_time = 0
peak_val = [0, 0]
current_working = "Right_Drive"

for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize the appended joystick (-1 means last array item)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    if debug: print ("Detected joystick "),joysticks[-1].get_name(),"'"

while keepPlaying:
    clock.tick(30)
    for event in pygame.event.get():
        try:
            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis: {event.axis} \nValue: {event.value}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button: {event.button}")
            else:
                print("none")
        except:
            #print(f'{event} does not have a valid axis')
            try:
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pygame.quit()
                        sys.exit()
            except:
                pass