<img src="https://github.com/abbackend/portfolio/blob/master/channels4_banner.jpg" width="100%"/>

# Youtube Downloader

This is a genuine, lightweight Python script for downloading YouTube videos.

## Description

YouTube is the most popular video-sharing platform in the world and as a hacker, you may encounter a situation where you want to script something to download videos. For this, I present to you: *youtube-downloader*.

*youtube-downloader* is a lightweight script written in Python. Which uses [pytube.io](https://pytube.io) library
dependencies and aims to be highly reliable.

## Features

- Support for downloade youtube videos.
- Support for downloade youtube videos in mp3 formats.
- Support for downloading the complete playlist

### Installation

Youtube-downloader requires an installation of Python 3.6 or greater, as well as pip. (Pip is typically bundled with Python [installations](https://python.org/downloads).)

To install from PyPI with pip:

```bash
$ python3 -m pip install pytube
```

Sometimes, the PyPI release becomes slightly outdated. To install from the source with pip:

```bash
$ python3 -m pip install git+https://github.com/pytube/pytube
```

### Using the command-line interface

Using the CLI is remarkably straightforward as well. To download a video at the highest progressive quality, you can use the following command:
```bash
$ python3 main.py
...
...Do yo want to download the playlist? (default: No)
...no
...
...Enter the YouTube video links: 
...https://www.youtube.com/watch?v=Zd3Mh3TeOGI
...
...Do yo want to download in mp3 format (default: No)
...no
...
...Enter the destination (leave blank for current directory)
...
...
...Please wait...
...Downloading... Gentle Whispering Schools MatPat in ASMR! 
...
...Completed :)
...
...Thanks for using this service.
```

You can also do the same for a audio:
```bash
$ python3 main.py
...
...Do yo want to download the playlist? (default: No)
...no
...
...Enter the YouTube video links: 
...https://www.youtube.com/watch?v=Zd3Mh3TeOGI
...
...Do yo want to download in mp3 format (default: No)
...yes
...
...Enter the destination (leave blank for current directory)
...
...
...Please wait...
...Downloading... Gentle Whispering Schools MatPat in ASMR! 
...
...Completed :)
...
...Thanks for using this service.
```

You can also do the same for a playlist:
```bash
$ python3 main.py
...
...Do yo want to download the playlist? (default: No)
...yes
...
...Enter the Playlist URL: 
...https://www.youtube.com/watch?v=UhhwNVHNIfc&list=PLSXTaG1fT0cTB1W3RGt8WR1nciBbv_QEN
...Found 2 videos in this playlist
...
...Do yo want to download in mp3 format (default: No)
...
...
...Enter the destination (leave blank for current directory)
...
...
...Please wait...
...Downloading... Kerry की Entry ने Daya को कर दिया दुखी | Taarak Mehta Ka Ooltah Chashmah | Kerry Entry
...
...Downloading... Kerry को देखर Popatlal हो गया लट्टू! | Taarak Mehta Ka Ooltah Chashmah | Kerry Entry
...
...Completed :)
...
...Thanks for using this service.
```

## Authors

- [@abbackend](https://www.github.com/abbackend)
