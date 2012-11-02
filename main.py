import os
from algorithm import algorithm



start_population_size = int(input('Eneter the size of initial population: '))

parents_n = int(input('Enter the number of parents, %: '))
	
epochn = int(input('Enter the number of the epoches: '))


alg = algorithm(start_population_size,parents_n)
epoch = 1
#while epoch <= epochn:
	alg.selection()




