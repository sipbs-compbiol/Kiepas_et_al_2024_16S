# README.md - Supplementray file 18
This ZIP file contains all Python and Scipts used to extract full-length sequences from filtered *Streptomyces* genomes. 

## Current set of files include:
- `Data`:
    - `retained_genomes.txt` - txt file containing genome accessions used to extract sequences (eg. no suppressed or replaced genomes)
    - `S_coelicolor_A32.fasta` - FASTA file containing 16S rRNA reference sequence extracted from GCF_008931305.1

- `scripts`:
    - `extract_16S.py` - Python script used to extract 16S rRNA sequences
    - `filter_16S_seq.py` - Python script used to filter the extracted sequences by retaining only sequences from genomes which exclusively consist of full-length and ambiguity free sequences
    - `align_sequences_with_nextalogn.sh` - Bash script used to align the filtered sequences
    - `trim_alignment.sh` - Bash scipt used to trim the alignment

- `output`:
    - `16S_seq_from_strep_genomes.fasta` - 16S rRNA sequences extracted using `extract_16S.py` script
    - `filtered_16S_seq_from_strep_genomes.fasta` - 16S rRNA sequences after filtration setp using `filter_16S_seq.py` Python script
    - `filtered_16S_seq_from_strep_genomes_aligned.fasta` - aligned sequenced
    - `16S_extracted_from_genomes_trimmed_aln.fasta` - trimmed alignment