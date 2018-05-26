import numpy as np
import random


MAX_WIDTH = 640
MAX_HEIGHT = 480
MULTIPLIERS = [.25, .5, 1, 2]


class GA_Note:

	def __init__(self, x, y, isNote):
		self.x = x
		self.y = y
		self.isNote = isNote

	def __repr__(self):
		return "GANOTE: {}, {}, {}".format(str(self.x), str(self.y), str(self.isNote))



def random_enc_note(max_dx = MAX_WIDTH, max_dy = MAX_HEIGHT):
	randX = random.randint(0,640)
	randY = random.randint(0, 480)
	# randDT = MULTIPLIERS[random.randint(0, len(MULTIPLIERS) - 1)] * bpm

	isNote = random.randint(0,1)
	return GA_Note(randX, randY, isNote)












def distance(x1, y1, x2, y2):
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**.5










