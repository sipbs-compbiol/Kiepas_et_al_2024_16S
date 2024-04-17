
#Set Up
from Bio import SeqIO
from itertools import chain
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from pathlib import Path

#Extracting Streptomyces sequences
def strep_seq_extraction(FASTA_file):
    """Extract sequences from a given FASTA_file
    if 'Streptomyces' word found in headers. 
    """

    records = list(SeqIO.parse(FASTA_file, 'fasta'))

    strep_records = [record for record in records if 'streptomyces' in record.description.lower()]

    return strep_records



SILVA_strep = strep_seq_extraction("../supplementary_file_2/SILVA_138.1_SSU_tax_silva.fasta")
RDP_strep = strep_seq_extraction("../supplementary_file_2/RDP_11_5.fa")
NCBI_strep = strep_seq_extraction("../supplementary_file_2/NCBI_33175.fasta")
GG_strep = strep_seq_extraction("../supplementary_file_2/gg_13_5_mapped_taxa.fasta")



#Getting complete 16S rRNA sequences
def get_full_length_seq(FASTA_file):
    """Extract sequences with at least 1200bp
    from a given FASTA_file. 
    """

    whole_seq = [_ for _ in FASTA_file if len(_.seq) >=1200]

    return whole_seq


SILVA_full_len = get_full_length_seq(SILVA_strep)
RDP_full_len = get_full_length_seq(RDP_strep)
NCBI_full_len = get_full_length_seq(NCBI_strep)
GG_full_len = get_full_length_seq(GG_strep)



#Merging database
merged = chain(SILVA_full_len, RDP_full_len, NCBI_full_len, GG_full_len)

#Replace U to T

def RNA_to_DNA(FASTA_file):
    """Takes FASTA file with RNA and DNA seq as an input 
    and returns them as FASTA file with DNA seq only.
    """
    records = [record.upper() for record in FASTA_file]
    dnarecords = []
    for record in records:
        dnarecords.append(SeqRecord(record.seq.back_transcribe(), id=record.id,
                                    description=record.description, name=record.name))
    return dnarecords

staranaralised = RNA_to_DNA(merged)

SeqIO.write(staranaralised, "all_DNA_whole_16S_strep_2.fasta", "fasta")


