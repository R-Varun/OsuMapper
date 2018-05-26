
import os
from Model.utils import *
from Sound.utils import *
from Sound.song import *
from GA.GeneticAlgorithm import *
from GA.utils import *
from GA.Fitness_Function import *
from GA.Crossover_Function import *
from GA.Mutate_Function import *
import matplotlib.pyplot as plt



def convertBestToNotes(GA_notes, mpbs, offset):
	ret = []
	timing = offset
	for i in GA_notes:
		if i.isNote:
			n = HitCircle(i.x, i.y, timing, new_combo=1)
			ret.append(n)
		timing += mpbs

	return ret






OSU_SONG_FILE = "./"
SONGNAME = "79363 DJ THT meets Scarlet - Live 2 Dance (Nightcore Mix)"

songPath = "./"

# Extremely lazy indexing, fix me later
osuFile = os.listdir(songPath)[list(map(lambda x : ".osu" in x, os.listdir(songPath))).index(True)]

osuAbs = join(songPath, osuFile)

bm = create_beatmap(osuAbs)
bm.Creator = "Svvag"
bm.write_to_file("./oo.osu")

print(bm.Timing[0].Mspb)


#
song = Song(join(songPath, bm.AudioFilename))


print(bm.Timing[0].to_string())

# g = GA(1000, 100, FF_Close(50, 20),crossover_function=Single_Point_Crossover(.4), mutate_function = Random_Mutate(.2,.1))
#
# g.train()








# print(bpm)
# for i in range(10):
# 	cur = off + i * bpm
# 	song.write_beat_to_wav(cur, window=100, file="output" + str(c) + ".wav")
# 	c+= 1
# show_waveform(song.data, condense_rate=(song.rate))
beats = get_likely_beats(song.rate, song.data[:int(len(song.data) / 20)], bm.Timing[0].Mspb,bm.Timing[0].Offset, divisions=4)



ff1 = FF_REWARD_PLACEMENT(beats)
# ff2 = FF_Close(50, 20)
# f= FF_Composite([ff1, ff2], [.7, .3])

#
g = GA(50, 50, ff1,crossover_function=Single_Point_Crossover(.4), mutate_function = Random_Mutate(.3,.1))

g.train(iterations=10000)

best = g.best
#
#
#
# notes = None
# with open('out.pickle', 'rb') as handle:
# 	notes = pickle.load(handle)

notes = convertBestToNotes(best, bm.Timing[0].Mspb,bm.Timing[0].Offset)
bm.Notes = notes
bm.Creator = "Svvag"
bm.Version = "SVVVAGSANE"

bm.write_to_file("ClariS - Connect (Holoaz) [svvag].osu")




# show_waveform(song.data, condense_rate=500)

# rate, data = song.get_beat(1013, window = 5000)
#
# for c, i in enumerate(bm.Notes[0:3]):
# 	song.write_beat_to_wav(i.ms, window=100, file="output" + str(c) +".wav")
# 	show_waveform(data, condense_rate=40)
#


#
#
# rate, data = live2Dance.get_beat(3578, window=50)
# show_waveform(data, condense_rate=30)
#
# rate, data = live2Dance.get_beat(3978, window=50)
# show_waveform(data, condense_rate=30)

