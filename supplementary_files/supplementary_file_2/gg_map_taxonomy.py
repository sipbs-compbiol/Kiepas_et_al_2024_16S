"""This Python script was used to map taxonomy information to
sequences found in Greengenes v13.5 database.

Due to the repository size limits for GitHub.com the FASTA file (gg_13_5.fasta)
containing sequences released in Greengenes v13.5 database must be downloaded directly 
from the https://greengenes.secondgenome.com website. Alternatively, you can access them
on zenodo at {INSERT DOI}. 

For the purpose of reproductibility, before running this scipt please check
if all sequences accessions in the downloaded FASTA file from the website match
gg_13_5.txt, and vice versa. 
"""

#Set Up
from Bio import SeqIO



records = list(SeqIO.parse("gg_13_5.fasta", "fasta"))

def get_records_medatada(metafile):
    """Read metafile, and return dictionary
    with taxa information string as a value, keyed by sequence ID.
    """

    gg_13_5_tax_dict = {}

    with open(metafile, "r") as ifh:
        for line in ifh.readlines():
            key, val = line.strip().split("\t")
            gg_13_5_tax_dict[key] = val
            
    return(gg_13_5_tax_dict)

gg_13_5_tax_dict = get_records_medatada("gg_13_5_taxonomy.txt")

for record in records:
    record.description = gg_13_5_tax_dict[record.id]

SeqIO.write(records, "gg_13_5_mapped_taxa.fasta", "fasta")