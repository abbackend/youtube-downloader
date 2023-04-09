# importing packages
import pytube
from helper import Audio, Video


if __name__ == "__main__":
    # Check for download the playlist
    print("Do yo want to download the playlist? (default: No)")
    isDownloadPlaylist = str(input("")) or 'No'

    if "yes" in isDownloadPlaylist.lower():
        # URL input from user
        yt = pytube.Playlist(str(input("\nEnter the Playlist URL: \n")))
        print('Found %s videos in this playlist.' % len(yt.video_urls))

        links = yt.video_urls
    else:
        links = []
        while not len(links):
            inputLinks = input("\nEnter the YouTube video links: \n")
            links = inputLinks.split()


    # Check for download audio or videos
    print("\nDo yo want to download in mp3 format (default: No)")
    isDownloadAudio = str(input("")) or 'No'

    # Check for destination to save file
    print("\nEnter the destination (leave blank for current directory)")
    destination = str(input("")) or '.'

    if "yes" in isDownloadAudio.lower():
        Audio.download(urls=links, destination=destination)
    else:
        Video.download(urls=links, destination=destination)

    # result of success
    print("\nThanks for using this service.")
