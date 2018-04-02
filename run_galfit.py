################################################
# run_galfit.py
#
# Aritra Ghosh
#
# Python script to run GALFIT on created parameter files
#################################################

from multiprocessing import Pool 
import os
import numpy as np


def run_galfit(x):
	command = "~/local_soft/galfit galfit_temp_"+str(x)
	print "~/local_soft/galfit galfit_temp_"+str(x)
	os.system(command)

if __name__ == '__main__':

	NUM_THREADS = 2
	NUM_FILES = 2

	pl = Pool(NUM_THREADS)
	pl.map(run_galfit,range(0,NUM_FILES))
	
	#all(i == 0 for i in exit_codes)

