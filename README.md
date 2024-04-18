# README.md - Kiepas_et_al_2024_16S: 16S taxonomy and clustering is not a proxy for taxonomy in *Streptomyces*

This repository contains all supplementary information for analyses reported in Kiepas *et al.* (2024) describing inconsistencies between taxonomies inferred using 16S and whole-genome identities in *Streptomyces*.

This repository is provided to enable both reproduction and independent exploration of the analysis reported in this manuscript.

## Table of contents

1. [Reporting Problems](#reporting-problems)
2. [Contributors](#contributors)
3. [Contact Us](#contact-us)
4. [Downloading Repository](#downloading-repository)
5. [Set Up](#set-up)
6. [Repository Files](#repository-files)
7. [Reproducing analyses](#reproducing-analyses-quick-guide)

## Reporting Problems

Please report any issues or problems with this repository [at the Issues page](https://github.com/kiepczi/Kiepas_et_al_2023_16S/issues).

## Contributors

This manuscript has the following contributors:

- [Angelika B. Kiepas](https://github.com/kiepczi) - PhD Candidate, Univeristy of Strathclyde
- [Dr Leighton Pritchard](https://github.com/widdowquinn) - Strathclyde Chancellor's Fellow, Univeristy of Strathclyde
- [Prof Paul A. Hoskisson](https://github.com/PaulHoskisson) - Professor, Univeirsty of Strathclyde

### Contact Us

How to reach us:

- Angelika B Kiepas:
    - Email: [angelika.kiepas@strath.ac.uk](mailto:angelika.kiepas@strath.ac.uk)
    - X: [@kiepczi](https://twitter.com/kiepczi?lang=en)
- Leighton Pritchard:
    - Email: [leighton.pritchard@strath.ac.uk](mailtoleighton.pritchard@strath.ac.uk)
    - X: [@widdowquinn](https://twitter.com/widdowquinn)
- Paul A Hoskisson:
    - Email: [paul.hoskisson@strath.ac.uk](mailto:paul.hoskisson@strath.ac.uk)
    - X: [@PaulHoskisson](https://twitter.com/PaulHoskisson?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)

## Downloading Repository

If you wish to indepedently explore, reproduce and/or validate the analyses reported in the manuscipt, you can use `git` to clone this repository to your machine.

```bash
git clone https://github.com/kiepczi/Kiepas_et_al_2023_16S.git
```

Alternatively, click [here](https://github.com/kiepczi/Kiepas_et_al_2023_16S/archive/refs/heads/main.zip) to download the current state of this repository as a `.zip` file, then expand it in the usual way for your operating system, then change directory to the repository root.

```bash
cd Kiepas_et_al_2023_16S
```

## Set Up

We strongly recommend to create a `conda` enviroment specific for this activity. For example, if you have cloned or downloaded the repository and navigated to its root directory, the commands below should set up an appropriate environment:

```bash
conda create --name streptomyces python=3.8 -y
conda activate streptomyces
conda install --file requirements.txt -y
```

You will need also to install the following software within the environment, and follow the installation instructions are appropriate for each program:

- [pyANI v0.3](https://github.com/widdowquinn/pyani)
- [nextalign v0.1.4](https://github.com/nextstrain/nextclade/releases/tag/nextalign-0.1.4)
- [Cytoscape v3.9.0](https://cytoscape.org)

Due to repository size limits at `GitHub` we are unable to provide the complete set of 16S sequences and genomes used in this manuscipt in this repository. To access these FASTA and GenBank files you can access them on `Zenodo` at {INSERT DOI}, and place them in the appropriate directories. NCBI refernce taxonomy is also available from `Zenodo`.


- The 16S sequence data used in this study are also available from  [Greengenes v13.5](https://gg-sg-web.s3-us-west-2.amazonaws.com/downloads/greengenes_database/gg_13_5/gg_13_5.fasta.gz), [SILVA v138.1](https://www.arb-silva.de/fileadmin/silva_databases/release_138_1/Exports/SILVA_138.1_SSURef_tax_silva.fasta.gz), [RDP v11.5](http://rdp.cme.msu.edu/download/current_Bacteria_unaligned.fa.gz) and the NCBI under BioProject [PRJNA33175](https://www.ncbi.nlm.nih.gov/nuccore?term=33175%5BBioProject%5D+OR+33317%5BBioProject%5D). However, it is possible that more recent downloads may not contain exactly the same sequences as used in the manuscript. Once the sequences are dowloaded from `Zenodo`, please unzip all files, and place the content of `supplementary_file_2_raw_16S_databases` into `supplementary_file_2`
- The genomes used in this study can be downloaded using the `download_genomes.sh` bash scipt provided in `supplementary file 17`. To ensure reproducibility, we strongly recommend to verify the accession IDs provided in supplementary file 2 and supplementary file 17 to confirm that the datasets match, and particularly that no extra sequences have been included in the download, before conducting analyses. Once the genome sequences are downloaded from `Zenodo`, please unzip all files, and place the content of `supplementary_file_17_NCBI_streptomyces_genomes` into `supplementary_file_17/data`.
- NCBI refernce taxonomy was downloaded from [https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip](https://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip). As this is a life document for the reproductibility sake we enourage to download the file from `Zenodo`, and place the contetnt of `supplementary_file_6_NCBI_taxonomy` into `summplementary_file_6`.

## Repository Files

Here you can find a list of all supplementary files provided in this repository. current set of subfolders include:

`Supplementary file 1`: Generate figures using Python and R. Directory containing all data, Python and R scripts to generate figures for this manuscript. (93MB)

`Supplementary file 2`: Raw 16S rRNA public databases. Directory containing four separate `.txt` files with sequence IDs for public 16S rRNA databases used in this manuscript, and an additional `.txt` file with Greengenes sequence taxonomy information, and a python script used to map taxonomy information to sequences found in Greengenes v13.5. (82.2MB)

`Supplementary file 3`: Filtration of 16S rRNA public databases. Directory containing python script used for filtration of the raw databases, and generated outputs. (84.2MB)

`Supplementary file 4`: Cleaning of the filtered 16S rRNA local. Directory containing all bash and Python scripts used to clean the local full-length 16S rRNA local databases by removing redundant and poor quality 16S rRNA sequences. (109.8MB)

`Supplementary file 5`: Sequence Clustering. Directory containing a bash script used to cluster full-length cleaned local 16S rRNA *Streptomyces* local databases at various thresholds, and provides `.txt` files with accessions for representative sequences, and cluster members for each clustering threshold. (471.7MB)

`Supplementary file 6`: Analysis of taxonomic composition for each clustering threshold. Directory containing Python scripts, NCBI taxonomy input and all outputs generated used to determine the taxonomic composition for each clustering threshold. (52.7MB)

`Supplementary file 7`: Cluster sizes. Empirical cumulative plot showing cluster size generated for all clustering thresholds. (PDF 44KB)

`Supplementary file 8`: Cluster taxID abundance.  Empirical cumulative plot for unique number of taxID present for all clustering thresholds. (PDF 9KB)

`Supplementary file 9`: MSA. Directory containing all python and bash scripts, and additional data needed to generate and clean MSA for phylogenetic analysis. (69.2MB)

`Supplementary file 10`: Phylogenetic reconstruction.  Directory containing bash scripts used for phylogenetic reconstruction, and all generated outputs and log files. (76MB).

`Supplementary file 11`: Collapse branches. Directory containing jupyter notebook used for collapsing branches with the same species names, and the collapsed tree in newick format. (3.5MB)

`Supplementary file 12`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree with marked branches with transfer bootstrap expectation support of >= 50%. (PDF 224KB)

`Supplementary file 13`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of *Streptomyces albus* and *Streptomyces griseus*. (PDF 229KB)

`Supplementary file 14`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of *Streptomyces albulus*, *Streptomyces lydicus* and *Streptomyces venezuelae*. (PDF 228KB)

`Supplementary file 15`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of *Streptomyces clavuligerus* and *Streptomyces coelicolor*. (PDF 227KB)

`Supplementary file 16`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of *Streptomyces lavendulae*, *Streptomyces rimosus* and *Streptomyces scabiei*. (PDF 228KB)

`Supplementary file 17`: *Streptomyces* genomes. Directory containing bash scripts used to download *Streptomyces* genomes, and Python scripts used to check assembly status. The directory also contains two separate `.txt` files with *Streptomyces* genomes used in this manuscript: one file with all initial candidates, and a second file with replaced genomes. (20.2MB)

`Supplementary file 18`: Extraction of full-length and ambiguity free 16S rRNA sequences from *Streptomyces* genomes. Directory containing all Python and bash scripts used to extract full-length sequences from the filtered *Streptomyces* genomes. A single FASTA file with all extracted 16S rRNA sequences, and a single FASTA file with filtered sequences. A `.txt` file with accession of genomes retained in the analysis. (28.2MB)

`Supplementary file 19`: ANI analysis among *Streptomyces* genomes with identical 16S rRNA sequences. Directory containing all bash and Python scripts used to determine taxonomic boundaries among *Streptomyces* genomes sharing identical full-length 16S rRNA sequences. All output and pyANI log files. (52.8MB)

`Supplementary file 20`: Network analysis of genomes based on shared 16S sequences. Directory containing jupyter notebook with NetworkX analysis and all associated output files including. bash script for pyANI analysis runs on all connected components and all associated matrices, heatmaps and log files. (106.9MB)

`Supplementary file 21`: Interactive network graph. HTML file containing interactive network graph of genomes sharing common full-length 16S sequences with each node colour corresponding to the number of connections/degrees. (HTML 4.7MB)

`Supplementary file 22`: Interactive network graph. HTML file containing interactive network graph of genomes sharing common full-length 16S sequences showing clique (blue) and non-clique (green) components. (HTML 4.7MB)

`Supplementary file 23`: Interactive network graph. HTML file containing interactive network graph of genomes sharing common full-length 16S sequences showing number of unique genera within each connected component. Each candidate genus is represented as a single node colour within a connected component. (HTML 4.7MB)

`Supplementary file 24`: Interactive network graph. HTML file containing interactive network graph of genomes sharing common full-length 16S rRNA sequences showing number of unique species within each connected component. Each candidate species is represented as a single node colour within a connected component. (HTML 4.7MB)

`Supplementary file 25`: Interactive network graph. HTML file containing interactive network graph of genomes sharing common full-length 16S rRNA sequences showing number of unique NCBI names within each connected component. Each NCBI assigned name is represented as a single node colour within a connected component. Gray nodes represent genomes currently lacking assigned species names. (HTML 4.7MB)

`Supplementary file 26`: Intragenomic 16S rRNA heterogeneity within 1,369 Streptomyces genomes which exclusively contain only full-length and ambiguity symbol-free 16S rRNA sequences. A total of 811 genomes containing single 16S rRNA sequences are not shown. (PDF 8KB)

`Supplementary file 27`: Distribution of 16S copies per genome with a distinction between unique and total copies for genomes at assembly level complete and chromosome. (PDF 7KB)

`Supplementary file 28`: Schematic workflow for construction of the full-length 16S rRNA Streptomyces phylogeny. Each arrow represents a process and is annotated with script used and corresponding supplementary file. Output/data files, and the number of remaining sequences after each step, are indicated by rectangles. The green shading represents a single processing step of collecting and collating 16S database sequences. (PDF 91KB)

`Supplementary file 29`: Schematic representation of the pipeline used to filter publicly available Streptomyces genomes. (PDF 59KB)

`Supplementary file 30`: Sankey plot showing counts of taxonomic names in source databases, assigned at ranks from phylum to genus, to sequences identified with a key word ‘Streptomyces’ in the taxonomy field. Note that Actinobacteria and Actinobacteriota are synonyms in LPSN for the correct Phylum name Actinomycetota, but that Actinomycetales and Streptomycetales are not taxonomic synonyms for each other. Streptomycetales is synonymous in LPSN with the correct name Kitasatosporales;   Actinomycetales is a distinct  taxonomic Order. The parent order of the Family Streptomycetaceae  in LPSN is Kitasatosporales. (PDF 64KB)

`Supplementary file 31`: Rectangular phylogram of the comprehensive maximum-likelihood tree of the genus Streptomyces based on the 16S sequence diversity of all 5,064 full-length 16S rRNA sequences with 100 TBE values. (PDF 194KB)

`Supplementary file 32`: Genomes sharing identical 16S rRNA sequences are assigned different names in NCBI. A total of 1,030 singleton clusters are not shown. (PDF 8KB)

`Supplementary File 33`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of members of the novel Acintacidiphila genus. (PDF 228KB)
`Supplementary File 34`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of members of the novel Phaeacidiphilus genus. (PDF 228KB)
`Supplementary File 35`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of members of the novel Mangrovactinospora genus. (PDF 228KB)
`Supplementary File 36`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of members of the novel Wenjunlia genus. (PDF 228KB)
`Supplementary File 37`: Phylogenetic tree. PDF file showing collapsed phylogenetic tree showing distribution of members of the novel Streptantibioticus genus. (PDF 228KB)




## Reproducing analyses (QUICK Guide)

### Analysis of 16S sequences from SILVA, Greengenes, RDP and NCBI

To reproduce the analyses, and phylogenetic tree using 16S sequences downloaded from SILVA, Greengenes, RDP and NCBI, please run the following scipts in this order:

- `gg_map_taxonomy.py` - (supplementary file 2) assign taxonomy to greengenes sequences
- `get_complete_strep_seq.py` - (supplementary file 3) extract full-length (1200bp or more) *Streptomyces* 16S sequences, and standaralise base coding to thymine rather than uracil
- `check_nomenclature_hierarchy.py` - (supplementary file 3; OPTIONAL) generate data providing nomenclature at ranks from phylum to genus
- `remove_redundancy.sh` - (supplementary file 4) remove redundant sequences
- `get_ambiguity_stats_info.py` - (supplementary file 4; OPTIONAL) calculate the variance and average count of ambiguity per sequence to choose an appropriate model
- `get_paraeters_for_qnbinom.py` - (supplementary file 4; OPTIONAL)  get parameters for `qnbinom()` function in R
- `qnbinom.R` - (supplementary file 4; OPTIONAL) determine the threshold for excluding sequences that contain an excessive amount of ambiguous symbols
- `remove_ambiguity.py` - (supplementary file 4) remove sequences with more than 153 ambiguity symbols
- `remove_chiemras.bash` - (supplementary file 4) remove chimeric sequences
- `cluster_sequences.sh` - (supplementary file 5) cluster sequences at theresholds varying between 98% and 100% in step of 0.1%
- `get_LSPN_status_and_NCBI_taxID.py` - (supplementary file 6) validate nomenclature at species level (LSPN and NCBI taxID)
- `cluster_composiion_analysis.py` - (supplementary file 6) investigate taxonomic comosition for each cluster generated at each clustering thereshold
- `add_outgroup.py` - (supplementary file 9) add outgroups
- `align_seq_nextalign.sh` - (supplementary file 9) align sequences
- `trim_alignment.sh` - (supplementary file 9) trim the alignment
- `alignment_dereplication.sh` - (supplementary file 9) dereplicate aligment
- `raxml_step.sh` - (supplementary file 10) calulate ML tree
- `raxml_bootstrap.sh` - (supplementary file 10) calculate 100 boostraps
- `raxml_tbe.sh` - (supplementary file 10) get TBE values
- `collapse_branches_AK.ipynb` - (supplementary file 11) collapse branches with the same names

### Analysis of 16S sequences from *Streptomyces* genomes

To reproduce the analyses, and phylogenetic tree using 16S sequences downloaded from SILVA, Greengenes, RDP and NCBI, please run the following scipts in this order:

- `download_genomes.sh` - (supplementary file 17) download *Streptomyces* genomes. NOTE: To ensure reproductibility, we stronly recommend to verify the accession IDs provided in supplementary file 17 to confirm that no extra sequences have been included or excluded before conducting analyses.
- `check_genome_status.py` - (supplementary file 17) check assembly status. HERE: suppresent genomes were excluded, and replaced genomes were manually downloaded from NCBI aznd provided in supplementary file 17
- `extract_16S.py` - (supplementary file 18) extract 16S sequences from downloaded genomes
- `filter_16S_seq.py` - (supplementary file 18) filter 16S sequences to retain genomes that exclusively contain only full-length and ambiguity symbol free 16S sequences
- `align_sequences_with_nextalign.sh` - (supplementary file 18) align  the retained sequences with netxalign
- `trin_alignment.sh` - (supplementary file 18) trim alignments with trimAl
- `get_input_genomes_for_pyani.py` - (supplementary file 19) get genome clusters; genomes that share identical 16S sequences
- `pyani_analysis.sh` - (supplementary file 19) run pyANI anlysis on the generated clusters
- `get_pyani_hetamaps.sh` - (supplementary file 19; OPTIONAL) get pyANI heatmpas
- `get_pyani_comparision_matrix.sh` - (supplementary file 20l OPTIONAL) get pyANI matrices for each comparsion
- `generate_viz_data_pyani_comparisions.py` - (supplementary file 19; OPTIONAL) generate dataframe for pyANI comparions that can be later used to genearte scatterplots
- `genome_16S_NetworkX.ipynb` - (supplementary file 20) generate network to visually represent connections between all 1369 that contain only full-length and ambiguity symbol free 16S rRNA sequences
- `pyani_analysis.sh` - (supplementary file 20) determine taxonomic boundaries for all genomes found in the same connected component/are connected by sharing 16S sequences
