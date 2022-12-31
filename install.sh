#!/bin/bash



dt=$(date '+%d%m%Y %H%M%S')
DAY=$(date +"%u")
c=$DAY$dt
d='.venv'
f="${d}${c}"
echo "running: " virtuaelnv --python=python3 ${f:0:8}
virtualenv --python=python3  ${f:0:8}
echo "activating..."
echo source ${f:0:8}/bin activate
source ${f:0:8}/bin activate
echo ".venv activated"
pip install -r requirements.txt