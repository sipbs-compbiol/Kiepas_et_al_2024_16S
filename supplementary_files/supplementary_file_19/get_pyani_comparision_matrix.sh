#!/bin/bash
#Get pyANI matrices comparisions


for i in {1..278}
do
   pyani report -o pyani_analysis_matrix --formats=stdout --run_matrices $i
done