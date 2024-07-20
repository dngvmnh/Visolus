import cv2
import numpy as np
import time
import PoseModule as pm
import pyttsx3
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

notify_event = threading.Event()
notify_thread = None

def notify(message):
    engine.say(message)
    engine.runAndWait()
    notify_event.clear()

def video_processing():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
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
            angle_1 = detector.findAngle(img, 24, 12, 14)
            per_1 = np.interp(angle_1, (20, 160), (0, 100))
            bar_1 = np.interp(angle_1, (20, 160), (650, 100))

            angle_2 = detector.findAngle(img, 23, 11, 13)
            per_2 = np.interp(angle_2, (200, 340), (100, 0))
            bar_2 = np.interp(angle_2, (200, 340), (100, 650))

            color = (52, 199, 89)
            bar = (bar_1 + bar_2) / 2
            per = (per_1 + per_2) / 2
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per <= 10:
                if dir == 1:
                    count += 0.5
                    dir = 0

            if 80 <= per <= 90 and not notify_event.is_set():
                notify_thread = threading.Thread(target=notify, args=("Bạn cần đưa tay cao hơn chút nữa.",))
                notify_thread.start()
                notify_thread.join()

            cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

            cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (52, 199, 89), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.imshow("Image", img)
        cv2.waitKey(1)

video_processing()
