# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import math
import sys

vals = [] #checks if the value entered is a number and makes the list
for value in sys.argv[1:]:
	try: 
		value = float(value)
		vals.append(float(value))
	except: raise
#print(vals)
size = (len(vals))

#checks for total probability is 1.0
assert(math.isclose(sum(vals), 1.0, abs_tol=0.01))

h = [] #performs the equation calculations
for value in range(size): 
	x = vals.pop()
#	print(x)
	answer = x * (math.log2(x))
#	print(answer)
	h.append(answer)
	x = None
	
H = (sum(h)) * (-1) #Shannon calc last step

print('python3 31entropy.py 0.1 0.2 0.3 0.4')
print(f'{H:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
