# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import sys
import random

genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])
'''
settings = [] #stores user values in a list
input = 0
for value in sys.argv[1:]: #checks if given integers and categorizes settings into variables
	try: value = int(value)
	except: raise
	settings.append(value)
	if input == 0:
		genome_size = value
		input += 1
	elif input == 1:
		read_num = value
		input += 1
	else:
		read_len = value
'''
'''
print(genome_size, read_num, read_len)
print(settings) #checks if the loop placed the settings in the correct vars and placed them into a list
'''
genome = [] 
for size in range(genome_size):
	genome.append(0)
#print(genome)
end = genome_size - read_len
for reads in range(read_num):
	start = random.randint(0, int(end)) #this prevents the read window from going over the end of the genome
	print(start)
	for i in range(start, start + read_len):
		genome[i] += 1
print(genome)
#print(genome[read_len:-read_len])
Min = min(genome[read_len:-read_len]) #collecting data to report
Max = max(genome[read_len:-read_len])
Average = (sum(genome[read_len:-read_len]))/(len(genome)-2 *read_len)

print(f'{Min} {Max} {Average:.5f}')
#undersampling by read_len - 1, or read_len
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
