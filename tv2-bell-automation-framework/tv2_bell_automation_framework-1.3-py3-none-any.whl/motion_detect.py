import cv2
import time
import numpy as np
from .display import Region


def detect_motion(dut, timeout_time=10.0):
    time.sleep(3.0)
    continous_check = True
    execution_start_time = time.time()
    while continous_check:
        frame1 = dut.display.get_frame()
        time.sleep(0.5)
        frame2 = dut.display.get_frame()
        # Difference between frame1(image) and frame2(image)
        diff = cv2.absdiff(frame1, frame2)

        # Converting color image to gray_scale image
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # Converting gray scale image to GaussianBlur, so that change can be find easily
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # If pixel value is greater than 20, it is assigned white(255) otherwise black
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=4)

        # finding contours of moving object
        contours, hirarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # making rectangle around moving object
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) > 700:
                # Show a green search box in the recording
                dut.display.add_region_annotation(Region(x, y, x + w, y + h),
                                                  text='motion detect',
                                                  duration=3.0,
                                                  color=(0,128, 0))
                continous_check = False
                return True

        if time.time() - execution_start_time >= timeout_time:
            print('TIMEOUT FAILURE')
            return False
