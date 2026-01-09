import gc
import threading

import cv2


# Security Camera Class
class Security(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        cap = cv2.VideoCapture(0)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter('security_home.mp4', fourcc, fps, (w, h))

        while True:
            ret, camera = cap.read()
            cv2.imshow('Security cameras', camera)
            out.write(camera)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()


# try ~ except ~ finally.
try:
    thread = Security()
    thread.run()

# Custom Exception, raise throw.
except ValueError as ext:
    print(ext)
    raise RuntimeError from None

# Once Exec.
finally:
    # GC collection.
    gc.collect()
