import urllib.request
import os
import asyncio
import glob


def goto_ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    os.chdir(d)


def download_audio(youtubeURL):
    urlStart='http://www.youtubeinmp3.com/fetch/?video='
    url = urlStart+youtubeURL
    fileName = youtubeURL[youtubeURL.index('=')+1:]+'.mp3'

    urllib.request.urlretrieve(url, fileName)

    return fileName


def dl():
    playlist.append(download_audio('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    playlist.append(download_audio('https://www.youtube.com/watch?v=ENXvZ9YRjbo'))


def play_playlist():
    pass


def clear():
    for item in glob.glob('*'):
        os.remove(item)

mixer.init()
goto_ensure_dir('music/')
playlist = []



#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
#CHECK OUT PYDUB
