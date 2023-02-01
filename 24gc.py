# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
#defines my GC's of interest
G = 0
C = 0
for nt in range(len(dna)): #scan the nt's of any sequence len(dna) and count GC
	if dna[nt] == 'G':
		G += 1
	elif dna[nt] == 'C':
		C += 1
	else: G += 0
GC = G + C #Use C and G counts to sum to GC count
ratio = ((G + C)/(len(dna)))
print(f'{ratio:.2f}')

"""
python3 24gc.py
0.42
"""
