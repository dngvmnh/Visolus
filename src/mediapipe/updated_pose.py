from cvzone.PoseModule import PoseDetector
import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the PoseDetector
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

while True:
    success, img = cap.read()

    # Detect the pose in the image
    img = detector.findPose(img)

    # Get the list of landmarks and bounding box info
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

    if lmList:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        # List of keypoints for which we want to calculate the angles
        # Here, each triplet represents (start point, middle point, end point)
        keypoints = [
            (11, 13, 15),  # Left arm
            (12, 14, 16),  # Right arm
            (23, 25, 27),  # Left leg
            (24, 26, 28),  # Right leg
            (11, 23, 25),  # Left side of body
            (12, 24, 26),  # Right side of body
            (0, 11, 12),   # Neck (head to shoulders)
            (11, 0, 12),   # Shoulders (left shoulder, head, right shoulder)
            (23, 11, 13),  # Left side of body to left arm
            (24, 12, 14),  # Right side of body to right arm
            (11, 23, 25),  # Left leg (hip, knee, ankle)
            (12, 24, 26)   # Right leg (hip, knee, ankle)
        ]
        

        for kp in keypoints:
            start, mid, end = kp

            # Calculate the angle
            angle, img = detector.findAngle(lmList[start][0:2],
                                            lmList[mid][0:2],
                                            lmList[end][0:2],
                                            img=img,
                                            color=(0, 0, 255),
                                            scale=10)

            # Check if the angle is close to a specific value (optional)
            isCloseAngle = detector.angleCheck(myAngle=angle,
                                               targetAngle=50,  # Example target angle
                                               offset=5)

            # Print the angle and the result of the angle check
            # print(f'Angle at {mid}: {angle}, Close to 50: {isCloseAngle}')

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(1)