import math

class fitness_function:
	min = 0
	max = 17

	def f(self,x):
		y = x/10 + math.cos(x)
		return y