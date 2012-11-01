import os
import algorithm
from fitness import fitness_function


start_population_size = int(
	input('Eneter the size of initial population: '))

Fit = fitness_function()

alg = algorithm(
		start_population_size,
		Fit.limit_min,
		Fit.limit_max)

print alg.population
