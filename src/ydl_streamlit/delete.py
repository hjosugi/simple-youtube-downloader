import os
import threading
import time


def delayed_delete(file_path, delay=10):
    def delete():
        time.sleep(delay)
        if os.path.exists(file_path):
            os.remove(file_path)

    threading.Thread(target=delete).start()
