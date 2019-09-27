#!/bin/bash
#SBATCH --job-name=1.00_M_NaCl_iso
#SBATCH --nodes=1
#SBATCH --ntasks=5
#SBATCH --gres=gpu:1
#SBATCH --time=168:00:00
#SBATCH --account=lu2019-2-15
#SBATCH --partition=gpu
#SBATCH -o run_iso.out
#SBATCH -e run_iso.err

module purge
module load GCC/7.3.0-2.30
module load CUDA/9.2.88

python run_openMM_iso.py