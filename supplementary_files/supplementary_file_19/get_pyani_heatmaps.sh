#!/bin/bash
#Get pyANI matrices comparisions



for i in {1..278}
do
   pyani plot -o pyani_analysis_heatmaps --run_id $i -v --formats pdf
done