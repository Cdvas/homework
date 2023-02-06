# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'
i = 0
frame_size = dna[i:i+2]
in_frame = 0
base_position = 0
#dna_size = len(dna)

for nt in dna:
	print(base_position, in_frame, nt)
	in_frame += 1
	base_position += 1
	if in_frame > 2:
		in_frame = 0
'''
dna_size -= 1
if dna_size < 3: 
	break
'''

"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
