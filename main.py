
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






OSU_SONG_FILE = "C:/Users/Varun/AppData/Local/osu!/Songs/427508 Wagakki Band - Senbonzakura [no video]"
SONGNAME = "Wagakki Band - Senbonzakura (pkk) [Insane].osu"

osuAbs =os.path.join(OSU_SONG_FILE, SONGNAME)

print(osuAbs)
bm = create_beatmap(osuAbs)
bm.Creator = "Svvag"
bm.write_to_file("./oo.osu")

print(bm.Timing[0].Mspb)


#
song = Song(join(OSU_SONG_FILE, bm.AudioFilename))


print(bm.Timing[0].to_string())



beats = get_likely_beats(song.rate, song.data[:int(len(song.data) / 20)], bm.Timing[0].Mspb,bm.Timing[0].Offset, divisions=4)
ff1 = FF_REWARD_PLACEMENT(beats)
ff2 = FF_Close(50, 20)
f= FF_Composite([ff1, ff2], [.3, .7])

#


co = Uniform_Crossover(.4, .5)
co2 = Single_Point_Crossover(.4)
g = GA(100, 77, f,crossover_function=co, mutate_function = Random_Mutate(.3,.1))

g.train(iterations=1000)

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

bm.write_to_file("Wagakki Band - Senbonzakura (pkk) [Svvag].osu")




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

