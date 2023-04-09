from pytube import YouTube
import os


class Audio:
    """
    Download the audio using urls & destination
    """
    @staticmethod
    def download(urls, destination):
        print("\nPlease wait...")
        for url in urls:
            yt = YouTube(url)

            # Getting the caption
            print("Downloading... %s \n" % yt.title)

            # Set the video stream to the highest resolution
            stream = yt.streams.filter(only_audio=True).first().download(destination)

            # Save the file
            base, ext = os.path.splitext(stream)
            file = base + '.mp3'
            os.rename(stream, file)

        print("\nCompleted :)")


class Video:
    """
    Download the video using urls & destination
    """
    @staticmethod
    def download(urls, destination):
        print("\nPlease wait...")
        for url in urls:
            yt = YouTube(url)

            # Getting the caption
            print("Downloading... %s \n" % yt.title)

            # Set the video stream to the highest resolution
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

            # Download the video
            stream.download(destination)

        print("\nCompleted :)")
