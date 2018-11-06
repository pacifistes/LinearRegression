#!/usr/bin/python
from __future__ import division
import csv

# Function readCSVFile
# Params : (String) fileName of the csv file ; (Char) delimiter
# Return : reader object or None if error
def readCSVFile(fileName, delimiter):
	dataList = None
	try:
		with open(fileName, mode='r') as csv_file:
			try:
				dictionnary = csv.reader(csv_file, delimiter=delimiter)
				next(dictionnary)
				dataList = [[int(data[0]), int(data[1])] for data in dictionnary]
				dataList = sorted(dataList, key=lambda key: key)
			except Exception:
				print 'Error in the file'
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
	return dataList

# Function writeThetaFile
# Params : (foat) list[2]
# Return : nothing
def writeThetaFile(infoList):
	try:
		with open('thetas.csv', mode='w+') as csv_file:
			fieldnames = ['theta0', 'theta1', 'xmin', 'xmax', 'ymin', 'ymax']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			dictionnary = {}
			for i in range(0, len(infoList)):
				dictionnary.update({fieldnames[i] : infoList[i]})
			writer.writerow(dictionnary)
	except Exception:
		print 'The params must be a float[2].'
	except IOError:
		print 'The file thetas.csv isn\'t writable.'

def standardize(value, minValue, maxValue):
	if minValue - maxValue == 0:
		return 0
	return (value - minValue) / (maxValue - minValue)

def estimateFinalPrice(mileage, infoList):
	theta0 = infoList[0]
	theta1 = infoList[1]
	xmin = infoList[2]
	xmax = infoList[3]
	ymin = infoList[4]
	ymax = infoList[5]
	mileage = standardize(mileage, xmin, xmax)
	price = theta0 + (theta1 * mileage)
	price = ((price * (ymax - ymin)) + ymin)
	if price < 0:
		price = 0
	return int(price)

# Funtion readThetaFile()
# Params : None
# Return : List[2] : [theta0, theta1] or [0, 0] if error
def readThetaFile():
	infoList = [0, 0, 0, 0, 0, 0]
	try:
		with open('thetas.csv', mode='r') as csv_file:
			try:
				csv_reader = csv.DictReader(csv_file)
				row = next(csv_reader)
				try:
					theta0 = float(row["theta0"])
					theta1 = float(row["theta1"])
					xmin = float(row["xmin"])
					xmax = float(row["xmax"])
					ymin = float(row["ymin"])
					ymax = float(row["ymax"])
					infoList = [theta0, theta1, xmin, xmax, ymin, ymax]
				except ValueError, TypeError:
					print 'Variables in the file incorrect.'
			except Exception:
				print 'Error in the file'
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
	return infoList
