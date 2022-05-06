#!/bin/python3

x = int(input("x = "))
y = int(input("y = "))

while y:
	t = y
	y = x % y
	x = t

print (x)