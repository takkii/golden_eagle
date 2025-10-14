import gc
import os
import pathlib
import traceback
from os.path import dirname, join

import face_recognition
import numpy as np
import numpy.typing as npt
from dotenv import load_dotenv

import golden_eagle as ga

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SIP = os.environ.get("single_param")
ALP = os.environ.get("all_param")
GAN = os.environ.get("ga_num_compare") or ""
LON = os.environ.get("lo_num") or ""

try:
    input_dir = str(ALP)
    input_list = list(pathlib.Path(input_dir).glob('**/*.gif'))

    for i in range(len(input_list)):
        img_file_name = str(input_list[i])
        all_pic = face_recognition.load_image_file(img_file_name)
        after_par = face_recognition.load_image_file(os.path.expanduser(str(SIP)))
        lo_pic = face_recognition.face_locations(all_pic, model='cnn')
        lo_aft = face_recognition.face_locations(after_par, model='cnn')
        around_the_face_b = face_recognition.face_landmarks(after_par, lo_aft)
        around_a = face_recognition.face_landmarks(all_pic, lo_pic)

        print('before compare path ' + str(SIP))

        ga_lose = GAN

        print("golden-eagle_version: " + ga.__version__)
        ga.compare_before_after(all_pic, after_par, float(ga_lose))

        # The data is processed as a feature quantity.
        all_pic = face_recognition.load_image_file(img_file_name)
        after_par = face_recognition.load_image_file(os.path.expanduser(str(SIP)))
        en_b = face_recognition.face_encodings(after_par)[0]
        en_a = face_recognition.face_encodings(all_pic)[0]
        face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
        hyoka: npt.DTypeLike = np.floor(face_d * 1000).astype(int) / 1000
        hyoka_fl = float(hyoka)

        lose = LON

        # # A return value of lose or less is expected.
        if hyoka.astype(np.float64)[0] < float(lose):
            truth = (
                "⭕️ true: "
                + str(lose)
                + " < hyoka_accuracy: "
                + str(hyoka_fl)
                + " before compare path "
                + str(img_file_name)
            )
            print(truth)

        # Values of lose or higher are expected.
        elif not hyoka.astype(np.float64)[0] < float(lose):
            failed = (
                "❎️ lose: "
                + str(lose)
                + " < hyoka_accuracy: "
                + str(hyoka_fl)
                + " before compare path "
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
