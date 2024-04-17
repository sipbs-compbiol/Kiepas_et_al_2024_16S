# Supplementary file 3 - Filtration of 16S rRNA public databases. 

This ZIP file contains Python script used to filtrate 16S rRNA detabases to retain only full length (1200bp or longer) *Streptomyces* 16S rRNA sequences, and standaralise base code to thymine, rather than uracil. 

**The current folder contains the following files:**
- Script 1:
    - `get_complete_strep_seq.py` - Python script used to extract sequences. 
    - Input files:
        - Input data are found in Supplementray File 2. 
    - Output files:
        - `all_DNA_whole_16S_strep_check.fasta` - Generated FASTA file

- Script 2:
    - `check_nomenclature_hierarchy.py` - Python script used to check nomenclature at each rank assigned to sequences extracted in `all_DNA_whole_16S_strep_check.fasta`
    - Output file:
        - `nomenclature_hierarchy_info.csv`
