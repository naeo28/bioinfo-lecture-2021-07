seq1 = "ATGTTATAG"
seq2 = ""

for s in seq1:
    if s == "A":
        seq2 += "T"
    elif s == "C":
        seq2 += "G"
    elif s == "G":
        seq2 += "C"
    elif s == "T":
        seq2 += "A"

print(seq1)
print(seq2)
