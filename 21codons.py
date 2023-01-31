# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator


dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for frame in range(1): #tells the program how many times to run through this sequence
	for position in range(frame, len(dna) -2, 3):
		codon = dna[position:position+3] #codons are every 3 bases
		print(codon)
"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
