#!/usr/bin/python
from __future__ import division
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

# Funtion readThetaFile()
# Params : None
# Return : (float)List[2] : [theta0, theta1] or [0.0, 0.0] if error
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
					print thetaList

				except ValueError, TypeError:
					print 'Variables in the file incorrect.'
			except Exception:
				print 'Error in the file'
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
	return thetaList


# Function readCSVFile
# Params : (String) fileName of the csv file ; (Char) delimiter
# Return : reader object or None if error
def readCSVFile(fileName, delimiter):
	dictionnary = None
	try:
		with open(fileName, mode='r') as csv_file:
			try:
				dictionnary = csv.reader(csv_file, delimiter=delimiter)
			except Exception:
				print 'Error in the file'
	except IOError:
		print 'The file thetas.csv doesn\'t exist or is not readable.'
	return dictionnary

# Function writeThetaFile
# Params : (foat) list[2]
# Return : nothing
def writeThetaFile(thetaList):
	try:
		with open('thetas.csv', mode='w+') as csv_file_writable:
			fieldnames = ['theta0', 'theta1']
			writer = csv.DictWriter(csv_file_writable, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({fieldnames[0] : thetaList[0], fieldnames[1] : thetaList[1]})
	except Exception:
		print 'The params must be a float[2].'
	except IOError:
		print 'The file thetas.csv isn\'t writable.'

def displayUI(mileageList, priceList, xList, yList):
		plt.plot(mileageList, priceList, 'ro', label='plop')
		plt.plot(xList, yList)
		# print xList
		# print yList
		plt.xlabel('mileage')
		plt.ylabel('price')
		plt.show()

def estimatePrice(mileage, theta0, theta1):
	# print '{}|{}|{}|result = {} '.format(theta0, theta1, mileage, theta0 + (theta1 * mileage))
	return theta0 + (theta1 * mileage)


# Main
if len(sys.argv) == 2:
	# thetaList = readThetaFile()
	thetaList = [0, 0]
	readerObject = readCSVFile(sys.argv[1], ',')
	print readerObject
	if readerObject != None:
		try:
			with open(sys.argv[1], mode='r') as csv_file_readable:
				reader = csv.reader(csv_file_readable, delimiter=',')
				next(reader)
				objectList = [[int(row[0]), int(row[1])] for row in reader]
				objectList = sorted(objectList, key=lambda key: key)
				mileageList = [row[0] for row in objectList]
				priceList = [row[1] for row in objectList]
				isIterateOnce = False
				learningRate = 0.01
				precision = 0.001
				test = 0
				dataSize = len(mileageList)

				tmpThetaList = thetaList
				lastThetaList = tmpThetaList
				# print tmpThetaList
				# print thetaList

				while test < 20 :
				# while (isIterateOnce == False or (abs(tmpThetaList[0] - lastThetaList[0]) < precision and abs(tmpThetaList[1] - lastThetaList[1]) < precision)):
					isIterateOnce = True
					foreachTheta0 = 0.0
					foreachTheta1 = 0.0
					lastThetaList = tmpThetaList
					i = 0
					while i < dataSize:
						error = estimatePrice(mileageList[i], tmpThetaList[0], tmpThetaList[1]) - priceList[i]
						print error
						foreachTheta0 += error
						foreachTheta1 += (error * mileageList[i])
						i += 1
					# print foreachTheta0
					# print foreachTheta1
					print 'b0 = {} - {} * {}'.format(tmpThetaList[0], learningRate, foreachTheta0)
					print 'b0 = {} - {} * {}'.format(tmpThetaList[0], learningRate, foreachTheta0)

					tmpThetaList[0] = tmpThetaList[0] - (learningRate * (1 / dataSize)) * foreachTheta0
					tmpThetaList[1] = tmpThetaList[1] - (learningRate * (1 / dataSize)) * foreachTheta1
					print 'theta0 = {} , theta1 = {}'.format(tmpThetaList[0], tmpThetaList[1])
					test += 1


				thetaList = tmpThetaList
				writeThetaFile(thetaList)
				xList = [mileageList[0], mileageList[dataSize - 1]]
				yList = [estimatePrice(mileageList[0], thetaList[0], thetaList[1]), estimatePrice(mileageList[dataSize - 1], thetaList[0], thetaList[1])]
				displayUI(mileageList, priceList, xList, yList)
		except Exception:
			print 'Error in the file'
			sys.exit(1)
else:
	print 'Error script : python train-prediction.py file.csv.'