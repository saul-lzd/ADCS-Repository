#!/bin/bash
git clone https://github.com/saul-lzd/ADCS-Repository.git

cd ADCS-Repository

mkdir code-analysis

# display output to terminal
prospector

# save output to prospector.txt file in the root of the project
prospector -o text:./code-analysis/prospector.txt

# show output to terminal
radon cc -a -s ./

# save output to radon.txt file in the root of the project
radon cc -a -s -O code-analysis/radon.txt ./


echo "output files:"
echo "/code-analysis/prospector.txt"
echo "/code-analysis/radon.txt"
read -p "Press any key to exit..." -n1 -s