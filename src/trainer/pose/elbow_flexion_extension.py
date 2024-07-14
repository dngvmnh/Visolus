import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

cap.set(cv2.CAP_PROP_FPS, 60)

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        #angle = detector.findAngle(img, 11, 13, 15,False)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))
        # print(angle, per)

        color = (52, 199, 89)
        if per == 100:
            color = (52, 199, 89)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (52, 199, 89)
            if dir == 1:
                count += 0.5
                dir = 0
      
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # cv2.rectangle(img, (0, 450), (250, 720), (52, 199, 89), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (52, 199, 89), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
    #             (255, 0, 0), 5)
    
    # if cv2.waitKey(1) & 0xFF == ord('q'): #for my mac
    #     break

    cv2.imshow("Image", img)
    cv2.waitKey(1)