#!/bin/bash
# alignment_dereplication.sh
# Remove redundant sequences in a given alignment

raxmlHPC-SSE3 -s data/strep_final_nextalign_MSA.fasta -f c -n strep_final_nextalign_MSA_reduced -m GTRCAT