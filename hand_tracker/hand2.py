import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
from pynput.mouse import Button,Controller
mouse=Controller()


#############
wCam,hCam=150,80


##########


pTime = 0
#cTime = 0
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector = htm.handDetector(detectionCon=0.2, trackCon=0.2)
while True:
    success, img = cap.read()
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 255), 3)
    img = detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if len(lmlist)!=0:
        mouse.position=1368-lmlist[8][1]*10,lmlist[8][2]*10


        
     
    
    

    

    cv2.imshow("Image", img)
    cv2.waitKey(1)
     