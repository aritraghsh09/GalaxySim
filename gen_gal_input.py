############################################
#  gen_gal_template.py
# 
#  Aritra Ghosh
#
#  A python script to generate GalSim Template files
#############################################

for i in range(1,3):
	
	template_file = open('galfit_temp_'+str(i),'w')

	template_file.write("===============================================================================\n")

	#File parameters	
	template_file.write("A) gal.fits\n")  # Input data image (FITS file)
	template_file.write("B) output_img_"+str(i)+".fits"+"\n") # Output data image block
	template_file.write("C) none\n") #Sigma Image
	template_file.write("D) none\n") #PSF
	template_file.write("E) 1\n") #PSF fine sampling factor relative to data
	template_file.write("F) none\n")
	template_file.write("G) none\n")
	template_file.write("H) 1 93 1 93\n") #Image region to fit (xmin xmax ymin ymax)
	template_file.write("I) 100 100\n") #Size of the convolution box (x y)
	template_file.write("J) 26.563\n") # Magnitude photometric zeropoint 
	template_file.write("K) 0.038 0.038\n") # Magnitude photometric zeropoint 
	template_file.write("O) regular\n") # Display type (regular, curses, both)
	template_file.write("P) 1\n\n") # Choose: 0=optimize, 1=model, 2=imgblock, 3=subcomps
	
	#Object number 1
	template_file.write(" 0) sersic\n") #object type
	template_file.write(" 1) 48.5180 51.2800 0 0\n")#position x y
	template_file.write(" 3) 20.0890 0\n")#Integrated Magnitude
	template_file.write(" 4) 5.1160 0\n")#R_e (half-light radius)   [pix]
	template_file.write(" 5) 4.2490 0\n")#Sersic index n (de Vaucouleurs n=4)
	template_file.write(" 6) 0.0000 0\n") 
	template_file.write(" 7) 0.0000 0\n")
	template_file.write(" 8) 0.0000 0\n")
	template_file.write(" 9) 0.7570 0\n")#axis ratio (b/a) 
	template_file.write("10) -60.3690 0\n")#position angle (PA) [deg: Up=0, Left=90]
	template_file.write(" Z) 0\n\n")#output option (0 = resid., 1 = Don't subtract) 

	#Object number 2
	template_file.write(" 0) sky\n")
	template_file.write(" 1) 1.3920 0\n") # sky background at center of fitting region [ADUs]
	template_file.write(" 2) 0.0000 0\n") # dsky/dx (sky gradient in x)
	template_file.write(" 3) 0.0000 0\n")  #  dsky/dy (sky gradient in y)
	template_file.write(" Z) 0\n\n") #  output option (0 = resid., 1 = Don't subtract)

	template_file.write("===============================================================================")
	template_file.close()
