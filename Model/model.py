#OSU file format Documented here: https://osu.ppy.sh/help/wiki/osu!_File_Formats/Osu_(file_format)


# Key: Category name, item type
# Types so far: int, dec, str, str_list, dec_list, int_list
# TODO: functions to encode these types to string, and vince versa
GENERAL = {"AudioFilename" : "str",
		   "AudioLeadIn" : "int",
		   "PreviewTime":"int",
		   "Countdown":"int",
		   "SampleSet":"str",
		   "StackLeniency":"dec",
		   "Mode":"int",
		   "LetterboxInBreaks":"int",
			"WidescreenStoryboard":"int"
		   }

EDITOR = {"Bookmarks": "int_list",
		  "DistanceSpacing" : "dec",
		  "BeatDivisor":"int",
		  "GridSize":"int",
		  "TimelineZoom":"int"
		  }

DIFFICULTY = {"HPDrainRate":"dec",
			  "CircleSize":"dec",
			  "OverallDifficulty":"dec",
			  "ApproachRate":"dec",
			  "SliderMultiplier":"dec",
			  "SliderTickRate":"dec"
			  }

METADATA = {"Title": "str",
			"TitleUnicode": "str",
			"Artist": "str",
			"ArtistUnicode" : "str",
			"Creator": "str",
			"Version": "str",
			"Source": "str",
			"Tags": "str",
			"BeatmapID" : "int",
			"BeatmapSetID" : "int"
			}


CATEGORIES = {GENERAL, EDITOR, DIFFICULTY,METADATA}
AGGLOMERATE = {"Notes", "Colour"}
class BeatMap:
	# AudioFilename (String) specifies the location of the audio file relative to the current folder.
	AudioFilename = None
	#Mode (Integer) defines the game mode of the beatmap. (0=osu!, 1=Taiko, 2=Catch the Beat, 3=osu!mania)
	Mode = None

	HPDrainRate = None
	CircleSize = None
	OverallDifficulty = None
	ApproachRate = None

	def __init__(self, **kwargs):
		for arg in kwargs:
			arg_val = kwargs[arg]
			if arg in AGGLOMERATE:
				setattr(self, arg, arg_val)
			else:
				category = None
				for cat in CATEGORIES:
					if arg in cat:
						category = cat
						break

				if category == None:
					raise Warning("Attribute: " + arg + " not a valid field.")

				arg_type = category[arg]
				# Check if argument value is of valid type
				if self._verify_type(arg_val, arg_type):
					setattr(self, arg, arg_val)



	def _verify_type(self, obj, type_str):
		if type_str == "dec":
			return isinstance(obj, float)
		if type_str == "int":
			return isinstance(obj, int)
		if type_str == "str":
			return isinstance(obj, str)

		if type_str == "int_list":
			for i in obj:
				if not isinstance(i, int):
					return False
			return True
		if type_str == "str_list":
			for i in obj:
				if not isinstance(i, str):
					return False
			return True
		if type_str == "dec_list":
			for i in obj:
				if not isinstance(i, float):
					return False
			return True



# Offset, Milliseconds per Beat, Meter, Sample Set, Sample Index, Volume, Inherited, Kiai Mode
# class TimingPoint:
# 	def __init__(self, **kwargs):




class HitCircle:
	def __init__(self, x, y, ms, hitsound, new_combo):
		self.x = x
		self.y = y
		self.ms = ms
		self.hitsound = hitsound
		self.new_combo = new_combo




# TODO: Sliders currently just hit-circles
class Slider:
	def __init__(self, x, y, ms, hitsound, new_combo):
		self.x = x
		self.y = y
		self.ms = ms
		self.hitsound = hitsound
		self.new_combo = new_combo
