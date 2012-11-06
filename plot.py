import numpy as np
import matplotlib.pyplot as plt
from fitness import *

class plot:
	
	

	def __init__(self):
		plt.ion()
		plt.figure(1)
		
	def get_dx(self,population):
		px = []
		for x in range(len(population)):
			if 0 < population[x]['value'] < 17:
				px.append(population[x]['value'])
		return px

	def get_dy(self,population):
		py = []
		for y in range(len(population)):
			if 0 < population[y]['value'] < 17:
				py.append(population[y]['fitness'])
		return py

	def get_x(self,population):
		px = []
		for x in range(len(population)):
			px.append(population[x]['value'])
		return px

	def get_y(self,population):
		py = []
		for y in range(len(population)):
			py.append(population[y]['fitness'])
		return py

	def plot(self,population,descendants):
		
		plt.clf()
		Fit = fitness_function()
		t = np.arange(Fit.min,Fit.max,0.01)
		

		x = self.get_x(population)
		y = self.get_y(population)

		dx = self.get_dx(descendants)
		dy = self.get_dy(descendants)				

		plt.subplot(211)
		plt.plot(t,Fit.f(t),'b-', dx,dy,'or', x,y,'og')

		plt.draw()