# TODO: get model working before attempting- to solve problems with encoding
from GA.utils import *

CROSSOVER_POPULATION = .1

class GA:
	#initial_population: iterable with elements parsable by fitness_function
	#popution_size: integer denoting size of each generation
	#fitness_function: function given X, output fitness of X in context

	population_size = None
	def __init__(self, population_size, individual_size, fitness_function, mutate_function = None):
		self.mutate_function = mutate_function
		self.fitness_function = fitness_function
		self.population_size = population_size
		self.individual_size = individual_size
		self.best = None
		self.best_fitness = None
		initial_population = []
		for i in range(population_size):
			cur = []
			for i in range(individual_size):
				cur.append(random_enc_note())
			initial_population.append(cur)


		self.population = np.array(initial_population)
		print(self.population.shape)






	def train(self, crossover_function, stop_conditions):
		pass




	def resample(self, size = population_size):
		prob = np.apply_along_axis(lambda x : self.fitness_function.eval(x), 1, self.population)
		prob = prob / np.sum(prob)

		print(self.population.shape)
		ns = np.random.choice(np.arange(self.population_size), size, p = prob, replace=True)

		self.population = np.take(self.population, ns, axis = 1)
		print(self.population)


	def mutate(self):
		if self.mutate_function != None:
			self.population = self.mutate_function.mutate(self.population)







