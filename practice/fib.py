#!/bin/python3

import sys

n = int(input("n = "))

f0 = 0
f1 = 1
f = 1

while n >= 1:
	# next element
	f = f0 + f1

	# steps forward
	f0 = f1
	f1 = f

	# decrement n
	n = n - 1

print (f)