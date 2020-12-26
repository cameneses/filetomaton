import json
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

folder_to_track = "/home/cesar/Downloads/"
file_types = {".pdf": "PDF Files"}


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            _, file_extension = os.path.splitext(src)

            if file_extension.lower() in file_types:
                container_folder = os.path.join(
                    folder_to_track, file_types[file_extension])
                if not os.path.isdir(container_folder):
                    os.mkdir(container_folder)

                new_destination = container_folder + "/" + filename
                os.rename(src, new_destination)


event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
