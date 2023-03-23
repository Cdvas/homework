# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import gzip
import sys

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
count = [0] * len(amino_acids)
total = 0
count2 = {'A': 0}
count2['A'] += 1
with gzip.open(sys.argv[1], 'rt') as aa:
	for line in aa.readlines():
		if line[0] == '>': continue	#implicit else	
		total += len(line) - 1 #a new line at the end is why -1
		for i, aa in enumerate(amino_acids): #1st instance i = 0 aa = A
			count[i] += line.count(aa)

for i in range(len(amino_acids)):
	print(f'{amino_acids[i]} {count[i]} {count[i]/total:.4f}')

"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz 23032 lines in file
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
