import gc
import os
import threading
from os.path import dirname, join
from typing import Optional

import cv2
import face_recognition
import matplotlib.pyplot as plt
from dotenv import load_dotenv

import golden_eagle as ga

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Yourself before picture image.
BFP = os.environ.get("before_param")
# Yourself after picture image.
AFP = os.environ.get("after_param")
# PyPi package golden-eagle accuary numbers reading in .env
GAN = os.environ.get("ga_num_run") or ""


# face class
class Face(threading.Thread):

    # use thread
    def __init__(self):
        threading.Thread.__init__(self)

    # run method
    def run(self):
        # Destination for the two images.
        before = os.path.expanduser(str(BFP))
        after = os.path.expanduser(str(AFP))

        # Specify the path of the face photo to be compared.
        my_before = face_recognition.load_image_file(before)
        my_after = face_recognition.load_image_file(after)

        # golden-eagle version.
        print("golden-eagle_version: " + ga.__version__)

        # golden-eagle accuary number.
        ga_lose: Optional[str] = GAN

        # value is 0.6 and lower numbers make face comparisons more strict:
        ga.compare_before_after(my_before, my_after, float(ga_lose))

        # Use dlib, face recognition.
        cv2.startWindowThread()
        # Use face recognition my_after/my_before.
        cv2.imshow('Yourself before picture image.', my_before)
        cv2.imshow('Yourself after picture image.', my_after)
        # Window closes in 8 seconds
        cv2.waitKey(15000)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        plt.show()


# try ~ except ~ finally.
try:
    thread = Face()
    thread.run()
# Custom Exception, raise throw.
except ValueError as ext:
    print(ext)
    raise RuntimeError from None

# Once Exec.
finally:
    # GC collection.
    gc.collect()
