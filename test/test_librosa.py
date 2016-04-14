import librosa
import numpy as np
import matplotlib.pyplot as plt

audio_path = "C:/Users/ZhangY/Desktop/blend/audio.mp3"


def feature_test():
    # Compute local onset autocorrelation
    y, sr = librosa.load(audio_path)
    hop_length = 512
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
    tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sr,
                                          hop_length=hop_length)

    print(tempogram)



    # Compute global onset autocorrelation
    ac_global = librosa.autocorrelate(oenv, max_size=tempogram.shape[0])
    ac_global = librosa.util.normalize(ac_global)
    # Estimate the global tempo for display purposes
    tempo = librosa.beat.estimate_tempo(oenv, sr=sr, hop_length=hop_length)

    plt.figure(figsize=(8, 6))
    plt.subplot(3, 1, 1)
    plt.plot(oenv, label='Onset strength')
    plt.xticks([])
    plt.legend(frameon=True)
    plt.axis('tight')
    plt.subplot(3, 1, 2)
    # We'll truncate the display to a narrower range of tempi
    librosa.display.specshow(tempogram, sr=sr, hop_length=hop_length,
                             x_axis='time', y_axis='tempo',
                             tmin=tempo/4, tmax=2*tempo, n_yticks=4)
    plt.subplot(3, 1, 3)
    x = np.linspace(0, tempogram.shape[0] * float(hop_length) / sr, num=tempogram.shape[0])
    plt.plot(x, np.mean(tempogram, axis=1), label='Mean local autocorrelation')
    plt.plot(x, ac_global, '--', alpha=0.75, label='Global autocorrelation')
    plt.xlabel('Lag (seconds)')
    plt.axis('tight')
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.show()


def segment_test():
    y, sr = librosa.load(audio_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    # onset_env = librosa.onset.onset_strength(y, sr=sr,
    #                                      aggregate=np.median)
    # tempo = librosa.feature.tempogram(onset_envelope=onset_env, y=y, sr=sr)
    # chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    boundary_frames = librosa.segment.agglomerative(beats, 30)
    boundary_times = librosa.frames_to_time(boundary_frames)
    print(boundary_times)

    # array([  0.   ,   1.672,   2.322,   2.624,   3.251,   3.506,
    # 4.18 ,   5.387,   6.014,   6.293,   6.943,   7.198,
    # 7.848,   9.033,   9.706,   9.961,  10.635,  10.89 ,
    # 11.54 ,  12.539])

    # Plot the segmentation against the spectrogram

    plt.figure()
    S = np.abs(librosa.stft(y))**2
    librosa.display.specshow(librosa.logamplitude(S, ref_power=np.max),
                          y_axis='log', x_axis='time')
    plt.vlines(boundary_frames, 0, S.shape[0], color='b', alpha=0.9,
               label='Segment boundaries')
    plt.legend(frameon=True, shadow=True)
    plt.title('Power spectrogram')
    plt.tight_layout()
    plt.show()


def beat_test():
    y, sr = librosa.load(audio_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    # librosa.frames_to_time(beats[:20], sr=sr)
    # # array([ 0.093,  0.534,  0.998,  1.463,  1.927,  2.368,  2.833,
    # # 3.297,  3.762,  4.203,  4.667,  5.132,  5.596,  6.06 ,
    # # 6.525,  6.989,  7.454,  7.918,  8.382,  8.847])
    #
    # # Track beats using a pre-computed onset envelope

    onset_env = librosa.onset.onset_strength(y, sr=sr,
                                             aggregate=np.median)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,
                                           sr=sr)
    # tempo
    # # 64.599609375
    # beats[:20]
    # array([ 461,  500,  540,  580,  619,  658,  698,  737,  777,
    # 817,  857,  896,  936,  976, 1016, 1055, 1095, 1135,
    # 1175, 1214])

    # Plot the beat events against the onset strength envelope

    import matplotlib.pyplot as plt
    hop_length = 512
    plt.figure()
    plt.plot(librosa.util.normalize(onset_env), label='Onset strength')
    plt.vlines(beats, 0, 1, alpha=0.5, color='r',
               linestyle='--', label='Beats')
    plt.legend(frameon=True, framealpha=0.75)
    # Limit the plot to a 15-second window
    # plt.xlim([10 * sr / hop_length, 25 * sr / hop_length])
    # plt.xticks(np.linspace(10, 25, 5) * sr / hop_length,
    #            np.linspace(10, 25, 5))
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()


def decompose_test():
    # Separate into harmonic and percussive

    y, sr = librosa.load(audio_path)
    D = librosa.stft(y)
    H, P = librosa.decompose.hpss(D)

    boundary_frames = librosa.segment.agglomerative(H, 30)
    boundary_times = librosa.frames_to_time(boundary_frames)
    print(boundary_times)

    # array([  0.   ,   1.672,   2.322,   2.624,   3.251,   3.506,
    # 4.18 ,   5.387,   6.014,   6.293,   6.943,   7.198,
    # 7.848,   9.033,   9.706,   9.961,  10.635,  10.89 ,
    # 11.54 ,  12.539])

    # Plot the segmentation against the spectrogram

    plt.figure()
    S = np.abs(librosa.stft(y))**2
    librosa.display.specshow(librosa.logamplitude(S, ref_power=np.max),
                          y_axis='log', x_axis='time')
    plt.vlines(boundary_frames, 0, S.shape[0], color='b', alpha=0.9,
               label='Segment boundaries')
    plt.legend(frameon=True, shadow=True)
    plt.title('Power spectrogram')
    plt.tight_layout()
    plt.show()



    # Or with a narrower horizontal filter

    # H, P = librosa.decompose.hpss(D, kernel_size=(13, 31))
    #
    # # Just get harmonic/percussive masks, not the spectra
    #
    # mask_H, mask_P = librosa.decompose.hpss(D, mask=True)
    # mask_H
    # # array([[ 1.,  0., ...,  0.,  0.],
    # # [ 1.,  0., ...,  0.,  0.],
    # # ...,
    # # [ 0.,  0., ...,  0.,  0.],
    # # [ 0.,  0., ...,  0.,  0.]])
    # mask_P
    # # array([[ 0.,  1., ...,  1.,  1.],
    # # [ 0.,  1., ...,  1.,  1.],
    # # ...,
    # # [ 1.,  1., ...,  1.,  1.],
    # # [ 1.,  1., ...,  1.,  1.]])


decompose_test()
