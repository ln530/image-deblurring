# Image Deblurring
## Dataset

## Setup
Creating the virtual environment and installing packages. 
``````bash
module load python/3.7.7
python3 -m venv pov
source pov/bin/activate
pip install --upgrade pip
pip --no-cache-dir install gdown
``````
## Downloading data
Run in HPC to download data. 
``````bash
sbatch download_data.sh
``````
