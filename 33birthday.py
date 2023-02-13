# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import random

days = int(sys.argv[1]) 
ppl = int(sys.argv[2]) #assigns what the input values will be (days or people)
simulations = 1000 #how many times I'm looping through these people's birthdays
match = 0 #how many times I've seen matches

for x in range(simulations): #the simulation
	bdays = []
	for person in range(ppl):
		day = random.randint(1, days) #each person has a random birthday within the range of days
		if day in bdays: 
			match += 1 
			break #stop everything if the birthday is already in the list, a match
		else:	bdays.append(day) #otherwise, add to the list and keep going
odds = match/simulations #how often there has been matches within the amount of simulations
print(odds)
		

"""
ie if there are 23 people in a room what are the odds they have the same birthday?
python3 33birthday.py 365 23
0.571
"""

