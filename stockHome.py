
#! /usr/bin/python2
from urllib.request import urlopen
import time
import sys
import json
import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os
from hx711 import HX711
import RPi.GPIO as GPIO

# take argument with command to run the code and append it to "item" variable.
item = sys.argv[1]
# ignore inconsequential warnings when starting
GPIO.setwarnings(False)

# Firebase setup
cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sensepi-c7a8f.firebaseio.com/'
})
weightdb = db.reference(item)

# Thingspeak setup
WRITE_API_KEY='TE6KKXKBIBDN5I29'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

# depending on argument entered when starting the script, the data will go into the relevant graph on Thingspeak
def writeData(val):
    # Sending the data to thingspeak in the query string
    if item == "potatoes":
    	conn = urlopen(baseURL + '&field1=%s' % (val))
    if item == "coffee":
        conn = urlopen(baseURL + '&field2=%s' % (val))
    if item == "sugar":
        conn = urlopen(baseURL + '&field3=%s' % (val))
    #print(conn.read())
    # Closing the connection
    conn.close()

# Call HX711 class from the hx711.py script, set pin 5 on the GPIO to data input and pin 6 to clock pulse    
hx = HX711(5, 6)

# This reference unit is for calibration, needs to be calculated when known weight is placed on the scale. You divide the output value by this number to give the correct weight
# When its done once, its done for all further measurements.
hx.set_reference_unit(471)

hx.reset()

# This is an initial measurement to set a zero point. Whatever is measured during the tare, will not be counted in the final measurement. So this is an 
# opportunity to place any containers on the scale before adding the items you plan to measure. 
hx.tare()

input("Tare done! Add weight now and press any key")

# assign reading to val, print and send it to the firebase database and thingspeak graphs. Sleep for 15 seconds after each measurement as Thingspeak will not accept data at
# quicker intervals.
while True:
    try:
        val = round(hx.get_weight(5),2)
        print(val)
        weightdb.update({
                    'weight': val
                    })
        writeData(val)
        hx.power_down()
        hx.power_up()
        time.sleep(15)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
