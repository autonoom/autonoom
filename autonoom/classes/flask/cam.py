#!/usr/bin/env python
from flask import Flask, render_template, Response
import threading

# emulated camera
from camera_pi import Camera

class cam(threading.Thread):
    class __cam(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            app = Flask(__name__)
            self.start()

        def gen(camera, self):
            """Video streaming generator function."""
            while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        @app.route('/video_feed')
        def video_feed(self):
            """Video streaming route. Put this in the src attribute of an img tag."""
            return Response(self.gen(Camera()),
                            mimetype='multipart/x-mixed-replace; boundary=frame')

        def run(self):
            self.app.run(host='0.0.0.0', debug=True, threaded=True)

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not cam.instance:
            cam.instance = cam.__cam()
        return cam.instance