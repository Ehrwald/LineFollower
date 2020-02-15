#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

###########################################
# Main method incoming

#motors
mRight = Motor(Port.D)
mLeft = Motor(Port.A)

#sensor
sRight = ColorSensor(Port.S1)

#other init for run_time
robot = DriveBase(mLeft,mRight, 56, 114)
nbrotate = 50  #nb 
speed = nbrotate/1 #deg/sec
speed2 = -30/1
timeA = 400 #ms
stop_type = Stop.COAST
waitA = False
colorA = Color.BLACK 
valeura = 30 #reflection de base
post = 0 #reflection qui change 
#PID
#incoming
 
#LineFollow
while True:
    #if sRight.color() == colorA : 
    if sRight.reflection() < valeura:
        mLeft.run(speed)#, timeA, stop_type, wait)
        mRight.run(speed2)
        post = sRight.reflection() # check de la couleur et enregistrement
        print("mLeft")
        print(sRight.reflection())

    elif sRight.reflection() > valustart:
        mRight.run(speed)#, timeA, stop_type, wait)
        mLeft.run(speed2)
        print("mRight")
        print(sRight.reflection())    

    elif post > 30 and sRight.reflection() > 30 or post < 30 and sRight.reflection() < 30 : 
        nbrotate =+10
        robot.run_time(speed, timeA, stop_type, wait)
    
    elif nbrotate > 100: 
        nbrotate == 100 