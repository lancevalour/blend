from pytube import YouTube
import os
import os.path
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
        if os.path.exists(video_filename):
            os.remove(video_filename)

        video.download(video_filename)

        if file_type == Downloader.VIDEO_ONLY:
            return
        elif file_type == Downloader.AUDIO_AND_VIDEO:
            if os.path.exists(self.filename):
                os.remove(self.filename)
            command = "ffmpeg -i " + video_filename + " -ab 160k -ac 2 -ar 44100 -vn " + self.filename
            subprocess.call(command, shell=True)
        else:
            if os.path.exists(self.filename):
                os.remove(self.filename)
            command = "ffmpeg -i " + video_filename + " -ab 160k -ac 2 -ar 44100 -vn " + self.filename
            subprocess.call(command, shell=True)
            os.remove(video_filename)

video_url = "https://www.youtube.com/watch?v=KUFgjTuvAvs"
audio_path = "C:/Users/ZhangY/Desktop/blend/audio.mp3"

downloader = Downloader(video_url, audio_path)
downloader.download(Downloader.AUDIO_ONLY)
