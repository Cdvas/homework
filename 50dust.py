#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size (Done)
# 2. has option and default value for entropy threshold (Done)
# 3. has a switch for N-based or lowercase (soft) masking (Done)
# 4. works with uppercase or lowercase input files (Done)
# 5. works as an executable (Done)
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)
import mcb185
import math
import argparse

#subprocess.run(42dust.py)

parser = argparse.ArgumentParser(description = 'This program runs Shannon entropy filtering on sequences in a set or defined window from a sequence file. Sequences can be filtered with lowercase or "N" filtering. Default filtering results will be lowercase filtering.') #program description

parser.add_argument('-w', required=False, type=int, default = 10, metavar='<int>', help='optional int argument [%(default)i]') #window variable
parser.add_argument('-t', required=False, type=float, default = 1.1, metavar='<float>', help='optional floating point argument [%(default).1f]') #threshold variable
parser.add_argument('-s', action = 'store_true', help ='on/off switch') #switch
parser.add_argument('file', type=str, metavar='<path>', help='some file') #file to process
arg = parser.parse_args()

#print(arg.t, arg.w)

def entropy(probs): #entropy calc
	assert(math.isclose(1.0, sum(probs)))
	h = 0
	for p in probs: 
		if p != 0: 
			h -= p * math.log2(p)
	return h #the entropy calc answer
	
def seq_entropy(seq):
	p = [] #stores compositions aka probabilities
	if seq.isupper(): #checks for nt casing
		A = seq.count('A') / len(seq)
		T = seq.count('T') / len(seq)
		C = seq.count('C') / len(seq)
		G = seq.count('G') / len(seq)
		p.append(A)
		p.append(T)
		p.append(C)
		p.append(G)
	
	else: #for lowercase nucleotides
		arg.s = False #turns off the switch if turned on to not hide filtered nts in lowercase seq file
		A = seq.count('a') / len(seq)
		T = seq.count('t') / len(seq)
		C = seq.count('c') / len(seq)
		G = seq.count('g') / len(seq) 
		p.append(A)
		p.append(T)
		p.append(C)
		p.append(G)
		
	return entropy(p) #sends probabilities to entropy calc

processing = []
for name, seq in mcb185.read_fasta(arg.file):
	processing = list(seq)
	for i in range(len(seq) - arg.w + 1): #how many times this happens
		frame = seq[i:i+arg.w] #area of analysis each time the loop above runs
		if seq_entropy(frame) < arg.t: #make N or lower
			if arg.s == False:
				for nt in range(i, i+arg.w):
					processing[nt] = 'N'
			else:
				for nt in range(i, i+arg.w):
					processing[nt] = processing[nt].lower()
'''
if arg.s: 
	print('switch on')
else:	
	print('switch off')
'''
processed = ''.join(processing)
print(name)
for i in range(0, len(seq), 60):
	print(processed[i:i+60])
	
"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
