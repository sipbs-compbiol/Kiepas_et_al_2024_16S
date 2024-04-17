"""This script was used to filter the extracted 16S rRNA sequences by retaining only
sequences from genomes that do not dontain a single 16S rRNA sequence with ambiguity symbol, 
or partial sequences (less than 1200bp long). 
"""

#Set Up
from Bio import SeqIO
import re
from collections import defaultdict


#Load data
records = list(SeqIO.parse("../output/16S_seq_from_strep_genomes.fasta", "fasta"))

#Get genomes which have a partial 16S rrNA sequence, or have ambiguity symbols within 16S records
genomes_with_partial_records = [_.description for _ in records if len(_.seq) <1200]
genomes_with_ambiguity = [_.description for _ in records if re.search(r"[^ATGC]", str(_.seq)) != None]

dicard = genomes_with_partial_records + genomes_with_ambiguity

#Extract sequences which are complete (longer than 1200bp), and do not have a single ambiuity symbol
clean_records = ([_ for _ in records if len(_.seq) >= 1200 and re.search(r"[^ATGC]", str(_.seq)) == None and _.description not in dicard])

SeqIO.write(clean_records, "../output/filtered_16S_seq_from_strep_genomes.fasta", "fasta")

retain_genomes = list(set([_.description for _ in clean_records]))
with open("../data/retained_genomes.txt", "w") as outfile:
    outfile.write("\n".join(retain_genomes))

