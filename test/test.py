from blend import Blend
from blend import Downloader

video_url = "https://www.youtube.com/watch?v=Y9ovl3ixqHs"
audio_path = "C:/Users/ZhangY/Desktop/blend/audio.mp3"


def test_main():
    test_downloader()
    test_rhythm()


def test_downloader():
    print("Test downloader...")
    downloader = Downloader(video_url, audio_path)
    downloader.download(Downloader.AUDIO_AND_VIDEO)


def test_rhythm():
    print("Test rhythm...")

test_main()
