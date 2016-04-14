from blend import Blend
from blend import Downloader
from blend import Rhythm

video_urls = ["https://www.youtube.com/watch?v=Y9ovl3ixqHs",
              ]

video_url = "https://www.youtube.com/watch?v=Y9ovl3ixqHs"
audio_path = "C:/Users/ZhangY/Desktop/blend/"


def test_main():
    # test_downloader()
    # test_rhythm()
    test_blend()


def test_downloader():
    print("Test downloader...")

    for i in range(0, len(video_urls)):
        downloader = Downloader(video_urls[i], audio_path + "audio" + str(i) + ".mp3")
        downloader.download(Downloader.AUDIO_AND_VIDEO)


def test_rhythm():
    print("Test rhythm...")
    audio_file = "C:/Users/ZhangY/Desktop/blend/audio.mp3"
    video_file = "C:/Users/ZhangY/Desktop/blend/output.mp4"
    scale_image = "C:/Users/ZhangY/Desktop/blend/image.jpg"

    beat = [10, 15, 20, 25, 30, 35]
    print(Rhythm.generate_beat_video(video_file, beat, scale_image))


def test_blend():

    directory = "C:/Users/ZhangY/Desktop/blend/"
    work_path = "C:/Users/ZhangY/Desktop/blend/work.mp4"
    blend = Blend(directory, work_path)
    blend.blend()

test_main()
