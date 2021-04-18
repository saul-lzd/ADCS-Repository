#!/bin/bash
git clone https://github.com/saul-lzd/ADCS-Repository.git

cd ADCS-Repository

mkdir code-analysis

# display outputs
prospector
radon cc -a -s ./

# create files
prospector -o text:./code-analysis/prospector.txt
radon cc -a -s -O code-analysis/radon.txt ./


echo "output files:"
echo "/code-analysis/prospector.txt"
echo "/code-analysis/radon.txt"
read -p "Press any key to exit..." -n1 -s