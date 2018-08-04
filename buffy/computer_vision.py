# Install imutils and opencv-python with pip
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

DIGITS_LOOKUP = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 1, 0): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9
}


class VisionForRobot:
    def __init__(self, picture_name="pic2", see_pics=False):
        self.picture_name = picture_name
        self.see_pics = see_pics
        """
        Recognize the number in a pH meter
        :param picture_name:    Which picture to check
        :param see_pics:        Follow progress or not
        """

    def recognize_numbers(self):
        # load the example image
        image = cv2.imread("pic2.jpg")

        # pre-process the image by resizing it, converting it to
        # graycale, blurring it, and computing an edge map
        image = imutils.resize(image, height=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if self.see_pics:
            cv2.imshow('Gray', gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        if self.see_pics:
            cv2.imshow('Blurred', blurred)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        edged = cv2.Canny(blurred, 50, 200, 255)
        if self.see_pics:
            cv2.imshow('Edge', edged)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # find contours in the edge map, then sort them by their
        # size in descending order
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        displayCnt = None

        if self.see_pics:
            cv2.drawContours(image, [cnts[0]], 0, (0, 0, 255), 3)
            cv2.drawContours(image, [cnts[1]], 0, (0, 255, 0), 3)
            cv2.drawContours(image, [cnts[2]], 0, (255, 0, 0), 3)
            cv2.imshow('Important points', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # loop over the contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            # if the contour has four vertices, then we have found
            # the thermostat display
            if len(approx) == 4:
                displayCnt = approx
                break

        # extract the thermostat display, apply a perspective transform
        # to it
        warped = four_point_transform(gray, displayCnt.reshape(4, 2))
        output = four_point_transform(image, displayCnt.reshape(4, 2))
        if self.see_pics:
            cv2.imshow('Warped', warped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # threshold the warped image, then apply a series of morphological
        # operations to cleanup the thresholded image
        thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        if self.see_pics:
            cv2.imshow('Threshold', thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        if self.see_pics:
            cv2.imshow('Open', thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()




        return -1






