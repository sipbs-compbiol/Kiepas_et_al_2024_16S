"""It was brought to our attention that some of the genomes were suppressed from the NCBI database.
This script was used to identify which genomes were suppresed or replaced. 
"""

#Set Up
import pandas as pd
from pathlib import Path

#Load data 
NCBI_status = pd.read_csv("data/assembly_summary_refseq_historical.txt", sep='\t', skiprows=1)

#Create a dictionary with RefSeq accession ids as keys, and their status as values
genome_status = NCBI_status.set_index('assembly_accession').to_dict()['version_status']

#List of all genomes used in the MLST analysis (1938)
datadir = Path("data/streptomyces_genomes/")
filenames = sorted(datadir.glob("*"))
all_genomes = ['_'.join(str(_).split('/')[-1].split('_')[:2]) for _ in filenames if '.DS' not in str(_)]



#We can now identify all gneomes that have been suppressed or replaced
troublesome_genomes = {genome:status for genome, status in genome_status.items() if genome in all_genomes}

#Create dataframe which will contain status information for all genome used in the analysis and their status
genome_status = pd.DataFrame(all_genomes, columns =['accession'])
genome_status['status'] = genome_status['accession'].map(troublesome_genomes)
genome_status = genome_status.fillna('available')

#saving data
genome_status.to_csv("output/strep_genome_status.csv", index=False)