from GA.utils import *



class Fitness_Function:
	def eval(self, entry):
		pass


class FF_Close(Fitness_Function):

	def __init__(self, proximity, reward, smoothing=10):

		self.smoothing = smoothing
		self.proximity = proximity
		self.reward = reward
	def eval(self, entry):
		score = 0
		entry = np.array(list(filter(lambda x : x.isNote == 1, entry)))
		# print(entry)
		for i in range(1, len(entry)):
			cur_note = entry[i]
			prev_note = entry[i - 1]
			dist = distance(cur_note.x, cur_note.y, prev_note.x, prev_note.y)
			if dist < 1:
				score = self.reward
			elif  dist < self.proximity:
				const = (self.proximity/ dist)

				score += (self.reward * const) / (const + 10)
		return score

# Placement on likely beats
class FF_REWARD_PLACEMENT:
	def __init__(self, reward_template):
		self.reward_template = reward_template

	def eval(self, entry):# Trim template to be same length as each pop entry
		if len(entry) == 0:
			return 0
		cur_template = self.reward_template[0:len(entry)]


		cur_item = np.array(list(map(lambda x : x.isNote, entry)))
		weighted = cur_item * cur_template
		score = np.sum(weighted)

		return score

class FF_REWARD_PLACEMENT:
	def __init__(self, reward_template):
		self.reward_template = reward_template

	def eval(self, entry):  # Trim template to be same length as each pop entry
		# print(entry.shape)
		if len(entry) == 0:
			return 0
		cur_template = self.reward_template[0:len(entry)]
		# print(cur_template.shape)
		cur_item = np.array(list(map(lambda x: x.isNote, entry)))
		weighted = cur_item * cur_template
		score = np.sum(weighted)

		return score


# Apply multiple fitness functions with differing weights
class FF_Composite:
	def __init__(self, funcs, weights=None):
		self.funcs = funcs
		self.weights = weights

	def eval(self, entry):
		vals = []
		for i in self.funcs:
			vals.append(i.eval(entry))

		if self.weights == None:
			return sum(vals) / len(vals)
		else:
			summ = 0
			for i, val in enumerate(vals):
				summ += val * self.weights[i]

			return summ


