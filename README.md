# Project Title 
**Computer Vision in Physical Therapy**   

## Abstract  
Integrating computer vision into physical therapy enhances rehabilitation by providing real-time assessments and feedback, addressing challenges such as inconsistent monitoring and patient non-compliance. This project aims to develop a system that accurately tracks and analyzes user movements in real-time, thereby supporting the effectiveness of physical therapy routines. The system employs motion sensors, tracking cameras, and advanced motion analysis software, including tools such as the Mediapipe library with BlazePose GHUM 3D models and OpenCV for motion tracking. These tools enable the system to track movements, calculate joint angles, and analyze user posture with high precision.

A key component of the project is the Dynamic Time Warping (DTW) algorithm, which compares patient movements against reference models to identify deviations and provide corrective feedback. The system demonstrated a 75% accuracy rate in counting repetitions for exercises targeting various body parts, such as the shoulders, arms, back, and knees. Additionally, voice recognition technology was integrated using multithreading, with comparisons between the offline pyttsx3 library and other online APIs, enhancing user-system interaction.

The project’s results underscore the effectiveness of combining computer vision with real-time feedback mechanisms and voice integration, offering a robust tool for physical therapy. By automating the tracking and analysis of therapeutic exercises, this project paves the way for more objective, precise, and personalized rehabilitation programs. The methodologies developed here could be expanded to other areas of health care, contributing to advancements in automated patient monitoring and intelligent feedback systems.

**Visolus** is the name chosen for this system, symbolizing the fusion of vision and well-being. Derived from two Latin words: *visio* (meaning vision) and *salus* (meaning well-being), **Visolus** reflects the system's goal of improving health and wellness through the power of vision technology.

[Link to Poster](<insert-poster-link-here>)

## Graphical Abstract  
Pipeline workflow:

![Pipeline Workflow](<insert-image-link-here>)

## Project Summary

### Problem:  
Physical therapy is essential for recovery from injuries, chronic conditions, and post-surgical rehabilitation, but it faces numerous challenges. One major issue is inconsistent monitoring of patient exercises due to limited access to therapists. This leads to low adherence to prescribed routines, as patients may perform exercises incorrectly or lack motivation without proper supervision. Furthermore, many physical therapy sessions rely on subjective assessments of progress, which reduces the effectiveness of treatment. There's also a demand for cost-effective, scalable solutions that allow for accurate, automated monitoring of exercises without the need for a therapist's constant presence.

### Research Question:  
Current research in physical therapy technology reveals several gaps. While computer vision-based systems are promising for automating the tracking of physical therapy exercises, their accuracy in complex movements remains a challenge, especially in comparison to traditional sensors like Kinect. Additionally, deep learning models used for pose estimation are not yet reliable enough to replace conventional methods, particularly for intricate exercises. Another gap lies in the development of affordable, markerless motion capture systems that can provide precise real-time feedback without requiring costly equipment. Lastly, there is a lack of research on how long-term adherence and rehabilitation outcomes are affected by home-based computer vision therapy.

### Methodology:  
The methodology employed focuses on tracking physical therapy exercises using computer vision and integrating voice interaction.

1. **Research and Identification of Physical Therapy Exercises:**  
    - A comprehensive review of physical therapy literature was conducted to identify exercises suitable for tracking using detection technology.
    - Exercises targeting the shoulders, arms, back, knees, and other body parts were selected for monitoring, such as shoulder external rotation and knee flexion-extension exercises.

2. **Computer Vision for Motion Tracking:**  
    - Mediapipe (BlazePose GHUM 3D models) was used to track human skeletal movements. The 33 key landmark points in the human body were identified to calculate joint angles, allowing posture and movement analysis.
    - OpenCV was employed to capture real-time video, while a custom "PoseModule" library was developed for landmark detection and angle calculation.

3. **Program Development for Exercise Tracking:**  
    - A system was built to recognize and track human skeletal movements in real-time, ensuring accurate detection of joints and posture during exercises.
    - The program demonstrated tracking of four different exercises (e.g., cross-arm stretch, knee flexion-extension). The system incorrectly counted 5 out of 20 repetitions, resulting in an accuracy rate of 75%.

4. **Voice Integration and Multithreading:**  
    - The project integrated voice recognition for user-system interaction.
    - Offline text-to-speech library pyttsx3 was compared with online APIs (OpenAI, Gemini) for converting text to speech.
    - Multithreading was used to handle both voice and image processing, though conflicts between these threads were encountered.

### Tools and Technologies:
- BlazePose (Mediapipe) for pose estimation and skeletal tracking.
- OpenCV for image and video processing.
- Pyttsx3 for offline text-to-speech, compared with cloud-based APIs.
- Threading to run multiple tasks concurrently (voice and image processing).

### Data Processing:  
Linear interpolation was used to estimate missing data points during motion tracking, ensuring smooth and continuous analysis of user movements.

### Dynamic Time Warping (DTW) Algorithm for Recognition  
Dynamic Time Warping (DTW) is used to measure the similarity between two temporal sequences, allowing for effective comparison between different actions captured over time. It operates by finding an optimal alignment between two sequences of body part angles derived from 3D skeletal models.

1. **Algorithm Implementation:**  
    - The DTW algorithm compares the user's movement data with a reference model to identify deviations and provide corrective feedback.
    - Feedback is provided based on distance measures from DTW comparisons, guiding the user to improve their form.

2. **DTW-Based Correction for Therapeutic Exercise:**  
    - DTW compares a patient’s movements against a reference model, suggesting corrections for form improvement.
    - Real-time feedback ensures correct posture and technique based on DTW calculations and joint angle analysis.

## Results & Discussion

### Research on Suitable Physical Therapy Exercises:
- Exercises such as shoulder external rotation, neural glide with ulnar bias, and knee flexion-extension are ideal for tracking and real-time feedback.

### Research and Reference on Computer Vision Technology:  
- Mediapipe’s BlazePose 3D model, along with OpenCV, was explored for accurate skeletal tracking and joint angle analysis.

### Demonstrating Four Different Exercises:  
- Demonstrations of the developed system showed 75% accuracy in counting repetitions for exercises, including knee flexion-extension and shoulder stretches.

### Voice Integration and Multithreading:  
- Offline and online text-to-speech solutions were compared, with multithreading used to integrate simultaneous voice and image processing.

### Limitations and Future Research:  
- Limitations include challenges with lighting conditions, distance from the camera, and tracking accuracy for larger range-of-motion exercises.
- Future research should focus on improving system accuracy and expanding it to more complex exercises and long-term rehabilitation programs.

## Conclusion:  
This project successfully integrates computer vision and voice recognition technologies into a physical therapy system, offering real-time feedback and monitoring for rehabilitation exercises. By utilizing Mediapipe BlazePose for skeletal tracking and OpenCV for video capture, the system effectively monitors movements and analyzes joint angles. The DTW algorithm provides precise comparisons between user actions and reference exercises, generating valuable feedback for therapy improvement.

The system demonstrated a 75% accuracy rate in tracking exercise repetitions. Voice recognition capabilities and real-time feedback mechanisms make this system a promising tool for improving rehabilitation outcomes. Further research is necessary to optimize the technology for complex movements and develop cost-effective, scalable solutions for home-based therapy.

**Visolus**, a fusion of *visio* (vision) and *salus* (well-being), encapsulates the system's mission: to enhance physical well-being through the power of vision technology.

## Report
For a detailed analysis, refer to the full report: View on GitHub
