# Download videos from youtube based on a link provided
# Selectic a version from a list available
# Requires pytube3 library

from pytube import YouTube
import os

video_url = input("Insert the full youtube link: ")

# youtube video object
yt_video = YouTube(video_url)

# streams available as a list
streams = yt_video.streams.filter(mime_type="video/mp4")
count = 0
for stream in streams:
    print(count, end=" : ")
    print(stream)
    count += 1
while True:
    selection = input("Whitch version do you want to download? (Default: 1): ")
    if not selection.strip():
        selection = 1
        break
    elif selection.isnumeric():
        selection = int(selection)
        break
    else:
        print("Chose a valid option")

# single stream object
video = streams[selection]

# Get the path of the script file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Add a folder next to the script
video.download(f'{dir_path}/videos')