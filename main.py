import cv2

from camera import Camera
from face_detection import FaceDetector
from body_detection import BodyDetector
from hand_detection import HandDetector
from touch_detection import TouchDetector


camera = Camera()
face = FaceDetector()
body = BodyDetector()
hand = HandDetector()
touch1 = TouchDetector()

while True:

    # frame = camera.get_frame()

    if frame is None:
        break

    # Face Detection
    frame = face.detect(frame)

    # Body Detection
    frame = body.detect(frame)

    # Hand Detection
    frame = hand.detect(frame)

    # # Finger Touch Detection
    # frame = touch1.detect(frame)
    

    # Display Output
    cv2.imshow("SmartBody Vision", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()



