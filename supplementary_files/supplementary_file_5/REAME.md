# Supplementary file 5 - Clustering of full-length 16S rRNA *Streptomyces* sequences 

This ZIP file contains a BASH script used to cluster our cleaned full-length 16S *Streptomyces* local database at various thresholds, and provides accessions for representative sequences generated for each threshold, and accessions for each cluster members. 

## The current repositiory contains the following subfiles:
- `cluster_sequences.sh` - BASH scipt used to cluster the sequences
- `clusters` - Folder containings output generated after running the above BASH script. This folder contains the following two subloders:

    - `centroid_seq` -  Representative sequences/accessions for each clustering thereshold.
    - `cluster_members` - Each folder `c{clustering_thereshold_ID}_clusters` contains a set of txt files with sequence accessions for every cluster member. 

NOTE: Due to the repository size limits for GitHub.com the generated FASTA files can be accessed
on zenodo at {INSERT DOI}. If the supplementary data was obtained from GitHub only txt files with sequences accessions are provided.