# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

anti = ''

for nt in dna:
	if nt == 'A':
		anti = 'T' + anti
	elif nt == 'T': 
		anti = 'A' + anti
	elif nt == 'C':
		anti = 'C' + anti
	else:	anti = 'G' + anti
print(anti)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
