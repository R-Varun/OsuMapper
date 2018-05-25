import numpy as np
import random


MAX_WIDTH = 640
MAX_HEIGHT = 480
MULTIPLIERS = [.25, .5, 1, 2]

def random_enc_note(max_dx, max_dy, bpm):
	randX = random.randint(0,640)
	randY = random.randint(0, 480)
	randDT = MULTIPLIERS[random.randint(0, len(MULTIPLIERS) - 1)] * bpm

	return [randX, randY, randDT]









