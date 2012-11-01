import random

class algorithm:

	population = []

	def __init__(size,min,max):
		while size > 0:
			person = min + random.random() * (max-min)
			size = size -1
			population.append(person)


