from zumi.util.camera import Camera

from flask import Flask, render_template, Response
import cv2
import time
import os
from threading import Thread

class DriveMode:
    def __init__(self, _zumi):
        self.zumi = _zumi
        self.camera = Camera()
        self.current_key = ''
        self.drive_thread = ''

    def __move_zumi(self):
        desired_angle = self.zumi.read_z_angle()

        while self.current_key != '':
            if self.current_key == "ArrowUp":
                k_p = 2.9
                k_i = 0.01
                k_d = 0.9
                accuracy = 0.8
                self.zumi.drive_at_angle(127, 40, desired_angle, k_p, k_d, k_i, accuracy)
            elif self.current_key == "ArrowDown":
                k_p = 2.9
                k_i = 0.01
                k_d = 0.9
                accuracy = 0.8
                self.zumi.drive_at_angle(127, -40, desired_angle, k_p, k_d, k_i, accuracy)
            elif self.current_key == "ArrowLeft":
                k_p = 0.6
                k_i = 0.001
                k_d = 0.3
                accuracy = 1
                self.zumi.drive_at_angle(127, 0, desired_angle + 360, k_p, k_d, k_i, accuracy)
            elif self.current_key == "ArrowRight":
                k_p = 0.6
                k_i = 0.001
                k_d = 0.3
                accuracy = 1
                self.zumi.drive_at_angle(127, 0, desired_angle - 360, k_p, k_d, k_i, accuracy)
            elif self.current_key == "q":
                self.send_image_thread.join()
            else:
                break

        print('out of loop')
        self.zumi.stop()

    def zumi_direction(self, input_key):
        if input_key != self.current_key:
            self.current_key = input_key
            print(input_key)
            self.drive_thread = Thread(target=self.__move_zumi)
            self.drive_thread.start()

    def zumi_stop(self):
        print('zumi stop')
        self.current_key = ''
        self.drive_thread.join()
        self.zumi.stop()

app = Flask(__name__)

@app.route('/')
def index():
   """Video streaming ."""
   return render_template('drivescreen.html')

def gen():
    camera = Camera(320, 240, auto_start=True)

    count = 0
    timee = 0
    start = time.time()

    if not os.path.isdir('/home/pi/Dashboard/DriveImg'):
        os.makedirs('/home/pi/Dashboard/DriveImg')

    """Video streaming generator function."""
    while True:
        if timee > 1:
            start = time.time()
        frame = camera.capture()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/home/pi/Dashboard/DriveImg/drivescreen.jpg', frame)
        yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('/home/pi/Dashboard/DriveImg/drivescreen.jpg', 'rb').read() + b'\r\n')
        end = time.time()
        timee = end-start
        count = count + 1
        if timee >= 1:
            count = 0


@app.route('/video_feed')
def video_feed():
   """Video streaming route. Put this in the src attribute of an img tag."""
   return Response(gen(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True, port=3456)