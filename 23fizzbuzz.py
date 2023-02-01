# 23fizzbuzz.py

# Write a program that prints the numbers from 1 to 100
# For multiples of 3 print “Fizz” instead of the number
# For the multiples of 5 print “Buzz”
# For numbers which are multiples of both 3 and 5 print “FizzBuzz”

# Note: this is a common interview question

length = 100
for x in range(1, length):
	if x % 3 == 0 and x % 5 == 0: 
		x = 'FizzBuzz'
	elif x % 5 == 0:
		x = 'Buzz'
	elif x % 3 == 0:
		x = 'Fizz'
	print(x)
	
"""	
	#print(x) #prints Fizz's
#for x in range(length+1):
	if x % 5 == 0: 
		x = 'Buzz'
		#print(x) #prints Buzz's
#for x in range(length+1):
	if x % 3 == 0 and x % 5 == 0: 
		x = 'FizzBuzz'
	#print(x) #prints Fizzbuzz's
"""
print(x)

"""
python3 23fizzbuzz.py
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
"""