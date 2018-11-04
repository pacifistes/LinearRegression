#!/usr/bin/python
import sys
import csv

# Funtion readThetaFile()
# Params : None
# Return : List[2] : [theta0, theta1] or [0, 0] if error
def readThetaFile():
	thetaList = [0, 0]
	try:
		with open('thetas.csv', mode='r') as csv_file:
			try:
				csv_reader = csv.DictReader(csv_file)
				row = next(csv_reader)
				try:
					theta0 = float(row["theta0"])
					theta1 = float(row["theta1"])
					thetaList = [theta0, theta1]
				except ValueError, TypeError:
					print 'Variables in the file incorrect.'
			except Exception:
				print 'Error in the file'
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
	return thetaList


# Main
if len(sys.argv) == 2:
	try:
		mileage = int(sys.argv[1])
	except ValueError:
		print 'Error script : python prediction.py mileage.'
		sys.exit(1)
	thetaList = readThetaFile();
	result = thetaList[0] + (thetaList[1] * mileage)
	if result < 0:
		result = 0
	print 'price of the car with {}km : {}.'.format(mileage, result
else:
	print 'Error script : python prediction.py mileage.'