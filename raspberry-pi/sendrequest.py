#retrive data from firebase
from firebase import firebase
firebase = firebase.FirebaseApplication('https://fir-test-c8a84.firebaseio.com/', None)


def sendrequest(lat,lon,DeviceID):
    firebase.put('helpRequest', DeviceID, {'g': 'help','l': {'0': lat,'1': lon}})
    #firebase.put('helpRequest/' + DeviceID, 'l', )
    print("request send..")


def helpnumber(DeviceID):
    number = firebase.get('/Users/Device/' + DeviceID + '/EmergencyNumber', None)
    return number


def helpname(DeviceID):
    name = firebase.get('/Users/Device/' + DeviceID + '/EmergencyName', None)
    return name