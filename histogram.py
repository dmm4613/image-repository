import imutils
import cv2

class RGBHistogram:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        #normalize histogram so image scale is not an issue
        hist = cv2.calcHist([image], [0,1,2],
        None, self.bins, [0, 256, 0, 256, 0, 256])

        #use OpenCV 2.4 to normalize histogram 
        if imutils.is_cv2():
            hist = cv2.normalize(hist)
        #or use OpenCV 3+
        else:
            hist = cv2.normalize(hist,hist)

        return hist.flatten()