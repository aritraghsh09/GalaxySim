#############################################
#   extra_proc.py
#
#   Aritra Ghosh
#
#   This script is meant to do extra processing to all the simulated images -- Convolve with the suitable PSF--add the noise.
############################################

import numpy as np
import pylab as plt
import tqdm
from astropy.io import fits
from multiprocessing import Pool
from astropy.convolution import convolve

dataReadPath = '/net/urry/ag2422/gal_sim_runs/gal_sim_images_13/'
dataWritePath = '/net/urry/ag2422/gal_sim_runs/gal_sim_images_13_extra_proc/'
psfFilePath = '/net/urry/ag2422/candels_cutouts/model_psf/vdwel_2012_psf/COSMOS/psfH.fits'
noiseFilePath = '/net/urry/ag2422/noise_images/candels_noise/noise_egs.npy'

NUM_FILES_TOTAL = 100000
NUM_THREADS = 15
IMG_WIDTH = IMG_HEIGHT = 83 #No of pixels length/width -wise in each cutout

noise = np.load(noiseFilePath)

def psf_and_noise(i):
	img_data = fits.getdata(dataReadPath+"output_img_"+str(i)+".fits",memmap=False)
	psf_data = fits.getdata(psfFilePath, memmap=False)
	convolved_data = convolve(img_data,psf_data,boundary='extend')
	final_data = convolved_data + np.random.choice(noise,size=(IMG_WIDTH,IMG_HEIGHT))	

	hdu = fits.PrimaryHDU(final_data)
	hdu.writeto(dataWritePath+"output_img_"+str(i)+".fits",overwrite=True) 
	# !!!! --- if you want to replace the exisiting file -- replace the name with the same name as that of the existing file and also add overwrite=True
	del hdu #to avoid garbage collection issues 




pl = Pool(NUM_THREADS)
pl.map(psf_and_noise,range(0,NUM_FILES_TOTAL))

#if you don't want this just replace this with the previous line
#this next line does the same thing as the pool call above, but now with a progress bar
#for _ in tqdm.tqdm(pl.imap_unordered(psf_and_noise,range(0,NUM_FILES_TOTAL)), total=NUM_FILES_TOTAL):
#	pass


