import gc
import os
import tkinter as tk
from os.path import dirname, join

import cv2
import face_recognition
import imutils
import numpy as np
from PIL import Image, ImageTk
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# before picture path.
BFP = os.environ.get("before_param")
PCI = os.environ.get("picture_images")
NAM = os.environ.get("name")

try:
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    takayuki_image = face_recognition.load_image_file(str(BFP))
    takayuki_face_encoding = face_recognition.face_encodings(takayuki_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [takayuki_face_encoding]

    known_face_names = [str(NAM)]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Only process every other frame of video to save time
        if process_this_frame:
            # Convert frame of BGR2RGB for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image to COLOR_BGR2RGB color (which face_recognition uses)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # The default is "hog" / other select "cnn"
            face_locations = face_recognition.face_locations(rgb_small_frame,
                                                             model='cnn')
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []

            for face_encoding in face_encodings:
                # tolerance = 0.4, default value.
                matches = face_recognition.compare_faces(known_face_encodings,
                                                         face_encoding,
                                                         tolerance=0.4)
                name = "Unknown"

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations,
                                                    face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
                          (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8,
                        (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('"Terminal, Please Ctrl+C"', frame)
            k = cv2.waitKey(1) & 0xff
            img = imutils.resize(frame, width=350)

            # Hit 'q' on the keyboard to quit!
            if k == ord('s'):
                cv2.imwrite(str(PCI), img)
                if os.path.isfile(str(PCI)):
                    pil_image = Image.open(str(PCI))
                    w_size = int(pil_image.width)
                    h_size = int(pil_image.height)
                    root = tk.Tk()
                    root.title("s=save / alt+F4=close")
                    canvas = tk.Canvas(root, width=w_size, height=h_size)
                    canvas.pack()
                    tk_image = ImageTk.PhotoImage(
                        image=pil_image.resize((w_size, h_size)))
                    canvas.create_image(0, 0, anchor='nw', image=tk_image)
                    root.mainloop()
                else:
                    raise ValueError('No images saved')

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

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
