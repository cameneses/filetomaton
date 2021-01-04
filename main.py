import json
import logging
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

folder_to_track = "/home/cesar/Downloads/"

file_types = {".pdf": "PDF Files", ".png": "Images",
              ".jpeg": "Images", ".jpg": "Images", ".gif": "Images",
              ".zip": "Compressed files", ".tar.gz": "Compressed files",
              ".rar": "Compressed files", ".tar.xz": "Compressed files",
              ".gz": "Compressed files", ".epub": "Books", ".deb": "Packages"}

logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            _, file_extension = os.path.splitext(src)

            if file_extension.lower() in file_types:
                container = file_types[file_extension]
                container_folder = os.path.join(
                    folder_to_track, container)
                if not os.path.isdir(container_folder):
                    os.mkdir(container_folder)

                new_destination = container_folder + "/" + filename
                os.rename(src, new_destination)
                logging.info("Moved {filename} to {container} in {downloads_folder}".format(
                    filename=filename, container=container, downloads_folder=folder_to_track))


if __name__ == "__main__":
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
