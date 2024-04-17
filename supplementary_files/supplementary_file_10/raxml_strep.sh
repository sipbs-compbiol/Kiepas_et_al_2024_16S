#!/bin/bash

#=============================================================
#
# Job script for running a single tree inference with RAxML-NG
#
#=============================================================

#======================================================
# Propagate environment variables to the compute node
#SBATCH --export=ALL
#
# Run in the standard partition (queue)
#SBATCH --partition=long
#
# No. of tasks required
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=64
#
# Reserve 64GB
#SBATCH --mem=64G
#
# Job name
#SBATCH --job-name=raxml-ng-strep
#
# Output file
#SBATCH --output=slurm-%j.out
#======================================================

# Needed to enable conda activation, which is configured
# in home directory
source ~/.bashrc

# RAxML-NG is only available in phd_rea environment
conda activate phd_rea

# Find an optimal tree with default (20) starting trees,
# the GTF+FO model and no partitions. Here uses
# raxml-ng-mpi on a single node (-N 1 above) with
# 64 threads (--cpus-per-task above)
raxml-ng-mpi \
--msa strep/01_parse.raxml.rba \
--model GTR+FO \
--threads 64 \
--seed 38745 \
--prefix strep/02_infer \
--extra thread-pin

# Exit environment
conda deactivate