import cv2
from win10toast import ToastNotifier

# Replace with your DroidCam IP address and port
droidcam_ip = "192.168.1.33"
droidcam_port = "4747"
# Construct the video stream URL with a higher frame rate
video_stream_url = f"http://{droidcam_ip}:{droidcam_port}/video?fps=30"

# Open the video stream
vs = cv2.VideoCapture(video_stream_url)

# Check if the video stream is opened successfully
if not vs.isOpened():
    print("Error: Couldn't open video stream.")
    exit()

# Initialize variables
first_frame = None
motion_detected = False
motion_start_frame = None
motion_duration_threshold = 20  # Number of consecutive frames with motion to trigger detection

while True:
    _, frame = vs.read()

    # Check if the frame is empty
    if frame is None:
        print("Error: Couldn't read frame.")
        break

    text = "No Motion Detected"  # Default text

    # Resize the frame to a smaller size
    frame = cv2.resize(frame, (640, 480))

    # Convert the frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # Compute the absolute difference between the current frame and the first frame
    frame_delta = cv2.absdiff(first_frame, gray)

    # Threshold the delta image
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the threshold image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check for motion
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            if not motion_detected:
                motion_start_frame = 0  # Start counting frames when motion is detected
            motion_detected = True

            # Draw bounding box around the detected motion
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the text on the frame
    if motion_detected:
        motion_start_frame += 1
        if motion_start_frame >= motion_duration_threshold:
            # Trigger motion detected status after sustained motion
            text = "Motion Detected"
    else:
        # Reset motion detection variables when no motion is detected
        motion_start_frame = None

    cv2.putText(frame, f"Status: {text}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show the frame with a delay of 1 millisecond
    cv2.imshow("Motion Detection", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# Clean up
vs.release()
cv2.destroyAllWindows()