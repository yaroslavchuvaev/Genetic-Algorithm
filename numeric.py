# -*- coding: UTF-8 -*-

# преобразует целое в двоичное представление
def int_to_binary(int_num):
	n = ""
	while int_num > 0:
		y = str(int_num % 2)
		n = y+n 
		int_num /= 2
	diff = 32 - len(n)
	for x in xrange(0,diff):
		n = '0'+n
	return n

# преобразует число с плавающей точкой в двоичное представление 
def float_to_binary(float_num):
	parts = str(float_num).split('.')
	int_n = int_to_binary(int(parts[0]))
	float_n = int_to_binary(int(parts[1]))
	zeros = 32 - len(float_n)
	for x in xrange(0,zeros):
		float_n += '0'
	return int_n + float_n

# преобразует двоичное представление в целое число
def binary_to_int(binary):
	return int(binary,2)

# преобразует двоичное представление в число с плавающей точкой
def binary_to_float(binary):
	int_part = binary_to_int(binary[:32])#0-31 - int
	float_part = binary_to_int(binary[32:])#32-63 - float
	n = str(int_part)+'.'+str(float_part)
	return float(n)