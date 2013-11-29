#!/bin/bash


lines=`wc -l data.txt`
no_lines=`wc -l final.txt`

while [ "$no_lines -le $lines" ];do 
#do

    python synth.py 
    cat output.txt >> final.txt
    rm -rf output.txt
    
done 