#!/usr/bin/env python3

# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import math
import mcb185

def entropy(probs): 
	assert(math.isclose(1.0, sum(probs)))
	h = 0
	for p in probs: 
		if p != 0:
			h -= p * math.log2(p)
	return h

def seq_entropy(seq):
	p = [] #stores compositions aka probabilities	
	A = seq.count('A') / len(seq) #nt composition
	T = seq.count('T') / len(seq)
	C = seq.count('C') / len(seq)
	G = seq.count('G') / len(seq)
	p.append(A) #places all probabilities into a list
	p.append(T)
	p.append(C)
	p.append(G)
	return entropy(p) #without the return statement, got 'None' outputs

#print(entropy([.1, .2, .3, .4])) tests entropy calc

processing = [] #holds the seqs in to change nts to 'N'

for name, genome in mcb185.read_fasta(sys.argv[1]):
	window = int((sys.argv[2]))
	threshold = float((sys.argv[3]))
	seq = genome
	processing = list(seq) #puts sequence into a list for processing
for i in range(len(seq) - window + 1): #process whole seq
	frame = seq[i:i+window]
	if seq_entropy(frame) < threshold: #entropy filter
		for nt in range(i, i+window):
			processing[nt] = 'N'

processed = ''.join(processing) #turns the processed list into a string
print(name)
for i in range(0, len(seq), 60): #output is 60nt at a time
	print(processed[i:i+60])

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
