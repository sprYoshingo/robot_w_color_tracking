# Color Tracking Robot with Raspberry Pi & Arduino

A robotics project that tracks a specific color using computer vision and moves toward it in real time.

---

## Overview

This project combines the **Raspberry Pi 3B+** and an **Arduino Uno R3** to create a mobile robot that:

- Detects and tracks a target color (like red, green, or blue) using a camera.
- Calculates the position of the color in the camera frame.
- Sends movement commands to the Arduino based on the position to steer the robot.

---

##  Hardware Used

-  **Raspberry Pi 3B+**
    - Runs the OpenCV color detection code.
    - Sends position data to the Arduino via USB serial.
-  **Arduino Uno R3**
    - Receives commands from the Pi.
    - Controls motors 


---

##  Software Used

- **Python 3** (on the Raspberry Pi)
- **OpenCV** for image processing and color detection
- **Arduino IDE** for motor control logic
- **Rest is WIP**

---

