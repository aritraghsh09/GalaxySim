# GalaxySim

GalaxySim is a simple repository to simulate large numbers of galaxies in parallel using [GALFIT](https://users.obs.carnegiescience.edu/peng/work/galfit/galfit.html). The code in the repository makes use of GALFIT and Python's multiprocessing library.

### Usage Info/Citation/Reference
This repository was used in the work pertaining to the following paper:-
"Galaxy Morphology Network (GaMorNet):  A Convolutional Neural Network used to study morphology and quenching in ∼100,000 SDSS and ∼20,000 CANDELS galaxies" , Ghosh et. al.
If you use this code for any published work, please cite the above paper and include a link to this GitHub repository

This code is being made available under a GNU General Public License v3.0. Please see the file called LICENSE in the repository for more details.


### How to Run Galaxy Sim?

#### Installation
Galaxy Sim is written in Python and the primary pre-requisite is GALFIT. Instllation instructions for GALFIT can be found [here](https://users.obs.carnegiescience.edu/peng/work/galfit/galfit.html). 

Other than GALFIT, Galaxy Sim depends on the following Python libraries:- numpy, tqdm (if you want a progress bar), pickle, multiprocessing


