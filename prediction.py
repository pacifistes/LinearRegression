#!/usr/bin/python
import sys
import csv

if len(sys.argv) == 2:
	try:
		mileage = int(sys.argv[1])
	except ValueError:
		'Error script : python prediction.py mileage.'
		sys.exit()
	try:
		with open('thetas.csv', mode='r') as csv_file:
			try:
				csv_reader = csv.DictReader(csv_file)
				row = next(csv_reader)
				try:
					theta0 = int(row["theta0"])
					theta1 = int(row["theta1"])
					print 'price of the car with {}km : {}.'.format(mileage, theta0 + (theta1 * mileage))
				except ValueError, TypeError:
					print 'Variables in the file incorrect.'
			except Exception:
				print 'Error in the file'
#				print 'theta0 = {} , theta1 = {}'.format(row["theta0"], row["theta1"])
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
else:
	print 'Error script : python prediction.py mileage.'