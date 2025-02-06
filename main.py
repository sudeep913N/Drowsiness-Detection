import cv2
import dlib
import numpy as np
from playsound import playsound  # Import the playsound library

# Load the frontal face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to calculate the eye aspect ratio (EAR)
def calculate_EAR(eye):
    p1, p2, p3 = eye[1], eye[5], eye[2]
    p4, p5, p6 = eye[4], eye[0], eye[3]

    # Calculate the distances between the eye landmarks
    top_width = np.linalg.norm(p1 - p2)
    bottom_width = np.linalg.norm(p3 - p4)
    height = np.linalg.norm(p1 - p5)

    # Calculate the EAR
    ear = (top_width + bottom_width) / (2.0 * height)
    return ear

# Function to detect eyes and calculate EAR
def detect_eyes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) == 0:  # If no faces are detected
        return 0  # Return 0 for eye closure percentage

    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])

        # Extract the eye landmarks
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]

        # Calculate the EAR for each eye
        left_ear = calculate_EAR(left_eye)
        right_ear = calculate_EAR(right_eye)

        # Calculate the average EAR
        ear = (left_ear + right_ear) / 2.0

        # Estimate eye closure percentage based on a threshold
        if ear < 0.2:
            eye_closure_percentage = 100
        elif ear < 0.3:
            eye_closure_percentage = 75
        elif ear < 0.4:
            eye_closure_percentage = 50
        else:
            eye_closure_percentage = 0

        return eye_closure_percentage

# Load a video file or capture from a camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect eyes and calculate EAR
    eye_closure_percentage = detect_eyes(frame)

    # Display the frame with the estimated eye closure percentage
    cv2.putText(frame, f"Eye Closure: {eye_closure_percentage}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Eye Closure Detection", frame)

    # Play sound if eye closure percentage is more than 50%
    if eye_closure_percentage > 50:
        playsound("alert.mp3")  # Make sure to have the alert.mp3 in your project folder

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
