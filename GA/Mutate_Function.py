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

		new_mutant_pop = np.take(pop, ns, axis=1)
		other_pop = np.take(pop, list(other_elements), axis = 1)

		return np.concatenate(new_mutant_pop, other_pop)




