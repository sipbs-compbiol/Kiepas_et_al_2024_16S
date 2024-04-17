#!/bin/bash
# remove_redundancy.sh
# The scipt was used to remove redundant sequences using vsearch 

vsearch --derep_fulllength ../../supplementary_file_3/all_DNA_whole_16S_strep.fasta --output output/derep_DNA_whole_16S_strep.fasta --uc  output/dereplication_info.txt --sizeout