#!/usr/bin/python3

seq1 = "ATGTTATAG"

for i in range(0,len(seq1),3):
    #print(seq1[i])    #025문제
    print(seq1[i:i+3])   #026문제

print(seq1[::-1])   #027문제

