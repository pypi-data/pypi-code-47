# Copyright (C) 2019 Spiralworks Technologies Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import base64
import os
import requests
import json
from robotlibcore import HybridCore, keyword
from PIL import Image
from pyzbar.pyzbar import decode
import pyqrcode


__version__ = '0.1.1a1'


class DecoderLibrary(HybridCore):
    """'Robot Framework Library For Decoding Various Encoded Data such as QR, \
        Barcode, or Captcha Image.

    This document will try to explain how to use this library and how to
        integrate it to your robot test suites.

    For more information about Robot Framework, see http://robotframework.org

    == About ==

    Created: January 06 2020 | 19:54:54 UTC + 8

    Author: Joshua Kim Rivera | joshua.rivera@mnltechnology.com

    Company: Spiralworks Technologies Inc.
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, captchaServiceUrl=None,
                 header={'Content-Type': 'application/x-www-form-urlencoded'},
                 payloadType='base64Captcha'
                 ):
        """DecoderLibrary's captchaServiceUrl could be set upon import, but \
            can also be set using `Set Captcha Service URL`.
        """
        libraries = [
        ]
        HybridCore.__init__(self, libraries)
        self.set_captcha_service_url(captchaServiceUrl,
                                     header,
                                     payloadType)

    @keyword
    def set_captcha_service_url(self, serviceURL,
                                header,
                                payloadType
                                ):
        """Sets the Captcha Service URL to be used.

        Example:
        | Set Captcha Service URL   | https://sample.captcha/service/url    |
        """
        self.serviceURL = serviceURL
        self.header = header
        self.payloadType = payloadType

    @keyword
    def capture_element_from_screenshot(self, imagepath, location,
                                        size, outputpath):
        """Crops the specified element from a screenshot given the \
            location and size using Python's Pillow Module. Fails if \
                the supplied image PATH does not exist.

        Example:
        | `Capture Element From Screenshot` | image.png | ${coordinates} | \
            ${size} | output.jpg |

        Where:
         - `image.png`       = path to the captcha image
         - `${coordinates}`  = element location, must be a dictionary
         - `${size}`         = element size, must be a dictionary
         - `outputpath`      = cropped_image
        """
        try:
            image = Image.open(imagepath)
        except Exception as e:
            raise e
        element = image.crop((int(location['x']),
                              int(location['y']),
                              int(size['width'])+int(location['x']),
                              int(size['height'])+int(location['y'])
                              ))
        element.save(outputpath)

    @keyword
    def create_qr_image(self, content, outputPath, scale=6, **kwargs):
        """Creates a QR Image given parameters.
        """
        qr = pyqrcode.create(content)
        qr.png(outputPath, scale=scale, **kwargs)

    @keyword
    def decode_qr_image(self, imagepath):
        """Decodes the given QR Image. Returns an object type variable.
        """
        return self._process_qr_image(imagepath)

    def _process_qr_image(self, imagepath):
        try:
            decoded_qr = decode(Image.open(imagepath))[0]
            return decoded_qr
        except Exception as err:
            raise err

    @keyword
    def decode_base64_captcha(self, imagepath):
        """Decodes the Base64 Captcha Image by converting the supplied \
            captcha image by sending a request to the captcha service URL.
        Example:
        | ${captcha_string} | `Decode Base64 Captcha` \
            | path/to/captcha/image |
        """
        base64_string = self.convert_captcha_image_to_base64(imagepath)
        payload = {self.payloadType: base64_string}
        decoded_string = \
            self._send_post_request_to_service_url(self.serviceUrl,
                                                   self.header, payload)
        return decoded_string.text

    def _send_post_request_to_service_url(self, serviceUrl, header, payload):
        """Send a POST Request to the Captcha Service API.
        """
        req = requests.post(serviceUrl, data=payload, headers=header)
        return req

    @keyword
    def convert_captcha_image_to_base64(self, imagepath):
        """Converts the supplied Captcha image to a Base64 String.
        Fails if the image does not exist
        Example:
        | `Convert Captcha Image To Base64` | captcha.png |

        Where:
         - `captcha.png` = the captcha image to be converted to \
             Base64 String.
        """
        try:
            with open(imagepath, "rb") as img_file:
                decoded_string = base64.b64encode(img_file.read())
                decoded_string = decoded_string.decode("utf-8")
                return decoded_string
        except Exception as e:
            raise e
