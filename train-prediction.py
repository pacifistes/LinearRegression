#!/usr/bin/python
from __future__ import division
import sys
import csv
# import matplotlib.pyplot as plt
# import numpy as np

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
def writeThetaFile(theta0, theta1):
	try:
		with open('thetas.csv', mode='w+') as csv_file:
			fieldnames = ['theta0', 'theta1']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({fieldnames[0] : theta0, fieldnames[1] : theta1})
	except Exception:
		print 'The params must be a float[2].'
	except IOError:
		print 'The file thetas.csv isn\'t writable.'

# def displayUI(mileageList, priceList, line):
# 		plt.plot(mileageList, priceList, 'ro', label='plop')
# 		plt.plot(line[0], line[1])
# 		plt.xlabel('mileage')
# 		plt.ylabel('price')
# 		plt.show()

def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def iterateTraining(theta0, theta1, dataList):
	learningRate = 0.01
	dataSize = len(dataList)
	errorSum = 0
	errorMultipliedByMileageSum = 0
	for i in range(0, dataSize):
		error = estimatePrice(dataList[i][0], theta0, theta1) - dataList[i][1]
		errorSum += error
		errorMultipliedByMileageSum += (error * dataList[i][0])
	newTheta0 = theta0 - (learningRate * (1 / dataSize)) * errorSum
	newTheta1 = theta1 - (learningRate * (1 / dataSize)) * errorMultipliedByMileageSum
	print 'theta0 = {} ; theta1 = {}'.format(newTheta0, newTheta1)
	return [newTheta0, newTheta1]

# Main
if len(sys.argv) == 2:
	dataList = readCSVFile(sys.argv[1], ',')
	if dataList != None:
		try:
			theta0 = 0
			theta1 = 0
			for iteration in range(0,100):
				theta0, theta1 = iterateTraining(theta0, theta1, dataList)
			# writeThetaFile(theta0, theta1)
			# dataSize = len(dataList)
			# line = []
			# line.append([dataList[0][0], dataList[dataSize-1][0]])
			# line.append([estimatePrice(dataList[0][0], theta0, theta1), estimatePrice(dataList[dataSize-1][0], theta0, theta1)])
			# displayUI(mileageList, priceList, line)
		except Exception:
			print 'Error in the file'
			sys.exit(1)
else:
	print 'Error script : python train-prediction.py file.csv.'