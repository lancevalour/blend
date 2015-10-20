from moviepy.editor import *


class Blend:
    def __init__(self):
        pass


# yt = YouTube("https://www.youtube.com/watch?v=Y9ovl3ixqHs")
# print(str(yt.filter('mp4')[0]).split(" ")[4])
# video = yt.get('mp4', str(yt.filter('mp4')[0]).split(" ")[4])
# video.download('C:/Users/ZhangY/Desktop/audio.mp4')

url = "https://www.youtube.com/watch?v=Y9ovl3ixqHs"
video_path = "C:/Users/ZhangY/Desktop/temp.mp4"
audio_path = "C:/Users/ZhangY/Desktop/audio.mp3"
clip_path = "C:/Users/ZhangY/Desktop/clip.mp4"

# downloader = AudioDownloader(url, audio_path)
# downloader.download(AudioDownloader.AUDIO_AND_VIDEO)

video = VideoFileClip(video_path)

video.write_videofile(clip_path, audio=audio_path)
