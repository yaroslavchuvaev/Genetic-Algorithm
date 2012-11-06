# -*- coding: UTF-8 -*-

# Главный модуль 

import os
from algorithm import algorithm
from plot import plot


start_population_size = int(input('Eneter the size of initial population: '))
parents_n = -100
while parents_n <= 0 or parents_n > start_population_size:
	parents_n = int(input('Enter the number of parents in population (0<parents<size_of_initial): '))
	
epochn = int(input('Enter the number of the epoches: '))


alg = algorithm(start_population_size,parents_n)
epoch = 0
p = plot()

while epoch <= epochn:
	p.plot(alg.population,alg.descendants)
	print 'Epoch #',epoch
	alg.pop_max()
	alg.selection()
	alg.crossingover()
	alg.mutation()
	alg.reduction()
	
	epoch += 1




