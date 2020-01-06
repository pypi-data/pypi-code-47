'''
This module contains classes for OCR.
'''

import time
import boto3
import cv2
import pytesseract
from datetime import datetime
import numpy as np
from PIL import Image
import io
import json
import requests
import base64

from tv2test.display import Region


class TesseractOcr:
    '''
    This class uses a locally installed instance of Tesseract to perform OCR on OpenCV images
    '''

    def ocr_text(self, dut, cv2_image, crop_rect=None):
        '''
        Detect text in the specified region of an image.

        The OCR region is highlighted in the recorded video
        '''
        start = datetime.now()
        img = cv2_image.copy()
        if crop_rect is not None:
            img = img[crop_rect.y:crop_rect.y+crop_rect.h,
                      crop_rect.x:crop_rect.x+crop_rect.w]
        else:
            crop_rect = Region(0, 0, img.shape[1], img.shape[0])

        cv2.imwrite('ocr.png', img)

        # Show a red search box in the recording
        annotation = dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.w, crop_rect.h),
                                                       text='Get text',
                                                       duration=3.0)

        pil_img = Image.fromarray(img)
        # --oem=1 uses new LSTM neural network for text detection vs legacy
        # --psm=8 is Page segmentation method; 8 = treat the image as a single word
        text = pytesseract.image_to_string(pil_img, lang="eng", nice=-10, config='--oem=1 --psm=8')
        #find_time = self._date_diff_in_seconds(datetime.now(), start)
        #print("Detected text: " + text + " in {:.2f}".format(find_time))

        # Show a green search box in the recording
        dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.w, crop_rect.h),
                                          text='Get text',
                                          duration=3.0,
                                          annotation_id=annotation.annotation_id)

        return text

    def _date_diff_in_seconds(self, dt2, dt1):
        timedelta = dt2 - dt1
        return timedelta.days * 24 * 3600 + timedelta.seconds + (timedelta.microseconds/1000000)

class AwsRekognize:
    '''
    This class uses the AWS Rekognize service to perform OCR on OpenCV images.
    '''

    def __init__(self):
        self.client = boto3.client("rekognition")

    def detect_text_cv2(self, image):
        '''
        Detect text in an OpenCV image
        '''
        # Convert OpenCV image to a binary image using Pillow
        pil_img = Image.fromarray(image)
        stream = io.BytesIO()
        pil_img.save(stream, format='PNG')
        bin_img = stream.getvalue()

        # Detect text
        response = self.client.detect_text(Image={'Bytes': bin_img})
        #print(repr(response))

        textDetections = response['TextDetections']
        # print("=== Detection result ===")
        # for text in textDetections:
        #     print('Detected text: ' + text['DetectedText'])
        #     print('Score: ' + "{:.2f}".format(text['Confidence']) + "%")
        return response

    def cv2_image_to_string(self, image, confidence_threshold=70.0):
        '''
        Convert all text in the specified image to a string.
        '''
        rekoResult = self.detect_text_cv2(image)
        result = ''
        for text in rekoResult['TextDetections']:
            if text['Type'] == 'WORD' and float(text['Confidence']) > confidence_threshold:
                result += text['DetectedText'] + ' '
        return result.strip()

    def isAllTextRecognized(self, rekoResult, words, threshold=90.0):
        '''
        Process results from detect_text_cv2 and return true if all
        the specified words are found. 
        '''
        textDetections = rekoResult['TextDetections']
        for word in words:
            found = False
            for text in textDetections:
                if text['DetectedText'].lower().find(word) >= 0:
                    found = True
                    break

            if found == False:
                return False
        return True

    def isAnyTextRecognized(self, rekoResult, words, threshold=90.0):
        '''
        Process results from detect_text_cv2 and return true if any
        of the specified words are found. 
        '''        
        textDetections = rekoResult['TextDetections']
        for word in words:
            for text in textDetections:
                if text['DetectedText'].lower().find(word) >= 0:
                    return True

        return False


class GVisionOcr:

    def ocr_text(self, dut, img, crop_rect=None, text='Text match', timestamp_name=None):
        google_api_key = dut.options['google_api_key']
        if timestamp_name is not None:
            dut.timestamps.append({timestamp_name: time.time()})
        if crop_rect is not None:
            img = img[crop_rect.y:crop_rect.y+crop_rect.height,
                      crop_rect.x:crop_rect.x+crop_rect.width]
        else:
            crop_rect = Region(0, 0, img.shape[1], img.shape[0])
        image_path = 'ocr.png'
        cv2.imwrite(image_path, img)

        # Show a red search box in the recording
        annotation = dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                                       text=text,
                                                       duration=3.0)
 
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        URL = 'https://vision.googleapis.com/v1/images:annotate?key=%s' % (google_api_key)

        data = {
            "requests": [{
                "image": {
                    "content": encoded_string.decode("utf-8")
                },
                "features": [{
                    "type": "TEXT_DETECTION",
                    "maxResults": 100
                }]
            }]
        }

        response = requests.post(url=URL, data=json.dumps(data))
        json_response = json.loads(response.text)
        all_texts = []
        if 'textAnnotations' in json_response['responses'][0]:
            texts = json_response['responses'][0]['textAnnotations'][0]['description']
            for text in texts.split('\n'):
                all_texts.append(text)

            # Show a green search box in the recording
            dut.display.add_region_annotation(Region(crop_rect.x, crop_rect.y, crop_rect.width, crop_rect.height),
                                            text='Get text',
                                            duration=3.0,
                                            annotation_id=annotation.annotation_id)
        return all_texts
