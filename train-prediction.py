#!/usr/bin/python
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) == 2:
	file_name = sys.argv[1]
	try:
		with open(file_name, mode='r') as csv_file_readable:
			try:
				csv_reader = csv.DictReader(csv_file_readable)
				dictionnaryList = sorted(csv_reader, key=lambda row:(row['km']))
				mileage = []
				price = []
				for row in dictionnaryList:
					mileage.append(row['km'])
					price.append(row['price'])
				plt.plot(mileage, price, 'ro', label='plop')
				plt.xlabel('mileage')
				plt.ylabel('price')
				plt.show()
				theta0 = 0
				theta1 = 0
				with open('thetas.csv', mode='w+') as csv_file_writable:
					fieldnames = ['theta0', 'theta1']
					writer = csv.DictWriter(csv_file_writable, fieldnames=fieldnames)
					writer.writeheader()
					writer.writerow({fieldnames[0] : theta0, fieldnames[1] : theta1})
			except Exception:
				print 'Error in the file'
#				print 'theta0 = {} , theta1 = {}'.format(row["theta0"], row["theta1"])
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable or writable.'
else:
	print 'Error script : python train-prediction.py file.csv.'