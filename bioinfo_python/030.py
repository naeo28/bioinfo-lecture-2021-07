
seq1 = "AGTTTATAG"

for i in range(len(seq1)):
    #print(i, seq[i])
    #print(i, i+2, seq[i:i+2])
    if seq1[i:i+2] == "TT":
        print(i, seq1[i:i+2])

