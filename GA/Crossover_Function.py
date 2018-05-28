from GA.utils import *
import numpy as np

class Crossover_Function:
	def cross(self, pop):
		pass




# Randomly splits a and B across a single point
class Single_Point_Crossover:
	def __init__(self, percentage):
		self.percentage = percentage

	def cross(self, pop):
		num_cross = int(self.percentage * len(pop))
		if num_cross % 2 == 1:
			num_cross -= 1

		crossers = np.random.choice(np.arange(len(pop)), num_cross, replace=False)
		crossers = crossers.reshape(-1, 2)
		newitems = []
		for pair in crossers:
			a, b = pair
			a = pop[a]
			b = pop[b]
			random_index = random.randint(0, len(a) - 1)
			child1 = list(a[0:random_index]) +  list(b[random_index:])
			child2 = list(b[0:random_index]) + list(a[random_index:])
			newitems.append(child1)
			newitems.append(child2)

		newitems = np.array(newitems)

		new_pop = np.vstack((pop, newitems))
		return new_pop

class Uniform_Crossover:
	def __init__(self, percentage_pop, percentage_gene):
		self.percentage_pop = percentage_pop
		self.percentage_gene = percentage_gene

	def cross(self, pop):
		num_cross = int(self.percentage_pop * len(pop))
		if num_cross % 2 == 1:
			num_cross -= 1

		crossers = np.random.choice(np.arange(len(pop)), num_cross, replace=False)
		crossers = crossers.reshape(-1, 2)
		newitems = []
		for pair in crossers:
			a, b = pair
			a = pop[a]
			b = pop[b]
			na = []
			nb = []
			for i in range(len(a)):
				rand = random.uniform(0,1)
				if rand < self.percentage_gene:
					na.append(b[i])
					nb.append(a[i])
				else:
					na.append(a[i])
					nb.append(b[i])
			# child1 = list(a[0:random_index]) + list(b[random_index:])
			# child2 = list(b[0:random_index]) + list(a[random_index:])
			newitems.append(na)
			newitems.append(nb)

		newitems = np.array(newitems)

		new_pop = np.vstack((pop, newitems))
		return new_pop


# Small test to see if they work
if __name__ == "__main__":

	s = Single_Point_Crossover(1)
	p = np.array([[GA_Note(0,0,1), GA_Note(0,0,1), GA_Note(0,0,1)],[GA_Note(1,1,1), GA_Note(1,1,1), GA_Note(1,1,1)]])

	p2 = s.cross(p)
	print(p2)
