import cv2

class Image :

    def capture(self, frame, location) :

        cv2.imwrite( filename = location, img = frame )









































