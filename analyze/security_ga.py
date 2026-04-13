import gc
import os
import threading
import warnings
from os.path import dirname, join
from typing import Optional

from dotenv import load_dotenv

import golden_eagle as ga

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.simplefilter('ignore', DeprecationWarning)

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

INC = os.environ.get("int_conn") or ""
ICL = os.environ.get("int_clock") or ""


# face class
class Face(threading.Thread):

    # use thread
    def __init__(self):
        threading.Thread.__init__(self)

    # run method
    def run(self):
        # golden-eagle version.
        print("golden-eagle_version: " + ga.__version__)

        inc: Optional[str] = INC
        icl: Optional[str] = ICL

        # home_security.
        ga.security(int(inc), int(icl))


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
