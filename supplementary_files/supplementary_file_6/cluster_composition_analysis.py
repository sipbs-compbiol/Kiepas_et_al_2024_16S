"""This script was used to generate dataframe about taxonomic composition for each clustering thereshold.

Here, we also include redundant sequences removed in previous step.
"""

#Set Up
import pandas as pd
from Bio import SeqIO
from pathlib import Path
import hashlib
from collections import defaultdict


#Loading data with taxID information
data = pd.read_csv("complete_strep_record_info.csv")


#Getting unique taxids for each sequence
seqid_taxid = data.set_index('accession').to_dict()['taxID']
#Getting organism name for each sequence
seqid_organism_name = data.set_index('accession').to_dict()['organism_name']



#Loading pre-dereplication data
pre_dereplication = list(SeqIO.parse("../supplementary_file_3/all_DNA_whole_16S_strep.fasta", "fasta"))



#Get sequence hashes
hash_sequences = defaultdict(list) #Hold an empty dictionary
for _ in pre_dereplication:
    my_hash = hashlib.md5(str(_.seq).encode('utf-8')).hexdigest() #Assign hash to sequences
    hash_sequences[my_hash].append(_.description.split(' ')[0]) #add genomes to the defaultdict based on hashes


#Removing poor quality reads (eg. chimeras and recors with large amount of ambiguity)
post_cleaning_sequences = [_.description.split(';')[0] for _ in SeqIO.parse("../supplementary_file_4/remove_chimeras/output/non_chimeras.fasta", "fasta")]


fixed_hash_sequences = {}
for hash, members in hash_sequences.items():
    for member in members:
        if member in post_cleaning_sequences:
            fixed_hash_sequences[hash] = members


#Hold empty data
df = pd.DataFrame()


datadir = Path("../supplementary_file_5/clusters/cluster_members/")
filenames = sorted(datadir.glob("c*_clusters/*clusters*"))




cols = ['theresholds_id', 'cluster_id', 'cluster_members', 'number_of_cluster_members', 'unique_number_of_cluster_members', 'member_names']


def get_dereplication_seq(current_members):
    new_and_current_members = []
    for _ in current_members:
        for hash, dereplication_members in fixed_hash_sequences.items():
            if _ in dereplication_members:
                new_and_current_members.extend(dereplication_members)
                new_and_current_members.append(_)
    return list(set(new_and_current_members))


for _ in filenames:
    thereshold_id = ''.join([str(int(str(_).split('/')[-1].split('_')[0].replace('c', ''))/10)+ '%' if int(str(_).split('/')[-1].split('_')[0].replace('c', '')) not in [100, 98, 99] else str(_).split('/')[-1].split('_')[0].replace('c', '')+'%'])
    cluster_id = str(_).split('/')[-1].split('clusters')[-1]
    print(thereshold_id.replace('%', '').replace('.', ''), cluster_id)
    cluster_members = [_.description.split(';')[0] for _ in list(SeqIO.parse(_, 'fasta'))]
    cluster_members = get_dereplication_seq(cluster_members)
    number_of_cluster_members = len(cluster_members)
    unique_number_of_cluster_members = len(set([seqid_taxid[_] for _ in cluster_members]))
    member_names = ', '.join([seqid_organism_name[_] for _ in cluster_members])
    df = df.append(pd.DataFrame([[thereshold_id, cluster_id, ', '.join(cluster_members), number_of_cluster_members, unique_number_of_cluster_members, member_names]], columns=cols), ignore_index=True)


datadir = Path("../supplementary_file_5/clusters/centroid_seq")
filenames = sorted(datadir.glob("length*"))


centroid_seq = {}
for _ in filenames:
    replace = {100: '100%', 990:'99%', 980:'98%'}
    data = list(SeqIO.parse(_, 'fasta'))
    thereshold_id = ''.join([str(int(str(_).split('/')[-1].split('_c')[-1].split('.')[0])/10)+'%' if  int(str(_).split('/')[-1].split('_c')[-1].split('.')[0]) not in [100, 990, 980] else replace[int(str(_).split('/')[-1].split('_c')[-1].split('.')[0])]])
    centroid_seq[thereshold_id] = [_.description for _ in data]




def get_representative_seq(row):
    """Return representative sequence ID"""

    try:
        rep_id = []
        for k, v in centroid_seq.items():
            if row['theresholds_id'] == k:
                for _ in v:
                    if row['cluster_id'] == _.split(';')[1].split('=')[-1]:
                        rep_id.append(_.split(';')[0])
                        print((_.split(';')[0]))


    except IndexError:
        rep_id = 'NA'

    return ''.join(rep_id)

df["cluster_representative"] = df.apply(get_representative_seq, axis=1)


df.to_csv('cluster_taxID_info.csv')


