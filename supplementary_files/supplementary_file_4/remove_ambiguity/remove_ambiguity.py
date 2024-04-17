"""This Python script was used to remove sequences
with more than 153 ambiguity symbols.
"""
from Bio import SeqIO
from pathlib import Path

records = list(SeqIO.parse("../dereplication/output/derep_DNA_whole_16S_strep.fasta", "fasta"))

removed_ambiguity = [record for record in records if len(record.seq) - record.seq.count('A') - record.seq.count('C') - record.seq.count('G') - record.seq.count('T') <=153]

SeqIO.write(removed_ambiguity, "output/derep_DNA_whole_16S_strep_removed_ambiguity_2.fasta", "fasta")