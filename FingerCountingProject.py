import cv2 as cv
import time
import os
import HandTrackingModule as htm
wCam, hCam= 640, 480
cap= cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath= "Photos"
myList= os.listdir(folderPath)
myList.sort()
print(myList)
overlayList= []
for imPath in myList:
    if imPath=='.DS_Store':
        continue
    image= cv.imread(f'{folderPath}/{imPath}')
    #print(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

pTime=0

detector= htm.handDetector(min_detection_confidence= 0.75)

tipIds= [4,8, 12, 16, 20]
while True:
    success, img= cap.read()
    img= detector.FindHands(img)
    lmlist= detector.findPosition(img, draw=False)
    #print(lmlist)

    if(len(lmlist)!= 0):
        fingers= []
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
                fingers.append(1)
        else:
            fingers.append(0)
        for id in range (1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)
        totalFingers= fingers.count(1)
        print(totalFingers)

        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w]= overlayList[totalFingers-1]

        cv.rectangle(img, (20,225), (170, 425), (0,255,0), cv.FILLED)
        cv.putText(img, str(totalFingers), (45, 375), cv.FONT_HERSHEY_PLAIN, 10, (255,0,0), 25)
    cTime= time.time()
    fps= 1/ (cTime-pTime)
    pTime= cTime

    cv.putText(img, f'FPS: {int(fps)}', (400, 70), cv.FONT_HERSHEY_PLAIN, 3 ,(255,0,0), 3)
    cv.imshow('Image', img)
    cv.waitKey(1)