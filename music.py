import urllib.request
import os
import asyncio
import glob
from pygame import mixer

def gotoEnsureDir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    os.chdir(d)
    
def downloadAudio(youtubeURL):
    urlStart='http://www.youtubeinmp3.com/fetch/?video='
    url = urlStart+youtubeURL
    fileName = youtubeURL[youtubeURL.index('=')+1:]+'.mp3'
    urllib.request.urlretrieve(url, fileName)
    return fileName
mixer.init()
gotoEnsureDir('music/')
playlist = []

def dl():
    playlist.append(downloadAudio('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    playlist.append(downloadAudio('https://www.youtube.com/watch?v=ENXvZ9YRjbo'))

    

def playPlaylist():
    mixer.music.load(playlist[0])
    mixer.music.play()
    mixer.music.set_endevent()

def clear():
    for item in glob.glob('*'):
        os.remove(item)
