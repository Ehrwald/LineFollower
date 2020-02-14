#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
#brick.sound.beep()

###########################################
# Main method incoming

#motors
mRight = Motor(Port.D)
mLeft = Motor(Port.A)

#sensor
sRight = ColorSensor(Port.S4)

#other init for run_time
speed = 360/4 #deg/sec
timeA = 500 #ms
stop_type = Stop.COAST
waitA = False



#PID
#incoming

#LineFollow
while True:
    if sRight.reflection() < 30:  
        mLeft.run_time(speed, timeA, stop_type, wait)
        print("mLeft")
        print(sRight.reflection())
    elif sRight.reflection() > 30:
        mRight.run_time(speed, timeA, stop_type, wait)
        print("mRight")
        print(sRight.reflection())    
