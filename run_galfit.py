################################################
# run_galfit.py
#
# Python script to run GALFIT on created parameter files
#################################################

from multiprocessing import Pool 
import os
import numpy as np
import time
import pickle

NUM_FILES = 2
NUM_THREADS = 1
#FILE_PATH = "/net/urry/ag2422/gal_sim_files_0/"
FILE_PATH = "./"

def run_galfit(x):
	command = "~/local_soft/galfit "+FILE_PATH+"galfit_temp_" + str(x) + " > /dev/null 2>&1" #Suppresses Screen I/O. Remove the end-part if you don't want this. 
	out = os.system(command)
	return out


if __name__ == '__main__':

	start_timestamp = time.time()
	
	pl = Pool(NUM_THREADS)
	exit_codes = pl.map(run_galfit,range(0,NUM_FILES))

	bool = all(i == 0 for i in exit_codes)
	
	if bool == True:
		print("All seems to have gone well!!")
	else:
		print("Some Images may have some issues")
		pickle_file = open("exit_codes.pkl","w")
		pickle.dump(exit_codes,pickle_file)
		print("Dumped Array of Exit Codes as a pickle.Check for non-zero exit codes.")		


	print("Real Time of Execution:- %s seconds" % (time.time() - start_timestamp) )
