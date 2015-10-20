from pytube import YouTube
import os
import subprocess


class Downloader:
    AUDIO_ONLY = "AUDIO"
    VIDEO_ONLY = "VIDEO"
    AUDIO_AND_VIDEO = "AUDIO_AND_VIDEO"

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download(self, file_type):
        yt = YouTube(self.url)
        resolution = str(yt.filter('mp4')[0]).split(" ")[4]
        print(resolution)
        video = yt.get('mp4', resolution)
        video_filename = self.filename[0:self.filename.rfind('/')] + '/temp.mp4'
        print(video_filename)
        video.download(video_filename)

        if file_type == Downloader.VIDEO_ONLY:
            return
        elif file_type == Downloader.AUDIO_AND_VIDEO:
            command = "ffmpeg -i " + video_filename + " -ab 160k -ac 2 -ar 44100 -vn " + self.filename
            subprocess.call(command, shell=True)
        else:
            command = "ffmpeg -i " + video_filename + " -ab 160k -ac 2 -ar 44100 -vn " + self.filename
            subprocess.call(command, shell=True)
            os.remove(video_filename)


# yt = YouTube("https://www.youtube.com/watch?v=Y9ovl3ixqHs")
# print(str(yt.filter('mp4')[0]).split(" ")[4])
# video = yt.get('mp4', str(yt.filter('mp4')[0]).split(" ")[4])
# video.download('C:/Users/ZhangY/Desktop/audio.mp4')

url = "https://www.youtube.com/watch?v=Y9ovl3ixqHs"
video_path = "C:/Users/ZhangY/Desktop/temp.mp4"
audio_path = "C:/Users/ZhangY/Desktop/audio.mp3"
clip_path = "C:/Users/ZhangY/Desktop/clip.mp4"

# downloader = Downloader(url, audio_path)
# downloader.download(AudioDownloader.AUDIO_AND_VIDEO)
