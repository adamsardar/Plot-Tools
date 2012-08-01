#!/usr/bin/env python

#Copyright 2012 Gough Group, University of Bristol.
#AUTHOR: Adam Sardar (adam.sardar@bris.ac.uk)


# Force matplotlib to not use any Xwindows backend.
import matplotlib
matplotlib.use('Agg')

import numpy as np
import pylab as pl
import sys
import argparse
import math

def main():

	parser = argparse.ArgumentParser(description='Produce histogram plots from input data using Matplot lib. requires the numpy, pylab  and argparse modules to be instlaled.')
		
	parser.add_argument('--file', '-f', metavar='FILE', required=True, type=argparse.FileType('r'), dest='InputFile', help='File of data that you wish to turn into a histogram')
	parser.add_argument('--output', '-o', metavar='OUTPUT', required=True, dest='Output', type=argparse.FileType('w'), help='Output image file (with file extension) - e.g Hist.png')
	parser.add_argument('--bins', '-b', metavar='BINS', required=False, dest='binsize', type=int, default=75, help='Number of bins in output image (default is 75)')
	
	parser.add_argument('--color', '-c', metavar='COLOR', required=False, dest='colour', type=str, default='#7D7D7D', help='Color of output histogram. Use HTML colours - e.g. #00FFFF for cyan')
	parser.add_argument('--title', '-t', metavar='TITLE', required=False, dest='title', type=str, default='Hisogram Of Data', help='Title of plot')
	parser.add_argument('--xlab', '-x', metavar='X_LABEL', required=False, dest='x_lab', type=str, default='Value', help='Label for the x-axis')
	
	parser.add_argument('--ylab', '-y', metavar='Y_LABEL', required=False, dest='y_lab', default='Frequency', type=str, help='Label for the y-axis')
	parser.add_argument('--delim', '-d', metavar='FILE_DELIMITER', required=False, dest='delim', default=':', type=str, help='Delimiter carachter in input file (defualt is :)')
	parser.add_argument('--label', '-l', metavar='DATA_LABEL', required=False, dest='label', type=str, default='data', help='Label data key')

	parser.add_argument('--ylimmax', metavar='Y_LIM_MAX', required=False, dest='ylimmax', type=float, help='A maximum value to set the plot y scale to')
	parser.add_argument('--xlimmax', metavar='X_LIM_MAX', required=False, dest='xlimmax', type=float, help='A maximum value to set the plot x scale to')

	parser.add_argument('--column', '-u', metavar='DATA_COLUMN', required=False, dest='column', type=int, default=1, help='Column to use of data file')
	parser.add_argument('--vline', metavar='VERTICAL_LINE', required=False, default=None, dest='vline', type=float, help='Adds a vertical line to plot at point on the x-axis')

	parser.add_argument('--log', required=False, dest='log', action='store_true', help='Log (natural base) transform the input data')
	parser.add_argument('--exp', required=False, dest='exp', action='store_true', help='Exponential (e^x) transform the input data')

	parser.add_argument('--xmax', metavar='MAXIMUM X VALUE', required=False, default=None, dest='xmax', type=float, help='The largest x value to include in the histogram. Note, you must also specify xmin')
	parser.add_argument('--xmin', metavar='MINIMUM X VALUE', required=False, default=None, dest='xmin', type=float, help='The smallest x value to include in the histogram. Note, you must also specify xmax')

	args = parser.parse_args()

	x=[]
	#x will be out data array
	for line in args.InputFile:
		
		RawData = line.split(eval('"'+args.delim+'"'))	
		
		if len(RawData)-1 < args.column:
			print "Delimiter is: "+args.delim
			print >> sys.stderr, "You have specified a data column number greater than the number of columns in the input file. Are you sure that the seperator carachter is set aprropriately?"
			sys.exit()	
		try:
			float(RawData[args.column])
		except ValueError:
			print >> sys.stderr, "Issues with your input file %s is not coercible into a float" % RawData[args.column].rstrip('\r\n')
			sys.exit()
		if args.log and float(RawData[args.column]) == 0:
			print >> sys.stderr, "Data value of 0 found. This is not allowed if you wish to log transform the data"
			sys.exit()	
		x.append(float(RawData[args.column]))

	
	if(args.log):
		x = [math.log(item) for item in x]
		
	if(args.exp):
		x = [math.exp(item) for item in x]
		
	if args.xmax is not None and args.xmin is not None:
		pl.hist(x, bins=args.binsize, range=(args.xmin,args.xmax),facecolor=args.colour,label=args.label)
	else:
		pl.hist(x, bins=args.binsize,facecolor=args.colour,label=args.label)
		#If wither args.xmax or xmin are not defined
		
	
	pl.xlabel(args.x_lab) ; pl.ylabel(args.y_lab) 
	pl.legend(loc='upper left')
	pl.title(args.title)
			# make a histogram

	if args.vline is not None:
		pl.axvline(linewidth=2, color='r',x=args.vline)
		
	if args.ylimmax is not None:
		pl.ylim((0,args.ylimmax))	

	if args.xlimmax is not None:
		pl.xlim((0,args.xlimmax))	
	
	# save the image to hardcopy
	pl.savefig(args.Output)

if __name__ == "__main__":
	main()
