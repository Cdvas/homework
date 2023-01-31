# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library
"""
What I want this to do. Take the value of 5. Make a new variable equal to 1 less than 5. Repeat this process until I make a variable = 1. Stop before 0. Multiply all of those values by each other as well as add those values together. Problem is I don't know how to make the program make a new variable and define it. I can only modify existing variables. Or, I have those variables premade and change their value in the loop.
"""
n = 5
n1 = None
n2 = None
n3 = None
n4 = None
if n1 == None:
	n1 = n - 1
print(n1)
if n2 == None: 
	n2 = n1 - 1
print(n2)
if n3 == None: 
	n3 = n2 - 1
print(n3)
if n4 == None:
	n4 = n3 - 1
print(n4)
print(n, n4+n3+n2+n1+n, n4*n3*n2*n1*n)


#print(n, f, s)

"""
python3 22sumfac.py
5 15 120
"""
