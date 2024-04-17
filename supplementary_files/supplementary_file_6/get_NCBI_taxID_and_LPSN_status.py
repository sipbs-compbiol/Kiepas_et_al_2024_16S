"""This script was used to assign NCBI taxID to all 48,981 full-length Streptomyces sequences
based on the nomenclature assigned to it in the source database, and to determined whether 
the assigned nommenclature was validly published under LSPN. 
"""

#Set Up
from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
from pathlib import Path
import csv


#Step 1: Get a dictionary with the sequences IDs as keys, and the species names as a value for every sequence used in this study
data = list(SeqIO.parse("../supplementary_file_3/all_DNA_whole_16S_strep.fasta", "fasta"))

db_names_accessions = {}

for _ in data:
    #Each databases had a diffrent FASTA header format, so each format must be dealt with separately
    if 's__' in _.description:
        if _.description.split('g__')[-1].replace('; s__', ' ') == 'Streptomyces ':
            db_names_accessions[_.description.split(' ')[0]] = 'Streptomyces sp.'
        else:
            db_names_accessions[_.description.split(' ')[0]] = str(_.description.split('g__')[-1].replace('; s__', ' '))
    elif 'Bacteria;A' in _.description:
        db_names_accessions[_.description.split(' ')[0]] = ' '.join(_.description.split(';')[-1].split(' ')[:2])
    elif 'Bacteria' in _.description:
        if 'Bacteria' in ' '.join(_.description.split(' ')[1:3]).split('\t')[0].replace('[Streptomyces]', 'Streptomyces').strip(';'):
            db_names_accessions[_.description.split(' ')[0]] = ' '.join(_.description.split(' ')[1:3]).split(';')[-1].replace('[Streptomyces]', 'Streptomyces')
        else:
            db_names_accessions[_.description.split(' ')[0]] = ' '.join(_.description.split(' ')[1:3]).split('\t')[0].replace('[Streptomyces]', 'Streptomyces').strip(';')
    else:
        db_names_accessions[_.description.split(' ')[0]] = ' '.join(_.description.split(' ')[1:3])


#Generate dataframe with sequence accession, and assigned species name
df = pd.DataFrame([k for k, v in db_names_accessions.items()], columns =['accession'])
df['organism_name'] = df['accession'].map(db_names_accessions)

#Step 2: Check LSPN status

class Taxon:
    
    genus = ""
    species = ""
    subspecies = ""
    status_kind = ""
    status_proposal = ""
    status_nom = ""
    status_tax = ""
    type_strains = []
    
    def has_type_strain(self, strain):
        """Returns true if passed strain is a type strain"""
        if strain.lower() in [_.lower() for _ in self.type_strains]:
            return True
        
        return False
    
    def __init__(self):
        pass
    
    def __repr__(self):
        """This is called when we represent the object as a string"""
        return f"<Taxon: {self.genus}, {self.species}, {self.subspecies}>"
    
    def __str__(self):
        """Return contents of Taxon as a string"""
        return f"{self.genus}, {self.species}, {self.subspecies}"

taxa = []

with open("LSPN_taxonomy.csv") as ifh:
    reader = csv.reader(ifh, delimiter=",")
    next(reader, None)  # skip header
    for row in reader:
        # Here is where we do the hard work
        taxon = Taxon()  # create new Taxon instance
        
        # Get nomenclature
        taxon.genus = row[0]
        taxon.species = row[1]
        taxon.subspecies = row[2]
        
        # Get status
        # All status is in column 4, but stored as several items
        status = [_.strip() for _ in row[4].split(";")]
        taxon.status_kind = status[0]
        taxon.status_proposal = status[1]
        taxon.status_nom = status[2]
        taxon.status_tax = status[3]
        
        # Get type strains
        taxon.type_strains = row[8].split("; ")
        
        # Add taxon to list
        taxa.append(taxon)


#Creating dictionary with taxon name/species as key and status tax as values
strep_status_tax = {}
for _ in taxa:
    strep_status_tax[f'{_.genus} {_.species}'] = _.status_tax
{v for k, v in strep_status_tax.items()}




df["LSPN_status"] = df["organism_name"].map(strep_status_tax)
df = df.fillna('-')



#Change status_tax to `no species info` if species are *Streptimyces sp.*, and `invalid name` if species name not found in LPSN data
def is_valid_info(row, col, col2):
    try:
        validity = 'not validly described' if 'Streptomyces sp.' in row[col] or 'unidentified' in row[col] else 'no record in LSPN entry' if row[col2] == '-' else row[col2]
    except IndexError:
        validity = 'NA'
        
        
    return validity
df['LSPN_status'] = df.apply(is_valid_info, col='organism_name', col2='LSPN_status', axis=1)


print(df)
#Step 3: Get NCBI taxI for a given organism name

def get_taxID(candidate):
    with open('names.dmp', "r") as handle:
        ncbi = handle.readlines()
        for line in ncbi:
            if candidate in line:
                columns = line.strip().split('|')
                taxid = columns[0].strip('\t')
                print(taxid)
                
                return taxid



df['organism_name'] = df['accession'].map(db_names_accessions)



NCBI_taxID = {}
for k, v in db_names_accessions.items():
    NCBI_taxID[k] = get_taxID(v)
    
df['taxID'] = df['accession'].map(NCBI_taxID)

df.to_csv('complete_strep_record_info_2.csv')