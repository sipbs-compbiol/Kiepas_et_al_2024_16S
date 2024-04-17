# Supplementary file 9
This ZIP file contains I/O files and scipts used to generate MSA of our non-redudant and free from poor quality reads full-length *Streptomyces* local database clustered at 100% ID. 

## The current set of files include:

Script:
- `add_outgroups.py` - Python script used to add outgroup sequences.
    Output:
    - `zOTUS_with_outgroups.fasta` - FASTA file containing all zOTU sequences and added outgroup sequences

Script:
- `align_seq_nextalign.sh` - Bash script used to align sequences using nextalign
    Output:
    - `zOTU_MSA.fasta` - FASTA file with aligned sequences

Script:
- `trim_alignment.sh` - Bash script used to trim the alignment edges with trimAL
    Output:
    - `strep_final_nextalign_MSA.fasta` - FASTA file with trimmed MSA

Script:
- `alignment_dereplication.sh` - Bash script used to remove replicate sequences from trimmed MSA
    Output:
    - `strep_final_nextalign_MSA_reduced.phy` - PHY file with dereplicated alignment
    Output:
    - `RAxML_info.strep_final_nextalign_MSA_reduced` - log file
