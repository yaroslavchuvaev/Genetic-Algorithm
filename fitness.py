# -*- coding: UTF-8 -*-

# модуль для описания фитнес-функции 

import numpy as np

class fitness_function:
	min = 0 							# начало интервала
	max = 17							# конец интервала
	optium = 2.26164124066				# экстремум, найденный линейным поиском

	# определение функции
	def f(self,x):
		y = x/10 + np.cos(x)
		return y
