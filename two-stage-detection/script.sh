#!/bin/bash

#SBATCH --account=st-sielmann-1-gpu
#SBATCH --cpus-per-task=8
#SBATCH --gpus-per-node=2
#SBATCH --job-name=weed-detection
#SBATCH --mail-type=ALL
#SBATCH --mail-user=astrollin.neil@gmail.com
#SBATCH --mem=12G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --output=logs/output.txt
#SBATCH --error=logs/error.txt
#SBATCH --time=12:00:00

module load gcc python miniconda3 cuda cudnn

source ~/.bashrc
conda activate two-stage-weed

cd $SLURM_SUBMIT_DIR

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

/home/nlin06/miniconda3/envs/two-stage-weed/bin/python /scratch/st-sielmann-1/agrobot/Weed-Detection/two-stage-detection/detectron2_train.py

conda deactivate
 