import cv2
import mediapipe as mp


class FaceDetector:

    def __init__(self):

        self.mp_face = mp.solutions.face_mesh

        self.face_mesh = self.mp_face.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )


    def detect(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.face_mesh.process(rgb)


        if results.multi_face_landmarks:

            h, w, _ = frame.shape


            for face in results.multi_face_landmarks:


                points = {

                    "Nose": 1,

                    "Left Eye": 33,
                    "Right Eye": 263,

                    "Left Eyebrow": 105,
                    "Right Eyebrow": 334,

                    "Mouth": 13,

                    "Left Ear": 234,
                    "Right Ear": 454

                }


                for name, index in points.items():

                    landmark = face.landmark[index]


                    x = int(
                        landmark.x * w
                    )

                    y = int(
                        landmark.y * h
                    )


                    cv2.circle(
                        frame,
                        (x, y),
                        5,
                        (0,255,0),
                        -1
                    )


                    cv2.putText(
                        frame,
                        name,
                        (x+10, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0,255,255),
                        2
                    )


        return frame