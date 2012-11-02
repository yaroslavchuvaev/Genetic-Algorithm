import math

class fitness_function:
	min = 0
	max = 17
	optium = 2.26164124066

	def f(self,x):
		y = x/10 + math.cos(x)
		return y