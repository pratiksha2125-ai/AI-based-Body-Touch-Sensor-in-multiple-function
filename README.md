# SmartBody Vision: AI-Based Body Part Touch Detection Using Index Finger

## Project Overview

SmartBody Vision is an Artificial Intelligence and Computer Vision-based project that detects human face and body parts in real time using a webcam. The system uses an index finger as an interaction point to identify which body part is being touched.

Unlike a normal detection system, this project does not continuously display all body part names. It displays the body part name only when the index finger touches that specific part.

Example:
Index Finger Touching:
Nose


---

# Features

## Face Part Detection

The system can detect:

- Nose
- Eyes
- Eyebrows
- Lips
- Cheeks
- Ears

## Body Part Detection

The system can detect:

- Shoulders
- Neck
- Hands
- Arms

## Touch Interaction

- Detects index finger position.
- Calculates distance between index finger and body parts.
- Identifies the touched body part.
- Displays only the touched part name.

---

# Technologies Used

## Python

Used as the main programming language for developing the computer vision application.

## OpenCV

Used for:
- Webcam access
- Image processing
- Real-time video display

## MediaPipe

Used for:
- Face landmark detection
- Hand landmark detection
- Body pose detection

## NumPy

Used for:
- Coordinate calculations
- Data processing

---

# Project Workflow

Webcam Input
|
|
OpenCV Processing
|
|
MediaPipe Detection
|
|
| Face Detection |
| Body Detection |
| Index Finger Detection |
  |
  |

Distance Calculation
|
|
Touch Detection
|
|
Display Touched Part Name


---

# System Modules

## 1. Camera Module (`camera.py`)

Responsibilities:

- Open webcam.
- Capture video frames.
- Send frames to detection modules.
- Release camera after completion.

---

## 2. Face Detection Module (`face_detection.py`)

Responsibilities:

- Detect facial landmarks.
- Identify positions of:
  - Nose
  - Eyes
  - Eyebrows
  - Lips
  - Cheeks
  - Ears

---

## 3. Body Detection Module (`body_detection.py`)

Responsibilities:

- Detect body landmarks.
- Identify:
  - Shoulders
  - Neck
  - Hands
  - Arms

---

## 4. Hand Detection Module (`hand_detection.py`)

Responsibilities:

- Detect hand landmarks.
- Track index finger tip.
- Provide index finger coordinates.

Index Finger Landmark:


Index Finger Tip = Landmark 8


---

## 5. Touch Detection Module (`touch_detection.py`)

Responsibilities:

- Compare index finger position with body part positions.
- Calculate distance between points.
- Detect touched body part.

Logic:


If Distance < Threshold

    ↓

Body Part Touched


---

# Touch Detection Algorithm

1. Detect index finger position.
2. Detect body part coordinates.
3. Calculate distance between them.

Formula:


Distance = √((x2-x1)² + (y2-y1)²)


4. If distance is below the threshold:
   

Touched Part = Body Part Name


---

# Project Structure


SmartBody_Vision/

│
├── main.py
├── camera.py
├── face_detection.py
├── body_detection.py
├── hand_detection.py
├── touch_detection.py
├── requirements.txt
└── README.md


---

# Installation

Install required libraries:

```bash
pip install opencv-python
pip install mediapipe
pip install numpy
How to Run
Clone or download the project.
Open the project folder.
Install dependencies:
pip install -r requirements.txt
# Run the main file:
python main.py
Use your index finger to touch different body parts.
The system displays the touched part name.
 # Example Output

When finger touches nose:

Touched Part:
Nose

When finger touches eye:

Touched Part:
Left Eye

When finger touches shoulder:

Touched Part:
Right Shoulder

# Applications
 1.Human-computer interaction systems
2.AI-based learning applications
3.Interactive games
4.Virtual assistants
5.Rehabilitation systems
6.Smart healthcare applications
7.Future Improvements
# Add voice feedback.
1.Add GUI dashboard.
2.Add touch history.
3.Add gesture recognition.
4.Improve accuracy using advanced AI models.
5.Develop mobile application support.


Author of project:
Pratiksha Pasarge
Conclusion

SmartBody Vision demonstrates the use of Artificial Intelligence and Computer Vision for real-time human interaction. The project combines face detection, body detection, hand tracking, and touch recognition to create an interactive AI-based system.
