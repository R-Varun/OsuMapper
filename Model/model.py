
# Documented here: https://osu.ppy.sh/help/wiki/osu!_File_Formats/Osu_(file_format)


class TimingPoint:


class BeatMap:
	# AudioFilename (String) specifies the location of the audio file relative to the current folder.
	AudioFilename = None
	#Mode (Integer) defines the game mode of the beatmap. (0=osu!, 1=Taiko, 2=Catch the Beat, 3=osu!mania)
	Mode = None



	HPDrainRate = None
	CircleSize = None
	OverallDifficulty = None
	ApproachRate = None

	def __init__(self, ):










class HitCircle:
	def __init__(self, x, y, ms, hitsound):
		self.x = x
		self.y = y
		self.ms = ms
		self.hitsound = hitsound


class Slider:

	def __init__(self, x, y, ms ):
