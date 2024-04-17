#!/bin/bash
# sequence_clustering.sh
# Clustering fo 16S rRNA sequences at theresholds varying between 98% and 100% in steps of 0.1%. 
mkdir clusters
for i in `seq 98 0.1 100`; do
    vsearch --cluster_fasta ../supplementary_file_4/remove_chimeras/output/non_chimeras.fasta -id $i --centroids clusters/centroid_seq/length_c$i.fasta --sizeout --clusterout_id --clusters clusters/cluster_members/c$i_clusters