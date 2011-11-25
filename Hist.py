#! /usr/local/bin/sage --python
#Using the sage implementation of python for nice easy access to scilab and matlibplot etc

# Hist.py -f inputdata as colon seperated file -o Outputpath(with file extension) -t "Hist title" -x "xlabel" -y "ylabel"

import numpy as np
import pylab as pl
import sys
import getopt

def main(argv):

	(binsize,colour,title,x_lab,y_lab,delim,label,column) = (75,'#7D7D7D','Hisogram Of Data','Value','Frequency',':','data',1)

	try:
		opts, args = getopt.getopt(argv, "f:o:b:c:t:x:y:d:l:u", ["File=", "Output=","bins=","colour=","title=","xlab=","ylab=","delim=","label=","column="])	
	except getopt.GetoptError:
		print "Input and Output filenames required along with data label"
		exit(2)
	
	for opt, arg in opts:
		if opt in ('-f','--File'):
			InputFile = arg
		elif opt in ('-o','--Output'):
			Output = arg
		elif opt in ('-b','--bins'):
			binsize = int(arg)
		elif opt in ('-c','--colour'):
			colour = arg
		elif opt in ('-t','--title'):
			title = arg
		elif opt in ('-x','--xlab'):
			x_lab = arg
		elif opt in ('-y','--ylab'):
			y_lab = arg
		elif opt in ('-d','--delim'):
			delim = arg
		elif opt in ('-l','--label'):
			label = arg
		elif opt in ('-u','--column'):
			column = int(arg)

	
	RawData = np.recfromcsv(InputFile,delimiter=delim)
	x = [tuple[column] for tuple in RawData]

	pl.hist(x, bins=binsize,color=colour,label=label)
	pl.xlabel(x_lab) ; pl.ylabel(y_lab) 
	pl.legend(loc='upper left')
	pl.title(title)
	# make a histogram

	# save the image to hardcopy
	pl.savefig(Output)

if __name__ == "__main__":
	main(sys.argv[1:])
