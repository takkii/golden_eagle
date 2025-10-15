import gc
import os
import pathlib
import traceback
from os.path import dirname, join

import cv2
import face_recognition
import numpy as np
import numpy.typing as npt
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SIP = os.environ.get("single_param")
ALP = os.environ.get("all_param")
LON = os.environ.get("lo_num") or ""

try:
    input_dir = str(ALP)
    input_list = list(pathlib.Path(input_dir).glob('**/*.gif'))

    for i in range(len(input_list)):
        img_file_name = str(input_list[i])
        all_pic = face_recognition.load_image_file(img_file_name)
        after_par = face_recognition.load_image_file(os.path.expanduser(str(SIP)))
        all_enc = cv2.cvtColor(all_pic, cv2.COLOR_BGR2RGB)
        after_enc = cv2.cvtColor(after_par, cv2.COLOR_BGR2RGB)

        lo_before = face_recognition.face_locations(all_enc, model='cnn')[0]
        lo_after = face_recognition.face_locations(after_enc, model='cnn')[0]

        print('before compare path ' + str(SIP))

        en_b = face_recognition.face_encodings(after_enc)[0]
        en_a = face_recognition.face_encodings(all_enc)[0]

        cv2.rectangle(all_enc, (lo_before[3], lo_before[0]), (lo_before[1], lo_before[2]), (0, 255, 0), 3)
        cv2.rectangle(after_enc, (lo_after[3], lo_after[0]), (lo_after[1], lo_after[2]), (0, 255, 0), 3)

        cv2.startWindowThread()
        cv2.imshow('ALL picture image.', all_enc)
        cv2.imshow('Before picture image.', after_enc)
        cv2.waitKey(15000)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
        hyoka: npt.DTypeLike = np.floor(face_d * 1000).astype(int) / 1000
        hyoka_fl = float(hyoka)

        lose = LON

        # # A return value of lose or less is expected.
        if hyoka.astype(np.float64)[0] < float(lose):
            successes = (
                "⭕️ success: "
                + str(lose)
                + " > hyoka_accuracy: "
                + str(hyoka_fl)
                + " after compare path "
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
                + " after compare path "
                + str(img_file_name)
            )
            print(failed)

        # Usually not reached.
        else:
            # Unique exception occurrence.
            raise ValueError("Please check the passcode for your face picture.")

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
        raise ValueError("None, Please Check the Current directory.")

# Once Exec.
finally:
    gc.collect()
