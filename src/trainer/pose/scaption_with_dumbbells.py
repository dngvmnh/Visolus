import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("src/trainer/test_vid/knee_flexion_extension.mp4", cv2.CAP_DSHOW)

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
        angle_1 = detector.findAngle(img, 24, 12, 14)
        # # Left Arm
        # angle_1 = detector.findAngle_1(img, 11, 13, 15,False)
        per_1 = np.interp(angle_1, (20, 160), (0, 100))
        bar_1 = np.interp(angle_1, (20, 160), (650, 100))
        # print(angle_1, per_1)
        angle_2 = detector.findAngle(img, 23, 11, 13)
        per_2 = np.interp(angle_2, (200, 340), (100, 0))
        bar_2 = np.interp(angle_2, (200, 340), (100, 650))
        # print(angle_1, per_1)

        # Check for the dumbbell curls
        color = (52, 199, 89)
        bar=(bar_1+bar_2)/2
        per=(per_1+per_2)/2
        if per==100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per<=10:
            if dir == 1:
                count += 0.5
                dir = 0
            

        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        # Draw Curl Count
        # cv2.rectangle(img, (0, 450), (250, 720), (52, 199, 89), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (52, 199, 89), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
    #             (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)