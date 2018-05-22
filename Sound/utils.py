import subprocess
import numpy as np
import scipy.io.wavfile
import os

DEFAULT_OUTFILE = "out.wav"

TEMP_WAV_FILE= "file.wav"


def convert_to_wav(filePath, output="file.wav"):
	subprocess.call(['ffmpeg', '-y','-i', filePath,
					 output])

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
