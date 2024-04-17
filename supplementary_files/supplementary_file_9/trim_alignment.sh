#!/bin/bash
# trim_alignment.sh
# Trimming 16S rRNA alignment, by selecting the columns. 

trimal -in data/zOTU_MSA.fasta -out data/strep_final_nextalign_MSA.fasta -selectcols { 0-159,1246-1526 }