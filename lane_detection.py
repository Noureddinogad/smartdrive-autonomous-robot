
import cv2

# Open the laptop webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found!")
    raise SystemExit(1)

print("SmartDrive - Lane Detection Started")
print("Press Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        break

    # Step 1: Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 2: Reduce image noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3: Extract bright pixels
    _, mask = cv2.threshold(
        blurred, 180, 255, cv2.THRESH_BINARY
    )

    # Step 4: Display the original and processed images
    cv2.imshow("1 - Original Camera", frame)
    cv2.imshow("2 - White Line Detection", mask)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
