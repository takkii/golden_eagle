import gc
import socket
import threading


class IPAd(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # Get, localhost ipadress
        ip = socket.gethostbyname(socket.gethostname())
        print(ip)  # 192.168.179.2


try:
    thread = IPAd()
    thread.run()
# Custom Exception.
except ValueError as ext:
    print(ext)
    raise RuntimeError from None

# Once Exec.
finally:
    # GC collection.
    gc.collect()
