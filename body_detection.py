import cv2
import mediapipe as mp


class BodyDetector:

    def __init__(self):

        self.mp_pose = mp.solutions.pose


        self.pose = self.mp_pose.Pose(

            static_image_mode=False,

            model_complexity=1,

            min_detection_confidence=0.5,

            min_tracking_confidence=0.5

        )


        self.mp_draw = mp.solutions.drawing_utils



    def detect(self, frame):


        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        results = self.pose.process(rgb)



        if results.pose_landmarks:


            self.mp_draw.draw_landmarks(

                frame,

                results.pose_landmarks,

                self.mp_pose.POSE_CONNECTIONS

            )


            h,w,_ = frame.shape


            landmarks = results.pose_landmarks.landmark


            body_points = {


                "Left Wrist": mp.solutions.pose.PoseLandmark.LEFT_WRIST,

                "Right Wrist": mp.solutions.pose.PoseLandmark.RIGHT_WRIST,

                "Left Knee": mp.solutions.pose.PoseLandmark.LEFT_KNEE,

                "Right Knee": mp.solutions.pose.PoseLandmark.RIGHT_KNEE


            }



            for name, point in body_points.items():


                lm = landmarks[point]


                x = int(lm.x*w)

                y = int(lm.y*h)


                cv2.circle(

                    frame,

                    (x,y),

                    8,

                    (255,0,0),

                    -1

                )


                cv2.putText(

                    frame,

                    name,

                    (x+10,y),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.5,

                    (255,255,0),

                    2

                )



        return frame