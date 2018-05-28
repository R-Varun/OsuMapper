import os
from Model.model import *


BIT_CIRCLE = 0
BIT_SLIDER = 1
BIT_NEW_COMBO = 2
BIT_SPINNER = 3




def join(*f):
	return os.path.join(*f)



# Parses a .osu file and creates a BeatMap object
def create_beatmap(filePath):

	f = open(filePath, "r",  encoding='utf-8')
	lines = f.readlines()

	cur_heading = None

	general = {}

	general["Notes"] = []
	general["Timing"] = []
	for line in lines:
		cur_line = line.strip()
		if cur_line.startswith("[") and cur_line.endswith("]"):
			cur_heading = cur_line[1:-1]
			continue
		if len(cur_line) == 0:
			continue

		if cur_line.startswith("//"):
			continue

		if cur_heading == "General":
			temp = cur_line.split(":")
			values = [temp[0].strip(), temp[1].strip()]
			if values[0] == 'Mode':
				values[1] = int(values[1])

			general[values[0]] = values[1]

		if cur_heading == "Difficulty":
			temp = cur_line.split(":")
			values = temp[0].strip(), float(temp[1].strip())
			general[values[0]] = values[1]




		if cur_heading == "Editor":
			temp = cur_line.split(":")

			values = temp[0].strip(), temp[1].strip()
			if values[0] == 'Bookmarks':
				# creates list of integers for Bookmakes
				intList = map(lambda x : int(x.strip()), values[1].split(","))
				general[values[0]] = intList

			elif values[0] == 'DistanceSpacing' or values[0]=="TimelineZoom":
				general[values[0]] = float(values[1])

			else:
				general[values[0]] = int(values[1])


		if cur_heading == "Metadata":
			temp = cur_line.split(":")

			values = temp[0].strip(), temp[1].strip()
			general[values[0]] = values[1]




		if cur_heading == "HitObjects":
			temp = cur_line.split(",")
			temp = list(map(lambda x: x.strip(), temp))
			mode = int(temp[3])
			x = int(temp[0])
			y = int(temp[1])
			time = int(temp[2])
			hs = int(temp[4])


			newObj = None
			newCombo = is_bit_on(mode, BIT_NEW_COMBO)
			if is_bit_on(mode, BIT_CIRCLE):
				newObj = HitCircle(x, y, time, hs, newCombo)
# 			TODO: add support for sliders
			if is_bit_on(mode, BIT_SLIDER):
				pass
				newObj = Slider(x, y, time, hs, newCombo)

			if is_bit_on(mode, BIT_SPINNER):
				pass
				newObj = Slider(x, y, time, hs, newCombo)

			general["Notes"].append(newObj)

		if cur_heading == "TimingPoints":
			offset, mspb, meter, sset, sindex, volume, inhereted, kiai = cur_line.split(",")
			model = {
				"Offset": int(offset),
				"Mspb": float(mspb),
				"Meter": int(meter),
				"Sset": int(sset),
				"Sindex": int(sindex),
				"Volume": int(volume),
				"Inherited": int(inhereted),
				"Kiai": int(kiai)
			}
			tp = TimingPoint(**model)
			general["Timing"].append(tp)



	# Uses unpacked kwargs to create BeatMap Object
	return BeatMap(**general)





# Determines whether n'th bit is 1
def is_bit_on(someInt, n):
	x = someInt >> n
	return x % 2 == 1



