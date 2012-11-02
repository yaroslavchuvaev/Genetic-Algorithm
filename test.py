from fitness import *

Fit = fitness_function()

i = Fit.min
max = -100000
while i<Fit.max:
	c = Fit.f(i)
	if c > max:
		max = c
	i=i+0.000001
print max