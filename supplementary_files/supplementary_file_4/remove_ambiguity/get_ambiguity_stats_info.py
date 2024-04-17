"""This script was used to calculate the Variance and average count of ambiguity per sequence
to help us choose an appropriate model.
"""

#SetUp
from Bio import SeqIO
import numpy as np


#Loading data 
records = list(SeqIO.parse("../dereplication/output/derep_DNA_whole_16S_strep.fasta", "fasta"))

#Counting number of ambiguity symbols per sequence
ambiguity_count = [len(record.seq) - record.seq.count('A') - record.seq.count('C') - record.seq.count('G') - record.seq.count('T') for record in records 
                    if len(record.seq) - record.seq.count('A') - record.seq.count('C') - record.seq.count('G') - record.seq.count('T') >0]

with open("output/ambiguity_stats_info.txt", "w") as text_file:
    text_file.write(f"""Average count of ambiguity per sequence: {np.mean(ambiguity_count)}\nVariance: {np.var(ambiguity_count)}""")
