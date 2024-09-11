#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, OUTPUT_D
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
# state constants
ON = True
OFF = False


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!')
    # rectangular path
    tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
    # for i in range(4):
    #     tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)
    #     tank_drive.on_for_rotations(SpeedPercent(-25), SpeedPercent(20.625), 0.5625)
    #     sleep(0.5)
    # sleep(1)
    # lemniscate path
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(25), 1)
    tank_drive.on_for_rotations(SpeedPercent(25), SpeedPercent(-25), 1)
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)
    tank_drive.on_for_rotations(SpeedPercent(25), SpeedPercent(-25), 0.25)
    tank_drive.on_for_rotations(SpeedPercent(25), SpeedPercent(25), 1)
    tank_drive.on_for_rotations(SpeedPercent(25), SpeedPercent(-25), 1)
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)
    sleep(0.5)
    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')

    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)

if __name__ == '__main__':
    main()
