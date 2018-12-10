#!/usr/bin/python
from __future__ import division
from utils import *
import sys

# Main
if len(sys.argv) == 2:
	try:
		mileage = int(sys.argv[1])
	except ValueError:
		print 'Error script : python prediction.py mileage.'
		sys.exit(1)
	infoList = readThetaFile();
	result = estimateFinalPrice(mileage, infoList)
	print 'price of the car with {}km : {} ({}).'.format(mileage, int(result), result)
else:
	print 'Error script : python prediction.py mileage.'