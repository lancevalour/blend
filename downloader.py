from pytube import YouTube
# from moviepy.editor import *
# from pprint import pprint
#
# import cv2
# import youtube_dl

import subprocess


class AudioDownloader:

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download(self):
        yt = YouTube(self.url)
        video = yt.get('mp4', '480p')
        video_filename = self.filename[0:self.filename.rfind('/')] + 'temp.mp4'
        video.download(video_filename)
        command = "ffmpeg -i " + video_filename + " -ab 160k -ac 2 -ar 44100 -vn " + self.filename
        subprocess.call(command, shell=True)


