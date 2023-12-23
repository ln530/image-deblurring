# Image Deblurring

## Dataset
This project is based on the GoPro dataset which was published in 2017 (https://seungjunnah.github.io/Datasets/gopro).

## Setup
Creating the virtual environment and installing packages. 
``````bash
module load python/3.10
python3 -m venv pov
source pov/bin/activate
pip install --upgrade pip

All the installed libraries can be found in the requirements.txt file.
``````

## Downloading data
Run in HPC to download data. 
``````bash
sbatch download_data.sh
``````

## Short description of the files in the repository

### Project environment requirements:
- requirements.txt

### Downloading and organizing data:
- download_data.py
- download_data.sh
- prepare_data.ipynb

### Helper functions:
- helper_functions

### Calculating the baseline:
- baseline_loss.ipynb

### Deblurring without neural networks:
- fourier_transform.ipynb

### Autoencoders:
- autoencoder_based_on_noblur_project.ipynb
- autoencoder_simple.ipynb

### Analysing model results
- analyse_best_models.ipynb
