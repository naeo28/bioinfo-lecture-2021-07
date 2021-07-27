#!/bin/bash

vcf_file=$1
#vcf_file = "SRR000982.filtered.variants.annotated.vcf"

cat ${vcf_file} | grep -v "^#" | grep "PASS" | cut -f7 | uniq -c
#grep -v "^#" ${vac_file} | grep "PASS" | cut -f7 | uniq -c

