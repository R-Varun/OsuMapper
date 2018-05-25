
import os
from Model.utils import *
from Sound.utils import *
from Sound.song import *
import matplotlib.pyplot as plt


OSU_SONG_FILE = "C:/Users/Varun/AppData/Local/osu!/Songs"
SONGNAME = "79363 DJ THT meets Scarlet - Live 2 Dance (Nightcore Mix)"

songPath = join(OSU_SONG_FILE, SONGNAME)

# Extremely lazy indexing, fix me later
osuFile = os.listdir(songPath)[list(map(lambda x : ".osu" in x, os.listdir(songPath))).index(True)]
mp3File = os.listdir(songPath)[list(map(lambda x : ".mp3" in x, os.listdir(songPath))).index(True)]


mp3Abs = join(songPath, mp3File)
osuAbs = join(songPath, osuFile)

rate, data = get_mp3(mp3Abs)
live2Dance = Song(rate, data)

bm = create_beatmap(osuAbs)
print(bm.AudioFilename)
#
#
# rate, data = live2Dance.get_beat(3578, window=50)
# show_waveform(data, condense_rate=30)
#
# rate, data = live2Dance.get_beat(3978, window=50)
# show_waveform(data, condense_rate=30)