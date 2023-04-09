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
$ python -m pip install pytube
```

Sometimes, the PyPI release becomes slightly outdated. To install from the source with pip:

```bash
$ python -m pip install git+https://github.com/pytube/pytube
```

### Using Youtbe downloader in a Python script

To download a video using the library in a script, you'll need to import the YouTube class from the library and pass an argument of the video URL. From there, you can access the streams and download them.

```python
 >>> from pytube import YouTube
 >>> YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
 >>> yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
 >>> yt.streams
  ... .filter(progressive=True, file_extension='mp4')
  ... .order_by('resolution')
  ... .desc()
  ... .first()
  ... .download()
```

### Using the command-line interface

Using the CLI is remarkably straightforward as well. To download a video at the highest progressive quality, you can use the following command:
```bash
$ pytube https://youtube.com/watch?v=2lAe1cqCOXo
```

You can also do the same for a playlist:
```bash
$ pytube https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n
```
