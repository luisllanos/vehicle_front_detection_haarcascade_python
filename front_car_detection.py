#! /usr/bin/python
 
import cv2
 
face_cascade = cv2.CascadeClassifier('cars.xml')
vc = cv2.VideoCapture('video1.avi')
 
if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
 
 
roi = [0,0,0,0]
lastdetected = 0
detections = 0
 
while rval:
    rval, frame = vc.read()
    fheight, fwidth, fdepth = frame.shape 
  
    # car detection.
    cars = face_cascade.detectMultiScale(frame, 1.1, 1)
 
    ncars = 0
    for (x,y,w,h) in cars:
       
        # do not detect cars in the sky. 
        if x > fwidth*0.4 and x < fwidth*0.5 and y > fheight*0.25 and w > 30 and h > 30:
 
                if ( abs(x-roi[0]) < 20 ):
                    x = roi[0]
 
                if ( abs(y-roi[1]) < 20 ):
                    y = roi[1]
 
                if ( abs(w-roi[2]) < 20 ):
                    w = roi[2]
 
                if ( abs(h-roi[3]) < 50 ):
                    h = roi[3]
 
                roi = [x,y,w,h]
                ncars = ncars + 1
                lastdetected = 0
                detections = detections + 1
 
    # seen in the last 50 frames
    if lastdetected < 5:
         cv2.rectangle(frame,(roi[0],roi[1]),(roi[0]+roi[2],roi[1]+roi[3]),(0,0,255),2)
 
    lastdetected = lastdetected + 1
    
    # show result
    cv2.imshow("Result",frame)
    cv2.waitKey(1);
vc.release()
