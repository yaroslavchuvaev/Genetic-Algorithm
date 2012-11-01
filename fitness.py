import math

class fitness_function:
	limit_min = 0
	limit_max = 17

	def f(self,x):
		y = x/10 + math.cos(x)
		return y