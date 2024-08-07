import cv2
from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture("src/3d_motion_capture/Video.mp4")
cap = cv2.VideoCapture(0)


detector = PoseDetector()
posList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            # lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},'

        posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("src/3d_motion_capture/AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])