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


def get_adaptive(filePath):
	ending = filePath[-3:]
	if  ending == "mp3":
		return get_mp3(filePath)
	elif ending == "wav":
		return get_wav(filePath)



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

def show_waveform_by_bpm(rate, data, mbps, offset, divisions = 4):
	points = []
	window = 10
	init = int(offset  * (rate / 1000))
	trav = int(mbps / divisions * (rate / 1000))
	for i in range(init, len(data), trav):
		index_before = int(max(0, i - (window // 2 * (rate / 1000))))
		index_after = int(min(i + (window // 2 * (rate / 1000)), len(data)))

		x = abs(np.mean(np.mean(data[index_before: index_after], axis=1)))



		points.append(x)

	points = np.array(points)

	print(points)
	x = np.convolve(points, [-.5, 1, -.5], 'same')
	y = x > .5

	plt.plot(np.arange(len(points)) * mbps / divisions + offset, y)
	plt.xticks(np.arange(len(points)) * mbps / divisions + offset)
	plt.show()

	plt.plot(np.arange(len(points)) * mbps / divisions + offset, x)
	plt.xticks(np.arange(len(points)) * mbps / divisions + offset)
	plt.show()


