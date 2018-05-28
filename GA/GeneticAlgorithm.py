# TODO: get model working before attempting- to solve problems with encoding
from GA.utils import *
import pickle
CROSSOVER_POPULATION = .1

class GA:
	#initial_population: iterable with elements parsable by fitness_function
	#popution_size: integer denoting size of each generation
	#fitness_function: function given X, output fitness of X in context

	def __init__(self, population_size, individual_size, fitness_function, crossover_function= None, mutate_function = None):
		self.crossover_function = crossover_function
		self.mutate_function = mutate_function
		self.fitness_function = fitness_function
		self.population_size = population_size
		self.individual_size = individual_size
		self.best = None
		self.best_fitness = float("-inf")
		initial_population = []
		for i in range(population_size):
			cur = []
			for i in range(individual_size):
				cur.append(random_enc_note())
			initial_population.append(cur)


		self.population = np.array(initial_population)






	def train(self,iterations=500, save_every=1000, save_filepath = "out.pickle"):

		training_iterations = 0
		while True:
			self.cross_over()
			if not isinstance(self.best, type(None)):
				self.population = np.vstack((self.population, self.best))
			self.resample(self.population_size)
			self.mutate()

			if training_iterations % save_every == 0:
				with open(save_filepath, 'wb') as handle:
					pickle.dump(self.best, handle, protocol=pickle.HIGHEST_PROTOCOL)

			if training_iterations % 10 == 0:
				print("FITNESS SCORE: " + str(self.best_fitness), "ITERATIONS: " + str(training_iterations))
			# print(self.population.shape)

			if iterations == -1:
				continue
			elif training_iterations >= iterations:
				break
			# INC Counter
			training_iterations+= 1




	def resample(self, size, choose_best_proportion = .5):
		prob = np.apply_along_axis(lambda x : self.fitness_function.eval(x), 1, self.population)
		prob[prob < 0] = 0
		best_arr = np.argmax(prob, axis= 0)
		if self.best_fitness == None:
			self.best_fitness = prob[best_arr]
			self.best = self.population[int(best_arr)]
		elif self.best_fitness < prob[best_arr]:
			self.best_fitness = prob[best_arr]
			self.best = self.population[int(best_arr)]

		prob = prob / np.sum(prob)

		num_best = int(choose_best_proportion * size)
		rest = size - num_best
		ns = np.random.choice(np.arange(len(self.population)), num_best , p = prob, replace=True)
		other = np.random.choice(np.arange(len(self.population)), rest , replace=False)
		ns = np.concatenate((ns, other))

		self.population = self.population[ns]


	def mutate(self):
		if self.mutate_function != None:
			self.population = self.mutate_function.mutate(self.population)


	def cross_over(self):
		if self.crossover_function != None:
			self.population = self.crossover_function.cross(self.population)







