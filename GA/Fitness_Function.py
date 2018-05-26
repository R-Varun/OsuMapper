from GA.utils import *



class Fitness_Function:
	def eval(self, entry):
		pass


class FF_Close(Fitness_Function):

	def __init__(self, proximity, reward):
		self.proximity = proximity
		self.reward = reward
	def eval(self, entry):
		score = 0
		for i in range(1, len(entry)):
			cur_note = entry[i]
			prev_note = entry[i - 1]
			if distance(cur_note.x, cur_note.y, prev_note.x, prev_note.y) < self.proximity:
				score += self.reward
		return score


def FF_REWARD_PLACEMENT(notes, reward_template):
	pass



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


