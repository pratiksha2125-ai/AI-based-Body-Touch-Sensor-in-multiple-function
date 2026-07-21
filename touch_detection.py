import math


class TouchDetector:

    def __init__(self):
        self.threshold = 40
        self.touch_frames = 0
        self.required_frames = 5


    def calculate_distance(self, p1, p2):

        return math.hypot(
            p1[0] - p2[0],
            p1[1] - p2[1]
        )


    def check_touch(self, finger, body_parts):

        if finger is None or not body_parts:
            self.touch_frames = 0
            return None


        closest_part = None
        min_distance = float("inf")


        # Find nearest body part
        for name, position in body_parts.items():

            distance = self.calculate_distance(
                finger,
                position
            )

            if distance < min_distance:
                min_distance = distance
                closest_part = name


        # Confirm touch
        if min_distance < self.threshold:

            self.touch_frames += 1

            if self.touch_frames >= self.required_frames:
                return closest_part

        else:
            self.touch_frames = 0


        return None