from __future__ import print_function
import librosa
import os
import subprocess
import numpy as np
from moviepy.editor import *
import matplotlib.pyplot as plt


# audio = "C:/Users/ZhangY/Desktop/blend/audio.mp3"
# video = "C:/Users/ZhangY/Desktop/blend/temp.mp4"


class Rhythm:
    def __init__(self):
        pass

    @staticmethod
    def extract_audio(video):
        audio = os.path.dirname(video) + "/" + os.path.basename(video).split(".")[0] + "_audio.mp3"
        command = "ffmpeg -i " + video + " -ab 160k -ac 2 -ar 44100 -vn " + audio
        subprocess.call(command)
        return audio

    @staticmethod
    def get_beat(audio):
        y, sr = librosa.load(audio)
        # y_harmonic, y_percussive = librosa.effects.hpss(y)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        print(tempo)
        print(beat_times)

        diff = []
        for i in range(0, len(beat_times) - 1):
            diff.append(beat_times[i + 1] - beat_times[i])

        print(len(diff))
        print(diff)

        return diff

    @staticmethod
    def generate_beat_video(video, beats, mark):
        beat_length = 0.2
        output = os.path.dirname(video) + "/" + os.path.basename(video).split(".")[0] + "_beat.mp4"
        command = "ffmpeg -i " + video
        overlay = " -filter_complex \""
        images = ""
        for i in range(0, len(beats)):
            images += " -i " + mark
            if i == 0:
                overlay += "[0:v][1:v]overlay=10:10:enable='between(t," + str(beats[0]) + "," \
                           + str(beats[0] + beat_length) + ")'[tmp]; "
            else:
                overlay += "[tmp][" + str(i + 1) + ":v] overlay=10:10:enable='between(t," + str(beats[0]) + "," + str(
                    beats[0] + beat_length) + ")'[tmp]; "

        overlay = overlay[0: len(overlay) - 8] + "\" "
        print(images)
        command += images + overlay + output
        print(command)

        subprocess.call(command, shell=True)

        return output


# audio_file = "C:/Users/ZhangY/Desktop/blend/audio.mp3"
# video_file = "C:/Users/ZhangY/Desktop/blend/output.mp4"
# scale_image = "C:/Users/ZhangY/Desktop/blend/image.jpg"
#
# beat = [10, 15, 20, 25, 30, 35]
# print(Rhythm.generate_beat_video(video_file, beat, scale_image))

