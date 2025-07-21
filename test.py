import cv2
import numpy as np 
import time

#open the camera
cam = cv2.VideoCapture(0)

#color to track (currently green)
lower_color = np.array([35, 100, 100])
upper_color = np.array([85, 255, 255])

last_time = time.time()

while True: #read from the cam until it fails / ends
    ret,frame = cam.read()
    if not ret:
        break

    #change frame to hsv color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    #seperate the tracked colors from the non tracked ones
    mask = cv2.inRange(hsv, lower_color, upper_color)

    #find the shape / outlines of the tracked colors
    contours , ignored = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    #find the largest shape / outline
    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 0: #can be used to hide tiny spaces but current doesnt do that
            x,y,w,h = cv2.boundingRect(largest)

            cx,cy= (x+w)//2, (y+h)//2


            #draw frame for tracking
            cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),2)
            cv2.circle(frame, (cx,cy),5,(255,0,0),-1)

            #print the time every second
            if time.time() - last_time > 1.0:
                print(f"Object position: ({cx},{cy})")
                last_time = time.time()

    #show the frame
    cv2.imshow("lol", frame)

    #stop tracking and close the window when 'a' is pressed
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cam.release()
cv2.destroyAllWindows()