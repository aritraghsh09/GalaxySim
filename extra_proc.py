#############################################
#   extra_proc.py
#
#   Aritra Ghosh
#
#   This script is meant to do extra processing to all the simulated images -- Convolve with the suitable PSF--add the noise and redshift them with FERENGI
############################################

import numpy as np
import pylab as plt
import tqdm
from astropy.io import fits
from multiprocessing import Pool
from astropy.convolution import convolve

dataReadPath = '/net/urry/ag2422/gal_sim_runs/gal_sim_images_6/'
dataWritePath = '/net/urry/ag2422/gal_sim_runs/gal_sim_images_6_convolved/'

NUM_FILES_TOTAL = 100000
NUM_THREADS = 15

def convolve_psf(i):
	img_data = fits.getdata(dataReadPath+"output_img_"+str(i)+".fits",memmap=False)
	psf_data = fits.getdata("/net/urry/ag2422/powell_17_data/GOODSN_ACS_cutouts/goodss_3dhst.v4.0.F775W_psf.fits",memmap=False)
	convolved_data = convolve(img_data,psf_data)
	
	hdu = fits.PrimaryHDU(convolved_data)
	hdu.writeto(dataWritePath+"output_img_"+str(i)+".fits",overwrite=True) 
	# !!!! --- if you want to replace the exisiting file -- replace the name with the same name as that of the existing file and also add overwrite=True
	del hdu #to avoid garbage collection issues 

if __name__ == '__main__':

	pl = Pool(NUM_THREADS)
	#pl.map(convolve_psf,range(0,NUM_FILES_TOTAL))

	#if you don't want this just replace this with the previous line
	#this next line does the same thing as the pool call above, but now with a progress bar
	for _ in tqdm.tqdm(pl.imap_unordered(convolve_psf,range(0,NUM_FILES_TOTAL)), total=NUM_FILES_TOTAL):
    		pass

