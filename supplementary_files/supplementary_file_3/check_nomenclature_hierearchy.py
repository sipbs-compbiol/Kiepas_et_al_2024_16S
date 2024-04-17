"""This script was used to get nomenclature at all ranks for all full-length sequences with the key word 'Streptomyces' in the FASTA headers
"""

#Set Uo
from Bio import SeqIO
from pathlib import Path
import pandas as pd
from collections import Counter

records = list(SeqIO.parse('all_DNA_whole_16S_strep.fasta', "fasta"))
df = pd.DataFrame([_.description.split(' ')[0] for _ in records], columns =['accession'])


#Step 1: Genus information
genus = {}
for _ in records:
    if 'g__' in _.description:
        genus[_.description.split(' ')[0]] = _.description.split('g__')[-1].split(';')[0]
    elif _.description.split(';')[-1] == 'genus':
        genus[_.description.split(' ')[0]] = (_.description.split(';')[-2]).replace('/', '-')
    elif 'Lineage' in _.description:
        genus[_.description.split(' ')[0]] = 'No Genus Info'
    elif 'NR' in _.description:
        genus[_.description.split(' ')[0]] = 'No Genus Info'
    elif _.description.split(';')[-2] in ['Mammalia', 'WS1', 'uncultured', 'MB-A2-108']:
        genus[_.description.split(' ')[0]] = 'No Genus Info'
    else:
        genus[_.description.split(' ')[0]] = _.description.split(';')[-2].replace('[Streptomyces] thermoautotrophicus', 'Streptomyces')


df['genus'] = df['accession'].map(genus)


#Step 2: Family information
family = {}
for _ in records:
    if 'f__' in _.description:
        family[_.description.split(' ')[0]] = _.description.split('f__')[-1].split(';')[0]
    elif 'ceae' in _.description:
        family[_.description.split(' ')[0]] = ''.join([name for name in [x for x in _.description.split(';') if 'ceae' in x][-1].replace('unclassified_', '').replace(' 1', '').split(' ') if name[-4:] == 'ceae'])

    else:
        family[_.description.split(' ')[0]] = 'No Family Info'

df['family'] = df['accession'].map(family)

#Step 3: Order information
order = {}
for _ in records:
    if 'o__' in _.description:
        order[_.description.split(' ')[0]] = _.description.split('o__')[-1].split(';')[0]
    elif 'order' in _.description:
        order[_.description.split(' ')[0]] = _.description.split(';order')[0].split(';')[-1].replace('"', '')
    elif 'NR' in _.description:
        order[_.description.split(' ')[0]] = 'No Order Info'
    elif 'ales' in _.description:
        order[_.description.split(' ')[0]] = [x for x in _.description.split(';') if 'ales' in x][0].replace('unclassified_', '').replace(' 1', '').split(' ')[0]
    else:
        order[_.description.split(' ')[0]] = 'No Order Info'

df['order'] = df['accession'].map(order)



#Step 4: Class information
class_ = {}
for _ in records:
    if 'c__' in _.description:
        class_[_.description.split(' ')[0]] = _.description.split('c__')[-1].split(';')[0]
    elif ';class' in _.description:
        class_[_.description.split(' ')[0]] = _.description.split(';class')[0].split(';')[-1]
    elif 'NR' in _.description:
        class_[_.description.split(' ')[0]] = 'No Class Info'
    elif _.description.split(';')[2] not in ['rootrank', 'Bacteria', 'uncultured Streptomyces sp.', 'MB-A2-108']:
        class_[_.description.split(' ')[0]] = _.description.split(';')[2]
    else:
        class_[_.description.split(' ')[0]] = 'No Class Info'

df['class'] = df['accession'].map(class_)


phylum = {}
for _ in records:
    if 'p__' in _.description:
        phylum[_.description.split(' ')[0]] = _.description.split('p__')[-1].split(';')[0]+' '
    elif ';phylum' in _.description:
        phylum[_.description.split(' ')[0]] = _.description.split(';phylum')[0].split(';')[-1].replace('"', '')+' '
    elif 'NR' in _.description:
        phylum[_.description.split(' ')[0]] = 'No Phylum Info'
    elif _.description.split(';')[1].split('=')[-1] not in ['rootrank', 'Root', 'WS1']:
        phylum[_.description.split(' ')[0]] = _.description.split(';')[1].split('=')[-1]+' '
    else:
        phylum[_.description.split(' ')[0]] = 'No Phylum Info'
    
df['phylum'] = df['accession'].map(phylum)



kingdom = {}
for _ in records:
    if 'Bacteria' in _.description:
        kingdom[_.description.split(' ')[0]] = 'Bacteria'
    elif 'NR' in _.description:
        kingdom[_.description.split(' ')[0]] = 'No Kingdom Info'
    else:
        kingdom[_.description.split(' ')[0]] = _.description.split(' ')[1].split(';')[0]
df['domain'] = df['accession'].map(kingdom)



df.to_csv("nomenclature_hierarchy_info_1.csv", index=False)