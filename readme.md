# Motion Detection with DroidCam

This Python script uses OpenCV to perform motion detection on a video stream obtained from DroidCam. It displays a live video feed and updates the status text based on motion detection.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3
- OpenCV (`pip install opencv-python`)
- DroidCam installed on your Android device

## Getting Started

1. **Install the required packages:**

   ```bash
   pip install opencv-python
2. **clone the repository**

    git clone https://github.com/deepanshu0211/motion-detection-droidcam.git
    cd motion-detection-droidcam

3. **Replace the placeholders in the script (motion_detection.py) with your DroidCam IP address and port:**

    # Replace with your DroidCam IP address and port
    droidcam_ip = "YOUR_DROIDCAM_IP"
    droidcam_port = "YOUR_DROIDCAM_PORT"

4. **Run the script:**
    python motion_detection.py


## Configuration

    Adjust the following parameters in the script to customize the motion detection:

    1. 'motion_duration_threshold:' Number of consecutive frames with motion to trigger detection.

    Feel free to explore and modify the script to suit your specific requirements.

## Usage

 **The live video feed will be displayed with the status text indicating whether motion is detected or not.**
**When motion is detected and sustained for the specified duration, the status text will change to "Motion Detected."**

## License

    This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

    Thanks to the OpenCV community for their excellent computer vision library.


Feel free to customize this `README.md` file further based on your preferences. Replace placeholders with your actual information and add any additional sections or details that you find relevant.


