"""This script was used to get parameters for qnbinom() function in R. 

Full information in README.md file. 
"""
#Set Up
from Bio import SeqIO
import numpy as np
from pathlib import Path

#Load data
records = list(SeqIO.parse("../dereplication/output/derep_DNA_whole_16S_strep.fasta", "fasta"))

#Total number of bases in all sequences with at least 1 ambiguity symbol
total_bases = sum([len(record.seq) for record in records if len(record.seq) - record.seq.count('A') - record.seq.count('C') - record.seq.count('G') - record.seq.count('T') != 0])

#Count of ambiguity per sequences with at least 1 ambiguity symbol
ambiguity_count = [len(record.seq) - record.seq.count('A') - record.seq.count('C') - record.seq.count('G') - record.seq.count('T') for record in records 
                    if len(record.seq) - record.seq.count('A') - record.seq.count('C') - record.seq.count('G') - record.seq.count('T') >0]

#Mean count of ambiguity symbols per sequece
mean_ambiguity = np.mean(ambiguity_count)

#Probablity
probablity = sum(ambiguity_count)/total_bases

#Run of positive outcomes
size = (mean_ambiguity*probablity)/(1-probablity)

with open("output/qnbinom_parameters.txt", "w") as text_file:
    text_file.write(f"""Mu: {mean_ambiguity}\nSize: {size}""")


