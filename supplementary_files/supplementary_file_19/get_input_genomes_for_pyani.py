"""This script was used to get input genome sequences for pyANI analysis.
16S rRNA sequences were extracted from the Streptomyces genomes and  aligned using nextalign; the alignments were then trimmed with trimAl.
Genomes sharing the same 16S rRNA sequences, will be used as input sets for pyANI analysis to determine, whether
diffrent Streptomyces species share identical 16S rRNA sequences."""

#Set Up
from Bio import AlignIO
import hashlib
import pandas as pd
from collections import defaultdict
import os
from pathlib import Path
from shutil import copy
from collections import Counter
from Bio import SeqIO




#Loading the alignemnt
align = AlignIO.read("../supplementary_file_18/output/16S_extracted_from_genomes_trimmed_aln.fasta"), "fasta")

#Getting a dictionary with sequence hash as key, and all genomes with the same seq/hash sequence as a value
hash_sequences = defaultdict(list) #Hold an empty dictionary


for _ in align:
    my_hash = hashlib.md5(str(_.seq).encode('utf-8')).hexdigest() #Assign hash to sequences
    hash_sequences[my_hash].append(_.description) #add genomes to the defaultdict based on hashes


#Generating and saving dataframe for future analysis
df = pd.DataFrame([k for k, v in hash_sequences.items()], columns=['cluster_hash'])

#Getting a total number of genomes
df['Total_genomes'] = df['cluster_hash'].map({k:len(set(v)) for k, v in hash_sequences.items()})
df['Cluster_members'] = df['cluster_hash'].map({k:','.join(list(set(v))) for k, v in hash_sequences.items()})



#Path to .fna files
datadir = Path("../supplementary_file_17/data")
filenames = sorted(datadir.glob("strep*/GCF*/*.fna"))


os.mkdir('genome_clusters')
for k, v in hash_sequences.items():
    if len(set(v)) !=1:
        os.mkdir('genome_clusters/'+k)
        for _ in list(set(v)):
            for fname in filenames:
                if _ in str(fname) and 'from' not in str(fname):
                    copy(fname, 'genome_clusters/'+k)




#Get organism names for each genome
datadir = Path("../supplementary_file_17/data")
filenames = sorted(datadir.glob("strep*/GCF*/*assembly_report.txt"))


NCBI_names_per_genome = {}
def get_organism_name(file):
    with open(file) as f:
        lines = f.readlines()
        organism = ' '.join([_.split('  ')[1].split(' ')[0:2] for _ in lines if 'Organism name' in _][0])
        
    return organism

    
for _ in filenames:
    NCBI_names_per_genome[str(_).split('/')[-2]] = get_organism_name(_)

NCBI_names_per_cluster = defaultdict(list)

for seq_hash, members in hash_sequences.items():
    for member in members:
        NCBI_names_per_cluster[seq_hash].append(NCBI_names_per_genome[member])

df['NCBI_names'] = df['cluster_hash'].map(NCBI_names_per_cluster)
df['Unique_names_per_cluster'] = df['cluster_hash'].map({k:len(set(v)) for k, v in NCBI_names_per_cluster.items()})

df.to_csv('genome_clusters_info.csv', index=False)



