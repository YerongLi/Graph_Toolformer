#!/bin/bash
#
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=V100:1
#SBATCH --gres=gpu:V100:1
#SBATCH --partition=eng-research-gpu
#SBATCH --output=ptrlog.log
##SBATCH --error=myjob.e%j
##SBATCH --mail-user=yerong2@illinois.edu

#
# End of embedded SBATCH options
#
watch -n 10 tail submit.s
git pull; python Framework_Graph_Toolformer.py
