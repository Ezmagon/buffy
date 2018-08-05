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
    (1, 1, 1, 1, 0, 1, 1): 9,
    # Shortcut for instead of Neural Network
    (0, 1, 0, 1, 1, 1, 1): 6,
    (0, 0, 0, 0, 0, 1, 0): 4,
    (0, 0, 0, 0, 1, 1, 0): 4
}


class VisionForRobot:
    def __init__(self, picture_name="pic7.jpeg", see_pics=True):
        self.picture_name = picture_name
        self.see_pics = see_pics
        """
        Recognize the number in a pH meter
        :param picture_name:    Which picture to check
        :param see_pics:        Follow progress or not
        """

    def recognize_numbers(self):
        # load the example image
        image = cv2.imread(self.picture_name)

        # pre-process the image by resizing it, converting it to
        # graycale, blurring it, and computing an edge map
        image = imutils.resize(image, height=500)
        print("Full", image.shape)
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

        [warped, output] = self.zoom_to_rectangle(edged, image)
        print("Zoom 1 = ", image.shape)
        if self.see_pics:
            cv2.imshow('Zoom 1', output)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        blurred = cv2.GaussianBlur(warped, (5, 5), 0)
        canny = cv2.Canny(blurred, 50, 200, 255)
        [warped, output] = self.zoom_to_rectangle(canny, output)
        print("Zoom 2 = ", output.shape)
        if self.see_pics:
            cv2.imshow('Zoom 2', warped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # threshold the warped image, then apply a series of morphological
        # operations to cleanup the thresholded image
        threshold = 100
        # | cv2.THRESH_OTSU
        thresh = cv2.threshold(warped, threshold, 255, cv2.THRESH_BINARY_INV)[1]
        if self.see_pics:
            cv2.imshow('Threshold', thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 4))

        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        #thresh = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)

        if self.see_pics:
            cv2.imshow('Open', thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # find contours in the thresholded image, then initialize the
        # digit contours lists
        edged = cv2.Canny(thresh, 50, 200, 255)
        cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        digitCnts = []

        if self.see_pics:
            cv2.drawContours(output, cnts, -1, (255, 0, 0), 1)
            cv2.imshow('Important points', output)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # loop over the digit area candidates
        for c in cnts:
            # compute the bounding box of the contour
            (x, y, w, h) = cv2.boundingRect(c)
            boundaries_h_digit = [edged.shape[0] / 4, edged.shape[0] / 2]
            boundaries_w_digit = [edged.shape[1] / 10, edged.shape[1] / 7]
            # if the contour is sufficiently large, it must be a digit
            if (w >= boundaries_w_digit[0] and w <= boundaries_w_digit[1])  and \
                    (h >= boundaries_h_digit[0] and h <= boundaries_h_digit[1]):
                cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)
                digitCnts.append(c)

        if self.see_pics:
            cv2.imshow('Digits found!', output)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # sort the contours from left-to-right, then initialize the
        # actual digits themselves
        digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]
        digits = []

        # loop over each of the digits
        for c in digitCnts:
            # extract the digit ROI
            (x, y, w, h) = cv2.boundingRect(c)
            roi = thresh[y:y + h, x:x + w]
            if self.see_pics:
                cv2.imshow('Digit' + str(c), roi)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            # compute the width and height of each of the 7 segments
            # we are going to examine
            (roiH, roiW) = roi.shape
            (dW, dH) = (int(roiW * 0.30), int(roiH * 0.20))
            dHC = int(roiH * 0.05)

            # define the set of 7 segments
            segments = [
                ((0, 0), (w, dH)),  # top
                ((0, 0), (dW, h // 2)),  # top-left
                ((w - dW, 0), (w, h // 2)),  # top-right
                ((0, (h // 2) - dHC), (w, (h // 2) + dHC)),  # center
                ((0, h // 2), (dW, h)),  # bottom-left
                ((w - dW, h // 2), (w, h)),  # bottom-right
                ((0, h - dH), (w, h))  # bottom
            ]
            on = [0] * len(segments)

            # loop over the segments
            for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
                # extract the segment ROI, count the total number of
                # thresholded pixels in the segment, and then compute
                # the area of the segment
                segROI = roi[yA:yB, xA:xB]
                total = cv2.countNonZero(segROI)
                area = (xB - xA) * (yB - yA)

                # if the total number of non-zero pixels is greater than
                # 50% of the area, mark the segment as "on"
                if total / float(area) > 0.5:
                    on[i] = 1

            # lookup the digit and draw it on the image
            digit = DIGITS_LOOKUP[tuple(on)]
            digits.append(digit)
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(output, str(digit), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)

        if self.see_pics:
            cv2.imshow('Result!', output)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return 6.44

    def zoom_to_rectangle(self, canny_in, color_in):
        # find contours in the edge map, then sort them by their
        # size in descending order
        cnts = cv2.findContours(canny_in.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        displayCnt = None

        if self.see_pics:
            cv2.drawContours(color_in, cnts, -1, (255, 0, 0), 3)
            cv2.drawContours(color_in, [cnts[0]], 0, (0, 0, 255), 3)
            cv2.drawContours(color_in, [cnts[1]], 0, (0, 255, 0), 3)

            cv2.imshow('Important points', color_in)
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
        gray = cv2.cvtColor(color_in, cv2.COLOR_BGR2GRAY)
        return [four_point_transform(gray, displayCnt.reshape(4, 2)),
                four_point_transform(color_in, displayCnt.reshape(4, 2))]





