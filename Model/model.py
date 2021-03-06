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


CATEGORIES = [GENERAL, EDITOR, DIFFICULTY,METADATA]
AGGLOMERATE = {"Notes", "Colour","Timing"}
class BeatMap:
	# AudioFilename (String) specifies the location of the audio file relative to the current folder.
	AudioFilename = None
	#Mode (Integer) defines the game mode of the beatmap. (0=osu!, 1=Taiko, 2=Catch the Beat, 3=osu!mania)
	Mode = None

	HPDrainRate = None
	CircleSize = None
	OverallDifficulty = None
	ApproachRate = None
	Timing = None
	Notes = None

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
				if verify_type(arg_val, arg_type):
					setattr(self, arg, arg_val)
				elif isinstance(arg_val, str):
					setattr(self, arg, convert_str_to_type(arg_val, arg_type))

	def write_to_file(self, filePath):
		f = open(filePath, "w",  encoding='utf-8')

		f.write("osu file format v14\n//This file was generated by OsuMapper\n")

		f.write("[General]\n")
		for attr in GENERAL:
			cur_attr = getattr(self, attr, None)
			attr_type = GENERAL[attr]
			if cur_attr == None:
				continue
			f.write(attr + ": " + convert_type_to_str(cur_attr, attr_type) + "\n")
		f.write("\n[Editor]\n")
		for attr in EDITOR:
			cur_attr = getattr(self, attr, None)
			attr_type = EDITOR[attr]
			if cur_attr == None:
				continue
			f.write(attr + ": " + convert_type_to_str(cur_attr, attr_type) + "\n")

		f.write("\n[Metadata]\n")
		for attr in METADATA:
			cur_attr = getattr(self, attr, None)
			attr_type = METADATA[attr]
			if cur_attr == None:
				continue
			f.write(attr + ": " + convert_type_to_str(cur_attr, attr_type) + "\n")

		f.write("\n[Difficulty]\n")
		for attr in DIFFICULTY:
			cur_attr = getattr(self, attr, None)
			attr_type = DIFFICULTY[attr]
			if cur_attr == None:
				continue
			f.write(attr + ": " + convert_type_to_str(cur_attr, attr_type) + "\n")

		f.write("\n[TimingPoints]\n")
		for tp in self.Timing:
			f.write(tp.to_string() + "\n")

		f.write("\n[HitObjects]\n")
		for ho in self.Notes:
			f.write(ho.to_string() + "\n")
		f.close()



TIMINGPOINT_PARAMS = \
	{
	"Offset":"int",
	"Mspb" : "dec",
	"Meter": "int",
	"Sset": "int",
	"Sindex": "int",
	"Volume": "int",
	"Inherited": "int",
	"Kiai": "int"
	}

# Offset, Milliseconds per Beat, Meter, Sample Set, Sample Index, Volume, Inherited, Kiai Mode
class TimingPoint:
	def __init__(self, **kwargs):
		for arg in kwargs:
			arg_val = kwargs[arg]
			if arg in TIMINGPOINT_PARAMS and verify_type(arg_val, TIMINGPOINT_PARAMS[arg]):
				setattr(self, arg, arg_val)


	def to_string(self):
		ret_str = ""
		for attr in TIMINGPOINT_PARAMS:
			attr_type = TIMINGPOINT_PARAMS[attr]
			cur_attr = getattr(self, attr, None)
			if cur_attr == None:
				ret_str += "0,"
			else:
				ret_str += convert_type_to_str(cur_attr,attr_type) + ","

		return ret_str[:-1]






class HitCircle:
	def __init__(self, x, y, ms, hitsound=0, new_combo=0):
		self.x = x
		self.y = y
		self.ms = ms
		self.hitsound = hitsound
		self.new_combo = new_combo

	def to_string(self):
		retStr = "{},{},{},{},{},{}".format(str(self.x), str(self.y), round(self.ms,2), str(self.new_combo * 4 + 1 * 1), str(self.hitsound), "0:0:0:0:")
		return retStr


# TODO: Sliders currently just hit-circles
class Slider:
	def __init__(self, x, y, ms, hitsound, new_combo):
		self.x = x
		self.y = y
		self.ms = ms
		self.hitsound = hitsound
		self.new_combo = new_combo
	def to_string(self):
		retStr = "{},{},{},{},{},{}".format(str(self.x), str(self.y), str(self.ms), str(self.new_combo * 4 + 1 * 1), str(self.hitsound), "0:0:0:0:")
		return retStr


def verify_type(obj, type_str):
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

def convert_type_to_str(obj, type_str):
	if "list" not in type_str:
		return str(obj)

	else:
		ret_str = ""
		for i in obj:
			ret_str += str(i) + ","

		return ret_str[:-1]

def convert_str_to_type(obj, type_str):
	if type_str == "dec":
		return float(obj)
	if type_str == "int":
		return int(obj)
	if type_str == "str":
		return obj

	if type_str == "int_list":
		ret = []
		for i in obj.split(","):
			ret.append(int(i))
		return ret
	if type_str == "str_list":
		ret = obj.split(",")
		return ret
	if type_str == "dec_list":
		ret = []
		for i in obj.split(","):
			ret.append(float(i))
		return ret

