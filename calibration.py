import pygame
import json

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
debug = True

checks = 0
peak_val = []


for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize the appended joystick (-1 means last array item)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    if debug: print ("Detected joystick "),joysticks[-1].get_name(),"'"

while keepPlaying:
    clock.tick(30)
