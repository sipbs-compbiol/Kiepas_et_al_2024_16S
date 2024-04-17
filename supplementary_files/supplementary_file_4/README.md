# Supplementary file 4 - Cleaning of the filtrated 16S rRA local database

This ZIP file contains all BASH and Python scripts used in this manuscript to clean the filtrated 16S rRNA local databses (genearted in supplementary file3) by removing redundant sequences, and poor quality sequences ie. contaminated with ambiguity symbols and chimeric reads. 

## The current repositiory contains the following subfiles:

- `dereplication` - containing a BASH script used to remove redundant sequences, and an output file to store all generated outputs. 
- `remove ambiguity` -  containing Python and R scripts used to identify and remove sequences with siginificant amount of ambiguity, and an otput file to store all geerated outputs. 
- `remove_chimeras` -  containing BASH script used to identify and remove chimeric sequences, and an output file to store generated outputs.



