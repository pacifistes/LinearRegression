#!/usr/bin/python
from __future__ import division
from utils import *
import sys
import matplotlib.pyplot as plt

def displayUI(dataList, line):
		plt.plot([data[0] for data in dataList], [data[1] for data in dataList], 'ro')
		plt.plot(line[0], line[1])
		plt.xlabel('mileage')
		plt.ylabel('price')
		plt.show()

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
	return [newTheta0, newTheta1]


def standardizationOfDataList(dataList):
	newDataList = []
	xmin = min(data[0] for data in dataList)
	xmax = max(data[0] for data in dataList)
	ymin = min(data[1] for data in dataList)
	ymax = max(data[1] for data in dataList)
	for data in dataList:
		x = standardize(data[0], xmin, xmax)
		y = standardize(data[1], ymin, ymax)
		newDataList.append([x, y])
	return [newDataList, xmin, xmax, ymin, ymax]

def linearRegression(dataList):
	theta0 = 0.0
	theta1 = 0.0
	thetaPres = 0.000001
	for iteration in range(0,100000000):
		tmpTheta0, tmpTheta1 = iterateTraining(theta0, theta1, dataList)
		if (abs(theta0 - tmpTheta0) < thetaPres and abs(theta1 - tmpTheta1) < thetaPres):
			break;
		theta0 = tmpTheta0
		theta1 = tmpTheta1
	return [theta0, theta1]

# Main
if len(sys.argv) == 2:
	dataList = readCSVFile(sys.argv[1], ',')
	if dataList != None:
		try:
			newDataList, xmin, xmax, ymin, ymax = standardizationOfDataList(dataList)
			theta0, theta1 = linearRegression(newDataList)
			infoList = [theta0, theta1, xmin, xmax, ymin, ymax]
			writeThetaFile(infoList)
			dataSize = len(dataList)
			line = []
			line.append([dataList[0][0], dataList[dataSize-1][0]])
			line.append([estimateFinalPrice(dataList[0][0], infoList), estimateFinalPrice(dataList[dataSize-1][0], infoList)])
			displayUI(dataList, line)
		except Exception:
			print 'Error in the file'
			sys.exit(1)
else:
	print 'Error script : python train-prediction.py file.csv.'