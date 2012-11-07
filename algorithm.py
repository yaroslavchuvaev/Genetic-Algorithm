# -*- coding: UTF-8 -*-

# Модуль описания алгоритма

import random
from fitness import fitness_function

from numeric import *
class algorithm:

	# заданное количество особей в популяции
	pop_size = int()

	# количество родителей, которые участвуют в размножении
	parents_num = int()

	# массив особей (популяция)
	population = []

	# массив пар родителей
	parents = []

	# массив для потомков
	descendants = []

	# иниициализирует начальную популяцию
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

	# селекция 
	def selection(self):
		num = self.parents_num
		i = 0
		self.parents = []
		while i<num:
			parent = []
			parent.append(self.population[i])
			if i+1<num:
				parent.append(self.population[i+1])
			else:
				parent.append(self.population[0])
			self.parents.append(parent)
			i+=2


	# кроссинговер
	def crossingover(self):
		n = 0
		self.descendants = []

		while n < len(self.parents):
			parent1 = float_to_binary(self.parents[n][0]['value'])
			parent2 = float_to_binary(self.parents[n][1]['value'])

			start_cross = random.randint(0,31)
			stop_cross = random.randint(32,63)
			descendant1_chromosome = parent1[:start_cross]+parent2[start_cross:stop_cross]+parent1[stop_cross:]
			descendant2_chromosome = parent2[:start_cross]+parent1[start_cross:stop_cross]+parent2[stop_cross:]

			d1 = {}
			d2 = {}

			d1['value'] = binary_to_float(descendant1_chromosome)
			d2['value'] = binary_to_float(descendant2_chromosome)

			d1['fitness'] = 0
			d2['fitness'] = 0

			self.descendants.append(d1)
			self.descendants.append(d2)
			n += 1

	# мутация
	def mutation(self):
		Fit = fitness_function()

		for x in xrange(0,len(self.descendants)):
			chromosome = float_to_binary( self.descendants[x]['value'])
			gen = random.randint(0,63)

			if chromosome[gen] == '0':
				chromosome = chromosome[:gen] + '1' + chromosome[gen+1:]
			else:
				chromosome = chromosome[:gen] + '0' + chromosome[gen+1:]

			self.descendants[x]['value'] = binary_to_float(chromosome)
			self.descendants[x]['fitness'] = Fit.f(self.descendants[x]['value'])

	# редукция
	def reduction(self):
		Fit = fitness_function()

		for x in xrange(0,len(self.descendants)):
			if self.descendants[x]['value'] > Fit.min and self.descendants[x]['value'] <= Fit.max:
				self.population.append(self.descendants[x])

		self.population.sort(reverse=True)
		self.population = self.population[:self.pop_size]
	

	# определяет максимальное значение в популяции
	def pop_max(self):
		Fit = fitness_function()
		print '####################################################'
		print 'Макс. значение популяции в точке x=',
		print self.population[0]['value']
		print 'f(x)=',
		print self.population[0]['fitness'],' / ',Fit.optium
		print '[ min / max ] [',
		print self.population[-1]['value'],';',self.population[0]['value'],']'
		print '####################################################'
		print
		print



	# выводит текущую популяцию
	def print_population(self):
		for x in xrange(0,self.pop_size):
			print '[',x,']',
			print self.population[x]['value'],'-',
			print self.population[x]['fitness']


