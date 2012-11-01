import random
from fitness import fitness_function

#from 
class algorithm:

# the size of population
	pop_size = int()
# array for the current population
	population = []

# initialize the first population
	def __init__(self,size,min,max): 
		self.pop_size = size
		while size > 0:
			Fit = fitness_function()
# find the random value and it's fitness valued 
			person = {}
			person['value'] = min + random.random() * (max-min)
			person['fitness'] = Fit.f(person['value'])
			size -= 1
			self.population.append(person)
			self.population.sort(reverse=True)

# print the current population
	def print_population(self):
		for x in xrange(0,self.pop_size):
			print '[',x,']',
			print self.population[x]['value'],'-',
			print self.population[x]['fitness']

