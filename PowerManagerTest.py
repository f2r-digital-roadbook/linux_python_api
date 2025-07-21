#!/bin/python3

from f2r.gamma import *

# Set PowerManagerConfig (Enable / Disable)
# The power manager uses a internal accelerometer to check a steady state of the device.
# If it detects a steady state, it starts counting the time.

# active - Enable disable PowerManager
# lowBrightnessTime - Time in minutes to lower the brightness of the screen 
# standbyTime - Time in minutes shutdown the screen
# shutdownTime - Time in minutes shutdown the device

# Initialize socket client
client = GammaClient()

# 0 - Set the config object
c = PowerManagerConfig( active=True, lowBrightnessTime=2, standbyTime=5, shutdownTime=60 );

# 0 - If the operation succeed.
print( c.perform(client) )
