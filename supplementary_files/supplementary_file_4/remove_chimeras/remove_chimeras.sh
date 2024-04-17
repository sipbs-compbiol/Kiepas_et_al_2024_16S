#!/bin/bash
# remove_chimeric_seq.sh
# The scipt was used to remove chimeric sequences using vsearch

vsearch --uchime_denovo ../remove_ambiguity/output/derep_DNA_whole_16S_strep_removed_ambiguity.fasta --chimeras output/chimeras.fasta --nonchimeras output/non_chimeras.fasta