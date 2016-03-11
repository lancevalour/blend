from moviepy.editor import *
from __future__ import print_function
import librosa
import matplotlib.pyplot as plt
import downloader

class Blend:
    def __init__(self):
        pass




# yt = YouTube("https://www.youtube.com/watch?v=Y9ovl3ixqHs")
# print(str(yt.filter('mp4')[0]).split(" ")[4])
# video = yt.get('mp4', str(yt.filter('mp4')[0]).split(" ")[4])
# video.download('C:/Users/ZhangY/Desktop/audio.mp4')

url = "https://www.youtube.com/watch?v=Y9ovl3ixqHs"
video_path = "C:/Users/ZhangY/Desktop/blend/temp.mp4"
audio_path = "C:/Users/ZhangY/Desktop/blend/audio.mp3"
clip_path = "C:/Users/ZhangY/Desktop/blend/clip.mp4"

# downloader = Downloader()
# downloader = AudioDownloader(url, audio_path)
# downloader.download(AudioDownloader.AUDIO_AND_VIDEO)


# y, sr = librosa.load("C:/Users/ZhangY/Desktop/blend/audio.mp3")

# onset = librosa.onset.onset_detect(y=y, sr=sr)

# time = librosa.frames_to_time(onset, sr=sr)

# print(len(time))

# print(time[0])
# print(time[1])
# print(time[2])


# video = VideoFileClip(video_path)
# print(video.duration);

# clip = video.fl_time(lambda t: )

# video.write_videofile(clip_path, audio=audio_path)



print("hahaha")