#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
chain_drive = Motor(Port.D)
scissor = Motor(Port.A)


# Write your program here.
ev3.speaker.beep()

def cut():
    speed = 1000
    scissor.run_until_stalled(-speed)
    scissor.run_until_stalled(speed)
    scissor.hold()
    scissor.reset_angle(0)
    
def run_dist(dist):
    chain_drive.run_angle(1000, dist)
    
def draw_UI():
    global unit
    global edit_mode
    button = ev3.buttons.pressed()
    
    if len(button) > 0 and edit_mode:
        if button[0] == Button.LEFT:
            ev3.screen.clear()
            ev3.screen.draw_box(0, 100, 80, 110, r=10, fill=True)
            unit = "inches"
        elif button[0] == Button.RIGHT:
            ev3.screen.clear()
            ev3.screen.draw_box(90, 100, 178, 110, r=10, fill=True)
            unit = "centimeters"
            
        if unit == "inches":
            ev3.screen.clear()
            inches_UI()
            ev3.screen.draw_box(0, 100, 80, 110, r=10, fill=True)
        elif unit == "centimeters":
            ev3.screen.clear()
            centimeters_UI()
            ev3.screen.draw_box(90, 100, 178, 110, r=10, fill=True)
        
    ev3.screen.draw_box(0, 10, 80, 118, r=10)
    ev3.screen.draw_text(10, 10, "Inches")
    ev3.screen.draw_text(22, 50, inches)
    
    ev3.screen.draw_box(90, 10, 178, 118, r=10)
    ev3.screen.draw_text(120, 10, "cm")
    ev3.screen.draw_text(120, 50, centimeters)
    
    
def inches_UI():
    global inches
    button = ev3.buttons.pressed()
    if len(button) > 0:
        if button[0] == Button.UP:
            inches += 1
        elif button[0] == Button.DOWN:
            inches -= 1

    wait(150)
    return inches

def centimeters_UI():
    global centimeters
    button = ev3.buttons.pressed()
    if len(button) > 0:
        if button[0] == Button.UP:
            centimeters += 1
        elif button[0] == Button.DOWN:
            centimeters -= 1

    wait(150)
    return centimeters
    
    
scissor.run_until_stalled(100)
scissor.hold()

print("SCREEN WIDTH:", ev3.screen.width)
print("SCREEN HEIGHT:", ev3.screen.height)
inches = 10
centimeters = 20
unit = "inches"
edit_mode = True
while True:
    button = ev3.buttons.pressed()
    if len(button) > 0:
        print("PRESSED")
        if button[0] == Button.CENTER:
            if edit_mode:
                ev3.speaker.play_file(SoundFile.CONFIRM)
            else:
                ev3.speaker.play_file(SoundFile.OVERPOWER)
            edit_mode = not edit_mode
    draw_UI()
    if not edit_mode:
        if unit == "inches":
            run_dist(inches*119.048)    
        else:
            run_dist(centimeters*47.1698)
        cut()
    wait(200)

# 1 Inch = 119.048 degrees
# 1 cm = 47.1698 degrees
