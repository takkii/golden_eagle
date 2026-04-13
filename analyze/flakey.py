import gc
import os
import pathlib
import traceback
import warnings
from os.path import dirname, join

import cv2
import face_recognition
import numpy as np
import numpy.typing as npt
from dotenv import load_dotenv
from tqdm import tqdm

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.simplefilter('ignore', DeprecationWarning)

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# before picture path.
SIP = os.environ.get("single_param")
# all picture path.
ALP = os.environ.get("all_param")
# accuracy assessment value reading in .env
LON = os.environ.get("lo_num") or ""

try:
    # Allows multiple images.
    input_dir = str(ALP)
    input_list = list(pathlib.Path(input_dir).glob('**/*.gif'))

    for i in tqdm(range(len(input_list))):
        # One-to-Many Face Recognition.
        img_file_name = str(input_list[i])
        all_pic = face_recognition.load_image_file(img_file_name)
        before_par = face_recognition.load_image_file(os.path.expanduser(str(SIP)))
        all_enc = cv2.cvtColor(all_pic, cv2.COLOR_BGR2RGB)
        before_enc = cv2.cvtColor(before_par, cv2.COLOR_BGR2RGB)

        # Which face detection model to use.
        # "hog" is less accurate but faster on CPUs.
        # "cnn" is a more accurate deep-learning model,
        # which is GPU/CUDA accelerated (if available) / The default is "hog".
        lo_all = face_recognition.face_locations(all_enc, model='cnn')[0]
        lo_before = face_recognition.face_locations(before_enc, model='cnn')[0]

        # Comparison source for face pictures.
        print(' before picture path ' + str(SIP))

        # The data is processed as a feature quantity.
        en_b = face_recognition.face_encodings(before_enc)[0]
        en_a = face_recognition.face_encodings(all_enc)[0]

        # Add a square green line around the face.
        cv2.rectangle(all_enc, (lo_all[3], lo_all[0]), (lo_all[1], lo_all[2]), (0, 255, 0), 3)
        cv2.rectangle(before_enc, (lo_before[3], lo_before[0]), (lo_before[1], lo_before[2]), (0, 255, 0), 3)

        # # Launch two images.
        cv2.startWindowThread()
        cv2.imshow('ALL picture image.', all_enc)
        cv2.imshow('Before picture image.', before_enc)
        cv2.waitKey(7500)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        # hyoka_accuracy calc / result.
        face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
        hyoka: npt.DTypeLike = np.floor(face_d * 1000).astype(int) / 1000
        hyoka_fl = float(hyoka)

        # Specify the accuracy assessment value.
        lose = LON

        # # A return value of lose or less is expected.
        if hyoka.astype(np.float64)[0] < float(lose):
            successes = (
                    "⭕️ success: "
                    + str(lose)
                    + " > hyoka_accuracy: "
                    + str(hyoka_fl)
                    + " all picture path "
                    + str(img_file_name)
            )
            print(successes)

        # Values of lose or higher are expected.
        elif not hyoka.astype(np.float64)[0] < float(lose):
            failed = (
                    "❎️ failed: "
                    + str(lose)
                    + " < hyoka_accuracy: "
                    + str(hyoka_fl)
                    + " all picture path "
                    + str(img_file_name)
            )
            print(failed)

        # Usually not reached.
        else:
            # Unique exception occurrence.
            raise ValueError("hyoka accuracy is diable, please select diffrent picture.")

# TraceBack.
except Exception:
    # Specify the folder to record the exception log.
    except_folder = os.getcwd()
    # Specify the file to log exception occurrences.
    except_file = os.getcwd() + '.log'

    # Load the dictionary.
    if os.path.isdir(os.path.expanduser(except_folder)):
        # Log writing process.
        with open(os.path.expanduser(except_file), 'a') as log_py:
            traceback.print_exc(file=log_py)

        # throw except.
        raise RuntimeError from None

    # Current directory Not Found.
    else:
        # Unique exception occurrence.
        raise ValueError("Check, error log output on folder tree.")

# Once Exec.
finally:
    gc.collect()
