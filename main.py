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
 # Main method

 #motors
 mRight = Motor(Port.D)
 mLeft = Motor(Port.A)

 #sensor
 sRight = ColorSensor(Port.S4)

#other init for run_time
speed = 360/4 #deg/sec
time = 500 #ms
stop_type = Stop.COAST
wait=false


#value
getValue = sRight.ambient()

#PID
#incoming



