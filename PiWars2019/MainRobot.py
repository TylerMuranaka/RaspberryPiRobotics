import RPiRobot
from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO
import time

Forward() = RPiRobot.Forward()
Reverse() = RPiRobot.Reverse()
TurnRight() = RPiRobot.TurnRight()
TurnLeft() = RPiRobot.TurnLeft()
Stop() = RPiRobot.Stop()

def dpad(pos):
    if pos.top:
        Forward()
    elif pos.bottom:
        Reverse()
    elif pos.left:
        TurnRight()
    elif pos.right:
        TurnLeft()
    elif pos.middle:
        
bd = BlueDot()
bd.when_pressed = dpad