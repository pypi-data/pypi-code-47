'''
This module contains classes and functions for template matching using OpenCV.

In a typical set-top box or streamer (e.g. Fire TV) device testing scenario,
a test case will send commands to the device under test, then look for
specific elements on the screen using template matching and OCR.

Usage tips:
- Use the smallest template image possible. Using small template images
  makes test cases more robust because changes to other parts of the screen
  will not affect matching.
- Crop frames. If you know the template image is in a specific part of the screen,
  crop the frame to this region so template matching is not affected by changes
  to other areas of the screen.
'''

from datetime import datetime
import time

import cv2

import tv2test.timeutil as timeutil
from tv2test.display import Region


def match_template(dut, template, frame, crop_rect=None, threshold=0.7, timestamp_name=None):
    '''Find an image within another image.

    Args:
        template: OpenCV (cv2) image to search for
        frame: OpenCV (cv2) image to search within
        threshold: Threshold to consider a positive match (0.0-1.0)
        timestamp_name: name of the timestamp to record, if the match is found
    '''
    if not timestamp_name:
        timestamp_name = 'img_match_template'
    dut.timestamps.append({timestamp_name: time.time()})
    cropped_frame = frame.copy()
    if crop_rect is not None:
        cropped_frame = cropped_frame[crop_rect.y:crop_rect.y+crop_rect.height,
                                      crop_rect.x:crop_rect.x+crop_rect.width]
    else:
        crop_rect = Region(0, 0, frame.shape[1], frame.shape[0])

    # Show a red search box in the recording
    annotation = dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                                   image=template,
                                                   color=(0, 0, 255))

    result = cv2.matchTemplate(cropped_frame, template, cv2.TM_CCOEFF_NORMED)
    (_, max_val, _, _) = cv2.minMaxLoc(result)
    if max_val > threshold:
        # Show a green search box in the recording
        dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                          image=template,
                                          color=(0, 255, 0),
                                          annotation_id=annotation.annotation_id)
        return True
    return False

def wait_for_match(dut, template, crop_rect=None, max_wait=5.0, threshold=0.7):
    '''Wait until a template image is found in the display.

    Args:
        dut: DeviceUnderTest with an attached Display
        template: OpenCV (cv2) image to search for
        crop_rect: CropRectangle defining the region to search
        max_wait: Maximum time to wait for a match. Default 5.0 sec
        threshold: Threshold to consider a positive match (0.0-1.0). Default 0.7

    Returns:
        True if match found
        Time (seconds) spent waiting
    '''
    start = datetime.now()
    while True:
        # Grab a frame and crop it if required
        frame = dut.display.get_frame()
        #cv2.imwrite('frame.jpg', frame)
        cropped_frame = frame.copy()
        if crop_rect is not None:
            cropped_frame = cropped_frame[crop_rect.y:crop_rect.y+crop_rect.height,
                                          crop_rect.x:crop_rect.x+crop_rect.width]
        else:
            crop_rect = Region(0, 0, frame.shape[1], frame.shape[0])

        # Show a red search box in the recording
        annotation = dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                                       image=template,
                                                       color=(0, 0, 255))

        # Attempt to match the template in the frame
        result = cv2.matchTemplate(cropped_frame, template, cv2.TM_CCOEFF_NORMED)
        (_, max_val, _, _) = cv2.minMaxLoc(result)
        now = datetime.now()
        time_waiting = timeutil.date_diff_in_seconds(now, start)
        if max_val > threshold:
            # Show a green search box in the recording
            dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                              image=template,
                                              color=(0, 255, 0),
                                              annotation_id=annotation.annotation_id)
            return True, time_waiting

        time.sleep(0.1)

        # Check for timeout
        if time_waiting > max_wait:
            return False, max_wait
