#############################################
#   extra_proc.py
#
#   Aritra Ghosh
#
#   This script is meant to do extra processing to all the simulated images -- Convolve with the suitable PSF--add the noise and redshift them with FERENGI
############################################

import numpy as np
import pylab as plt
from astropy.io import fits
import math
import time
from multiprocessing import Pool
from astropy.convolution import convolve

dataPath = '/gpfs/loomis/project/fas/urry/ag2422/data/gal_sim_images_0/'

NUM_FILES_TOTAL = 55000
NUM_THREADS = 10

