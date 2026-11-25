
import cv2

# Open the laptop's default camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera not found!")
    exit()

print("SmartDrive camera started successfully!")
print("Press Q to close the camera.")

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to capture an image.")
        break

    # Add the project name to the video
    cv2.putText(
        frame,
        "SMARTDRIVE - CAMERA TEST",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Display the live video
    cv2.imshow("SmartDrive Vision System", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
