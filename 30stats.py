# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

print(sys.argv)
vals = []
count = len(vals)

for thing in sys.argv[1:]: #this loop puts the sys.argv values in the list
#	print(thing)
	vals.append(float(thing))
	count += 1
vals.sort() #numerical sort
Min = min(vals) #takes out the first value of the sorted list
Max = vals.pop() #takes out the last value of the sorted list
vals.append(Max)#Puts the popped value back since that messes up the Sum calculation I intended if I don't

Sum = sum(vals) #Mean calculation
#print(Sum)
Mean = Sum/len(vals)

Numerator = []
for thing in sys.argv[1:]: #Calculating Std. dev.
	First_calc = float(thing) - Mean
	sq_num = First_calc ** 2
	Numerator.append(sq_num)
Calculating = sum(Numerator)
std_dev = (Calculating/(len(vals))) ** 0.5

for val in vals: #Finds Median
	if len(vals) % 2 == 0:
		Median_value = len(vals)/2
		Median = vals[int(Median_value)]
	else:
		Median_value = len(vals)/2
		Median = vals[int(Median_value)]	

vals = [] #puts list values back in reverse order
for thing in sys.argv:
	vals.append(thing)
	
print(f'python3 30stats.py {vals}')
print(f'Count: {count}')
print(f'Minimum: {Min}')
print(f'Maximum: {Max}')
print(f'Mean: {Mean:.3f}')
print(f'Std. dev: {std_dev:.3f}')
print(f'Median {Median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
