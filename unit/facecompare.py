import gc
import os
import threading
from os.path import dirname, join
from typing import Optional

import face_recognition
from dotenv import load_dotenv

import golden_eagle as ga

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BFP = os.environ.get("before_param_face")
AFP = os.environ.get("after_param_face")
GAN = os.environ.get("ga_num") or ""


# face class
class Face(threading.Thread):

    # use thread
    def __init__(self):
        threading.Thread.__init__(self)

    # run method
    def run(self):
        # Specify the path of the face photo to be compared.
        my_before = face_recognition.load_image_file(os.path.expanduser(str(BFP)))
        my_after = face_recognition.load_image_file(os.path.expanduser(str(AFP)))

        # facecompare version.
        print('{}'.format('-----------------------------------------------------------------'))
        print('\n')
        print("golden-eagle_version: " + ga.__version__)

        # golden-eagle accuary number.
        ga_lose: Optional[str] = GAN

        # value is 0.6 and lower numbers make face comparisons more strict:
        ga.compare_before_after(my_before, my_after, float(ga_lose))


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
