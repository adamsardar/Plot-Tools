#!/usr/bin/python

#Copyright 2012 Gough Group, University of Bristol.
#AUTHOR: Adam Sardar (adam.sardar@bris.ac.uk)

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
	
	parser.add_argument('--column', '-u', metavar='DATA_COLUMN', required=False, dest='column', type=int, default=1, help='Column to use of data file')
	parser.add_argument('--vline', metavar='VERTICAL_LINE', required=False, dest='vline', type=float, help='Adds a vertical line to plot at point on the x-axis')
	parser.add_argument('--log', required=False, dest='log', action='store_true', help='Log (natural base) transform the input data')

	args = parser.parse_args()
	
	RawData = np.recfromtxt(args.InputFile,delimiter=args.delim)

	if(args.log):
		x = [math.log(tuple[args.column]) for tuple in RawData]
	else:
		x = [tuple[args.column] for tuple in RawData]
		
	pl.hist(x, bins=args.binsize,facecolor=args.colour,label=args.label)
	pl.xlabel(args.x_lab) ; pl.ylabel(args.y_lab) 
	pl.legend(loc='upper left')
	pl.title(args.title)
	# make a histogram
	
	try:
		args.vline
		pl.axvline(linewidth=2, color='r',x=args.vline)
	except NameError:
		args.vline = 'none'
		
	# save the image to hardcopy
	pl.savefig(args.Output)

if __name__ == "__main__":
	main()
