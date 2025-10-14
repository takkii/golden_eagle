import os
import pathlib
from os.path import dirname, join

import cv2
import face_recognition
import numpy as np
import numpy.typing as npt
from dotenv import load_dotenv

import golden_eagle as ga

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BFP = os.environ.get("before_param")
ALP = os.environ.get("all_param")

input_dir = str(ALP)
input_list = list(pathlib.Path(input_dir).glob('**/*.gif'))

for i in range(len(input_list)):
    img_file_name = str(input_list[i])
    img_np = np.fromfile(img_file_name, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    all_pic = face_recognition.load_image_file(img_file_name)
    my_before = face_recognition.load_image_file(os.path.expanduser(str(BFP)))
    lo_pic = face_recognition.face_locations(all_pic, model='cnn')
    lo_before = face_recognition.face_locations(my_before, model='cnn')
    around_the_face_b = face_recognition.face_landmarks(my_before, lo_before)
    around_a = face_recognition.face_landmarks(all_pic, lo_pic)

    # facecompare version.
    print("golden-eagle_version: " + ga.__version__)

    # The data is processed as a feature quantity.
    en_b = face_recognition.face_encodings(my_before)[0]
    en_a = face_recognition.face_encodings(all_pic)[0]
    face_d: npt.NDArray = face_recognition.face_distance([en_b], en_a)
    hyoka: npt.DTypeLike = np.floor(face_d * 1000).astype(int) / 1000

    # Accuracy evaluation, no face picture editing.
    accuracy = "accuracy:" + str(hyoka)
    print(accuracy)

# output
# golden-eagle_version: 1.0.5.5
# = Same picture.
# accuracy:[0.]
# ≠ Different picture.
# golden-eagle_version: 1.0.5.5
# accuracy:[0.255]
