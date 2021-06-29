#!/usr/bin/env python3
#https://www.instructables.com/id/RF-433-MHZ-Raspberry-Pi/
#gpio 27, vcc, gnd

import signal
import sys
import time
import RPi.GPIO as GPIO
from rpi_rf import RFDevice
rf_gpio = 27
print('done1')
"""
buf = []
buf1=[]


GPIO.setmode(GPIO.BCM)
GPIO.setup(rf_gpio, GPIO.IN)
while 1:
    for i in range(0,8):
        buf.append(GPIO.input(rf_gpio))
    print(buf,end='\n')
    buf.
    buf1.append(buf)
    time.sleep(0.1)
rfdevice = None

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(rf_gpio)
rfdevice.enable_rx()
timestamp=None
while True:

    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        print(str(rfdevice.rx_code) + " [pulselength " + str(rfdevice.rx_pulselength) + ", protocol " + str(rfdevice.rx_proto) + "]")

    time.sleep(0.01)
    #print(rfdevice.rx_code)
    #print(rfdevice.rx_proto)

rfdevice.cleanup()"""


def status():
    #print('receive true')
    return True