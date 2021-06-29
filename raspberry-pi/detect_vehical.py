import cv2


def detect_vehical(img):
    #cap = cv2.VideoCapture(video_src)

    bike_cascade = cv2.CascadeClassifier('two_wheeler.xml')
    bus_cascade = cv2.CascadeClassifier('Bus_front.xml')
    cars_cascade = cv2.CascadeClassifier('cars.xml')
    pedestrian_cascade = cv2.CascadeClassifier('pedestrian.xml')
    """
    while True:
        ret, img = cap.read()
        if (type(img) == type(None)):
            break
    """
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    #bike
    bike = bike_cascade.detectMultiScale(gray, 1.19, 1)
    for(x, y, w, h) in bike:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 215), 2)
            
    #bus
    bus = bus_cascade.detectMultiScale(gray, 1.16, 1)
    for (x, y, w, h) in bus:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
         
    #cars
    cars = cars_cascade.detectMultiScale(gray, 1.1, 2)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
            
    #pedestrian
    pedestrian = pedestrian_cascade.detectMultiScale(gray, 1.3, 2)
    for(a, b, c, d) in pedestrian:
        cv2.rectangle(img, (a, b), (a+c, b+d), (0, 255, 210), 4)
    
    return img