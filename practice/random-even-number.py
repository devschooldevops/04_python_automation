#!/bin/python3

from random import randrange

n = randrange(100)

if n % 2 == 0:
	print("Even: %d" % (n))
else:
	print("Odd: %d" % (n))