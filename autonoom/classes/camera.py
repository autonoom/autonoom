#File for computer vision stuff
import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import platform
from matplotlib import pyplot as plt


class Camera:
    def __init__(self):

        os = platform.system()
        if os == "Windows":
            cam = cv.VideoCapture(0)
            cam.resolution = (1080, 480)
            cam.framerate = 32
            cam.rotation = 180
        elif os == "Linux":
            cam = PiCamera()
            cam.resolution = (1080, 480)
            cam.framerate = 32
            cam.rotation = 180
            rawCapture = PiRGBArray(cam, size=(1080, 480))

        time.sleep(0.1)

        # capture frames from the camera
        for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the $
        # and occupied/unoccupied text
            cam = frame.array

            src = np.array([[325, 150], [675, 150], [0, 480], [1020, 480]], np.float32)
            dst = np.array([[0, 0], [1080, 0], [0, 480], [1080, 480]], np.float32)

            M = cv.getPerspectiveTransform(src, dst)
            warp = cv.warpPerspective(cam.copy(), M, (1080, 480))
            gray = cv.cvtColor(cam, cv.COLOR_BGR2GRAY)

            edges = cv.Canny(gray, 50, 150, apertureSize = 3)
            minLineLength = 20
            maxLineGap = 20
            lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
            for x1, y1, x2, y2 in lines[0]:
                cv.line(warp, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # cv2.imshow("gray",edges)

                # show the frame
                cv.imshow("Frame", warp)
            key = cv.waitKey(1) & 0xFF
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                cv.destroyAllWindows()
                break



