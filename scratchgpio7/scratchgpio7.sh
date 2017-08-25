#!/bin/bash
#Version 0.2 - add in & to allow simultaneous running of handler and Scratch
#Version 0.3 - change sp launches rsc.sb from "/home/pi/Documents/Scratch Projects"
#Version 0.4 - 20Mar13 meltwater - change to use provided name for home
#Version 1.0 - 29Oct13 sw - change to cd into simplesi_scratch_handler to run servods OK
sudo pkill -f scratchgpio_handler
cd /scratchgpio7
sudo python scratchgpio_handler7.py 127.0.0.1 standard  &
scratch --document "/home/linaro/Documents/Scratch Projects/GPIO_IN_OUT_TEST.sb" &
