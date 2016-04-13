from __future__ import print_function
import librosa
import os
import subprocess
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
                overlay += "[0:v][1:v]overlay=10:10:enable='between(t," + str(beats[0]) + ","\
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


#
# y, sr = librosa.load(audio)
#
# # 3. Run the default beat tracker
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#
# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#
# # 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#
# print(beat_times)
# print(len(beat_times))
# diff = []
#
# for i in range(0, len(beat_times) - 1):
#     diff.append(beat_times[i + 1] - beat_times[i])
#
# print(len(diff))
# print(diff)
#
# clip = VideoFileClip("myHolidays.mp4")
#
# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip("boom", fontsize=70, color='white')
#
# # Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(0.1)
#
# # Overlay the text clip on the first video clip
# video = CompositeVideoClip([clip, txt_clip])
#
# # Write the result to a file
# video.write_videofile("myHolidays_edited.avi", fps=24, codec='mpeg4')
#
# # print('Saving output to beat_times.csv')
# # librosa.output.times_csv('beat_times.csv', beat_times)

audio_file = "C:/Users/ZhangY/Desktop/blend/audio.mp3"
video_file = "C:/Users/ZhangY/Desktop/blend/output.mp4"
scale_image = "C:/Users/ZhangY/Desktop/blend/image.jpg"
# print(Rhythm.get_beat(Rhythm.extract_audio(video_file)))

_beats = Rhythm.get_beat(audio_file)
print(_beats)

plt.plot(range(0, len(_beats), 1), _beats, 'ro')
plt.show()

# print(Rhythm.generate_beat_video(video_file, _beats, scale_image))

#
# print(Rhythm.get_beat())
