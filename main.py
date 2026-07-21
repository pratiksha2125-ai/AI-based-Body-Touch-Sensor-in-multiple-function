# import cv2

# from camera import Camera
# from face_detection import FaceDetector
# from body_detection import BodyDetector
# from hand_detection import HandDetector
# from touch_detection import TouchDetector


# camera = Camera()
# face = FaceDetector()
# body = BodyDetector()
# hand = HandDetector()
# touch1 = TouchDetector()

# while True:

#     # frame = camera.get_frame()

#     if frame is None:
#         break

#     # Face Detection
#     frame = face.detect(frame)

#     # Body Detection
#     frame = body.detect(frame)

#     # Hand Detection
#     frame = hand.detect(frame)

#     # # Finger Touch Detection
#     # frame = touch1.detect(frame)
    

#     # Display Output
#     cv2.imshow("SmartBody Vision", frame)

#     # Exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# camera.release()
# cv2.destroyAllWindows()




import cv2
import mediapipe as mp
from touch_detection import TouchDetector


# MediaPipe setup
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils


touch_detector = TouchDetector()


camera = cv2.VideoCapture(0)


while True:

    ret, frame = camera.read()

    if not ret:
        break


    frame = cv2.flip(frame, 1)


    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # Detect hand
    hand_result = hands.process(rgb)


    # Detect body
    pose_result = pose.process(rgb)


    finger = None
    body_parts = {}


    # Get index finger position
    if hand_result.multi_hand_landmarks:

        hand = hand_result.multi_hand_landmarks[0]


        h, w, c = frame.shape


        index_tip = hand.landmark[
            mp_hands.HandLandmark.INDEX_FINGER_TIP
        ]


        finger = (
            int(index_tip.x * w),
            int(index_tip.y * h)
        )


        cv2.circle(
            frame,
            finger,
            10,
            (0,255,0),
            -1
        )


    # Get body positions
    if pose_result.pose_landmarks:

        landmarks = pose_result.pose_landmarks.landmark

        h, w, c = frame.shape


        body_parts = {

    "Nose":(
        int(landmarks[0].x*w),
        int(landmarks[0].y*h)
    ),

    "Left Eye":(
        int(landmarks[2].x*w),
        int(landmarks[2].y*h)
    ),

    "Right Eye":(
        int(landmarks[5].x*w),
        int(landmarks[5].y*h)
    ),

    "Left Ear":(
        int(landmarks[7].x*w),
        int(landmarks[7].y*h)
    ),

    "Right Ear":(
        int(landmarks[8].x*w),
        int(landmarks[8].y*h)
    ),

    "Left Lip":(
        int(landmarks[9].x*w),
        int(landmarks[9].y*h)
    ),

    "Right Lip":(
        int(landmarks[10].x*w),
        int(landmarks[10].y*h)
    ),

    "Left Shoulder":(
        int(landmarks[11].x*w),
        int(landmarks[11].y*h)
    ),

    "Right Shoulder":(
        int(landmarks[12].x*w),
        int(landmarks[12].y*h)
    ),

    "Left Hand":(
        int(landmarks[15].x*w),
        int(landmarks[15].y*h)
    ),

    "Right Hand":(
        int(landmarks[16].x*w),
        int(landmarks[16].y*h)
    )
}
        for name, point in body_parts.items():

            cv2.circle(
                frame,
                point,
                5,
                (255,0,0),
                -1
            )


    # Touch detection
    touched_part = touch_detector.check_touch(
        finger,
        body_parts
    )


    if touched_part:

        cv2.putText(
            frame,
            "Touched: " + touched_part,
            (30,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )


    cv2.imshow(
        "SmartBody AI",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



camera.release()
cv2.destroyAllWindows()