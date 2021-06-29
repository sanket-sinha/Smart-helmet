#https://circuitdigest.com/microcontroller-projects/raspberry-pi-3-gps-module-interfacing
#gpio 14 ,15 , vcc, gnd



import time
import serial
import pynmea2




def getlat():
    return latval


def getlon():
    return longval

#the serial port to which the pi is connected.
#create a serial object
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)
msg=[]
try:
    while True:
        data = str(ser.readline())
        #wait for the serial port to churn out data
        gpgga_data_available = data.find("$GPGGA")
        if gpgga_data_available>0:  # the long and lat data are always contained in the GPGGA string of the NMEA dat
            msg = data.split("$GPGGA,",1)[1]
            msg_buff = (msg.split(','))
            
            #parse the latitude and print
            latval = msg_buff[1]
            #concatlat = "lat:" + str(latval)
            
            #parse the longitude and print
            longval = msg_buff[3]
            #concatlong = "long:" + str(longval)
            #print(concatlong)
            if not latval:
                latval = 22.9532
            if not longval:
                longval = 88.3772
            
        latval = 22.9532
        longval = 88.3772
        break
        print("g")
        #time.sleep(0.5)  #wait a little before picking the next data.
except:
    print("loading...")