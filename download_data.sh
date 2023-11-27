#!/bin/bash
#SBATCH --job-name="Download data"
#SBATCH --time=6:00:00

module load python/3.7.7
source ./pov/bin/activate

python ./download_data.py
