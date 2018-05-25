import subprocess
import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
import os

DEFAULT_OUTFILE = "out.wav"
TEMP_WAV_FILE= "file.wav"


# Subprocess call to FFmpeg, outputs to devnull so that output is not shown to console
def convert_to_wav(filePath, output="file.wav"):
	subprocess.call(['ffmpeg', '-y','-i', filePath,
					 output], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_wav(filePath):
	rate, data = scipy.io.wavfile.read(filePath)
	return rate, data


def get_mp3(filePath):
	convert_to_wav(filePath, TEMP_WAV_FILE)
	rate, data = get_wav(TEMP_WAV_FILE)
	os.remove(TEMP_WAV_FILE)
	return rate, data


def write_wave(rate, data, file = DEFAULT_OUTFILE):
	scipy.io.wavfile.write(file, rate, data)



def show_waveform(data, condense_rate=500):
	diff = len(data) % condense_rate
	# diff = min(diff, condense_rate - diff)

	# Trim data by amount to ensure divisibility
	print(len(data))
	data = data[0: 0-diff]
	print(len(data))
	c = np.mean(np.mean(data, axis=1).reshape(-1, condense_rate), axis=1)
	plt.plot(np.arange(len(c)), c)
	plt.show()