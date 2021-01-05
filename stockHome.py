
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

# Call HX711 class from the hx711.py script, set channel 5 to     
hx = HX711(5, 6)

hx.set_reference_unit(471)


hx.reset()

hx.tare()

input("Tare done! Add weight now and press any key")


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
