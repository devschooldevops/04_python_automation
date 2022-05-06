#!/bin/python3

from datetime import date

file = open("date.txt", "w")
file.write(str(date.today()))
file.close()