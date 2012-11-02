import os
from algorithm import algorithm



start_population_size = int(input('Eneter the size of initial population: '))
parents_n = -100
while parents_n <= 0 or parents_n > start_population_size:
	parents_n = int(input('Enter the number of parents in population (0<parents<size_of_initial): '))
	
epochn = int(input('Enter the number of the epoches: '))


alg = algorithm(start_population_size,parents_n)
epoch = 0
while epoch < epochn:
	print 'Epoch #',epoch
	alg.pop_max()
	alg.selection()
	alg.crossingover()
	alg.mutation()
	alg.reduction()
	epoch += 1




