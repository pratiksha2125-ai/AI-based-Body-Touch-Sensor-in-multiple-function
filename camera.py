# import cv2

# class Camera:

#     def __init__(self):
#         self.cap = cv2.VideoCapture(0)

#     def get_frame(self):
#         success, frame = self.cap.read()

#         if success:
#             return frame
#         return None

#     def release(self):
#         self.cap.release()


import cv2
class Camera:
    cap = cv2.VideoCapture(0)

    print(cap.isOpened())

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow("BodyPart Touch Senser", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()