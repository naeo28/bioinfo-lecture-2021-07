#!/usr/bin/python

#딕셔녀리 사용하기

data = {"A":0 "C":0, "G":0, "T":0} #이거 없어지고
#data = dict()  #{}이렇게 생긴건데,  얘 생기면서 #부분 진행

with open("covid19.fasta", "r") as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            #if base not in data:
                #data[base] = 0
            data[base] += 1

print(f"A: {data['A']}")
print(f"C: {data['C']}")
print(f"G: {data['G']}")
print(f"T: {data['T']}")
#print(data)
