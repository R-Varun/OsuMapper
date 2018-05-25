import numpy as np
from Sound.utils import *



class Song:
	# Change these if you don't want to
	default_window = 50
	default_out = "out.wav"

	def __init__(self, rate, data, def_window = default_window, def_out = default_out):
		self.rate = rate
		self.data = data
		self.default_window = def_window
		self.default_out = def_out



	# Finds the beat at a given ms
	def get_beat(self, ms, window = default_window):
		index = ms * (self.rate / 1000)
		index_before = int(max(0, index - (window//2 * (self.rate / 1000))))
		index_after = int(min(index +  (window//2 * (self.rate / 1000)), len(self.data)))

		beat_data = self.data[index_before:index_after]

		return self.rate, beat_data

	def write_beat_to_wav(self, ms, file=default_out, window= default_window):
		rate, data = self.get_beat(ms, window)
		write_wave(rate, data, file = file)

