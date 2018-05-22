import os
from Model.model import *


BIT_CIRCLE = 0
BIT_SLIDER = 1
BIT_NEW_COMBO = 2
BIT_SPINNER = 3




def join(*f):
	return os.path.join(*f)




def create_beatmap(filePath):

	f = open(filePath, "r")
	lines = f.readlines()

	cur_heading = None

	general = {}
	hitObs = []


	for line in lines:
		cur_line = line.strip()
		if cur_line.startswith("[") and cur_line.endswith("]"):
			cur_heading = cur_line[1:-1]
			continue
		if len(cur_line) == 0:
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

			hitObs.append(newObj)

	general["Notes"] = hitObs

	return BeatMap(**general)





# Determines whether n'th bit is 1
def is_bit_on(someInt, n):
	x = someInt >> n
	return x % 2 == 1