import random
from fitness import fitness_function

from numeric import *
class algorithm:

# the size of population
	pop_size = int()

# the size of tournament group
	parents_num = int()

# array for the current population
	population = []

	parents = []

# initialize the first population and fitness calculation
	def __init__(self,size,parents_n): 
		self.pop_size = size

		if parents_n > 100:
			parents_n = 100

		self.parents_num = parents_n
		while size > 0:
			Fit = fitness_function() 
			person = {}
			person['value'] = Fit.min + random.random() * (Fit.max-Fit.min)
			person['fitness'] = Fit.f(person['value'])
			size -= 1
			self.population.append(person)
			self.population.sort(reverse=True)

# selection
	def selection(self):
		self.parents = self.population[0:self.pop_size/100*self.parents_num]


# crossingover

# mutation



# print the current population
	def print_population(self,arr):
		for x in xrange(0,self.pop_size):
			print '[',x,']',
			print self.population[x]['value'],'-',
			print self.population[x]['fitness']


