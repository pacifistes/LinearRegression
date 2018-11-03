#!/usr/bin/python
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

try:
	with open(sys.argv[1], mode='r') as csv_file_readable:
		try:
			reader = csv.reader(csv_file_readable, delimiter=',')
			print reader
			next(reader)
			# dictionnary = [[int(row[0]), int(row[1])] for row in reader]
			# dictionnary = sorted(dictionnary, key=lambda key: key)
			# mileage = [row[0] for row in dictionnary]
			# price = [row[1] for row in dictionnary]
			# plt.plot(mileage, price, 'ro', label='plop')
			# plt.xlabel('mileage')
			# plt.ylabel('price')
			# x = 1
			# y = 1
			# iteration = 0
			# maxIteration = 20

			# theta0 = 0
			# theta1 = 0				
			# tmptheta1 = 0.0
			# while iteration < maxIteration:
			# 	learningRate = 0.1
			# 	error = (tmptheta0 + (tmptheta1 * x)) - y
			# 	tmptheta0 = tmptheta0 - learningRate * error
			# 	tmptheta1 = tmptheta1 - learningRate * error * x
			# 	print 'theta0 = {} , theta1 = {}'.format(tmptheta0, tmptheta1)
			# 	iteration += 1
			# plt.show()

			# with open('thetas.csv', mode='w+') as csv_file_writable:
			# 	fieldnames = ['theta0', 'theta1']
			# 	writer = csv.DictWriter(csv_file_writable, fieldnames=fieldnames)
			# 	writer.writeheader()
			# 	writer.writerow({fieldnames[0] : theta0, fieldnames[1] : theta1})
		except Exception:
			print 'Error in the file'
#				print 'theta0 = {} , theta1 = {}'.format(row["theta0"], row["theta1"])
except IOError:
	print 'The file thetas.csv doesn\'t exist or is not readable or writable.'