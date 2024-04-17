"""This scripts was used to add outgroups to our sequences clustered at 100%, 
and remove forbiden chacaters from FASTA headers.
"""

from Bio import SeqIO


sequences = list(SeqIO.parse("../supplementary_file_5/clusters/centroid_seq/length_c100.fasta", "fasta"))
outgroups = list(SeqIO.parse("data/outgroups.fasta", "fasta"))



def change_FASTA_headers(data):
    """Remove cluster size infomration
    from FASTA headers
    """

    for _ in data:
        _.description = _.description.split(';')[0]
        _.name = _.description
        _.id = _.description

    return data


sequences = change_FASTA_headers(sequences)
outgroup = change_FASTA_headers(outgroups)

new_sequences = sequences+outgroups


SeqIO.write(new_sequences, "data/zOTUs_with_outgroups.fasta", "fasta")