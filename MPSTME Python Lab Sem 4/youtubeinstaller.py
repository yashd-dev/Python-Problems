from pytube import YouTube
import os
from pathlib import Path

link = input("Enter link here: ")

url = YouTube(link)

print("downloading....")

video = url.streams.get_by_resolution("360p")

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print("Downloaded! :)")