"""This script was used to generate dataframe for visualization of pyani analysis for genomes which share identical 16S rRNA sequences.
"""


#Set Up
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict



def comparision_type(row, col, thereshold):
    """Return inter if the ID% is more than 95%"""

    try:
        val = 'intra' if row[col] >=thereshold else 'inter'
    except IndexError:
        val = 'NA'

    return val


#Path to all files
datadir = Path("pyani_analysis_matrix/")
filenames = sorted(datadir.glob("*.tab"))

#Create empty df
data = pd.DataFrame(columns=['run_id','genome1', 'genome2', 'unique_taxa_names', 'coverage', 'identity'])

# #Hold defaultdict, so cluster ids can be assigned per group
# cluster_ids = defaultdict(list)


#Matching coverage and identity values
for i in range(1,279):
    #Loading data
    identity = pd.read_csv(f"pyani_analysis_matrix/matrix_identity_{i}.tab", sep='\t').rename(columns={'Unnamed: 0': 'genome1'})
    coverage = pd.read_csv(f"pyani_analysis_matrix/matrix_coverage_{i}.tab", sep='\t').rename(columns={'Unnamed: 0': 'genome1'})
    #Melting data
    identity_melt = pd.melt(identity, id_vars=['genome1'], value_vars=[_ for _ in identity if _ != 'genome1'], var_name='genome2', value_name='identity')
    coverage_melt = pd.melt(coverage, id_vars=['genome1'], value_vars=[_ for _ in identity if _ != 'genome1'], var_name='genome2', value_name='coverage')
    #Combine data
    combined = pd.merge(identity_melt, coverage_melt,  how='left', left_on=['genome1', 'genome2'], right_on = ['genome1','genome2'])
    #append to the final dataframe
    data = data.append(combined)
    #adding run_id
    data['run_id'] = data['run_id'].fillna(int(i))


data = data[data['genome1'] != data['genome2']]
data['comparision_type_species'] = data.apply(comparision_type, col='identity', thereshold=0.95, axis=1)
data['comparision_type_genus'] = data.apply(comparision_type, col='coverage', thereshold=0.50, axis=1)


#Adding the cluster_id/cluster_hash
df = pd.read_csv("genome_clusters/runs.tab", sep='\t')
data['cluster_hash'] = data['run_id'].map(df.set_index('run ID').to_dict()['name'])


#Adding number of unique NCBI species names per cluster
df2 = pd.read_csv("genome_clusters_info.csv")
data['unique_taxa_names'] = data['cluster_hash'].map(df2.set_index('cluster_hash').to_dict()['Unique_names_per_cluster'])


#Assign cluster ids gruped by the unique number of taxa present
unique_species_cluster_id = defaultdict(list)
for cluster_hash, unique_species in data.set_index('cluster_hash').to_dict()['unique_taxa_names'].items():
    unique_species_cluster_id[unique_species].append(cluster_hash)

data['cluster_id'] = data['cluster_hash'].map({_[1]:_[0] for k, v in unique_species_cluster_id.items() for _ in enumerate(v)})


data.to_csv('pyANI_comparision_info.csv')
    
