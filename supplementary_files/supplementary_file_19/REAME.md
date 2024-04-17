# README.md - Supplementary file 19
This ZIP file contains all Python and Bash scripts used to determine taxonomic boundries between genomes which share idnetical 16S rRNA sequences. 

## Current set of subfolder include:

- `get_input_genomes_for_pyani.py` - Python script used to get input sets for pyANI analysis
    - `genome_clusters` - A directory that included sub-files comprising of genome accessions that share identical 16S rRNA sequences, as well as all coreposing files.
- `pyani_analysis.sh` - Bash scipt used to run pyANI analysis on cluster found in `genome_clusters` directory
- `get_pyani_comparision_matrix.sh` - Bash scipt used to extract comparision matrices form pyANI analysis
    - `pyani_analysis_matrix` -  A directory that consists of all pyANI matrices
- `generate_viz_data_pyani_comparisions.py` - Python script used to get information about each individual pyANI comparision (genome 1 vs genome 2)
    - `pyANI_comparision_info.csv` - data containing all information for each pyANI comparision