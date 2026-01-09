import datetime
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

        start = datetime.datetime.now()

        # 1日経過後、breakを実行 (days=2)など変更可
        # t1 = datetime.timedelta(days=1)
        # 1時間経過後、breakを実行 (hours=2)など変更可
        t1 = datetime.timedelta(hours=1)
        # 1分経過後、breakを実行 (mininutes=2)など変更可
        # t1 = datetime.timedelta(mininutes=1)
        # 1秒経過後、breakを実行 (seconds=2)など変更可
        # t1 = datetime.timedelta(seconds=1)

        while True:
            end = datetime.datetime.now()
            elapsed_time = end - start
            if elapsed_time >= t1:
                break

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
