import os


def join(*f):
	return os.path.join(*f)




def create_beatmap(filePath):

	f = open(filePath, "r")
	lines = f.readlines()

	cur_heading = None

	general = {}
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
			temp = cur_line.split()

