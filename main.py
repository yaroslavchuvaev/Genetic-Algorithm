# -*- coding: UTF-8 -*-

# Главный модуль 

import os
from algorithm import algorithm
from plot import plot

start_population_size = -1
while start_population_size < 2:
	start_population_size = int(input('Введите размер начальной популяции(не меньше чем 2): '))
parents_n = -100
while parents_n < 2 or parents_n > start_population_size:
	parents_n = int(input('Введите число особей, участвующих в размножении (2<=родители<=нач.попул.): '))
	
epochn = int(input('Введите число эпох(смен популяций): '))
print ('Подготовка начальной популяции, подождите...')

alg = algorithm(start_population_size,parents_n)

print 'Популяция готова, нажмите [Enter], чтобы начать оптимизацию'
raw_input()

epoch = 0
p = plot()

while epoch <= epochn:
	p.plot(alg.population,alg.descendants)
	print 'Эпоха #',epoch
	alg.pop_max()
	alg.selection()
	alg.crossingover()
	alg.mutation()
	alg.reduction()
	
	epoch += 1
print 'Конец эволюции'
raw_input()




