from __future__ import print_function
import librosa
import matplotlib.pyplot as plt


class Rhythm:
    def __init__(self):
        pass


y, sr = librosa.load("C:/Users/ZhangY/Desktop/blend/audio.mp3")

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print(len(beat_times))

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)


# 3. Run the default beat tracker
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#
# # y_harmonic, y_percussive = librosa.effects.hpss(y)
#
# # tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
# #                                              sr=sr)
#
# s = librosa.feature.tempogram(y=y, sr=sr)



#
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#
# print(len(beat_times))
#
# print(beat_times[1] - beat_times[0])
#
# print(beat_times[0])




# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#
# print(beat_frames[0])
#
# print(len(beat_frames))
#
# # 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#
# print(len(beat_times))
#
# print(beat_times[1] - beat_times[0])
# print(beat_times[0])

# print('Saving output to beat_times.csv')
# librosa.output.times_csv('C:/Users/ZhangY/Desktop/blend/beat_times.csv', beat_times)
