"""This script was used to extract 16s RNA sequences from Streptomyces genomes. Suppressed genomes were excluded.
"""

#Set Up
from Bio import SeqIO, SeqFeature
from Bio.SeqRecord import SeqRecord
import pandas as pd
from pathlib import Path
import re

#Extraction of 16S rRNA sequences
def extract_16S(gb_file):
    """Extract and return all 16S rRNA sequences
    for a given genbank file. 
    """
    records = SeqIO.parse(gb_file, "genbank")
    accession = '_'.join(str(gb_file).split('/')[-1].split('_')[0:2])

    seq_16S = []
    for genome in records:
        for gene in genome.features:
            if gene.__dict__['type'] == 'rRNA':
                if '16S' in gene.qualifiers['product'][0]:
                    if gene.strand == 1:
                        start = gene.location.nofuzzy_start
                        end = gene.location.nofuzzy_end
                        seqs = genome.seq[start:end]
                        record = SeqRecord(
                            seqs,
                            id=accession,
                            name=accession,
                            description=accession,
                        )
                        seq_16S.append(record)
                        
                    if gene.strand == -1:
                        start = gene.location.nofuzzy_start
                        end = gene.location.nofuzzy_end
                        seqs = genome.seq[start:end].reverse_complement()
                        record = SeqRecord(
                            seqs,
                            id=accession,
                            name=accession,
                            description=accession,
                        )
                        seq_16S.append(record)




    return seq_16S


###Generating the dataframe
##First getting a list of genomes of interest

#Discarding genomes, which were suppressed or replaced
datadir = Path("../supplementary_file_17/data")
filenames = sorted(datadir.glob("strep*/GCF*/*.gbff"))

suppressed_genomes = pd.read_csv("../supplementary_file_17/output/strep_genome_status.csv")
available_genomes = [_ for _ in suppressed_genomes.loc[suppressed_genomes['status'] == 'available', 'accession']]
#Getting the replaced genomes
replaced = ['_'.join(str(fname).split('/')[-1].split('_')[0:2]) for fname in filenames if 'replace' in str(fname)]
all_genomes = available_genomes+replaced

#Datafarme
df = pd.DataFrame(available_genomes+replaced, columns=['accession'])


all_16S_per_genome = {}
unique_16S_per_genome = {}
extracted_16S_sequences = []

for fname in filenames:
    if '_'.join(str(fname).split('/')[-1].split('_')[0:2]) in all_genomes:
        print(fname)
        records = extract_16S(fname)
        extracted_16S_sequences.extend(records)


retain = []
for record in extracted_16S_sequences:
    retain.append(record)



# Geretating datafram for genomes which 
SeqIO.write(retain, "../output/16S_seq_from_strep_genomes.fasta", "fasta")


