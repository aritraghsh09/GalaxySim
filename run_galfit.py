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

NUM_THREADS = 15
NUM_FILES = 100000
FILE_PATH = "/net/urry/ag2422/gal_sim_files_0/"

def run_galfit(x):
	command = "~/local_soft/galfit "+FILE_PATH+"galfit_temp_" + str(x) + " > /dev/null 2>&1"
	out = os.system(command)
	return out


if __name__ == '__main__':

	pl = Pool(NUM_THREADS)
	exit_codes = pl.map(run_galfit,range(0,NUM_FILES))

	bool = all(i == 0 for i in exit_codes)
	print bool #if FALSE is printed. Somethin went wrong. Check
