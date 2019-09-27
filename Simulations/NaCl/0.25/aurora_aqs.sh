#!/bin/bash
#SBATCH --job-name=0.25_M_NaCl_aqs
#SBATCH --nodes=1
#SBATCH --ntasks=5
#SBATCH --gres=gpu:1
#SBATCH --time=168:00:00
#SBATCH --account=lu2019-2-15
#SBATCH --partition=gpu
#SBATCH -o run_aqs.out
#SBATCH -e run_aqs.err

module purge
module load GCC/7.3.0-2.30
module load CUDA/9.2.88

python run_openMM_aqs.py