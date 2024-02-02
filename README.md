# Hand Tracking Project

This repository contains Python scripts utilizing OpenCV and MediaPipe for hand tracking. The main script uses webcam input to track hand movement and perform actions like mouse movement and clicks.

## Features

- Real-time hand tracking with webcam input.
- Mouse control using hand movements.
- Click actions based on finger positions.

## Prerequisites

- Python 3.x
- OpenCV (`opencv-python-headless`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)
- Autopy (`autopy`)

Install the required libraries using:

```bash
pip install opencv-python-headless mediapipe numpy autopy
```
## Usage
```
python hand_tracking.py
```
## How it works
The script captures video from the webcam, detects hand landmarks, and interprets gestures to control the mouse. It allows for mouse movement with the index finger and clicking by pinching the index and middle fingers.
