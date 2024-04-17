#Set Up
import pandas as pd
from collections import defaultdict

#Load data
data = pd.read_csv("cluster_taxID_info.csv")

#Get rows for 
data = data.loc[data['theresholds_id'] == '100%']
cluster_members = data.set_index('cluster_representative').to_dict()['cluster_members']


#Load data with taxID info
data2 = pd.read_csv("complete_strep_record_info.csv")
taxIDs = data2.set_index("accession").to_dict()['taxID']
LSPN = data2.set_index("accession").to_dict()['LSPN_status']



cluster_taxIDs = defaultdict(list)

for k, v in cluster_members.items():
    for _ in v.split(', '):
        cluster_taxIDs[k].append(taxIDs[_])

counter = 0
for k, v in cluster_taxIDs.items():
    if len(set(v)) == 1:
        if list(set(v))[0] in [1887.0, 1211.0]:
            counter += 1

print(f"Number of clusters with unclassified species only: {counter}")

def func(a, b):
  return len(set(a).intersection(b)) != 0

lst1 = [1887.0, 1211.0]


counter = 0
for k, v in cluster_taxIDs.items():
    if func(lst1, list(set(v))) == True:
        counter +=1 

print(f"Number of clusters with at least 1 sequence unclassified: {counter}")


cluster_LSPN_records = defaultdict(list)
for k, v in cluster_members.items():
    for _ in v.split(', '):
        cluster_LSPN_records[k].append(LSPN[_])



counter = 0
for k, v in cluster_LSPN_records.items():
    if len(set(v)) == 1:
        if 'no record in LSPN entry' in v:
            counter +=1
            print(k)


print(f"Number of clusters with all no record in LSPN entry: {counter}")


counter = 0
for k, v in cluster_LSPN_records.items():
    if func(['no record in LSPN entry'], list(set(v))) == True:
        counter +=1 

print(f"Number of clusters with at least 1 name with n o reord in LSPN: {counter}")

