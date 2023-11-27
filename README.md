# Image Deblurring
##Dataset

##Setup
``````bash
module load python/3.7.7
python3 -m venv pov
source venv_nlp/bin/activate
pip install --upgrade pip
pip --no-cache-dir install gdown
``````
##Downloading data
``````bash
sbatch download_data.sh
``````
