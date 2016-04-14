import os
from os import path
from rhythm import Rhythm
import subprocess


class Blend:
    __video_files = []
    __audio_files = []

    def __init__(self, work_dir, output):
        self.__work_dir = work_dir
        self.__output = output

    def __check_video_files(self):
        if len(self.__video_files) != 0:
            print(str(len(self.__video_files)) + " video files found")
            return True
        print("Video files not found")
        return False

    def __check_audio_files(self):
        if len(self.__audio_files) != 0:
            print(str(len(self.__audio_files)) + " audio files found")
            return True
        print("Audio files not found")
        return False

    def __check_files(self):
        os.chdir(self.__work_dir)
        files = [f for f in os.listdir(self.__work_dir) if path.isfile(f)]

        for f in files:
            ext = os.path.splitext(f)[1]
            if ext == '.mp4':
                self.__video_files.append(f)
            elif ext == '.mp3':
                self.__audio_files.append(f)

        return self.__check_audio_files() and self.__check_video_files()

    def blend(self):
        if self.__check_files():
            print(self.__audio_files)
            print(self.__video_files)
            print("blending")

            # self.blend_by_beat()

    def blend_by_beat(self):
        beats = Rhythm.get_beat(self.__audio_files[0])
        self.concat(self.__video_files, self.__output)

    def concat(self, video_files, output):
        os.chdir(self.__work_dir)
        temp = open("clips.txt", "wb")
        for _file in video_files:
            temp.write("file " + "'" + _file + "'" + "\n");
        temp.close()

        command_concat = "ffmpeg -f concat -i " + input + " -c copy " + output
        subprocess.call(command_concat, shell=True)


directory = "C:/Users/ZhangY/Desktop/blend/"
output_path = "C:/Users/ZhangY/Desktop/blend/work.mp4"


blend = Blend(directory, output_path)
blend.blend()

