#! /usr/bin/python

import numpy as np
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():

	#Define the command line options	
	
	parser = argparse.ArgumentParser(description="A simple line plotting script")

	parser.set_defaults(colours=[])
	parser.set_defaults(sep=",")

	parser.add_argument("-f", "--input", dest="inputfile", help="Define the SEP seperated file used as input")
	parser.add_argument("-o", "--output", dest="outputfile", help="Define the file (with extension) which to save output to")
	parser.add_argument("--xlab",  dest="xlab", help="define a label for the x axis")
	parser.add_argument("--ylab",  dest="ylab", help="define a label for the y axis")
	parser.add_argument("-t", "--title",  dest="title", help="define a title for the plot")
	parser.add_argument("-s", "--seperator", dest="sep", default=",", help="Define SEP, the seperator in the input file (default is ',')")
	parser.add_argument("-x", "--xfields",  dest="xfields", action='append', type=int, help="row indicies to be used as x values (each individual value is appenended to a list)")
	parser.add_argument("-y", "--yfields",  dest="yfields", action='append', type=int, help="row indicies to be used as y values (each individual value is appenended to a list) (must be same size as xfields)")
	parser.add_argument("--legend",  dest="legend",  action='append', help="add legend to plot")
	parser.add_argument("--legend_placement",  dest="legplace", type=int,help="specify legend placement as a numeric code (see matplot lib webpages for details)")
	parser.add_argument("-c", "--colours",  dest="colours", action='append', help="colours to be used for lines (each individual value is appenended to a list) (must be same size or larger than xfields) (default is black, red, blue, green, yellow)")
		
	#grab options
	args = parser.parse_args()
	
	if (not len(args.colours[:])):
		args.colours=['k','r','b','g','y']
	#Set default colours if unasssinged
			
	finput = open(args.inputfile,'r+')
	
	InputData = []
	#This will become a 2D list of the input file

	for line in finput:
		 InputData.append(line.split(args.sep))
	
	DataArray = np.array(InputData)
	#An array of doubles, extracted from the input file

	fig = plt.figure()
	
	for index in range(0,len(args.xfields)):

		xcolumn = args.xfields[index]
		ycolumn = args.yfields[index]
		colour = args.colours[index]
		plt.plot(DataArray[:,xcolumn],DataArray[:,ycolumn],colour)

	if (args.xlab):
		plt.xlabel(args.xlab)
	if (args.ylab):
		plt.ylabel(args.ylab)
	if (args.title):
		plt.title(args.title)
	if (args.legend):
		if (args.legplace):	
			plt.legend(args.legend, shadow=True, loc=args.legplace)
		else:
			plt.legend(args.legend, shadow=True)
	
	# save the image to hardcopy
	plt.savefig(args.outputfile)

if __name__ == "__main__":
	main()
