#!/bin/bash
#Run pyANI v3



for FILE in genome_clusters/*; do
    pyani index -i $FILE
    file="${FILE##}"
    job_id=`echo "$FILE" | cut -d'/' -f2`
    echo $job_id
    pyani anim -i=$file -o ${file}/output -v -l ${file}/output.log --name $job_id --labels ${file}/labels.txt --classes ${file}/classes.txt
    pyani report -v --runs -o genome_clusters --format html
    done
