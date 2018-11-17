#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    wget --user tipster --password cdroms https://trec.nist.gov/results/trec26/rts/$line
    echo "Text read from file: $line"
done < "$1"

#https://trec.nist.gov/results/trec26/rts/adv_lirmm-Run1.gz