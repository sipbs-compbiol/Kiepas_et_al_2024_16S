# Supplementary file 17
This ZIP file contains I/O files and scipts used to download *Streptomyces* genomes, and check their assembly status. 

## The current set of files include:

Script:
- `download_genomes.sh` - Bash script used to download *Streptomyces* genomes
    Output/Data:
    - `streptomyces_genomes.txt` - txt file containing genome accessions for downloaded genomes

Script:
- `check_genome_status.py` - Python scirpt used to check the assembly status against `assembly_summary_refseq_historical.txt`
    Output:
    - `strep_genome_status.csv` - CSV file providing each genomes assembly status

Other:
- `streptomyces_replaced_genomes.txt` - txt file containing genome accessions for downloaded replaced genomes

