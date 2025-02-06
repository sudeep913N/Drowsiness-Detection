# Drowsiness-Detection
This project demonstrates real-time eye closure detection using OpenCV, dlib, and NumPy in Python. It calculates the Eye Aspect Ratio (EAR) to estimate eye closure and triggers an alert sound when the eyes are closed beyond a certain threshold.

## Features

* Real-time eye closure detection from webcam or video file.
* Calculates Eye Aspect Ratio (EAR) to quantify eye openness.
* Estimates eye closure percentage based on EAR values.
* Plays an alert sound (e.g., "alert.mp3") when the eye closure percentage exceeds a defined threshold (e.g., 50%).
* Displays the eye closure percentage on the video frame.

## Requirements

* Python 3.x
* OpenCV (`cv2`)
* dlib
* NumPy (`numpy`)
* playsound
* A pre-trained shape predictor model (`shape_predictor_68_face_landmarks.dat`) - You can download this from [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).  Extract the `.dat` file and place it in the same directory as your Python script.
* An alert sound file (`alert.mp3`) - Place this in the same directory as your Python script.  You can use any `.mp3` file you like.

## Installation

1.  **Clone the repository (optional):**  If you've downloaded the code as a zip file, skip this step. If you're using git, clone it:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)  # Replace with your repository URL
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Install the required libraries:**
    ```bash
    pip install opencv-python dlib numpy playsound
    ```

3.  **Download the shape predictor:** Download `shape_predictor_68_face_landmarks.dat` from the link provided above and place it in the project directory.

4.  **Place `alert.mp3`:** Place your `alert.mp3` file in the project directory.

## Usage

1.  Run the Python script:
    ```bash
    python eye_closure_detection.py
    ```

2.  The script will capture video from your webcam (default).  To use a video file, change `cv2.VideoCapture(0)` to `cv2.VideoCapture("path/to/your/video.mp4")`.

3.  The video feed will be displayed, showing the estimated eye closure percentage.

4.  When the eye closure percentage exceeds 50% (or your defined threshold), the alert sound will play.

5.  Press 'q' to exit the program.

## Code Explanation

*   **`calculate_EAR(eye)`:** Calculates the Eye Aspect Ratio (EAR) for a given eye region.
*   **`detect_eyes(frame)`:** Detects faces, extracts eye landmarks, calculates EAR, and estimates eye closure percentage.
*   The main loop captures video frames, calls `detect_eyes`, displays the results, and plays the alert sound when necessary.
