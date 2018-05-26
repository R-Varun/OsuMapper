from GA.utils import *
import numpy as np

class Mutate_Function:
	def mutate(self, pop):
		pass


class Random_Mutate(Mutate_Function):

	def __init__(self, percent_pop, percent_element):
		self.percent_pop = percent_pop
		self.percent_element = percent_element

	def mutate(self, pop):

		mutate_size = int(len(pop) * self.percent_pop)

		ns = np.random.choice(np.arange(len(pop)), mutate_size, replace = False)
		element_set = set(ns)
		total_set = set(np.arange(len(pop)))

		other_elements = total_set.difference(element_set)
		new_mutant_pop = pop[ns]

		for entry in new_mutant_pop:
			for element in entry:
				if np.random.uniform() < self.percent_element:
					element.x = random.randint(0, 640)
					element.y = random.randint(0, 480)
					element.isNote = random.randint(0, 1)



		other_pop = pop[list(other_elements)]


		new_mutant_pop = np.vstack((other_pop, new_mutant_pop))
		return new_mutant_pop

# Small test to see if they work
if __name__ == "__main__":

	s = Random_Mutate(1,.5)
	p = np.array([[GA_Note(0,0,1), GA_Note(0,0,1), GA_Note(0,0,1)]])

	p2 = s.mutate(p)
	print(p2)
