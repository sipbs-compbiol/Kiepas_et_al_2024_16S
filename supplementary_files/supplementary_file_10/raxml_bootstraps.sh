#!/bin/bash

#=============================================================
#
# Job script for running bootstraps on the strep 16S sequences
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
#SBATCH --job-name=raxml-ng-strepboot
#
# Output file
#SBATCH --output=slurm-%j.out
#======================================================

# Needed to enable conda activation, which is configured
# in home directory
source ~/.bashrc

# RAxML-NG is only available in phd_rea environment
conda activate phd_rea

# Find 100 bootstrap trees, after finding a new
# optimal tree beginning with default (20) starting trees,
# the GTF+FO model and no partitions. Here uses
# raxml-ng-mpi on a single node (-N 1 above) with
# 64 threads (--cpus-per-task above)
raxml-ng-mpi \
--msa strep/01_parse.raxml.rba \
--all \
--model GTR+FO \
--bs-trees 100 \
--threads 64 \
--seed 24875 \
--prefix strep/03_bootstrap \
--extra thread-pin

# Exit environment
conda deactivate