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

#sensor value
getValue = sRight.reflection()

#PID
Kp = 1
Ki = 0
Kd = 0
integral = 0
previous_error = 0

while True:
    error = getValue - sRight.reflection()
    integral += (error * timeA)
    derivative = (error - previous_error) / timeA

    pid = (Kp * error) + (Ki * integral) + (Kd * derivative)

    if speed + abs(pid) > 1000:
        if pid >= 0:
            pid = 1000 - speed
        else:
            pid = speed - 1000


#LineFollow
    
    if pid >= 0:
        mLeft.run_time(speed_sp=speed + pid, time_s=timeA, stop_type, waitA)
        mRight.run_time(speed_sp=speed - pid, time_sp=timeA, stop_type, waitA)
        sleep(timeA / 1000)
    else:
        mLeft.run_time(speed_sp=speed - pid, time_sp=timeA, stop_type)
        mRight.run_time(speed_sp=speed + pid, time_sp=timeA, stop_type)
        sleep(timeA / 1000)   

    previous_error = error

#PID code from Carl Strömberg -> https://gist.github.com/CS2098